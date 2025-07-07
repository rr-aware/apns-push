from push import Push
from pathlib import Path

key_path = Path(__file__).parent / "keys" / "AuthKey_xxxx.p8"

Push.configure(
    auth_key_id="your auth_key_id", 
    team_id="your team id", 
    bundle_id="you app's bundle id", 
    key_path=str(key_path),
    use_sandbox=True
)

payload = {
    "aps": {
        "alert": {
            "title": "this is title",
            "body": "this is body"
        },
        "sound": "default"
    }
}

device_token = "a device token in str"

result = Push.send(device_token=device_token, payload=payload)

print("Success:", result["success"])
print("Status Code:", result.get("status_code"))
print("STDOUT:", result["output"]["stdout"])
print("STDERR:", result["output"]["stderr"])
