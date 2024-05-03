from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib import messages
from .models import Standard, Subject, Youtube, Qpaper, Notes, Books, Contactinfo, GalleryImage
from .filters import ContentFilter
from django.core.paginator import Paginator

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

    paginator = Paginator(filter_instance.qs, 7)
    page_number = request.GET.get('page')
    YoutubeData = paginator.get_page(page_number)
    totalpage = YoutubeData.paginator.num_pages
    
    images = GalleryImage.objects.all()  

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        Contactinfo.objects.create(name=name, email=email, message=message)

        # You can also add additional logic or redirect the user to a thank you page
        messages.success(request, "Thanks for submitting the form")

    return render(request, 'index.html', {'filter':filter_instance, 'subjects':subjects, 'standard':standard, 'youtube':YoutubeData, 'selected_subjects': selected_subjects, 'selected_standard': selected_standard, 'lastpage':totalpage, 'totalPageList':[n+1 for n in range(totalpage)], 'images': images})


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

    paginator = Paginator(filter_instance.qs, 7)
    page_number = request.GET.get('page')
    QpaperData = paginator.get_page(page_number)
    totalpage = QpaperData.paginator.num_pages

    images = GalleryImage.objects.all()  
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        Contactinfo.objects.create(name=name, email=email, message=message)

        # You can also add additional logic or redirect the user to a thank you page
        messages.success(request, "Thanks for submitting the form")
          
    return render(request, 'qpaper.html', {'filter':filter_instance, 'subjects':subjects, 'standard':standard, 'qpapers':QpaperData, 'selected_subjects': selected_subjects, 'selected_standard': selected_standard, 'lastpage':totalpage, 'totalPageList':[n+1 for n in range(totalpage)], 'images': images})


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

    paginator = Paginator(filter_instance.qs, 7)
    page_number = request.GET.get('page')
    NotesData = paginator.get_page(page_number)
    totalpage = NotesData.paginator.num_pages

    images = GalleryImage.objects.all()  

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        Contactinfo.objects.create(name=name, email=email, message=message)

        # You can also add additional logic or redirect the user to a thank you page
        messages.success(request, "Thanks for submitting the form")
          
    return render(request, 'notes.html', {'filter':filter_instance, 'subjects':subjects, 'standard':standard, 'notes':NotesData, 'selected_subjects': selected_subjects, 'selected_standard': selected_standard, 'lastpage':totalpage, 'totalPageList':[n+1 for n in range(totalpage)], 'images': images})


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

    paginator = Paginator(filter_instance.qs, 7)
    page_number = request.GET.get('page')
    BooksData = paginator.get_page(page_number)
    totalpage = BooksData.paginator.num_pages

    images = GalleryImage.objects.all()  
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        Contactinfo.objects.create(name=name, email=email, message=message)

        # You can also add additional logic or redirect the user to a thank you page
        messages.success(request, "Thanks for submitting the form")
          
    return render(request, 'books.html', {'filter':filter_instance, 'subjects':subjects, 'standard':standard, 'books':BooksData, 'selected_subjects': selected_subjects, 'selected_standard': selected_standard, 'lastpage':totalpage, 'totalPageList':[n+1 for n in range(totalpage)], 'images': images})


def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        Contactinfo.objects.create(name=name, email=email, message=message)

        # You can also add additional logic or redirect the user to a thank you page
        messages.success(request, "Thanks for submitting the form")
    return render(request,'contact.html')

def policy(request):
    return render(request,'policy.html')

def terms(request):
    return render(request,'terms.html')

def disclaimer(request):
    return render(request,'disclaimer.html')

def contactinfo(request):
    contact_entries = Contactinfo.objects.all()
    return render(request, 'contactinfo.html', {'contact_entries': contact_entries})

def delete_contact_entry(request, entry_id):
    entry = get_object_or_404(Contactinfo, id=entry_id)
    entry.delete()
    return redirect(contactinfo)

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})