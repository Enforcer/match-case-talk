from typing import Any
import functools
from models import *
from models2 import *

from event_handlers.event_handler import event_handler



@event_handler.register
def handle_account_created(event: AccountCreated) -> None:
    ...


@event_handler.register
def handle_account_updated_to_paid(event: AccountUpdatedToPaid) -> None:
    ...


@event_handler.register
def handle_account_updated_to_trial(event: AccountUpdatedToTrial) -> None:
    print("GOT AccountUpdatedToTrial", event)


@event_handler.register
def handle_account_deleted(event: AccountDeleted) -> None:
    print("GOT AccountDeleted", event)

