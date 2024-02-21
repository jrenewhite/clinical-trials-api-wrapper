class APIError(Exception):
    """A custom exception for API errors"""

    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response

    def __str__(self):
        return f"APIError: {self.message} (Status code: {self.status_code})"

    @staticmethod
    def from_response(response):
        """
        Creates an APIError from an HTTP response object.

        Args:
            response (requests.Response): The response object from a failed API request.

        Returns:
            APIError: An instance of this class initialized with the error message extracted from the response.
        """
        try:
            # Attempt to get JSON error message from response
            error_info = response.json()
            message = error_info.get('message', 'Unknown error occurred')
        except ValueError:
            # Fallback if response is not in JSON format
            message = response.text or f"API error occurred with status code {response.status_code}"

        # Include the status code in the error message for clarity
        full_message = f"API Error {response.status_code}: {message}"

        return APIError(full_message, status_code=response.status_code, response=response)
