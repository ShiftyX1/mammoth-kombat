from fastapi import APIRouter

from models.user import User

from schemas.score import ScoreUpdate


click_router = APIRouter()

@click_router.post("/click")
async def click(data: ScoreUpdate):
    user = await User.get_or_none(username=data.username)
    if not user:
        user = await User.create(username=data.username)
    user.score += 1
    await user.save()
    return {"username": user.username, "score": user.score}

@click_router.get("/leaderboard")
async def leaderboard():
    return await User.all().order_by('-score').values('username', 'score')
