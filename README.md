Installation

Clone the repository to your local computer:

bash
Copy code
git clone https://github.com/TomaszCiesla/Calculator-BMI
Navigate to the project directory:

bash
Copy code
cd calculator-bmi
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate
Install the required dependencies:

Copy code
pip install -r requirements.txt
Run the database migrations:

Copy code
python manage.py migrate
Start the development server:

Copy code
python manage.py runserver
The application will be accessible at http://localhost:8000/.

========================================================================================================================================================================

Usage

Open a web browser and go to http://localhost:8000/.
Enter your weight (in kilograms) and height (in meters) in the respective fields.
Click the "Click here to check BMI" button.
Enter your weight (in kilograms), height (in meters), age, select gender, and choose the level of physical activity in the Calories Calculator fields.
Click the "Calculate Calories" button.
The application will display your BMI and provide an interpretation of the result, along with information regarding calorie intake.
========================================================================================================================================================================

Project Structure

.
├── calculator-bmi
│ ├── templates
│ │ └── my_site
│ │ └── base.html
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── .gitignore
├── manage.py
└── requirements.txt

calculator-bmi: The main directory of the application.
templates: Contains HTML templates.
base.html: Template for the main page.
settings.py: Django configuration file.
urls.py: Defines URL paths.
wsgi.py: Configuration file for the WSGI server.
manage.py: Script for managing the project.

========================================================================================================================================================================

Technologies
Python 3.11
Django 4.2.2

========================================================================================================================================================================

Authors:
Tomasz Dymek
Email: tomasdymek@gmail.com
GitHub: tomasdymek

Sylwia Pokrzywa
Email: sylwia.pokrzywa@gmail.com
GitHub: sylwiapokrzywa

Tomasz Cieśla
Email: tomasz.ciesla81@gmail.com
GitHub: TomaszCiesla

Agnieszka Lenart
Email: molines@op.pl
GitHub: AgnieszkaLenart24
