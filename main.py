import importlib

day = 3
part = 2

def get_user_input():
    try:
        day = int(input("day: "))
        if day not in range(1, 25):
            raise ValueError("Day must be between 1 and 25.")
        part = int(input("part: "))
        if part not in [1, 2]:
            raise ValueError("Part must be 1 or 2.")
        return day, part
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None

def execute_day_method(day, part):
    try:
        day_module_name = f"days.day{day}"
        day_module = importlib.import_module(day_module_name)

        method_name = f"part{part}"
        if not hasattr(day_module, method_name):
            print(f"Method '{method_name}' not found in {day_module_name}.")
            return

        method = getattr(day_module, method_name)
        print(f"Executing {day_module_name}.{method_name}...")
        result = method()
        print(f"Result: {result}")
    except ModuleNotFoundError:
        print(f"Module for day {day} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if day is None or part is None:
        day, part = get_user_input()
    execute_day_method(day, part)