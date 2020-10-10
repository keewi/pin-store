# pin-store

# Setup
Clone the repo and navigate to the folder in your terminal. Then, follow the steps below to set up your environment based on your OS.
## MacOS
1. Install python: `python -m pip install --upgrade pip`
2. Install virtualenv: `python3 -m pip install --user virtualenv`
3. Create your new virtual environment: `python3 -m venv env` (Note: You can change `env` to the name you'd like to set for the environment)
4. Run the virtualenv (to keep your environment isolated for this project): `source env/bin/activate`
5. Install stripe: `pip install --upgrade stripe`
## Windows
1. Install python: `py -m pip install --upgrade pip`
2. Install virtualenv: `py -m pip install --user virtualenv`
3. Create your new virtual environment: `py -m venv env` (Note: You can change `env` to the name you'd like to set for the environment)
4. Run the virtualenv (to keep your environment isolated for this project): `.\env\Scripts\activate`
5. Install stripe: `pip install --index-url https://code.stripe.com --upgrade stripe`

# Running the app
1. Activate virtualenv: `source env/bin/activate` (Result: If you are successful, you will see your environment name in parentheses at the beginning of your terminal input line.)
2. Run the application: `python manage.py runserver` (Result: You will see the app load and a line that says "Starting development server at http://127.0.0.1:8000/")
3. Open the website in your browser: Go to `http://127.0.0.1:8000/` to view the site
