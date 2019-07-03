from invoke import task, Collection

from inv import db


@task
def lint(c):  # pylint: disable=invalid-name
    c.run('./venv/bin/pylint proj')


ns = Collection(db, lint)  # pylint: disable=invalid-name
