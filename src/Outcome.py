from enum import Enum, auto

class OutcomeType(Enum):
    PRIMARY = auto()
    SECONDARY = auto()
    OTHER = auto()


class Outcome:
    """
    Represents an outcome of a clinical trial, including its identifiers, 
    measure, description, and time points.

    Attributes:
        id (str): The unique identifier for the outcome.
        title (str): A brief title of the outcome.
        description (str): A detailed description of the outcome.
        type (OutcomeType): The class of outcome (primary, secondary, etc.).
        time_frame (str): The time points or the overall period when the outcome is measured.
        measure (str): Describes what is being measured by the outcome.
    """
    def __init__(self, id=None, title=None, type=None, time_frame=None, measure=None, description=None):
        self.id = id
        self.title = title
        self.type = OutcomeType[type.upper()] if type else None
        self.time_frame = time_frame
        self.measure = measure
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the Outcome object.
        """
        type_str = self.type.name if self.type else "Not specified"
        return f"Outcome(ID: {self.id}, Title: {self.title}, Type: {type_str}, Time Frame: {self.time_frame}, Measure: {self.measure}, Description: {self.description})"

    @staticmethod
    def from_api_data(data):
        """
        Factory method to create an Outcome instance from the API response data.
        """
        outcome_type = data.get('type', '').upper()
        return Outcome(
            id=data.get('id'),
            title=data.get('title'),
            type=outcome_type if outcome_type in OutcomeType.__members__ else None,
            time_frame=data.get('time_frame'),
            measure=data.get('measure'),
            description=data.get('description')
        )
