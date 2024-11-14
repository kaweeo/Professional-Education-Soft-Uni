from typing import List

from sqlalchemy import create_engine, Null
from sqlalchemy.orm import sessionmaker

from helpers import session_decorator
from models import Recipe, Chef

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost/sqlalchemy_project_exercise")
Session = sessionmaker(bind=engine)

session = Session()


# 2. Create Recipe
@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str) -> None:
    new_recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions
    )

    session.add(new_recipe)


# # Query all recipes
# recipes = session.query(Recipe).all()
# for recipe in recipes:
#     print(recipe.name + 'Ingredients: ' + recipe.ingredients)

# 3. Update Recipe
@session_decorator(session)
def update_recipe(name: str, new_name: str, new_ingredients: str, new_instructions: str) -> int:
    changed_records: int = (
        session.query(Recipe)
        .filter_by(name=name)
        .update({
            Recipe.name: new_name,
            Recipe.ingredients: new_ingredients,
            Recipe.instructions: new_instructions
        })
    )
    # recipe_to_update = session.query(Recipe).filter_by(name=name).first()
    #
    # recipe_to_update.name = new_name
    # recipe_to_update.ingredients = new_ingredients
    # recipe_to_update.instructions = new_instructions

    return changed_records


# 4. Delete Recipe by name
@session_decorator(session)
def delete_recipe_by_name(name: str) -> int:
    records_changed: int = (
        session.query(Recipe)
        .filter_by(name=name)
        .delete()
    )

    return records_changed


# 5. Get recipies by ingredient
@session_decorator(session)
def get_recipe_by_ingredient(ingredient: str) -> List:
    recipes = (
        session.query(Recipe)
        .filter(Recipe.ingredients.like(f'%{ingredient}%'))
        .all()
    )

    return recipes


# 6. Swap transaction recipe ingredients
@session_decorator(session)
def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str):
    first_recipe = (
        session.query(Recipe)
        .filter_by(name=first_recipe_name)
        .with_for_update()  # Lock the record in DB, cannot be modified from other
        .one()  # One record if more raise error
    )

    second_recipe = (
        session.query(Recipe)
        .filter_by(name=second_recipe_name)
        .with_for_update()
        .one()
    )

    first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients


# 9. Recipe and Chef Relations
@session_decorator(session)
def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str):
    searched_recipe = (
        session.query(Recipe)
        .filter_by(name=recipe_name)
        .one()
    )
    searched_chef = (
        session.query(Chef)
        .filter_by(name=chef_name)
        .one()
    )

    if searched_recipe and searched_recipe.chef:
        raise Exception(f"Recipe: {recipe_name} already has a related chef")

    searched_recipe.chef = searched_chef

    return f"Related recipe {recipe_name} with chef {chef_name}"


# 10. Chef and Recipe integration
@session_decorator(session)
def get_recipes_with_chef() -> str:
    # recipes_with_chef = (
    #     session.query(Recipe)
    #     .where(Recipe.chef != Null)
    # )
    #
    # result = ""
    #
    # for recipe in recipes_with_chef:
    #     result += f"Recipe: {recipe.name} made by chef: {recipe.chef.name}\n"
    #
    # return result
    #
    recipes_with_chef = (
        session.query(Recipe.name, Chef.name.label("chef_name"))  # label is alais, here is not needed
        .join(Chef, Recipe.chef)
        .all()
    )

    # SELECT
    #     recipe.name,
    #     chef.name AS 'chef_name'
    # FROM
    #     recipes
    # JOIN
    #     chef
    # ON
    #     recipe.chef_id = chef.id

    return "\n".join(
        f"Recipe: {recipe_name} made by chef: {chef_name}"
        for recipe_name, chef_name in recipes_with_chef
    )
