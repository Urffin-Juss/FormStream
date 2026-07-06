from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    """Форма для заполнения анкеты торгового представителя"""

    class Meta:
        model = Application
        fields = [
            'operation_type',
            'payment_type',
            'client_name',
            'contact_person',
            'inn',
            'kpp',
            'legal_address',
            'actual_address',
            'delivery_address',
            'gps_coordinates',
            'contact_phone',
            'delivery_start_time',
            'delivery_end_time',
            'has_break',
            'break_start_time',
            'break_end_time',
        ]
        widgets = {
            'operation_type': forms.Select(attrs={'class': 'form-control'}),
            'payment_type': forms.Select(attrs={'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ООО "Ромашка"'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов Иван Иванович'}),
            'inn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '7701234567'}),
            'kpp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '770101001'}),
            'legal_address': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'г. Москва, ул. Тверская, д. 1'}),
            'actual_address': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'г. Москва, ул. Тверская, д. 1'}),
            'delivery_address': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'г. Москва, ул. Тверская, д. 1'}),
            'gps_coordinates': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '55.7558, 37.6176'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'}),
            'delivery_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'delivery_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'has_break': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'has_break'}),
            'break_start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'break_end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def clean_inn(self):
        """Валидация ИНН (должен быть 10 или 12 цифр)"""
        inn = self.cleaned_data.get('inn')
        if not inn.isdigit():
            raise forms.ValidationError("ИНН должен содержать только цифры")
        if len(inn) not in [10, 12]:
            raise forms.ValidationError("ИНН должен содержать 10 или 12 цифр")
        return inn

    def clean_kpp(self):
        """Валидация КПП (должен быть 9 цифр)"""
        kpp = self.cleaned_data.get('kpp')
        if not kpp.isdigit():
            raise forms.ValidationError("КПП должен содержать только цифры")
        if len(kpp) != 9:
            raise forms.ValidationError("КПП должен содержать 9 цифр")
        return kpp

    def clean(self):
        """Валидация связей между полями"""
        cleaned_data = super().clean()
        has_break = cleaned_data.get('has_break')
        break_start = cleaned_data.get('break_start_time')
        break_end = cleaned_data.get('break_end_time')

        if has_break:
            if not break_start or not break_end:
                raise forms.ValidationError("Если указан перерыв, нужно указать время начала и окончания")
            if break_start >= break_end:
                raise forms.ValidationError("Время начала перерыва должно быть раньше времени окончания")

        delivery_start = cleaned_data.get('delivery_start_time')
        delivery_end = cleaned_data.get('delivery_end_time')
        if delivery_start and delivery_end and delivery_start >= delivery_end:
            raise forms.ValidationError("Время начала доставки должно быть раньше времени окончания")

        return cleaned_data