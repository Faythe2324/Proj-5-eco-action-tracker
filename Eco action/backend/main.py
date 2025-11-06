from fastapi import FastAPI
from backend.models import User, Action, Challenge
from backend.database import init_db
from fastapi.middleware.cors import CORSMiddleware

init_db()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/signup")
def signup(username: str, email: str, password: str):
    try:
        user = User(username, email, password)
        user.save()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.post("/login")
def login(username: str, password: str):
    user = User.login(username, password)
    if user:
        return dict(user)
    return {"status": "error", "detail": "Invalid credentials"}

@app.post("/action")
def perform_action(user_id: int, name: str, points: int, co2: float):
    action = Action(user_id, name, points, co2)
    action.save()
    leaderboard = User.get_leaderboard()
    return {"status": "success", "leaderboard": [dict(r) for r in leaderboard]}

@app.get("/challenges")
def get_challenges():
    return [dict(c) for c in Challenge.all()]

@app.post("/challenges/join")
def join_challenge(challenge_id: int, username: str):
    Challenge.join(challenge_id, username)
    return {"status": "joined"}
