'''
In order to create a table from Deta Space you should:
- from the Dashboard -> goto Collections -> Name it -> Choose Base -> Name it
That base is you database
- get the Project Key
'''
import os
from deta import Deta
from dotenv import load_dotenv  # pip install python-dotenv

# Load the environment variable
load_dotenv('.env')
DETA_KEY = os.getenv('DETA_KEY')

# Initailize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect to a database
db = deta.Base('database')


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)