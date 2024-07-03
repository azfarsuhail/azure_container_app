from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def creator():
    return {"creator": "Azfar Suhail"}
