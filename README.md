# cps847-assignment2
Usage of a variety of CI-CD tools and Cloud services

# Group 17 Members

- Alize De Matas
- Jasmine Joy
- Sauban Sakhi
- Syed Abdullah
- Tiago Valverde


# Setup

Create virtual environment
``
virtualenv venv --python=python
source venv/bin/activate
``

Install packages

```
pip install -r requirements.txt
```

# Sample Code

Invoice class calculating total cost to pay
``
python app.py
``

# Run Tests Manually
``
pytest test_invoice.py
pytest --cov=./
``


# Resources

Package to setup upload to codecov with travis
- https://github.com/codecov/codecov-python
- https://github.com/codecov/example-python
