import os
import sys

# Путь к вашему проекту
path = '/home/afiyatenergy/afiyat-energy'
if path not in sys.path:
    sys.path.append(path)

# Активация виртуального окружения
activate_this = '/home/afiyatenergy/.virtualenvs/afiyat-env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
