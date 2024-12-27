import click
from domainfy import domainfy


@click.group()
def cli():
    pass


@click.command()
# @click.option("--domain", "-d", help="Domain to check", multiple=True, type=str)
@click.option("--domain", default=1, help="domain to check")
@click.argument("domains")
def check_domain(domain: str):
    click.echo("initializing, welcome to domainfy!")
    try:
        domainfy.IntervalRunner(60, domainfy.Domainfy(domain).check_domains).run()
    except KeyboardInterrupt:
        click.echo("Bye!")

cli.add_command(check_domain)
