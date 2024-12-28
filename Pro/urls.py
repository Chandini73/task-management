from App import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from App.views import upload_image

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('register/', views.register, name='register'),
                  path('login', views.user_login, name='login'),
                  path("logout/", views.user_logout, name="logout"),
                  path('tasks/create/', views.create_task, name='create_task'),
                  path('tasks/update/<int:task_id>/', views.update_task, name='update_task'),
                  path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
                  path('task-chart/', views.task_chart, name='task_chart'),
                  path('', views.home, name='home'),
                  path('categories/create/', views.create_category, name='create_category'),
                  path('category_list', views.category_list, name='category_list'),
                  path('categories/<int:category_id>/', views.category_task, name='category_task'),
                  path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
                  path('upload_image', upload_image, name='upload_image'),
                  path('image-success/', views.image_success, name='image_success'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
