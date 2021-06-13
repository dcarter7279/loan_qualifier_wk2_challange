# Project Title

This is a command-line interface application which allows users to see loans which they may qualify for based on specific user supplied data. The application uses a `daily_rate_sheet` of loan criteria from various loan providers, by asking the user some qualifying questions to determine their loan elgibility and returns a list of qualifying loans.

The purpose of this application is to provide the user with a list of loans which they are qualified for based on the data provided. The application helps the user to not waste time applying for loans which they may not actually qualify for.

---

## Technologies

This project leverages python 3.3.8.5 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [pytest](https://docs.pytest.org/en/stable/) - For basic assertion testing of financial calculators and filters, and filio.

---

## Installation Guide

Install the following dependencies before running the application

```python
pip install fire
pip install questionary
pip install pytest
pip install mkdocs
```

## Examples

After launching the loan qualifier application you will be given the following prompts.

![Loan Qualifier Prompts](Images/loan_qualifier.png)

---

## Usage

To use the application clone the repository and run the  **app.py** with:

```python
python app.py
```

---

## Contributors

Brought to you by Donell Carter
email: dcarter7279@gmail.com

---

## License

MIT
