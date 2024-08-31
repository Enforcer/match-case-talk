data = {"name": "sebastian"}

match data:
    case {"name": str() as name}:
        print(f"It has a name - {name}!")
    case _:
        print("No idea")
