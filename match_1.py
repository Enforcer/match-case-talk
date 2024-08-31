def handle(payload: dict) -> None:
    # HAMMER TIME! 🔨
    match payload:
        case _:
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
