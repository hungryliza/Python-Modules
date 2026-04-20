def input_temperature(temp_str: str) -> int:
    return(int(temp_str))

def test_temperature():
    values = ["25", "abc"]
    for i in values:
        try:
            input_temperature(i)
            print(f"Input data is '{i}'")
            print(f"Temperature is now {i}°C")
        except ValueError as err:
            print(f"Input data is '{i}'")
            print(f"Caught input_temperature error: {err}")
    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()