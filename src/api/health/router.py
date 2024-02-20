from fastapi import APIRouter


router_health = APIRouter(
    prefix="/health",
    tags=["Health Check"]
)


@router_health.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"msg": "pong!"}

