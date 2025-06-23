from pathlib import Path
import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# المفتاح السري
SECRET_KEY = os.getenv("SECRET_KEY", "insecure-key-if-not-set")

# وضع التصحيح
DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1", "yes"]

# النطاقات المسموح بها
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    # تطبيقات المشروع
    'core',
    'storefront',
    'orders',
    'pages',
    'products',
]

# الطبقات الوسيطة
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# إعداد المسارات
ROOT_URLCONF = 'florealesa.urls'

# إعداد القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# إعداد WSGI
WSGI_APPLICATION = 'florealesa.wsgi.application'

# إعداد قاعدة البيانات
if DEBUG:
    # قاعدة بيانات SQLite محليًا
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # قاعدة بيانات PostgreSQL عند النشر
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'db_florealesa'),
            'USER': os.getenv('DB_USER', 'db_florealesa_user'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'wOgaZRDSklNPMqIMtzneQC7bVV8DC4s5'),
            'HOST': os.getenv('DB_HOST', 'dpg-d1c1688dl3ps73f5llng-a.db.render.com'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

    # تأكيد وجود ENGINE لتفادي خطأ ImproperlyConfigured
    if not DATABASES["default"].get("ENGINE"):
        DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql"

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# إعدادات الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# إعدادات ملفات الوسائط
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# التوجيه بعد تسجيل الدخول والخروج
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# إعداد الحقول التلقائية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
