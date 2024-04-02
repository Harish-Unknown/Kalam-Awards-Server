from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from models.Registration import Regsitration

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kalamawards2024:BofKJBCyqbuyqyXj@kalamawards.7ba0hpm.mongodb.net/?retryWrites=true&w=majority&appName=KalamAwards"

client = MongoClient(uri)
db = client.kalamAwards2k24
registrations = db.registrations

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"Message": "Hello World!"}


@app.post("/register")
def register(data: Regsitration):
    count = registrations.count_documents({})
    sub = data.subject[0:4].upper()
    org = data.organisationType[0:4].upper()
    if data.organisationType == "GovernmentAided":
        org = "GOAI"
    uuid = f"SAIKLA24-{org}-{sub}-{str(count).zfill(4)}"
    data.uid = uuid
    x = registrations.insert_one(dict(data))
    return {"success": x.acknowledged, "id": uuid}

