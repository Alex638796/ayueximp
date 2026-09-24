import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    ADMIN_ID = int(os.environ.get("ADMIN_ID", "0"))
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    TXT_LOG = int(os.environ.get("TXT_LOG", "0"))
    AUTH_LOG = int(os.environ.get("AUTH_LOG", "0"))
    HIT_LOG = int(os.environ.get("HIT_LOG", "0"))
    DRM_DUMP = int(os.environ.get("DRM_DUMP", "0"))
    CHANNEL = int(os.environ.get("CHANNEL", "0"))
    CH_URL = os.environ.get("CH_URL", "")
    OWNER = os.environ.get("OWNER", "")
    THUMB_URL = os.environ.get("THUMB_URL", "")
    HOST = os.environ.get("HOST", "https://api.masterapi.tech")
