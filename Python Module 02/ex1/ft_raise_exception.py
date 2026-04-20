def input_temperature(temp_str: str) -> int:
    new_temp = int(temp_str)
    if new_temp > 40:
        raise ValueError(f"Caught input_temperature error: {new_temp}°C is too hot for plants (max 40°C)")
    elif new_temp < 0:
        raise ValueError(f"Caught input_temperature error: {new_temp}°C is too cold for plants (min 0°C)")
    else:
        return(int(temp_str))

def test_temperature():
    values = ["25", "abc", "100", "-50"]
    for i in values:
        try:
            input_temperature(i)
            print(f"Input data is '{i}'")
            print(f"Temperature is now {i}°C")
        except ValueError as err:
            print(f"Input data is '{i}'")
            print(f"{err}")
    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()