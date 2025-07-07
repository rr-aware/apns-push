import json
import time
import jwt
from typing import Dict, Any
import platform
from pathlib import Path
import subprocess
from typing import Optional

class Push:
    _config = {}
    _private_key = None

    @classmethod
    def configure(cls,
                  auth_key_id: str,
                  team_id: str,
                  bundle_id: str,
                  key_path: str,
                  use_sandbox: bool = True):
        with open(key_path, "r") as f:
            cls._private_key = f.read()

        cls._config = {
            "auth_key_id": auth_key_id,
            "team_id": team_id,
            "bundle_id": bundle_id,
            "key_path": key_path,
            "use_sandbox": use_sandbox
        }

    @classmethod
    def send(cls, device_token: str, payload: Dict[str, Any], bundle_id: Optional[str] = None) -> Dict[str, Any]:
        if not cls._config:
            raise RuntimeError("Push not configured. Call Push.configure() first.")

        payload_json = json.dumps(payload)
        url_host = "api.sandbox.push.apple.com" if cls._config["use_sandbox"] else "api.push.apple.com"
        app_bundle_id = bundle_id or cls._config["bundle_id"]

        response = subprocess.run(
            [
                cls._get_command(),
                "-v",
                "--http2",
                "--header", f"apns-topic: {app_bundle_id}",
                "--header", f"authorization: bearer {cls._generate_jwt()}",
                "--data", payload_json,
                f"https://{url_host}/3/device/{device_token}"
            ],
            capture_output=True,
            text=True
        )

        return {
            "success": response.returncode == 0,
            "status_code": cls._parse_status_code(response),
            "output": {
                "stdout": response.stdout,
                "stderr": response.stderr
            },
            "return_code": response.returncode
        }

    @classmethod
    def _get_command(cls) -> str:
        if platform.system() == "Windows":
            return str(Path(__file__).parent / "curl.exe")
        else:
            return "curl"

    @classmethod
    def _parse_status_code(cls, response: subprocess.CompletedProcess) -> int:
        for line in response.stderr.splitlines():
            if line.startswith("< HTTP/2"):
                try:
                    return int(line.split()[2])
                except (IndexError, ValueError):
                    pass
        return None

    @classmethod
    def _generate_jwt(cls) -> str:
        jwt_token = jwt.encode(
            {
                "iss": cls._config["team_id"],
                "iat": int(time.time() - 1)
            },
            cls._private_key,
            algorithm="ES256",
            headers={"alg": "ES256", "kid": cls._config["auth_key_id"]}
        )
        return jwt_token.decode("utf-8") if isinstance(jwt_token, bytes) else jwt_token
