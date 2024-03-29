from datetime import datetime
import re
from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, URL

from utils.enums import Genre, State

def is_valid_phone(number):
    """ Validate Vietnam phone numbers """

    regex = re.compile('^\+?(\d{2})?\s?\d{3,4}\s?\d{3,4}\s?\d{3,4}$')
    return regex.match(number)

def validate(self):
    rv = FlaskForm.validate(self)
    if not rv:
        return False
    if not is_valid_phone(self.phone.data):
        self.phone.errors.append('Invalid phone.')
        return False
    if not set(self.genres.data).issubset(dict(Genre.choices()).keys()):
        self.genres.errors.append('Invalid genres.')
        return False
    if self.state.data not in dict(State.choices()).keys():
        self.state.errors.append('Invalid state.')
        return False
    return True

class ShowForm(FlaskForm ):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link'
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )



class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
     )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
     )

    website_link = StringField(
        'website_link'
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )

