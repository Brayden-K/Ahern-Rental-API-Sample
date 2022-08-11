from dotenv import load_dotenv
import os
load_dotenv()

#Load DB info from .env
MYSQLHOST = os.getenv("MYSQLHOST")
MYSQLUSER = os.getenv("MYSQLUSER")
MYSQLPASS = os.getenv("MYSQLPASS")
MYSQLDB = os.getenv("MYSQLDB")

#Environment Type | dev/prod
ENVIRONMENT = os.getenv("ENVIRONMENT")

#Flask secret key
SECRET_KEY = os.getenv("SECRET_KEY")