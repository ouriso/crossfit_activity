from fastapi import FastAPI

from data.router import router_wod

app = FastAPI()
app.include_router(router_wod)


@app.get("/")
async def root():
    return {"message": "Hello World"}
