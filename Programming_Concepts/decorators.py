def validate_args_decorator(func):
    def wrapper(length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values.")
        return func(length, width)
    return wrapper

@validate_args_decorator
def calculate_rectangle_area(length, width):
    return length * width

# Usage
area = calculate_rectangle_area(5, 4)  # Valid input
print(f"Rectangle area: {area}")

try:
    invalid_area = calculate_rectangle_area(-1, 4)  # Invalid input
except ValueError as e:
    print(f"Error: {e}") 