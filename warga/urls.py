from django.urls import path
from .views import WargaListView, WargaDetailView, PengaduanListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),  # /warga/
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),  # /warga/pengaduan/
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),  # /warga/1/
]
