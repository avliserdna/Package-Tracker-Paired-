from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    SelectField,
    BooleanField,
    SubmitField
)
from wtforms.validators import DataRequired

from map.map import map

class PackageForm(FlaskForm):
    sender_name = StringField('Sender name', validators=[DataRequired()])
    recipient_name = StringField('Recipient name', validators=[DataRequired()])
    origin = SelectField('Origin', choices=[(city, city) for city in map], validators=[DataRequired()])
    destination = SelectField('Destination', choices=[(city, city) for city in map], validators=[DataRequired()])
    express = BooleanField("Express Shipping?", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
