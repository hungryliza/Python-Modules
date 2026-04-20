import sys

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0].split("/")[-1]} <file>")
    for file in sys.argv[1:]:
        print(f"Accessing file '{file.split("\\")[-1]}'")
        try:
            print("---\n")
            f = open(file, "r")
            flst = f.read()
            print(flst)
            f.close()
            print(f"\n---\nFile '{file.split("\\")[-1]}' closed.\n")
            fi = open(file, "r")
            filst = fi.read().split("\n")
            newlst = [i + "#" for i in filst]
            updated_file = "\n".join(newlst)
            print("Transform data:\n---\n")
            print(updated_file)
            print(f"\n---\n")
            new_file = input("Enter new file name (or empty): ")
            if len(new_file) == 0:
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file}'")
                new_file_access = open(new_file, "w")
                new_file_access.write(updated_file)
                new_file_access.close()
                print(f"Data saved in file '{new_file}'.")
        except FileNotFoundError as e:
            print(f"Error opening file '{file}': {e}")
        except PermissionError as err:
            print(f"Error opening file '{file}' {err}")
