from django.contrib import admin
#Make the poll app modifiable in the admin
from .models import Question

admin.site.register(Question)