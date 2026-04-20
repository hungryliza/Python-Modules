def secure_archive(filename, action="r", content=None):
    try:
        with open(filename, action) as f:
            if action == "r":
                content = f.read()
            elif action == "w":
                f.write(f"{content}")
                content = 'Content successfully written to file'
        return(True, content)
    except FileNotFoundError as e:
        return(False, f"{e}")
    except PermissionError as err:
        return(False, f"{err}")

if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print(f"Using 'secure_archive' to read from a nonexistent file:"
          f"\n{secure_archive('/not/existing/file')}")
    print()
    print(f"Using 'secure_archive' to read from an inaccessible file:"
          f"\n{secure_archive('/etc/master.passwd')}")
    print()
    content_read = secure_archive('ancient_fragment.txt')
    print(f"Using 'secure_archive' to read from a regular file:"
          f"\n{content_read[0], content_read[1]}")
    print()
    print(f"Using 'secure_archive' to write previous content to a new file:"
          f"\n{secure_archive('new_file.txt', 'w', content_read[1])}")
