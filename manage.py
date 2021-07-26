from flask.cli import FlaskGroup

from src import create_app, db
from src.api.participants.models import Participant
from src.api.screeners.models import Screener

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
    db.session.add(Screener(prospect_name="Bilbo Baggins",
                            prospect_email="bilbo@theshire.net",
                            prospect_phone="19173456789",
                            prospect_id="thisisbilbosid",
                            study_name="Mondelez",
                            response_1="Yes indeed, I love eating!",
                            response_2="I eat 7 meals per day, on average",
                            response_3="My favorite meal? Oh definitely second breakfast",
                            response_4="I love SmartSweets but they do not fill my tummy.",
                            response_5="Yes, I have hair on my feet. Why do you ask?"))
    db.session.commit()


if __name__ == '__main__':
    cli()
