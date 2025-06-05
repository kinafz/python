import os

apps = os.getenv("APPS", "").split(',')

token=os.getenv("API_TOKEN")
if not token:
    print("API_TOKEN environment variable is not set. Please set it.")
    exit(1)

baseUrl=os.getenv("API_URL", "http://localhost:8000")
if baseUrl.endswith('/'):
    baseUrl = baseUrl[:-1]

reportsDir = os.path.join(os.path.dirname(__file__), 'reports')
if not os.path.exists(reportsDir):
    os.makedirs(reportsDir)

logDir = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(logDir):
    os.makedirs(logDir)

logPath = os.path.join(logDir,'monitor.log')

db_host=os.getenv("DB_HOST", "localhost")
db_port=os.getenv("DB_PORT", "5432")
db_name=os.getenv("DB_NAME", "dbname")
db_user=os.getenv("DB_USER", "dbuser")
db_password=os.getenv("DB_PASSWORD", "dbpassword")
