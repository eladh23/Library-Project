# My Library Project

Welcome to the My Library project! 
This is a Django-based web application for managing a library's books collection and loans.

# Features

- Users can register and log in to the system.
- Registered users can borrow books from the library.
- Administrators can add, update, and remove books from the library.
- Users can search for books in the library.
- Users can view their borrowed books and their due dates.

# Links

- **Project on Render:** : https://django-library-if60.onrender.com
- **GitHub Repository:** : https://github.com/eladh23/Library-Project

# Usage

1. Visit the https://django-library-if60.onrender.com to access the web application.
2. Log in using your registered user credentials:
    - **User Credentials:** Username: 'elad_admin' | Password: 123
    - **Admin Credentials:** Username: elad_user | Password: 12345

3. Browse the collection of books, borrow loans , and view your loans.
4. Administrators can access additional features such as adding and updating books.


# Preparation Instructions for the Programmer

Follow these steps to set up and run the My Library project on your local development environment:

1. **Clone the Repository:**
git clone https://github.com/eladh23/Library-Project

2. **Navigate to the Project Directory:**
cd my-library

3. **Create a Virtual Environment:**
python -m venv venv

4. **Activate the Virtual Environment:**
- On macOS and Linux:
  `source venv/bin/activate`

- On Windows:
   `venv\Scripts\activate`
  

5. **Install Dependencies:**
pip install -r requirements.txt

6. **Apply Database Migrations:**
python manage.py migrate


7. **Create a Superuser (Admin User):**
python manage.py createsuperuser

8. **Run the Development Server:**
python manage.py runserver

9. **Access the Application:**
Open a web browser and go to `http://127.0.0.1:8000` (with using : `python manage.py runserver`)
to access the My Library application.

10. **Log in with Admin Credentials:**
 - Username: `admin`
 - Password: `adminpassword`

# Have fun!
