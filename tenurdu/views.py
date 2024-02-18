from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib import messages
from .models import Standard, Subject, Youtube, Qpaper, Notes, Books, Contactinfo
from .filters import ContentFilter

# Create your views here.
def home(request):
    # content = Content.objects.all()
    subjects = Subject.objects.all()
    standard = Standard.objects.all()
    youtube = Youtube.objects.all()
    filter_instance = ContentFilter(request.GET, queryset=youtube)
    if filter_instance.form.is_valid():
        selected_subjects = filter_instance.form.cleaned_data.get('subject')
        selected_standard = filter_instance.form.cleaned_data.get('standard')
    else:
        # Handle the case when the form is not valid
        selected_subjects = None
        selected_standard = None
    return render(request, 'tenurdu/index.html', {'filter':filter_instance, 'subjects':subjects, 'standard':standard, 'youtube':filter_instance.qs, 'selected_subjects': selected_subjects, 'selected_standard': selected_standard})


def qpaper(request):
    qpapers = Qpaper.objects.all()
    subjects = Subject.objects.all()
    standard = Standard.objects.all()
    filter_instance = ContentFilter(request.GET, queryset=qpapers)
    if filter_instance.form.is_valid():
        selected_subjects = filter_instance.form.cleaned_data.get('subject')
        selected_standard = filter_instance.form.cleaned_data.get('standard')
    else:
        # Handle the case when the form is not valid
        selected_subjects = None
        selected_standard = None
    return render(request, 'tenurdu/qpaper.html', {'filter':filter_instance, 'subjects':subjects, 'standard':standard, 'qpapers':filter_instance.qs, 'selected_subjects': selected_subjects, 'selected_standard': selected_standard})


def notes(request):
    notes = Notes.objects.all()
    subjects = Subject.objects.all()
    standard = Standard.objects.all()
    filter_instance = ContentFilter(request.GET, queryset=notes)
    if filter_instance.form.is_valid():
        selected_subjects = filter_instance.form.cleaned_data.get('subject')
        selected_standard = filter_instance.form.cleaned_data.get('standard')
    else:
        # Handle the case when the form is not valid
        selected_subjects = None
        selected_standard = None
    return render(request, 'tenurdu/notes.html', {'filter':filter_instance, 'subjects':subjects, 'standard':standard, 'notes':filter_instance.qs, 'selected_subjects': selected_subjects, 'selected_standard': selected_standard})


def books(request):
    books = Books.objects.all()
    subjects = Subject.objects.all()
    standard = Standard.objects.all()
    filter_instance = ContentFilter(request.GET, queryset=books)
    if filter_instance.form.is_valid():
        selected_subjects = filter_instance.form.cleaned_data.get('subject')
        selected_standard = filter_instance.form.cleaned_data.get('standard')
    else:
        # Handle the case when the form is not valid
        selected_subjects = None
        selected_standard = None
    return render(request, 'tenurdu/books.html', {'filter':filter_instance, 'subjects':subjects, 'standard':standard, 'books':filter_instance.qs, 'selected_subjects': selected_subjects, 'selected_standard': selected_standard})


def about(request):
    return render(request,'tenurdu/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        Contactinfo.objects.create(name=name, email=email, message=message)

        # You can also add additional logic or redirect the user to a thank you page
        messages.success(request, "Thanks for submitting the form")
    return render(request,'tenurdu/contact.html')

def policy(request):
    return render(request,'tenurdu/policy.html')

def terms(request):
    return render(request,'tenurdu/terms.html')

def disclaimer(request):
    return render(request,'tenurdu/disclaimer.html')

def contactinfo(request):
    contact_entries = Contactinfo.objects.all()
    return render(request, 'tenurdu/contactinfo.html', {'contact_entries': contact_entries})

def delete_contact_entry(request, entry_id):
    entry = get_object_or_404(Contactinfo, id=entry_id)
    entry.delete()
    return redirect(contactinfo)