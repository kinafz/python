import requests
from logger import logger
from config import baseUrl, token, apps

def check_app_status(app_name):
    url = f'{baseUrl}/status?app={app_name}'
    headers = {'Authorization': f'Bearer {token}'}
    logger.info(f"Checking status for {app_name} at {url} and bearer {token.replace(token, '****')}")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error checking status for {app_name}: Status code: {response.status_code}, Error: {e}")
        return None

def checkAllStatus():
    logger.info("Starting status check for all apps")
    for app in apps:
        status = check_app_status(app)
        if status:
            logger.info(f"Status for {app}: {status}")
        else:
            logger.error(f"Failed to retrieve status for {app}")
            
if __name__ == "__main__":
    logger.info("Monitor script started")
    checkAllStatus()
    logger.info("Monitor script finished")