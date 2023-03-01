import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "5658502641:AAFg_0wViDGxf1h2JolViCOSfHfZk2Sd0K0")
BOT_NAME = getenv("BOT_NAME", "Nurlan")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LaylaBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("API_ID", "21432212"))
API_HASH = getenv("API_HASH", "e060eee264cc7570d2935323e3b6115d")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "elman")
OWNER_NAME = getenv("OWNER_NAME", "HEROGAMERS1")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AwesomeSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5096741943").split()))
