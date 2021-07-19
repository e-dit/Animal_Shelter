from django import forms
from django.contrib.auth.models import User

from shelter_app.models import Animal


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "wprowadzono różne hasła"
            )


class AnimalForm(forms.ModelForm):
    chip_number = forms.IntegerField(required=False)

    class Meta:
        model = Animal
        fields = ['name', 'date_of_birth', 'breed', 'gender', 'color', 'chip_number']
        labels = {
            'name': ('Imię zwierzęcia:'),
            'date_of_birth': ('Rok urodzenia:'),
            'breed': ('Rasa:'),
            'gender': ('Płeć:'),
            'color': ('Umaszczenie:'),
            'chip_number': ('Numer chip:'),
        }

        help_texts = {
            'chip_number': ('Chip musi zawierać 15 znaków.'),
        }


class AdmissionForm(forms.Form):
    admission_date = forms.DateField(label='Data przyjęcia:',  widget=forms.SelectDateWidget)
    a_name = forms.CharField(label="Nazwa oddającego zwierzę:", max_length=64)
    a_address = forms.CharField(label="Adres oddającego:", max_length=128,
                                    widget=forms.TextInput(attrs={'size': '128'}))
    ADMISSION_SUBJECT = (
        ('G', 'Gminna'),
        ('O', 'Osoba fizyczna'),
        ('SM', 'Straż Miejska'),
        ('P', 'Policja'),
        ('I', 'Inne'),
    )
    a_subject = forms.ChoiceField(label="Rodzaj podmiotu:", choices=ADMISSION_SUBJECT, widget=forms.RadioSelect)


class OutcomeForm(forms.Form):
    OUT_TYPE = (
        ('Z', 'Zaginiony'),
        ('A', 'Adoptowany'),
        ('W', 'Odebrany przez właściciela'),
        ('E', 'Eutanazja'),
        ('ZG', 'Zgon'),
    )
    type = forms.ChoiceField(label='Powód wydania:', choices=OUT_TYPE)
    outcome_date = forms.DateField(label='Data wydania:', widget=forms.SelectDateWidget)
    o_name = forms.CharField(label='Podmiot odbierający:', required=False)
    o_address = forms.CharField(label='Adres odbierającego:', max_length=128, required=False,
                                widget=forms.TextInput(attrs={'size': '128'}))
    OUTCOME_SUBJECT = (
        ('O', 'Osoba fizyczna'),
        ('F', 'Fundacja'),
        ('S', 'Schronisko'),
        ('I', 'Inne'),
    )
    subject_type = forms.ChoiceField(label='Typ odbierającego:', required=False, choices=OUTCOME_SUBJECT)
    is_active = forms.BooleanField(required=False)


class HealthCareForm(forms.Form):
    treat_name = forms.CharField(label="Nazwa zabiegu:")
    VET_TYPE = (
        ('S', 'Szczepienie'),
        ('ZP', 'Zwalczanie pasożytów'),
        ('ZCH', 'Zabieg chirurgiczny'),
        ('SK', 'Sterylizacja/Kastracja'),
        ('I', 'Inne'),
    )
    vet_type = forms.ChoiceField(label="Rodzaj zabiegu:", choices=VET_TYPE)
    treat_date = forms.DateField(label="Data zabiegu:", widget=forms.SelectDateWidget)

    OUT_TYPE = (
        ('Z', 'Zaginiony'),
        ('A', 'Adoptowany'),
        ('W', 'Odebrany przez właściciela'),
        ('E', 'Eutanazja'),
        ('ZG', 'Zgon'),
    )
    date_of_expire = forms.DateField(label="Ważność wygasa:", required=False)
