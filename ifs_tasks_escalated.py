def handle(payload: dict) -> None:
    # code this like it's 2020 😎
    # ...and pretend we're in control 🙈🙉🙊
    if payload.get("type") == "AccountCreated":
        ...
    elif payload.get("type") == "AccountDeleted":
        ...
    elif payload.get("type") == "AccountUpdated":
        if payload["new_status"] == "paid":
            ...
        elif payload["new_status"] == "trial":
            ...
    else:
        print("Omg, what is this?!")

