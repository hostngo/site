from django.urls import path
from .views import home, aboutus, certificate, contactus, foundernote, work, login, admin_panel

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
    path('certificate/', certificate, name='certificate'),
    path('contactus/', contactus, name='contactus'),
    path('foundernote/', foundernote, name='foundernote'),
    path('work/', work, name='work'),
    path('login/', login, name='login'),
    path('admin-panel/', admin_panel, name='admin_panel'),
]
