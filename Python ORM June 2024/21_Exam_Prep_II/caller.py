import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Order, Product


# Create queries within functions
# Django Queries I


def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ""

    query_name = Q(full_name__icontains=search_string)
    query_email = Q(email__icontains=search_string)
    query_phone_number = Q(phone_number__icontains=search_string)

    profiles = (
        Profile.objects
        .filter(query_name | query_email | query_phone_number)
        .order_by('full_name')
    )
    if len(profiles) == 0:
        return ""

    return "\n".join(
        f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}"
        for p in profiles
    )


def get_loyal_profiles() -> str:
    loyal_profiles = (
        Profile.objects
        .get_regular_customers()
        .annotate(orders_count=Count('orders'))
        .order_by('-orders_count')
    )
    if not loyal_profiles:
        return ""

    result = ''
    for profile in loyal_profiles:
        result += f'Profile: {profile.full_name}, orders: {profile.orders_count}\n'

    return result


def get_last_sold_products() -> str:
    # last_order = (
    #     Order.objects
    #     .last()
    # )

    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ''

    products = [p.name for p in last_order.products.all()]

    return f'Last sold products: {", ".join(products)}'


# Django Queries II

def get_top_products() -> str:
    top_products = (
        Product.objects
        .annotate(orders_count=Count('products_orders'))
        .filter(orders_count__gt=0)
        .order_by('-orders_count', 'name')[:5]
    )

    if not top_products:
        return ""

    result = "Top products:\n"
    result += "\n".join(f"{p.name}, sold {p.orders_count} times" for p in top_products)

    return result


def apply_discounts() -> str:
    orders_for_discount = (
        Order.objects
        .annotate(products_count=Count('products'))
        .filter(is_completed=False, products_count__gt=2)
    )

    updated_count = orders_for_discount.update(total_price=F('total_price') * 0.9)
    if not updated_count:
        updated_count = 0

    return f"Discount applied to {updated_count} orders."


def complete_order() -> str:
    oldest_order = (
        Order.objects
        .filter(is_completed=False)
        .order_by('creation_date')
        .first()
    )

    if oldest_order is None:
        return ''

    for p in oldest_order.products.all():
        p.in_stock -= 1
        if p.in_stock == 0:
            p.is_available = False

        p.save()

    oldest_order.is_completed = True
    oldest_order.save()

    return "Order has been completed!"
