import os
from datetime import date, timedelta
from typing import List

import django
from django.db.models import QuerySet, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, \
    Car


# 01. Library

def show_all_authors_with_their_books() -> str:
    authors_with_books = []

    authors = Author.objects.all().order_by("id")
    # # Use prefetch_related to optimize querying related books
    # authors = Author.objects.prefetch_related('book_set').order_by("id")

    for author in authors:
        books = Book.objects.filter(author=author)
        # books = author.book_set.all()

        if not books:
            continue

        titles = ", ".join(b.title for b in books)
        authors_with_books.append(
            f"{author.name} has written - {titles}!"
        )

    return "\n".join(authors_with_books)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


# 02. Music App

def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)
    # song.artists.add(artist)


def get_songs_by_artist(artist_name: str) -> QuerySet:
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by("-id")


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)
    # song.artists.remove(artist)


# 03. Shop

def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    # product = Product.objects.get(name=product_name)
    # reviews = product.reviews.all()
    #
    # total_rating = sum(r.rating for r in reviews)
    # average_rating = total_rating / len(reviews)
    #
    # return average_rating

    product = Product.objects.annotate(
        average_rating=Avg('reviews__rating'),
    ).get(name=product_name)

    return product.average_rating


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
    get_products_with_no_reviews().delete()


# 04. License

def calculate_licenses_expiration_dates() -> str:
    ordered_licenses = DrivingLicense.objects.order_by('-license_number')

    result = []
    for ol in ordered_licenses:
        expiration_date = ol.issue_date + timedelta(days=365)
        result.append(f"License with number: {ol.license_number} expires on {expiration_date}!")

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date: date) -> List[Driver]:
    # drivers_w_expired_licenses = []
    #
    # for dl in DrivingLicense.objects.all():
    #     if dl.issue_date - timedelta(days=365) < due_date:
    #         drivers_w_expired_licenses.append(dl.driver)
    #
    # return drivers_w_expired_licenses
    #
    expiration_cutoff_date = due_date - timedelta(days=365)

    drivers_with_expired_licenses = Driver.objects.filter(
        license__issue_date__gt=expiration_cutoff_date,
    )

    return drivers_with_expired_licenses


# 05. Car Registration

def register_car_by_owner(owner: Owner) -> str:
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.registration = registration
    car.save()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."

# # Test Code
# # Create instances of the Owner model
# owner1 = Owner.objects.create(name='Ivelin Milchev')
# owner2 = Owner.objects.create(name='Alice Smith')
#
# # Create instances of the Car model and associate them with owners
# car1 = Car.objects.create(model='Citroen C5', year=2004)
# car2 = Car.objects.create(model='Honda Civic', year=2021)
#
# # Create instances of the Registration model for the cars
# registration1 = Registration.objects.create(registration_number='TX0044XA')
# registration2 = Registration.objects.create(registration_number='XYZ789')
#
# print(register_car_by_owner(owner1))
