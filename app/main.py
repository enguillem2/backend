from fastapi import FastAPI,HTTPException
from routes.task import task


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



app.include_router(task)
