import os
import sys

app_env = os.getenv("APP_ENV")
if not app_env:
    print("ERROR: APP_ENV is missing!")
    sys.exit(1)

print(f"Configuration OK: APP_ENV={app_env}")
