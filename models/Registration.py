from typing import Union
from pydantic import BaseModel
from typing import Literal
from datetime import datetime


class Regsitration(BaseModel):
    uid: Union[str, None] = None
    nominationType: Literal["Teacher","School","Principal"]
    organisationType: Literal["Matriculation", "Government", "CBSE", "GovernmentAided", "International"]
    fullName: str
    gender: Literal["Male", "Female"]
    aadharNumber: str
    schoolName: str
    dob: str
    schoolRegistrationNumber: str
    location: str
    schoolContactNumber: str
    contactPersonNumber: str
    emailId: str
    landline: str

    class Config:
        schema_extra = {
            "example": {
                "uid": "dfadf",
                "nominationType": "Teacher",
    "organisationType":"Matriculation", 
    "fullName": "Kalam",
    "gender": "Male",
    "aadharNumber": "dafsdf",
    "schoolName": "fasdfa",
    "dob": 24234234,
    "schoolRegistrationNumber": "str",
    "location": "str",
    "schoolContactNumber": "str",
    "contactPersonNumber": "str",
    "emailId": "str",
    "landline": "str",
            }
        }