from fastapi import FastAPI

from .routers.channel_partner import router as channel_partner_router


app = FastAPI()


app.include_router(channel_partner_router)


@app.get("/")
def root():
    return {
        "message": "Channel Partner API is running"
    }