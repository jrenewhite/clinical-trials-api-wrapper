from enum import Enum, auto

class ConditionType(Enum):
    CHRONIC = auto()
    ACUTE = auto()
    RARE = auto()
    COMMON = auto()

from APIClient import ClinicalTrialsApiClient

class Condition:
    """
    Represents a medical condition or disease in a clinical trial.

    Attributes:
        id (str): The unique identifier for the condition.
        name (str): The name of the condition.
    """
    def __init__(self, id=None, name=None, condition_type=None):
        self.id = id
        self.name = name
        self.condition_type = ConditionType[condition_type] if condition_type else None

    def __str__(self):
        """
        Returns a string representation of the Condition object.
        """
        return f"Condition(ID: {self.id}, Name: {self.name}, Description: {self.condition_type})"

    @staticmethod
    def from_api_data(data):
        """
        Map the data received from the API to a new instance of the Condition object.
        The API's contract concerning the type should follow the keys in the enum.
        """
        id = data.get('id')
        name = data.get('name')
        type_from_api = data.get('type', '').upper()  # Assuming the API returns the condition's type as a string
        condition_type = ConditionType[type_from_api] if type_from_api in ConditionType.__members__ else None
        return Condition(id, name, condition_type)


    @classmethod
    def fetch_all(self, api_client:ClinicalTrialsApiClient):
        """
        This method will hit an endpoint that is supposed to return all possible conditions.
        """
        data = api_client.request('GET', 'conditions/all')
        return [self.from_api_data(condition) for condition in data]

    @classmethod
    def search(self, api_client, condition_query):
        """
        This method will use the search/filtered endpoint to find the best fit for the entered condition.
        """
        parameters = {'query': condition_query}
        data = api_client.request('GET', 'conditions/search', params=parameters)
        return [self.from_api_data(condition) for condition in data]
