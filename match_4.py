def handle(payload: dict) -> None:
    # HAMMER TIME! 🔨
    match payload:
        case {"type": "AccountCreated"}:
            ...
        case {"type": "AccountDeleted"}:
            ...
        case {"type": "AccountUpdated"}:
            if payload["new_status"] == "paid":
                ...
            elif payload["new_status"] == "trial":
                ...
        case _:
            print("Omg, what is this?!")

