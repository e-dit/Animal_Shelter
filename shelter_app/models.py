from django.db import models


ADMISSION_SUBJECT = (
    ('G', 'Gminna'),
    ('O', 'Osoba fizyczna'),
    ('SM', 'Straż Miejska'),
    ('P', 'Policja'),
    ('I', 'Inne'),
)

OUTCOME_SUBJECT = (
    ('O', 'Osoba fizyczna'),
    ('F', 'Fundacja'),
    ('S', 'Schronisko'),
    ('I', 'Inne'),
)


OUT_TYPE = (
    ('Z', 'Zaginiony'),
    ('A', 'Adoptowany'),
    ('W', 'Odebrany przez właściciela'),
    ('E', 'Eutanazja'),
    ('ZG', 'Zgon'),
)

VET_TYPE = (
    ('S', 'Szczepienie'),
    ('ZP', 'Zwalczanie pasożytów'),
    ('ZCH', 'Zabieg chirurgiczny'),
    ('SK', 'Sterylizacja/Kastracja'),
    ('I', 'Inne'),
)


class Animal(models.Model):
    name = models.CharField(max_length=64, null=False)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    chip_number = models.CharField(max_length=15, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Admission(models.Model):
    admission_date = models.DateField()
    a_name = models.CharField(max_length=64)
    a_address = models.CharField(max_length=128)
    a_subject = models.CharField(max_length=3, choices=ADMISSION_SUBJECT)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)


class Outcome(models.Model):
    type = models.CharField(max_length=32, choices=OUT_TYPE, null=False)
    outcome_date = models.DateField()
    o_name = models.CharField(max_length=64)
    o_address = models.CharField(max_length=128)
    subject_type = models.CharField(max_length=3, choices=OUTCOME_SUBJECT)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)


class VeterinaryTreatment(models.Model):
    treat_name = models.CharField(max_length=64)
    vet_type = models.CharField(max_length=3, choices=VET_TYPE)
    animal = models.ManyToManyField(Animal, through='Treatment')


class Treatment(models.Model):
    treat_date = models.DateField(null=False)
    date_of_expire = models.DateField(null=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)
    veterinary_treatment = models.ForeignKey(VeterinaryTreatment, on_delete=models.CASCADE, null=True)
