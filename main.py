from fastapi import FastAPI, HTTPException, status

app = FastAPI()

users = [
    {"id": 1, "email": "at@fsm.com", "name": "Alan Turing"},
    {"id": 2, "email": "gh@fsm.com", "name": "Grace Hopper"},
    {"id": 2, "email": "gh@fsm.com", "name": "Grace Hopper"},
]


async def get_user(email: str):
    for user in users:
        if user["email"] == email:
            return user
    return None


@app.get("/users")
async def get_users():
    return users
