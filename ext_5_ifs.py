data = {"name": "sebastian"}

match data:
    case {"name": str() as name} if name[0] == name[0].upper():
        print(f"Hello! {name}!")
    case _:
        print("Name should start with a capital letter, mate!")
