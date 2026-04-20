import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    arguments = sys.argv
    print("Program name:", arguments[0])
    if len(arguments) > 1:
        print(f"Arguments received: {len(arguments) - 1}")
        j = 1
        for i in arguments[1:]:
            print(f"Argument {j}: {i}")
            j += 1
        print(f"Total arguments: {len(arguments)}")
    else:
        print(f"No arguments provided!")
        print(f"Total arguments: {len(arguments)}")
