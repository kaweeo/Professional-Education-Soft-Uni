from django.core.exceptions import ValidationError


def validate_menu_categories(menu_text: str) -> None or ValidationError:
    must_have_categories = ["Appetizers", "Main Course", "Desserts"]
    # for category in must_have_categories:
    #     if category not in menu_text:
    #         raise ValidationError(
    #             message='The menu must include each of the categories "Appetizers", "Main Course", "Desserts".'
    #        )
    if not all(c.lower() in menu_text.lower() for c in must_have_categories):
        raise ValidationError(
            'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".'
        )
