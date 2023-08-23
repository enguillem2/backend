from fastapi import FastAPI,HTTPException
from routes.task import task
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()

origins=[
    config('FRONTED_URL')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}



app.include_router(task)
