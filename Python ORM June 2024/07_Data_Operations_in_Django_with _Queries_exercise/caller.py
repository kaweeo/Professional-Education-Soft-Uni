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


# print(create_pet('Bubi', 'Siamease'))


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


# print(create_artifact('weapon', 'India', 2500, 'Weapon artifact', True))


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name)
    # UPDATE artefact SET name = new_name WHERE is_magical=TRUE && age > 250 && id = 1
    # SQL level, for 1 element id=artifact.id equal to pk=artifact.pk

    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


# weapon = Artifact.objects.get(id=1)
# print(weapon.name)
# rename_artifact(weapon, 'Indian Magic Weapon')
# print(weapon.name)


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
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


# Exercise: 05. Task Encoder

def show_unfinished_tasks() -> str:
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return '\n'.join(str(t) for t in unfinished_tasks)


def complete_odd_tasks() -> None:
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()

    # Task.objects.bulk_update(tasks, {'is_finished': True})


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(e) - 3) for e in text)
    # targeted_tasks = Task.objects.filter(title=task_title)

    # for task in targeted_tasks:
    #     task.description = decoded_text
    #     task.save()

    Task.objects.filter(title=task_title).update(description=decoded_text)


# Exercise: 06. Hotel Room

def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_deluxe_rooms = [str(r) for r in deluxe_rooms if r.id % 2 == 0]

    return "\n".join(even_deluxe_rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room() -> None:
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room() -> None:
    room = HotelRoom.objects.last()

    if not room.is_reserved:
        room.delete()


# Exercise: 07. Character

def update_characters() -> None:
    Character.objects.filter(class_name="Mage").update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name="Warrior").update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty"
    )
    # UPDATE table
    # SET
    #   intelligence = intelligence - 7,
    #   level = level + 3
    # WHERE class_name IN ("Assassin", "Scout")


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + " " + second_character.name
    class_name = "Fusion"
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = first_character.hit_points + second_character.hit_points

    if first_character.class_name in ["Mage", "Scout"]:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=fusion_name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()

