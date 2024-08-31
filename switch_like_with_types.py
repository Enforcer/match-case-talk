data = {"name": "Sebastian"}

match data:
    case {"name": name}:
        print(f"That's a dict with 'name' = {name}")
    case _:
        print("No idea")
