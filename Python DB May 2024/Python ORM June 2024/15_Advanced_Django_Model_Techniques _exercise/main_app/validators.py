import re

from django.core.exceptions import ValidationError


# 01. Customer
def validate_name(value):
    for e in value:
        if not (e.isalpha() or e.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


# class ValidateName:
#     def __init__(self, message: str):
#         self.message = message
#
#     def __call__(self, value):
#         for char in value:
#             if not (char.isalpha() or char.isspace()):
#                 raise ValidationError(self.message)
#
#     def deconstruct(self):
#         return (
#             'main_app.validators.ValidateName',
#             (self.message, ),
#             {}
#         )
def validate_age(value):
    if value < 18:
        raise ValidationError("Age must be greater than or equal to 18")


# ERRORS:
# main_app.Customer.age: (fields.E008) All 'validators' must be callable.
# 	HINT: validators[0] (None) isn't a function or instance of a validator class.

def validate_phone_number(value):
    if not re.match(r'^\+359\d{9}$', value):
        raise ValidationError("Phone number must start with '+359' followed by 9 digits")


