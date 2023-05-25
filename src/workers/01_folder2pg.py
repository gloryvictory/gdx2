from typing import Optional

import databases
import sqlalchemy
import ormar
import asyncio

from src import cfg
from src.log import set_logger

engine = sqlalchemy.create_engine(cfg.DB_DSN)
database = databases.Database(cfg.DB_DSN)
metadata = sqlalchemy.MetaData(schema=cfg.DB_SCHEMA)


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


# Note that all type hints are optional
# below is a perfectly valid model declaration
# class Author(ormar.Model):
#     class Meta(BaseMeta):
#         tablename = "authors"
#
#     id = ormar.Integer(primary_key=True) # <= notice no field types
#     name = ormar.String(max_length=100)

class Author(ormar.Model):
    class Meta(BaseMeta):
        tablename = "authors"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)


class Book(ormar.Model):
    class Meta(BaseMeta):
        tablename = "books"

    id: int = ormar.Integer(primary_key=True)
    author: Optional[Author] = ormar.ForeignKey(Author)
    title: str = ormar.String(max_length=100)
    year: int = ormar.Integer(nullable=True)


# async def db_get_connection():
#     database_ = database
#     # metadata.create_all(engine)
#     if not database_.is_connected:
#         print(f"connecting... {database_.url}")
#         await database_.connect()
#     return database_
async def create():
    # Create some records to work with through QuerySet.create method.
    # Note that queryset is exposed on each Model's class as objects
    tolkien = await Author.objects.create(name="J.R.R. Tolkien")
    await Book.objects.create(author=tolkien,
                              title="The Hobbit",
                              year=1937)
    await Book.objects.create(author=tolkien,
                              title="The Lord of the Rings",
                              year=1955)
    await Book.objects.create(author=tolkien,
                              title="The Silmarillion",
                              year=1977)

    # alternative creation of object divided into 2 steps
    sapkowski = Author(name="Andrzej Sapkowski")
    # do some stuff
    await sapkowski.save()

    # or save() after initialization
    await Book(author=sapkowski, title="The Witcher", year=1990).save()
    await Book(author=sapkowski, title="The Tower of Fools", year=2002).save()


async def with_connect(function):
    # note that for any other backend than sqlite you actually need to
    # connect to the database to perform db operations
    async with database:
        print(f"database.is_connected {database.is_connected}")
        await function()


def main():
    log = set_logger()
    print(cfg.DB_DSN)
    # for func in [create, read, update, delete, joins,
    #              filter_and_sort, subset_of_columns,
    #              pagination, aggregations]:
    # print(f"Executing: {func.__name__}")
    # asyncio.run(with_connect(func))
    asyncio.run(with_connect(create))

    # db_connect =  db_get_connection()
    # print(f"connecting... {db_connect.__name__}")

    # note that if you use framework like `fastapi` you shouldn't connect
    # in your endpoints but have a global connection pool
    # check https://collerek.github.io/ormar/fastapi/ and section with db connection


# gather and execute all functions
# note - normally import should be at the beginning of the file


# note that normally you use gather() function to run several functions
# concurrently but we actually modify the data and we rely on the order of functions


if __name__ == "__main__":
    main()

import databases
import sqlalchemy
