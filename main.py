import click


@click.command()
@click.option("--name", default="", help="Your name")
def hello(name):
    click.echo("Hello %s"%name)


if __name__ == "__main__":
    hello()