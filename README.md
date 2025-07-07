# apns-push

A lightweight Python library for sending push notifications to Apple Push Notification service (APNs) using `curl` and JWT.

## ✨ Features

- Uses Apple's recommended HTTP/2 + JWT push mechanism
- Leverages system `curl`, compatible with macOS, Linux, and Windows
- Supports both sandbox and production environments
- Ideal for server-side or script-based push workflows

## 📦 Installation

```bash
pip install apns-push  # after publishing to PyPI

# or for development
git clone https://github.com/yourname/apns-push.git
cd apns-push
pip install -e .
```

## 🚀 Usage

```python
from push import Push

Push.configure(
    auth_key_id="YOUR_KEY_ID",
    team_id="YOUR_TEAM_ID",
    bundle_id="com.example.app",
    key_path="path/to/AuthKey_XXXXXX.p8",
    use_sandbox=True
)

result = Push.send(
    device_token="abcdef123456...",
    payload={
        "aps": {
            "alert": {
                "title": "Hello",
                "body": "This is a test push."
            },
            "sound": "default"
        }
    }
)

print(result)
```

## 📁 Example

See [`examples/demo.py`](examples/demo.py)

## 📄 License

MIT License
