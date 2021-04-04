# بازم خودتی :=)

from django.contrib import admin
from Damasanj.models import *
al = [
    Feedback,
    SFile

    ]

admin.site.register(Lesson)
admin.site.register(Dor)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Role)
admin.site.register(door)
for q in al:
    admin.site.register(q)

