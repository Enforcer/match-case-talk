from models import *


def handle(payload: dict) -> None:
    # HAMMER TIME! 🔨
    match payload:
        case {"type": "AccountCreated"}:
            event = AccountCreated(**payload)
        case {"type": "AccountDeleted"}:
            event = AccountDeleted(**payload)
        case {"type": "AccountUpdated", "new_status": "paid"}:
            event = AccountUpdated(**payload)
        case {"type": "AccountUpdated", "new_status": "trial"}:
            event = AccountUpdated(**payload)
        case _:
            print("Omg, what is this?!")

    print(locals().get('event'))


from messages import c, d, u1, u2, mal
for mes in c, d, u1, u2, mal:
    handle(mes)

