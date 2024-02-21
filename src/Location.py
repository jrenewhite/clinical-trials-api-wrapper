class Location:
    """
    Represents the location or facility for a clinical trial.

    Attributes:
        id (str): The unique identifier for the location.
        name (str): The name of the facility or location.
        address (str): The street address of the location.
        city (str): The city where the location is based.
        state (str): The state or region of the location.
        country (str): The country of the location.
        contact (str): Contact information for the location.
    """
    def __init__(self, id=None, name=None, address=None, city=None, state=None, country=None, contact=None):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.contact = contact

    def __str__(self):
        """
        Returns a string representation of the Location object.
        """
        return f"Location(ID: {self.id}, Name: {self.name}, Address: {self.address}, City: {self.city}, State: {self.state}, Country: {self.country}, Contact: {self.contact})"

    @staticmethod
    def from_api_data(data):
        """
        Factory method to create a Location instance from the API response data.
        """
        return Location(
            id=data.get('id'),
            name=data.get('name'),
            address=data.get('address'),
            city=data.get('city'),
            state=data.get('state'),
            country=data.get('country'),
            contact=data.get('contact')
        )
