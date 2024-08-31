def handle(payload: dict) -> None:
    # HAMMER TIME! 🔨
    match payload:
        case {"type": "AccountCreated"}:
            ...
        case {"type": "AccountDeleted"}:
            ...
        case {"type": "AccountUpdated", "new_status": "paid"}:
            ...
        case {"type": "AccountUpdated", "new_status": "trial"}:
            ...
        case _:
            print("Omg, what is this?!")

