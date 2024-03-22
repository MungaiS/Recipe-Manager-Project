from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

if __name__ == '__main__':
  engine = create_engine('sqlite:///recipe.db')