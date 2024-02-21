# ClinicalTrials.gov API Wrapper

## Overview

This repository contains a Python wrapper for the ClinicalTrials.gov REST API version 2.0.0-beta2. The API provides metadata, statistics, and the latest version of clinical trials available on ClinicalTrials.gov. It features operations for retrieving study data based on query and filter parameters, returning results in formats such as JSON or CSV. Additionally, it enables searching for specific study information using its NCT Number, among other functionalities like obtaining metadata from study data fields, search areas, enumeration types, and statistics on study sizes and field values.

For more details, you can review the complete documentation at [ClinicalTrials.gov API](https://beta.clinicaltrials.gov/api/oas/v2).

## Features

- Retrieval of study data based on various parameters.
- Support for JSON and CSV output formats.
- Functionality to search by NCT Number.
- Access to metadata of study data fields and search areas.
- Enumeration types and statistics about studies.

## Installation

Instructions on how to install and configure the wrapper in your environment.

```bash
pip install <name-of-the-package>
```

## Usage

Examples on how to use the wrapper to interact with the ClinicalTrials.gov API, including retrieving studies, searching by conditions, and more.

```python
from clinical_trials_api import APIClient

# Example usage
client = APIClient()
study_details = client.get_study_by_nct_number('NCT02938888')
print(study_details)
```

## Contributing

Information on how to contribute to the project, including guidelines for submitting pull requests, reporting bugs, and suggesting enhancements.

## License

Details about the license under which the project is released.

## Contact

Information on how to reach out to the project maintainers or community, including email, project forums, or issue trackers.