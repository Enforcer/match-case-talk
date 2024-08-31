data = {"price": 123}

match data:
    case {"name": _} | {"price": _}:
        print(f"It has a name or a price!")
    case _:
        print("No idea")
