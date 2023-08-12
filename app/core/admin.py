"""
Admin site for core app.
"""

from django.contrib import admin

from core.models import *

admin.site.register(Student)