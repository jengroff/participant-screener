from flask.cli import FlaskGroup

from src import create_app, db
from src.api.participants.models import Participant

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    db.session.add(Participant(name='jengroff', email='josh@marchingant.com', phone='+19172975952'))
    db.session.add(Participant(name='joshengroff', email='josh.engroff@gmail.com', phone='+19172975952'))
    db.session.commit()


if __name__ == '__main__':
    cli()
