import uvicorn

from fastapi import FastAPI

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from util.common import log
from search import router as search_router
from health_check import router as health_check_route

limiter = Limiter(key_func=get_remote_address, default_limits=["300/minute"])

app = FastAPI()
app.include_router(health_check_route)
app.include_router(search_router, prefix="/timeline")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# for local debugging only
if __name__ == "__main__":
    log.debug("App startup from command line")
    uvicorn.run("api:app", host="0.0.0.0", port=8001, reload=True)
