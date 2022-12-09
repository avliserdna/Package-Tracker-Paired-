from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    SelectField,
    BooleanField,
    SubmitField
)
from map.map import map

class PackageForm(FlaskForm):
    sender_name = StringField()
