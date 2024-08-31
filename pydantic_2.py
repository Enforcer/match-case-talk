from pydantic import BaseModel
from typing import Literal

data = {"type": "AccountCreated", "id": "64160ccb", "name": "Mateusz"}


class AccountCreated(BaseModel):
    type: Literal["AccountCreated"]
    id: str
    name: str

m = AccountCreated(type="BAZINGA", id="123", name="Seba")
print(repr(m))
# AccountCreated(type='AccountCreated', id='64160ccb', name='Mateusz')
