from django.contrib import admin
from core.models import *
admin.site.register([Service,Contact,BlogCategory,Blogs,RepairChoices,Device,Client,Estimate])
