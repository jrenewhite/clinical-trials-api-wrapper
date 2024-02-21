class Participant:
    """
    Represents a participant in a clinical trial, focusing on their demographic and other relevant details.

    Attributes:
        age (str): The age or age range of the participant.
        gender (str): The gender of the participant.
        health_status (str): A description of the participant's health status.
    """
    def __init__(self, age=None, gender=None, health_status=None):
        self.age = age
        self.gender = gender
        self.health_status = health_status

    def __str__(self):
        """
        Returns a string representation of the Participant object.
        """
        return f"Participant(Age: {self.age}, Gender: {self.gender}, Health Status: {self.health_status})"

    @staticmethod
    def from_api_data(data):
        """
        Factory method to create a Participant instance from the API response data.
        """
        return Participant(
            age=data.get('age'),
            gender=data.get('gender'),
            health_status=data.get('health_status')
        )
