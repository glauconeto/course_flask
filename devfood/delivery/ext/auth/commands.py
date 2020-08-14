import click

from delivery.ext.auth.models import User
from delivery.ext.auth.controller import  create_user

# TODO: Mover para controller
def list_users():
    users = User.query.all()
    click.echo(f"lista de usuarios {users}")


@click.option("--email", "-e")
@click.option("--password", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, password, admin):
    """adiciona novo usuario"""
    # TODO: tratar User Exists exception
    create_user(email=email, password=password, admin=admin)

    click.echo(f"Usuário {email} criado com sucesso!")
