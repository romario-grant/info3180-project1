from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = IntegerField('No. of Rooms', validators=[DataRequired()])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    property_type = SelectField(
        'Property Type',
        choices=[('House', 'House'), ('Apartment', 'Apartment')]
    )
    photo = FileField('Photo', validators=[DataRequired()])