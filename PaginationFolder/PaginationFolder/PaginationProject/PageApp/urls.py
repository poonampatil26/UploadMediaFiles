from django.urls import path
from .views import add_mobile, update_mobile, show_mobile, delete_mobile, home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add/',add_mobile, name='add'),
    path('update/<int:id>/', update_mobile, name='update'),
    path('delete/<int:id>/', delete_mobile, name='delete'),
    path('show/', show_mobile, name='show'),
    path('home/', home, name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)