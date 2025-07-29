# Add your details here and then deploy by clicking on HEROKU Deploy button
from os import environ

API_ID = int(environ.get("API_ID", "28329455"))
API_HASH = environ.get("API_HASH", "9de39a5d0a350cacfceb3e1bace9a40d")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Sudo Users Configuration
SUDO_USERS = list(map(int, environ.get("SUDO_USERS", "7526345865").split(","))) if environ.get("SUDO_USERS", "") else []

# Admin Configuration - Has FULL and PERMANENT access
ADMIN_USERS = list(map(int, environ.get("ADMIN_USERS", "7611019705").split(","))) if environ.get("ADMIN_USERS", "") else []
