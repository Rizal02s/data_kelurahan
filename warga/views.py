from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# 🟢 Daftar semua warga
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'  # opsional, buat konteks di template lebih eksplisit


# 🟢 Detail satu warga (plus daftar pengaduan miliknya)
class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'


# 🟢 Daftar semua pengaduan + fitur filter & search
class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        status = self.request.GET.get('status')

        if q:
            queryset = queryset.filter(aduan__icontains=q)
        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by('-tanggal_aduan')



# ✳️ Tambah data warga
class WargaCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')


# ✳️ Edit data warga
class WargaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')


# ✳️ Hapus data warga
class WargaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')


# ✳️ Tambah data pengaduan
class PengaduanCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

    def form_valid(self, form):
        messages.success(self.request, "Pengaduan berhasil ditambahkan!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Terjadi kesalahan. Silakan periksa input Anda.")
        return super().form_invalid(form)


# ✳️ Edit data pengaduan
class PengaduanUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')


# ✳️ Hapus data pengaduan
class PengaduanDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')
