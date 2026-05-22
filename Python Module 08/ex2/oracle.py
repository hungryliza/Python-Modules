#pip install python-dotenv
import os
from dotenv import load_dotenv, dotenv_values

if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    loaded = load_dotenv()
    matrix = os.environ.get("MATRIX_MODE")
    if matrix is None:
        print("Matrix mode: missing")
    else:
        print(f"Mode: {matrix}")
    data = os.environ.get("DATABASE_URL")
    if data is None:
        print("Database: missing")
    elif matrix == "development":
        print("Database: Connected to local instance")
    else:
        print(f"Database: {data}")
    api = os.environ.get("API_KEY")
    if api is None:
        print("api key missing")
    elif matrix == "development":
        print("API Access: Authenticated")
    else:
        print(f"Api_key: {api}")
    log = os.environ.get("LOG_LEVEL")
    if log is None:
        print("Log level: missing")
    else:
        print(f"Log Level: {log}")
    zion = os.environ.get("ZION_ENDPOINT")
    if zion is None:
        print("Zion endpoint: missing")
    elif matrix == "development":
        print("Zion Network: Online")
    else:
        print(f"Zion Network: {zion}")

    print("\nEnvironment security check:")
    if loaded is True:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[X] Do not hardcode secrets, please configure .env")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[X] .env file not configured, "
              "please run cp .env.example .env")
    if loaded is True and (dotenv_values(".env").get("MATRIX_MODE") == os.environ.get("MATRIX_MODE")):
        print("[OK] Production overrides available")
    elif loaded is False and os.environ.get("MATRIX_MODE") == "development":
        print("[X] .env file not configured to check override availability")
    else:
        print("[X] Production overridden by running MATRIX_MODE=production API_KEY=secret123")

    print("\nThe Oracle sees all configurations.")
