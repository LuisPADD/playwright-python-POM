# Playwright Automation Tests

This project contains a set of browser automation tests built with Python, pytest, and Playwright. The tests exercise a public demo page for common UI interactions such as login, form input, element locators, mouse actions, file upload, and drag-and-drop.

## Project Structure

- `tests/test_login_successful.py` - verifies a successful login flow
- `tests/test_actions.py` - covers form interactions, checkboxes, radio buttons, selects, mouse actions, file upload, and drag-and-drop
- `tests/test_all_locators.py` - demonstrates locator strategies such as role, text, label, placeholder, alt text, title, and test id
- `tests/test_open_url.py` - opens the target page and validates the page title
- `files/sample1.pdf` - sample file used for the upload test

## Prerequisites

- Python 3.8+ recommended
- pip

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install pytest pytest-playwright playwright
playwright install
```

## Running the Tests

Run all tests:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_login_successful.py -v
```

## What the Tests Cover

- Login flow with valid credentials
- Text field input and keyboard actions
- Checkbox and radio selection
- Dropdown selection
- Single click, double click, right click, shift-click, and hover interactions
- File upload using a local sample PDF
- Drag-and-drop behavior
- Different locator strategies supported by Playwright

## Notes

The tests target the demo page:

https://leogcarvalho.github.io/test-automation-practice/

If you want to extend this suite, you can add more scenarios for validation messages, error handling, and additional UI controls.
