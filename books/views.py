from django.shortcuts import render, redirect

from books.forms import AnimeBooksForm, BookUpdateForm, BookCreateForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def book_lists(request):
    if request.method == 'POST':
        form = AnimeBooksForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            title = request.POST.get('title')
            author = request.POST.get('author')
            published_date = request.POST.get('published_date')
            pages = request.POST.get('pages')
            form = AnimeBooksForm()
            form.save_m2m()
            return redirect("/")
    else:
        form = AnimeBooksForm()

    return render(request, 'index.html', {'form': form})


def book_create(request):
    form = BookCreateForm
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  # Redirect to a page displaying all books
    else:
        form = BookCreateForm()

    return render(request, 'index.html', {'form': form})


def book_update(request, id):
    form = BookUpdateForm
    if request.method == 'POST':
        form = BookUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            BookUpdateForm()
            return redirect("/")  # Redirect to a page displaying all books
    else:
        form = BookUpdateForm

    return render(request, 'index.html', {'form': form})
