from fastapi import FastAPI

app = FastAPI()

@app.get("/auctionhouse")
def home():
    return{"data": "test"}

