from pydantic import BaseModel

data = {"type": "AccountCreated", "id": "64160ccb", "name": "Mateusz"}


class AccountCreated(BaseModel):
    type: str
    id: str
    name: str

m = AccountCreated(**data)
print(repr(m))
# AccountCreated(type='AccountCreated', id='64160ccb', name='Mateusz')
