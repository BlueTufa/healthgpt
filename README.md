# healthgpt
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
![GitHub Actions Status](https://github.com/BlueTufa/healthgpt/actions/workflows/verify.yml/badge.svg)

A GPT-based Social Media Analysis Utility

## Getting Started
Follow these steps to establish your initial development environment setup.  You can run the unit tests to verify that you have all baseline requirements met before continuing.

You may need to set one or more environment variables to get unit tests passing.  Please see `.env.sample` for example environment variables.
```bash
poetry install
poetry shell
pre-commit install
pytest --cov -vv
```

## Testing the Endpoint
Once you have a development environment estalished, you can start testing the endpoint.
### Start the HTTP Server
```bash
python src/api.py
```
### Use curl to test the endpoint
In order to maximize the amount of backend work in this example, all testing is performed with `curl` or Postman.
The following is an example of consuming the search API:
```bash
curl 'http://localhost:8001/timeline/search?tag=mentalhealth'
```

Example output:
```json
[
  {
    "timeline": {
      "title": "Children Who Survive Shootings Endure Huge Health Obstacles and Costs - KFF Health News",
      "text": "A new study finds that young people who have been injured by firearms are more prone to psychiatric diagnoses and developing a substance use disorder than kids who have not been shot — and their families also suffer long-term ill effects."
    },
    "message": "Children who survive shootings not only face psychological and emotional challenges but also endure significant health obstacles and costs, according to a report by KFF Health News. The physical consequences of gun violence can be severe and long-lasting, with many survivors experiencing long-term disabilities and chronic pain.\n\nInjuries from shootings often include damage to vital organs, bones, and nerves, leading to complications such as paralysis, mobility issues, and chronic conditions. Additionally, gunshot wounds can cause infections, requiring extensive medical treatment and rehabilitation. These health obstacles can have a profound impact on a child's overall well-being and quality of life.\n\nThe financial burden of gunshot injuries is also immense. The costs of initial emergency care, surgeries, and hospitalizations are often just the beginning. Many survivors require ongoing medical care, therapy, specialized equipment, and medications, all of which add up to significant expenses for them and their families. Moreover, these costs can create financial strain and hinder access to necessary healthcare and support services.\n\nThis report highlights the need for comprehensive support systems for child survivors of shootings, including mental health resources, specialized medical care, and financial assistance. Policymakers and healthcare providers must recognize the unique challenges faced by these children and work to address their healthcare needs effectively.\n\nIn conclusion, surviving a shooting as a child can result in substantial health obstacles and costs. Ensuring that child survivors have access to the necessary medical care, psychological support, and financial assistance is crucial in helping them recover and lead healthy lives."
  }
]
```

## Highlights
* FastAPI-based
* Pydantic models
* Unit test automation with code coverage artifacts
* environment variable-based configuration
* Containerized deployment
* Poetry
* pre-commit automated linting
* Integrated GitHub Actions

## What's left to do
* Performance optimization.
* Consider Celery broker and a backend data store.
* Implement JWT-based authentication.
* Implement semantic release and release publishing.
