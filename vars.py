# Add your details here and then deploy by clicking on HEROKU Deploy button
from os import environ

API_ID = int(environ.get("API_ID", "29435108"))
API_HASH = environ.get("API_HASH", "2d211eb63606dae1bcb413d57391b2de")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Sudo Users Configuration
SUDO_USERS = list(map(int, environ.get("SUDO_USERS", "6050965589").split(","))) if environ.get("SUDO_USERS", "") else []

# Admin Configuration - Has FULL and PERMANENT access
ADMIN_USERS = list(map(int, environ.get("ADMIN_USERS", "6050965589").split(","))) if environ.get("ADMIN_USERS", "") else []
