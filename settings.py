ALLOWED_HOSTS = ['oil4us.com','https://oil4us.com/']
# another option
ALLOWED_HOSTS = ['*']


# static folder connection to your hosting server

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR,"static-in-env")

MEDIA_URL  = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")

CKEDITOR_UPLOAD_PATH = 'uploads_directory/'