from django.urls import path
from .views import home, aboutus, certificate, contactus, foundernote, work

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
    path('certificate/', certificate, name='certificate'),
    path('contactus/', contactus, name='contactus'),
    path('foundernote/', foundernote, name='foundernote'),
    path('work/', work, name='work'),
]
