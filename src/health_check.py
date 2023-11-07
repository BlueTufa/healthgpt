from util.common import log
from fastapi.routing import APIRouter

router = APIRouter()

# Healthcheck - not authenticated
@router.get("/")
async def get_health():
    log.debug("Health check was called")
    return {"Health": "OK"}
