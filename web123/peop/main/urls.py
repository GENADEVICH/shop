from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('proddog', views.proddog, name='proddog'),
    path('gprodcat', views.gprodcat, name='gprodcat'),
    path('prodbird', views.prodbird, name='prodbird'),
    path('prodgriz', views.prodgriz, name='prodgriz'),
    path('reviews', views.reviews, name='reviews'),
    path('order', views.order, name='order')



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
