from models import *
from pydantic import TypeAdapter, Discriminator, Tag, ValidationError
from typing import Annotated, Union, assert_never

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
    try:
        event = adapter.validate_python(payload)
    except ValidationError:
        # unhandled message
        print("Omg, what is this?!")
        return

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
            assert_never("This should never happen")


if __name__ == "__main__":
    from messages import c, d, u1, u2, mal
    for mes in c, d, u1, u2, mal:
        handle(mes)
