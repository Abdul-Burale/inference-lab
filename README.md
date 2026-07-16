# InferenceLab

InferenceLab is a Python project for experimenting with foundation-model inference and evaluation through Amazon Bedrock.

The project currently provides a small application scaffold with validated environment-based configuration, an installable command-line entry point, and automated tests.

## Requirements

* Python 3.11+
* AWS CLI v2
* An AWS account

## Installation

Clone the repository:

```powershell
git clone https://github.com/YOUR-USERNAME/inference-lab.git
cd inference-lab
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the project and development dependencies:

```powershell
python -m pip install -e ".[dev]"
```

## Configuration

Copy `.env.example` to `.env` and update the values for your local environment.

```powershell
Copy-Item .env.example .env
```

Example configuration:

```env
APP_NAME=InferenceLab
ENVIRONMENT=development
DEBUG=true
AWS_PROFILE=inference-lab
AWS_REGION=eu-west-2
REQUEST_TIMEOUT_SECONDS=30
LOG_LEVEL=INFO
```

Do not commit `.env` or AWS credentials.

## Usage

Run the application:

```powershell
inference-lab
```

Alternatively:

```powershell
python -m inference_lab.main
```

## Testing

Run the test suite:

```powershell
python -m pytest -v
```

## Dependencies

Runtime dependencies:

* Pydantic
* Pydantic Settings

Development dependencies:

* Pytest

## Project structure

```text
src/inference_lab/   Application source code
tests/               Automated tests
pyproject.toml       Package and dependency configuration
.env.example         Example local configuration
```

## Status

InferenceLab is in early development. Amazon Bedrock model invocation and evaluation features are not yet implemented.
