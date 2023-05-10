from fastapi import FastAPI

from data.router import router_ds

app = FastAPI()
app.include_router(router_ds)


@app.get("/")
async def root():
    return {"message": "Hello World"}
