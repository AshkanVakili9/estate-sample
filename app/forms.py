from django import forms
from .models import FileRecord

class FileRecordForm(forms.ModelForm):
    class Meta:
        model = FileRecord
        fields = ['file_code', 'user', 'creator']
        labels = {
            'file_code': 'کد فایل',
            'user': 'کاربر',
            'creator': 'ثبت کننده',
        }
