from django.urls import reverse_lazy
import os
from pathlib import Path
from django.contrib.messages import constants as messages

import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "django_countries",
    "bootstrap4",
    "requests",
    "openpyxl",
]

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "blogs.apps.BlogsConfig",
    "news.apps.NewsConfig",
    "profiles.apps.ProfilesConfig",
    "articles.apps.ArticlesConfig",
    "comments.apps.CommentsConfig",
    "projects.apps.ProjectsConfig",
    "likes.apps.LikesConfig",
    "search.apps.SearchConfig",
    "polls.apps.PollsConfig",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

""" 기본 USER를 대체할 때 사용 (현재는 Default User 사용) """
# AUTH_USER_MODEL = "myapp.MyUser"
# AUTH_USER_MODEL = "users.User"


# 정적파일(Static files) - CSS, JavaScript, Images
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

# STATIC_ROOT라는 변수에 우리가 python manage.py collectstatic을 했을 때 경로를 지정해준 것임
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


# media 관련 설정
# MEDIA_URL은 주소창에 MEDIA 이하의 경로로 접근을 해야지 실제 MEDIA 파일에 접근가능함
# 예) 127.0.0.1:8000/MEDIA/TEST.jpg
# MEDIA_ROOT는 MEDIA 파일을 서버에 올렸을 때,어느경로에 지정이 될 것인지, 그 바닥에 있는 경로가 어디가 될것인지에 대한 정보
# 장고에서 이미지를 관리할 때 필요한 라이브러리가 있음 (pillow 설치: pip install pillow)
MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = reverse_lazy("core:home")
LOGOUT_REDIRECT_URL = reverse_lazy("users:login")
