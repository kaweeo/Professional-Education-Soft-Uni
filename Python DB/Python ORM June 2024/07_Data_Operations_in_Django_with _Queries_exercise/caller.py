import os
import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Exercise: 01. Pet

def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


# Exercise: 02 Artifact

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f'The artifact {artifact.name} is {artifact.age} years old!'


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


# Exercise: 03. Location

def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(l) for l in locations)


def new_capital() -> None:
    # Location.objects.filter(pk=1).update(is_capital=True)  # Faster and correct

    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


# Exercise: 04. Car


def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        discount_percentage = sum(int(e) for e in str(car.year)) / 100
        car.price_with_discount = float(car.price) - discount_percentage * float(car.price)
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.all().filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


# Exercise: 05. Task Encoder

def show_unfinished_tasks() -> str:
    unfinished_tasks = Task.objects.all().filter(is_finished=False)

    return '\n'.join(str(t) for t in unfinished_tasks)


def complete_odd_tasks() -> None:
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(e) - 3) for e in text)
    # targeted_tasks = Task.objects.filter(title=task_title)

    # for task in targeted_tasks:
    #     task.description = decoded_text
    #     task.save()

    Task.objects.filter(title=task_title).update(description=decoded_text)


# Exercise: 06. Hotel Room

def get_deluxe_rooms() -> str:
    all_deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_id_deluxe_rooms = []

    for room in all_deluxe_rooms:
        if room.id % 2 == 0:
            even_id_deluxe_rooms.append(str(room))

    return '\n'.join(even_id_deluxe_rooms)


def increase_room_capacity() -> None:
    all_rooms = HotelRoom.objects.all().order_by("id")
    previous_room_capacity = None

    for room in all_rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.order_by(id).last()

    if last_room.is_reserved:
        last_room.delete()


def update_character() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 7,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory='The inventory is empty',
    )


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + ' ' + second_character.name
    fusion_class_name = 'Fusion'
