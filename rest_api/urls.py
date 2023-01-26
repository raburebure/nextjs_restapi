from django.contrib import  admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # api直下のurls.pyで定義したurlへのアクセスを可とさせる
    path('api/', include('api.urls')),
]
