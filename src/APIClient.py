import requests
import logging
from APIError import APIError

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClinicalTrialsApiClient:
    def __init__(self, BaseURL, ApiKey=None):
        self.BaseURL = BaseURL
        self.ApiKey = ApiKey

    def request(self, endpoint, params=None, method='GET'):
        headers = {}
        if self.ApiKey:
            headers['Authorization'] = f'Bearer {self.ApiKey}'

        full_url = f"{self.BaseURL}/{endpoint}"
        logging.info(f'Making {method} request to {full_url} with params: {params}')

        try:
            if method == 'GET':
                response = requests.get(full_url, params=params, headers=headers)
            else:
                logging.error(f'Unsupported method: {method}')
                return None

            # Check for HTTP errors
            if response.status_code >= 400:
                raise APIError.from_response(response)
            
            logging.info(f'Successful {method} request to {full_url}')
            return self.handle_response(response)

        except requests.exceptions.RequestException as err:
            logging.error(f'Unexpected Error: {err}')
            raise APIError(f'Unexpected Error: {err}') from err

    def handle_response(self, response):
        return response.json()
