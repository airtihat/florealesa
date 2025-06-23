from pathlib import Path
import os

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ لا تستخدم هذا المفتاح في بيئة الإنتاج!
SECRET_KEY = 'django-insecure-%p5hua%pco-0#0gu#a=ngsb4giig-392)2eo3@b_omkpl%ptrm'

# وضع التصحيح (يُفعل فقط أثناء التطوير)
DEBUG = True

# المجالات المسموح بها (تحديثها عند النشر)
ALLOWED_HOSTS = ['*']

# التطبيقات المثبتة
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'core',
    'storefront',
    'orders',
    'pages',  # ✅ تمت إضافة تطبيق الصفحات الثابتة
]

# الطبقات الوسيطة (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# رابط التوجيه الرئيسي
ROOT_URLCONF = 'florealesa.urls'

# إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # مجلد templates العام
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

# قاعدة البيانات (SQLite لتجربة محلية)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تحقق من كلمات المرور
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

# إعدادات الملفات الثابتة (CSS - JS - صور التصميم)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # لملفاتك الخاصة
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')    # لتجميع ملفات Django Admin وغيرها
# إعدادات الوسائط (صور المنتجات - المرفقات)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# إعادة التوجيه بعد تسجيل الدخول والخروج
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# نوع الحقل الافتراضي للمفاتيح الأساسية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
