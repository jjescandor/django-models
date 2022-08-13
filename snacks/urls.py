from django.urls import path
from .views import SnackList, SnackDetail, AboutView

urlpatterns = [
    path('snack', SnackList.as_view(), name="snack_list"),
    path('<int:pk>', SnackDetail.as_view(), name='snack_detail'),
    path('about', AboutView.as_view(), name='about'),
]