from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView

from shelter_app.forms import RegistrationForm, AnimalForm, AdmissionForm, OutcomeForm, HealthCareForm
from shelter_app.models import Animal, Admission, Outcome, VeterinaryTreatment, Treatment


class RegistrationView(View):
    """
    Form to register new user.
    """

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username, email, password)
            success_url = '/login/'
            return redirect(success_url)
        else:
            message = 'Nie udało się utworzyć użytkownika'
        return HttpResponse(message)


@method_decorator(login_required, name='dispatch')
class AnimalsView(ListView):
    """
    View that displays all animals.
    """

    model = Animal
    template_name = 'animals_list.html'
    paginate_by = 5
    animals = Animal.objects.all()


@method_decorator(login_required, name='dispatch')
class AnimalDetail(DetailView):
    """
    View that displays selected animal.
    """
    model = Animal
    template_name = 'animal.html'
    context_object_name = 'animal'


@method_decorator(login_required, name='dispatch')
class NewAnimalView(View):
    """
    Form witch creates new animal in database.
    """

    def get(self, request):
        form = AnimalForm()
        return render(request, 'animal_form.html', {'form': form})

    def post(self, request):
        form = AnimalForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date_of_birth = form.cleaned_data['date_of_birth']
            breed = form.cleaned_data['breed']
            gender = form.cleaned_data['gender']
            color = form.cleaned_data['color']
            chip_number = form.cleaned_data['chip_number']
            Animal.objects.create(name=name, date_of_birth=date_of_birth, breed=breed, gender=gender, color=color,
                                  chip_number=chip_number)

            return HttpResponseRedirect('/animals')


@method_decorator(login_required, name='dispatch')
class UpdateAnimalView(View):
    """
    Form witch updates animal in database.
    """

    def get(self, request, animal_id):
        animal = Animal.objects.get(pk=animal_id)
        form = AnimalForm(instance=animal)
        return render(request, 'update_animal_form.html', {'form': form, 'animal': animal})

    def post(self, request, animal_id):
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            date_of_birth = form.cleaned_data['date_of_birth']
            breed = form.cleaned_data['breed']
            gender = form.cleaned_data['gender']
            color = form.cleaned_data['color']
            chip_number = form.cleaned_data['chip_number']
            Animal.objects.filter(id=animal_id).update(name=name, date_of_birth=date_of_birth, breed=breed,
                                                       gender=gender, color=color, chip_number=chip_number)
            return HttpResponseRedirect(f'/animals/{animal_id}')


@method_decorator(login_required, name='dispatch')
class AdmissionView(View):
    """
    Form witch creates details for animal admission.
    """

    def get(self, request, animal_id):
            form = AdmissionForm()
            animal = Animal.objects.get(pk=animal_id)
            return render(request, 'admission_form.html', {'form': form, 'animal': animal})

    def post(self, request, animal_id):
        form = AdmissionForm(request.POST)
        Animal.objects.get(pk=animal_id)
        if form.is_valid():
            animal = Animal.objects.get(pk=animal_id)
            admission_date = form.cleaned_data['admission_date']
            a_name = form.cleaned_data['a_name']
            a_address = form.cleaned_data['a_address']
            a_subject = form.cleaned_data['a_subject']
            Admission.objects.create(animal_id=animal.pk, admission_date=admission_date, a_name=a_name,
                                     a_address=a_address, a_subject=a_subject)

            return HttpResponseRedirect(f'/animals/{animal_id}')


@method_decorator(login_required, name='dispatch')
class OutcomeView(View):
    """
    Form witch creates details for animal outcome.
    """

    def get(self, request, animal_id):
        form = OutcomeForm()
        animal = Animal.objects.get(pk=animal_id)
        return render(request, 'outcome_form.html', {'form': form, 'animal': animal})

    def post(self, request, animal_id):
        form = OutcomeForm(request.POST)
        if form.is_valid():
            animal = Animal.objects.get(pk=animal_id)
            type = form.cleaned_data['type']
            outcome_date = form.cleaned_data['outcome_date']
            o_name = form.cleaned_data['o_name']
            o_address = form.cleaned_data['o_address']
            subject_type = form.cleaned_data['subject_type']
            Outcome.objects.create(animal_id=animal.pk, type=type, outcome_date=outcome_date, o_name= o_name,
                                   o_address=o_address, subject_type=subject_type)
            animal = Animal.objects.get(id=animal_id)
            animal.is_active = False
            animal.save()

            return HttpResponseRedirect(f'/animals/{animal_id}')


@method_decorator(login_required, name='dispatch')
class HealthCareView(View):
    """
    Form witch creates veterinary treatments for animal.
    """
    def get(self, request, animal_id):
        form = HealthCareForm()
        animal = Animal.objects.get(pk=animal_id)
        return render(request, 'health_care.html', {'form': form, 'animal': animal})

    def post(self, request, animal_id):
        form = HealthCareForm(request.POST)
        if form.is_valid():
            animal = Animal.objects.get(pk=animal_id)
            treat_name = form.cleaned_data['treat_name']
            vet_type = form.cleaned_data['vet_type']
            treat_date = form.cleaned_data['treat_date']
            date_of_expire = form.cleaned_data['date_of_expire']
            veterinary_treatment = VeterinaryTreatment.objects.create(treat_name=treat_name, vet_type=vet_type)
            Treatment.objects.create(animal_id=animal.pk, veterinary_treatment=veterinary_treatment,
                                     treat_date=treat_date, date_of_expire=date_of_expire)

            return HttpResponseRedirect(f'/animals/{animal_id}')
