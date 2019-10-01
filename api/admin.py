from api.mana.models import Mana, Episode
from django.contrib import admin
from api.user.models import User
from api.models import Url


admin.site.register(User)
admin.site.register(Mana)
admin.site.register(Episode)
admin.site.register(Url)
