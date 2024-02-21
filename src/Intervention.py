from enum import Enum, auto

class InterventionType(Enum):
    DRUG = auto()
    PROCEDURE = auto()
    DEVICE = auto()
    BEHAVIORAL = auto()
    OTHER = auto()


class Intervention:
    """
    Represents an intervention in a clinical trial.

    Attributes:
        id (str): The unique identifier for the intervention.
        name (str): The name of the intervention.
        type (InterventionType): The type of intervention.
        description (str): A detailed description of the intervention.
    """
    def __init__(self, id=None, name=None, type=None, description=None):
        self.id = id
        self.name = name
        self.type = InterventionType[type.upper()] if type else None
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the Intervention object.
        """
        type_str = self.type.name if self.type else "Not specified"
        return f"Intervention(ID: {self.id}, Name: {self.name}, Type: {type_str}, Description: {self.description})"

    @staticmethod
    def from_api_data(data):
        """
        Factory method to create an Intervention instance from the API response data.
        """
        id = data.get('id')
        name = data.get('name')
        type_from_api = data.get('type', '').upper()  # Assuming the API returns the intervention's type as a string
        description = data.get('description')
        return Intervention(id, name, type=type_from_api if type_from_api in InterventionType.__members__ else None, description=description)
