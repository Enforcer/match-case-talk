from models import *
from models2 import *
from pydantic import TypeAdapter
from typing import Any
from event_handlers import event_handler


def handle(payload: dict) -> None:
    supported_model = (
        AccountCreated | AccountDeleted | AccountUpdatedToTrial | AccountUpdatedToPaid | Any
    )
    adapter = TypeAdapter(supported_model)
    event = adapter.validate_python(payload)

    event_handler(event)

    print(repr(locals().get('event')))


from messages import c, d, u1, u2, mal
for mes in c, d, u1, u2, mal:
    handle(mes)

