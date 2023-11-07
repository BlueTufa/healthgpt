#! /usr/bin/env python
from os import path

import json
import time
import uuid
from jose import jwt
from jose.constants import ALGORITHMS


def mint_bearer_token():
    seconds_since_epoch = round(time.time(), 0)
    # expires in 1 year
    expiration_time_since_epoch = round(seconds_since_epoch + 60 * 60 * 24 * 365)
    jti_id = str(uuid.uuid4())

    with open(path.join(path.dirname(__file__), "keypair.jwk")) as key:
        jwk = json.loads(key.read())
    claim = jwt.encode(
        {
            "sub": "testuser",
            "auth_time": seconds_since_epoch,
            "iss": "bluetufa.com",
            "exp": expiration_time_since_epoch,
            "iat": seconds_since_epoch,
            "jti": jti_id,
        },
        jwk,
        ALGORITHMS.RS256,
    )

    print(claim)


if __name__ == "__main__":
    mint_bearer_token()
