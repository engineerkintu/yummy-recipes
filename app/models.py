from flask_login import UserMixin
from wekzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create a User table
    """
    __tablename__ = 'users'
    user_id = 0

    user_id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(60), index=True, unique=True)
    username=db.Column(db.String(60), index=True, unique=True)
    last_name=db.Column(db.String(60), index=True, unique=True)
    password_hash=db.Column(db.String(128))
       

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def passsword(self, password):
        """
        Set password to a hashed password
        """
        self.passwor_harsh = generate_password_hash(password)

    def verify_password(self, password):
        """
         Check if hashed password matches actual password
         """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    #Set up user_loader
    @login_manager.user_loarder
    def load_user(user_id):
        return User.query,get(int(user_id))


class RecipeCategory(db.Model):
   
    """
    Create a Recipe Category table
    """
    __tablename__ = 'categories'
    
    cat_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    user = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return '<RecipeCategory: {}>'.format(slef.category_name)

   
class Recipe(db.Model):
    """
    Create a Recipe table
    """
    __tablename__ = 'recipes'
   
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(60), unique=True)
    ingredient = db.Column(db.String(300))
    making_steps = db.Column(db.String(300))
    quantity_expected = db.Column(db.String(60))
    people_served = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('categories.cat_id'))
    cook = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return '<Recipe: {}>'.format(self.recipe_name)

   


    
        
    
    
    
        
    

    
