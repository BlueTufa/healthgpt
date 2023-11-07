import json

from common import log
from os import path
from starlette.requests import Request
from jose import jwt
from fastapi import HTTPException


class JwtBearerTokenAuthorizer:
    def __init__(self):
        self.jwk = None

    def __call__(self, request: Request):
        if self.jwk is None:
            with open(path.join(path.dirname(__file__), "public.jwk")) as key:
                self.jwk = json.loads(key.read())

        try:
            token = request.headers.get("Authorization")
            if not token:
                raise
            # by default, jose jwt will verify the signature,
            # expiration date, issuer, etc
            # simply hard-code the issuer for demo purposes
            jwt.decode(token, self.jwk, "RS256", {"verify_aud": True}, issuer="bluetufa.com")
        except Exception:
            log.warning("Authentication failed for ")
            raise HTTPException(
                status_code=401,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
