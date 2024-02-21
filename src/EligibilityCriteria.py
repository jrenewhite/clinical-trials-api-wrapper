class EligibilityCriteria:
    """
    Represents the eligibility criteria for participation in a clinical trial.

    Attributes:
        inclusion_criteria (str): Text detailing the inclusion criteria.
        exclusion_criteria (str): Text detailing the exclusion criteria.
    """
    def __init__(self, inclusion_criteria=None, exclusion_criteria=None):
        self.inclusion_criteria = inclusion_criteria
        self.exclusion_criteria = exclusion_criteria

    @staticmethod
    def from_api_data(data):
        """
        Factory method to create an EligibilityCriteria instance from the API response data.
        """
        inclusion_criteria = data.get('inclusion_criteria')
        exclusion_criteria = data.get('exclusion_criteria')
        return EligibilityCriteria(inclusion_criteria, exclusion_criteria)

    def __str__(self):
        """
        Returns a string representation of the EligibilityCriteria object.
        """
        return f"Inclusion Criteria: {self.inclusion_criteria}\nExclusion Criteria: {self.exclusion_criteria}"
