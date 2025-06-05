import os

apps = os.getenv("APPS", "").split(',')

token=os.getenv("API_TOKEN")
if not token:
    print("API_TOKEN environment variable is not set. Please set it to your API token.")
    exit(1)

baseUrl= os.getenv("API_URL", "http://localhost:8000")
if not baseUrl:
    print("API_URL environment variable is not set. Please set it to the base URL of your API.")
    exit(1)
if baseUrl.endswith('/'):
    baseUrl = baseUrl[:-1]

reportsDir = os.path.join(os.path.dirname(__file__), 'reports')
if not os.path.exists(reportsDir):
    os.makedirs(reportsDir)

logDir = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(logDir):
    os.makedirs(logDir)

logPath = os.path.join(logDir,'monitor.log')
