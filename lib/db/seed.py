from models import create_engine, sessionmaker, Base, User, Recipe, Ingredient, Procedure
from faker import Faker

engine = create_engine('sqlite:///recipe.db')
Base.metadata.create_all(engine)

sessioncreator = sessionmaker(bind=engine)
mysession = sessioncreator()

fakedata = Faker()

# Create fake users
for i in range(10):
    user = User(name=fakedata.name(), email_address=fakedata.email())
    session.add(user)

# Create fake recipes for each user
for user in session.query(User).all():
    for i in range(5):
        recipe = Recipe(name=fakedata.word(), user=user)
        mysession.add(recipe)

# Create fake ingredients for each recipe
for recipe in session.query(Recipe).all():
    for i in range(5):
        ingredient = Ingredient(name=fake.word(), quantity=fake.random_int(min=1, max=10), unit=fake.word(), recipe=recipe)
        mysession.add(ingredient)

# Create fake procedures for each recipe
for recipe in session.query(Recipe).all():
    for i in range(10):
        procedure = Procedure(step=i+1, description=fake.sentence(), recipe=recipe)
        mysession.add(procedure)

mysession.commit()