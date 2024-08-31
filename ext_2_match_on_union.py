data = {"price": 123}

match data:
    case {"price": int() | float()}:
        print(f"That has a price tag on it!")
    case _:
        print("No idea")
