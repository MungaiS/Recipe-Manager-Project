from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email_address = Column(String)
    recipes = relationship('Recipe', back_populates='user')
    
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='recipes')


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    unit = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship('Recipe', back_populates='ingredients')

class Procedure(Base):
    __tablename__ = 'procedures'

    id = Column(Integer, primary_key=True)
    step = Column(Integer)
    description = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship('Recipe', back_populates='procedures')

if __name__ == '__main__':
  engine = create_engine('sqlite:///recipe.db')
  Base.metadata.create_all(engine)

  sessioncreator = sessionmaker(bind=engine)
  mysession = sessioncreator()

  recipe1 = Recipe(name="Pilau", description = "cxbrnje", instructions="cjsojadjs")
  mysession.add(recipe1)
  mysession.commit()


# class Ingredient(Base):
#     __tablename__ = 'ingredients'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     quantity = Column(String)
#     recipe_id = Column(Integer, ForeignKey('recipes.id'))