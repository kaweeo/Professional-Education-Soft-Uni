import os
from typing import List

import django
from django.db.models import Case, When, Value, QuerySet
from django.forms import CharField

from helpers import populate_model_with_data
from main_app.choices import OperationSystemChoice, DungeonDifficultyChoice

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout


# 01. Artwork Gallery

def show_highest_rated_art() -> str:
    highest_rated_artwork = ArtworkGallery.objects.all().order_by('-rating', 'id').first()

    return f"{highest_rated_artwork.art_name} is the highest-rated art with a {highest_rated_artwork.rating} rating!"


# artwork1 = ArtworkGallery(artist_name='Vincent van Gogh', art_name='Starry Night', rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name='Leonardo da Vinci', art_name='Mona Lisa', rating=5, price=1500000.0)


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create(
        [first_art, second_art]
    )


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# 02. Laptop

def show_the_most_expensive_laptop() -> str:
    highest_price_laptop = Laptop.objects.order_by('-price', '-id').first()
    return f"{highest_price_laptop.brand} is the most expensive laptop available for {highest_price_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=("Asus", "Lenovo")).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=("Apple", "Dell", "Acer")).update(memory=16)


# def update_operation_systems() -> None:
#     Laptop.objects.filter(brand="Asus").update(operation_system="Windows")
#     Laptop.objects.filter(brand="Apple").update(operation_system="Windows")
#     Laptop.objects.filter(brand__in=("Dell", "Acer")).update(operation_system="Linux")
#     Laptop.objects.filter(brand="Lenovo").update(operation_system="Chrome OS")


# def update_operation_systems() -> None:
#     Laptop.objects.update(
#         operation_system=Case(
#             When(brand="Asus", then="Windows"),
#             When(brand="Apple", then="Windows"),
#             When(brand__in=["Dell", "Acer"], then="Linux"),
#             When(brand="Lenovo", then="Chrome OS"),
#             output_field=CharField(),
#         )
#     )


def update_operation_systems() -> None:
    # Solution 1
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value(OperationSystemChoice.WINDOWS)),
            When(brand="Apple", then=Value(OperationSystemChoice.MACOS)),
            When(brand__in=("Dell", "Acer"), then=Value(OperationSystemChoice.LINUX)),
            When(brand="Lenovo", then=Value(OperationSystemChoice.CHROME_OS))
        )
    )


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


# 03. Chess Player


player1 = ChessPlayer(
    username='Player1',
    title='no title',
    rating=2200,
    games_played=50,
    games_won=20,
    games_lost=25,
    games_drawn=5,
)
player2 = ChessPlayer(
    username='Player2',
    title='IM',
    rating=2350,
    games_played=80,
    games_won=40,
    games_lost=25,
    games_drawn=15,
)


def bulk_create_chess_players(args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title="IM")


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title="FM")


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title="regular player")


# 04. Meal

def set_new_chefs() -> None:
    # Meal.objects.filter(meal_type="Breakfast").update(chef="Gordon Ramsay")
    # Meal.objects.filter(meal_type="Lunch").update(chef="Julia Child")
    # Meal.objects.filter(meal_type="Dinner").update(chef="Jamie Oliver")
    # Meal.objects.filter(meal_type="Snack").update(chef="Thomas Keller")

    Meal.objects.update(
        chef=Case(
            When(meal_type="Breakfast", then=Value("Gordon Ramsay")),
            When(meal_type="Lunch", then=Value("Julia Child")),
            When(meal_type="Dinner", then=Value("Jamie Oliver")),
            When(meal_type="Snack", then=Value("Thomas Keller")),
        )
    )


def set_new_preparation_times() -> None:
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type="Breakfast", then=Value("10 minutes")),
            When(meal_type="Lunch", then=Value("12 minutes")),
            When(meal_type="Dinner", then=Value("15 minutes")),
            When(meal_type="Snack", then=Value("5 minutes")),
        )
    )


def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=("Breakfast", "Dinner")).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).delete()


# 05. Dungeon

def show_hard_dungeons() -> str:
    hard_dungeons = Dungeon.objects.filter(difficulty="Hard").order_by("-location")
    return '\n'.join(str(d) for d in hard_dungeons)


# def show_hard_dungeons() -> str:
#     hard_dungeons = Dungeon.objects.filter(
#         difficulty=DungeonDifficultyChoice.HARD
#     ).order_by("-location")  # Z - A
#
#     return "\n".join(str(d) for d in hard_dungeons)
#


def bulk_create_dungeons(args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(args)


def update_dungeon_names() -> None:
    Dungeon.objects.update(
        name=Case(
            When(difficulty="Easy", then=Value("The Erased Thombs")),
            When(difficulty="Medium", then=Value("The Coral Labyrinth")),
            When(difficulty="Hard", then=Value("The Lost Haunt")),
        )
    )


# def update_dungeon_names() -> None:
#     Dungeon.objects.filter(
#         difficulty=DungeonDifficultyChoice.EASY
#     ).update(name="The Erased Thombs")
#
#     Dungeon.objects.filter(
#         difficulty=DungeonDifficultyChoice.MEDIUM
#     ).update(name="The Coral Labyrinth")
#
#     Dungeon.objects.filter(
#         difficulty=DungeonDifficultyChoice.HARD
#     ).update(name="The Lost Haunt")


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty="Easy").update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.update(
        recommended_level=Case(
            When(difficulty="Easy", then=Value(25)),
            When(difficulty="Medium", then=Value(50)),
            When(difficulty="Hard", then=Value(75)),
        )
    )


def update_dungeon_rewards() -> None:
    Dungeon.objects.update(reward=Case(
        When(boss_health=500, then=Value("1000 Gold")),
        When(location__startswith="E", then=Value("New dungeon unlocked")),
        When(location__endswith="s", then=Value("Dragonheart Amulet")),
    ))


def set_new_locations() -> None:
    Dungeon.objects.update(location=Case(
        When(recommended_level=25, then=Value("Enchanted Maze")),
        When(recommended_level=50, then=Value("Grimstone Mines")),
        When(recommended_level=75, then=Value("Shadowed Abyss")),
    ))


# 06. Workout

def show_workouts() -> str:
    searched_workouts = Workout.objects.filter(
        workout_type__in=("Calisthenics", "CrossFit")
    ).order_by("id")

    return '\n'.join(str(w) for w in searched_workouts)


def get_high_difficulty_cardio_workouts() -> QuerySet:
    return Workout.objects.filter(
        workout_type="Cardio",
        difficulty="High"
    ).order_by("instructor")


def set_new_instructors() -> None:
    Workout.objects.update(instructor=Case(
        When(workout_type="Cardio", then=Value("John Smith")),
        When(workout_type="Strength", then=Value("Michael Williams")),
        When(workout_type="Yoga", then=Value("Emily Johnson")),
        When(workout_type="CrossFit", then=Value("Sarah Davis")),
        When(workout_type="Calisthenics", then=Value("Chris Heria")),
    )
    )


def set_new_duration_times() -> None:
    Workout.objects.update(duration=Case(
        When(instructor=("John Smith"), then=Value("15 minutes")),
        When(instructor=("Sarah Davis"), then=Value("30 minutes")),
        When(instructor=("Chris Heria"), then=Value("45 minutes")),
        When(instructor=("Michael Williams"), then=Value("1 hour")),
        When(instructor=("Emily Johnson"), then=Value("1 hour and 30 minutes")),
    ))


def delete_workouts() -> None:
    Workout.objects.exclude(workout_type__in=("Strength", "Calisthenics")).delete()
