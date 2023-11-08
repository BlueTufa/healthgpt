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
            # TODO: file I/O is not necessary here.  env var?
            with open(path.join(path.dirname(__file__), "public.jwk")) as key:
                self.jwk = json.loads(key.read())

        try:
            # TODO: scrape the Bearer token prefix, when present
            token = request.headers.get("Authorization")
            if not token:
                raise
            # by default, jose jwt will verify the signature,
            # expiration date, issuer, etc
            # simply hard-code the issuer for demo purposes
            jwt.decode(token, self.jwk, "RS256", {"verify_aud": True}, issuer="bluetufa.com")
        except BaseException as e:
            log.warning("JWT Authentication failed. %s", e)
            raise HTTPException(
                status_code=401,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )
