from fastapi import FastAPI

from data.datasets.router import router_ds
from data.workout.router import router_wod

app = FastAPI()
app.include_router(router_ds)
app.include_router(router_wod)


@app.get("/")
async def root():
    return {"message": "Hello World"}
