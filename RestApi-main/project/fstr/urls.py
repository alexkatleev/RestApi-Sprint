from django.urls import path
from .views import PerevalList, submit_data, get_data, update_data, PerevalViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'submitData', PerevalViewSet)

urlpatterns = [
    path('api/submitData/', PerevalList.as_view(), name='pereval_list'),
    path('api/submitData/create/', submit_data, name='submit_data'),
    path('api/submitData/<int:pk>/', get_data, name='get_data'),
    path('api/submitData/<int:pk>/update/', update_data, name='update_data'),
]

urlpatterns += router.urls
