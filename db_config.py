# db_config.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pos_db',
        'USER': 'asauser',
        'PASSWORD': '#FRU2003',
        'HOST': 'evfrupos-db.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}
