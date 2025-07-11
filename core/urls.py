# from django.urls import path
# from .views import TaskListCreate, TaskDetail

# urlpatterns = [
#     path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
#     path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
# ]

from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = router.urls
