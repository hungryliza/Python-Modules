import sys

if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0].split("/")[-1]} <file>")
    for file in sys.argv[1:]:
        print(f"Accessing file '{file.split("\\")[-1]}'")
        try:
            print("---\n")
            f = open(file, "r")
            print(f.read())
            f.close()
            print(f"\n---\nFile '{file.split("\\")[-1]}' closed.")
        except FileNotFoundError as e:
            print(f"Error opening file '{file}': {e}")
        except PermissionError as err:
            print(f"Error opening file '{file}' {err}")
