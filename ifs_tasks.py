def handle(payload: dict) -> None:
    # code this like it's 2020 😎
    if payload.get("type") == "AccountCreated":
        ...
    elif payload.get("type") == "AccountDeleted":
        ...
    elif payload.get("type") == "AccountUpdated":
        ...
    else:
        print("Omg, what is this?!")

