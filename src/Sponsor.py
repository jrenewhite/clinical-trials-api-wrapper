class Sponsor:
    """
    Represents a sponsor of a clinical trial, which could be an organization or an individual supporting the research.

    Attributes:
        name (str): The name of the sponsoring entity or organization.
        type (str): The type of sponsor (e.g., "Pharmaceutical", "Academic").
        contact_info (str): Contact information for the sponsor.
    """
    def __init__(self, name:str=None, type:str=None, contact_info:str=None):
        """
        Initializes a Sponsor object with data from the API response.

        Parameters:
            name (str): The name of the sponsoring entity or organization.
            type (str): The type of sponsor (e.g., "Pharmaceutical", "Academic").
            contact_info (str): Contact information for the sponsor.
        """
        self.name = name
        self.type = type
        self.contact_info = contact_info

    def __str__(self):
        """
        Returns a string representation of the Sponsor object.
        """
        return f"Sponsor(Name: {self.name}, Type: {self.type}, Contact Info: {self.contact_info})"

    @staticmethod
    def from_api_data(data):
        """
        Factory method to create a Sponsor instance from the API response data.
        """
        return Sponsor(
            name=data.get('name'),
            type=data.get('type'),
            contact_info=data.get('contact_info')
        )
