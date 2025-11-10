def divide(c, b):
    """Return the result of dividing a by b, or an error message if division by zero occurs."""
    try:
        result = c / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."