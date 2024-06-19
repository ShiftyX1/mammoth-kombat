from fastapi import APIRouter
from .user import user_router
from .auth import auth_router
from .clicker import click_router


main_router = APIRouter()


main_router.include_router(
    router=user_router,
    prefix="/user",
    tags=["User"]
)

main_router.include_router(
    router=auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

main_router.include_router(
    router=click_router,
    prefix="/clickapi",
    tags=["Clcik Logic"]
)
