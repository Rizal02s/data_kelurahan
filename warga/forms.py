from django import forms
from .models import Warga, Pengaduan

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = ['nik', 'nama', 'alamat', 'no_telepon']


class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['aduan', 'isi', 'status', 'pelapor']
        widgets = {
            'isi': forms.Textarea(attrs={'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'pelapor': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_pelapor(self):
        pelapor = self.cleaned_data.get('pelapor')
        if pelapor is None:
            raise forms.ValidationError("Pelapor harus dipilih dari daftar warga terdaftar.")
        return pelapor
