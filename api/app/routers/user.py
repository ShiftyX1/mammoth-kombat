from fastapi import APIRouter


user_router = APIRouter()

@user_router.get("/")
def default_route():
    return {"msg": "Hello!!!"}