from pydantic import BaseModel

class ChannelPartnerCreate(BaseModel):
    name: str
    person_of_contact: str
    email: str
    mobile: str