"""Test settings: SQLite in memory, local storage, no external services."""
import os

os.environ.setdefault("SECRET_KEY", "test-secret-key")
os.environ.setdefault("CLOUDINARY_URL", "cloudinary://test:test@test")

from .settings import *  # noqa: E402,F401,F403

DEBUG = False
ALLOWED_HOSTS = ["testserver", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

CLOUDINARY_STORAGE = {"CLOUD_NAME": "test", "API_KEY": "test", "API_SECRET": "test"}
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
