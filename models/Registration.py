from typing import Union
from pydantic import BaseModel
from typing import Literal
from datetime import datetime


class Regsitration(BaseModel):
    uid: Union[str, None] = None
    nominationType: Literal["Teacher","Student"]
    organisationType: Literal["Matriculation", "Government", "CBSE", "GovernmentAided", "International"]
    fullName: str
    gender: Literal["Male", "Female"]
    aadharNumber: str
    schoolName: str
    dob: str
    schoolRegistrationNumber: str
    location: str
    schoolContactNumber: str
    address: str
    contactPersonNumber: str
    district: str
    subject: Literal["Tamil", "English", "Maths", "Science", "Social", "Computer Science"]
    schoolEmailId: str
    emailId: str
    mobileNumber: str
    landline: str

    class Config:
        schema_extra = {
            "example": {
                "uid": "dfadf",
                "nominationType": "Teacher",
    "organisationType":"Private", 
    "fullName": "Kalam",
    "gender": "Male",
    "aadharNumber": "dafsdf",
    "schoolName": "fasdfa",
    "dob": 24234234,
    "schoolRegistrationNumber": "str",
    "location": "str",
    "schoolContactNumber": "str",
    "address": "str",
    "contactPersonNumber": "str",
    "district": "str",
    "subject": "Tamil",
    "schoolEmailId": "str",
    "emailId": "str",
    "mobileNumber": "str",
    "landline": "str",
            }
        }