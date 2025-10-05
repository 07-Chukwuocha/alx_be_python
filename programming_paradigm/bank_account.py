def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Try dividing
        result = num / denom
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

