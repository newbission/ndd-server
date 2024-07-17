import os

envget = lambda key: os.environ.get(key) 

GOOGLE_OAUTH2_CLIENT_ID = envget("GOOGLE_OAUTH2_CLIENT_ID")
GOOGLE_OAUTH2_CLIENT_SECRET = envget("GOOGLE_OAUTH2_CLIENT_SECRET")

KAKAO_OAUTH2_CLIENT_ID = envget("KAKAO_OAUTH2_CLIENT_ID")
KAKAO_OAUTH2_CLIENT_SECRET = envget("KAKAO_OAUTH2_CLIENT_SECRET")

HOST = envget("HOST")

OAUTH2_CLIENT_ID = {
    "kakao": envget("KAKAO_OAUTH2_CLIENT_ID"),
    "google": envget("GOOGLE_OAUTH2_CLIENT_ID"),
}

OAUTH2_CLIENT_SECRET = {
    "kakao": envget("KAKAO_OAUTH2_CLIENT_SECRET"),
    "google": envget("GOOGLE_OAUTH2_CLIENT_SECRET")
}

ACCESS_TOKEN_COOKIE_NAME = "ndd_access"