from library.models import CustomerUser, Books, Loan
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime, timedelta, timezone



def all_books(request):
    all_books = Books.objects.all()
    context = {
        'books': all_books
    }
    return render(request, 'all_books.html', context)


def single_book(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        book = None
    context = {'book': book}
    return render(request, 'single_book.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('all_books')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('all_books')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        city = request.POST.get('city')
        age = request.POST.get('age')

        if CustomerUser.objects.filter(username=username).exists():
            messages.error(
                request, 'Username already exists. Please choose a different username.')
            return redirect('register')

        customer = CustomerUser(username=username, city=city, age=age)
        customer.set_password(password)
        customer.save()

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')

    return render(request, 'register.html')

def search_book(request):
    query = request.GET.get('query')
    if query:
        books = Books.objects.filter(name__icontains=query)
    else:
        books = []

    context = {'books': books, 'query': query}
    return render(request, 'search_book.html', context)





def my_loans(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'my_loans.html', {'message': 'You have to log in first.'})

    loans = Loan.objects.filter(customer=user)
    current_date = datetime.now().date()

    for loan in loans:
        if loan.return_date:
            days_left = (loan.return_date - current_date).days
            loan.days_left = max(days_left, 0)
        else:
            loan.days_left = None

    context = {
        'loans': loans,
    }
    return render(request, 'my_loans.html', context)

@staff_member_required
def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        year_published = request.POST.get('year_published')
        Books.objects.create(name=name, author=author, year_published=year_published)
        return redirect('all_books')

    return render(request, 'add_book.html')

@login_required(login_url='login')
def loan_book(request, book_id):
    user = request.user
    book = Books.objects.get(id=book_id)

    loan_type = int(request.POST.get('loan_type'))
    loan_days = 0

    if loan_type == 1:
        loan_days = 10
    elif loan_type == 2:
        loan_days = 5
    elif loan_type == 3:
        loan_days = 2

    loan_date = datetime.now().date()
    return_date = loan_date + timedelta(days=loan_days)

    loan = Loan.objects.create(
        customer=user,
        book=book,
        loan_date=loan_date,
        return_date=return_date,
        loan_type=loan_type
    )

    return redirect('my_loans')


def remove_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    
    if request.user.is_superuser:
        book.delete()
    
    return redirect('all_books')

def update_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)

    if request.method == 'POST':
    
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.year_published = request.POST.get('year_published')
        book.image = request.POST.get('image')
        book.save()
        return redirect('all_books')

    return render(request, 'update_book.html', {'book': book})


@login_required(login_url='not_logged_in') 
def return_book(request, loan_id):
    if request.method == 'POST':
        try:
            loan = Loan.objects.get(id=loan_id)
            if loan.customer == request.user:
                loan.delete()
                return redirect('my_loans')

        except Loan.DoesNotExist:
            return render(request, 'my_loans.html') 

    return redirect('my_loans')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def contact(request):
    return render(request, 'contact.html')