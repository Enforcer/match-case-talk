from models import *
from pydantic import TypeAdapter
from typing import Any

supported_model = (
    AccountCreated | AccountDeleted | AccountUpdated | Any
)
adapter = TypeAdapter(supported_model)


def handle(payload: dict) -> None:
    # HAMMER TIME! 🔨
    event = adapter.validate_python(payload)

    match event:
        case AccountCreated():
            ...
        case AccountDeleted():
            ...
        case AccountUpdated(new_status="paid"):
            ...
        case AccountUpdated(new_status="trial"):
            ...
        case _:
            print("Omg, what is this?!")


if __name__ == "__main__":
    from messages import c, d, u1, u2, mal
    for mes in c, d, u1, u2, mal:
        handle(mes)
