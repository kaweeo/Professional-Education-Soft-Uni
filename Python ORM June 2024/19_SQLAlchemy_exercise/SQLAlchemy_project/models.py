from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, Relationship, relationship

Base = declarative_base()

# 1. Model Recipe

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    ingredients = Column(
        Text,
        nullable=False
    )

    instructions = Column(
        Text,
        nullable=False
    )

    chef_id = Column(
        Integer,
        ForeignKey('chefs.id'),
    )

    chef = relationship(
        "Chef",
        back_populates="recipes"
    )

# 7. Model Chef

class Chef(Base):
    __tablename__ = 'chefs'

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    recipes = relationship(
        "Recipe",
        back_populates="chef",
    )