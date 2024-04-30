from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    'http://localhost:3000',
    'http://localhost:5173',
    'http://localhost:9000',
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/todos")
def home():
    return [
        {"id": 1, "content": "a"},
        {"id": 2, "content": "b"},
        {"id": 3, "content": "c"},
    ]
