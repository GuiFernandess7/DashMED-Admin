from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("accounts.urls"), name="accounts_urls"),
    path('api/', include("app.urls"), name="api")
]
