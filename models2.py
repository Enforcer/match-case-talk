from pydantic import BaseModel
from typing import Literal


class AccountCreated(BaseModel):
    type: Literal["AccountCreated"]
    id: str
    name: str


class AccountDeleted(BaseModel):
    type: Literal["AccountDeleted"]
    id: str


class AccountUpdated(BaseModel):
    type: Literal["AccountUpdated"]
    id: str
    old_status: Literal["trial", "paid"]
    new_status: Literal["trial", "paid"]


class AccountUpdatedToPaid(BaseModel):
    type: Literal["AccountUpdated"]
    id: str
    old_status: Literal["trial"]
    new_status: Literal["paid"]


class AccountUpdatedToTrial(BaseModel):
    type: Literal["AccountUpdated"]
    id: str
    old_status: Literal["paid"]
    new_status: Literal["trial"]


#print(repr(AccountUpdated(type="AccountUpdated", id="123", old_status="paid", new_status="trial")))
