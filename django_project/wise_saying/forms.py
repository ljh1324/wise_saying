from django import forms

from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('member_id', 'password', 'name')
        widgets = {
            'member_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'40자 이내'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'16자 이내'}),
        }

        labels = {
            'member_id': 'ID',
            'password': 'Password',
            'name': '이름'
        }

    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__( *args, **kwargs)
        self.fields['member_id'].widget.attrs['maxlength'] = 15
        self.fields['password'].widget.attrs['maxlength'] = 40
        self.fields['name'].widget.attrs['maxlength'] = 16


class MemberLoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('member_id', 'password')
        widgets = {
            'member_id': forms.TextInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'member_id': 'ID',
            'password': 'Password',
            'name': '이름'
        }

    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(MemberLoginForm, self).__init__( *args, **kwargs)
        self.fields['member_id'].widget.attrs['maxlength'] = 15
        self.fields['password'].widget.attrs['maxlength'] = 40