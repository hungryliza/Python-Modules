def garden_operations(operation_number):
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        a = 7 / 0
        print(a)
    elif (operation_number == 2):
        my_file = open("/non/existent/file", "r")
        print(my_file.read())
    elif (operation_number == 3):
        print('The result is : ' + 3)
    else:
        print("Operation completed successfully")

def test_error_types():
    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as err:
            print(f"Caught {type(err).__name__}: {err}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
