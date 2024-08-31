from models import *
from pydantic import TypeAdapter, Discriminator, Tag
from typing import Any, Annotated, Union

supported_model = (
    AccountCreated | AccountDeleted | AccountUpdated | Any
)
adapter = TypeAdapter(
    Annotated[
        Union[
            Annotated[AccountCreated, Tag("AccountCreated")],
            Annotated[AccountDeleted, Tag("AccountDeleted")],
            Annotated[AccountUpdated, Tag("AccountUpdated")],
        ],
        Discriminator(lambda v: v.get("type"))
    ]
)


def handle(payload: dict) -> None:
    # HAMMER TIME! 🔨
    event = adapter.validate_python(payload)  # Would also have to handle unknown differently

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
    for mes in c, d, u1, u2:
        handle(mes)
