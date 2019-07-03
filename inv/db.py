from invoke import task


@task
def up(c):
    c.run("echo up")

@task
def down(c):
    c.run("echo down")

@task
def head(c):
    c.run("echo head is ...")
