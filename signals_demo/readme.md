# Django Signals & Custom Classes Interview Solutions  

This repository contains solutions for Django signals and Python custom classes interview questions. The project demonstrates how Django signals work and includes a custom iterable `Rectangle` class.

---

## Project Structure  
django_signals_interviews/ │── signals_demo/ # Django app for signals demonstration │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── signals.py # Django signals implementation │ ├── tests.py │ ├── views.py │── manage.py # Django project management script │── README.md # Project documentation │── .gitignore # Ignoring unnecessary files like venv │── venv/ # Virtual environment (not tracked)



---

## How to Set Up and Run the Project  

### 1. Clone the Repository  
```bash
git clone <your-repo-url>
cd django_signals_interviews

2. Create a Virtual Environment & Install Dependencies
python -m venv venv
source venv/Scripts/activate  # On Windows
source venv/bin/activate      # On Mac/Linux
pip install -r requirements.txt

3. Run Migrations and Start the Django Server
python manage.py migrate
python manage.py runserver




---

### **How to Add This README to Your GitHub Repository**  

1. **Create the README File in VS Code**  
   - Open VS Code and navigate to your project directory.  
   - Create a new file named `README.md`.  
   - Copy and paste the above content into it.  
   - Save the file.  

2. **Add and Commit the README File Using Git**  
   Run the following commands in the terminal:  

   ```bash
   git add README.md
   git commit -m "Added project documentation in README"
   git push origin main  # Change 'main' if your branch is different



