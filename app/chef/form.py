from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

from ..models import Recipe, RecipeCategory, User

class AddRecipesForm(FlaskForm):
    """
    Form for chef to enter recipe
    """

    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    people_served = StringField('Number of Plates')
    quantity = StringField('Quantity')
    ingredient = StringField('Ingredient')
    making_steps = StringdField('Making Steps')
    category = QuerySelectField(query_factory=lambda: RecipeCategory.query.all(), get_label="name")
    cook = QuerySelectField(query_factory=lambda: User.query.all(), get_label="name")
    submit = SubmitField('Submit')

class EditRecipeForm(FlaskForm):
    """
    Form for the chef to edit recipe
    """
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    people_served = StringField('Number of Plates')
    quantity = StringField('Quantity')
    ingredient = StringField('Ingredient')
    making_steps = StringdField('Making Steps')
    category = QuerySelectField(query_factory=lambda: RecipeCategory.query.all(), get_label="name")
    cook = QuerySelectField(query_factory=lambda: User.query.all(), get_label="name")
    submit = SubmitField('Save')


    
class AddRecipeCategoryForm(FlaskForm):
    
    """
    Form for the chef to enter recipe category
    """
    category_name = StringField('Category Name', validators = [DataRequired])
    details = StringField('Details')
    user = StringField('Cook')
    submit = SubmitField('Submit')


class EditRecipeCategory(FlaskForm):
    
    """
    Form for chef to edit recipe category
    """
    category_name = StringField('Category Name', validators = [DataRequired])
    user = StringField('Cook')
    submit = SubmitField('Save')
    


