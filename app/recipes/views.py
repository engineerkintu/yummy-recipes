#app/recipe/views.py

from flask import render_template
from flask_login import login_required

from . import recipe

# Recipe views
@recipes.route('/recipes', methods=['GET', 'POST'])

def list_recipes():
    """
    List all recipes
    """

    check_recipe()

    recipes = Recipe.query.all()

    return render_template('chef/recipes.html',
                           recipes=recipes, title="Recipes")


                        
