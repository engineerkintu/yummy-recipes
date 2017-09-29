import os

from flask import abort, url_for

from app.models import User, Recipe, RecipeCategory

class TestModels(TestBase):

    def test_user_model(self):
        """
        Test number of records in User table
        """
        self.assertEqual(User.query.count(), 2)

    def test_recipe_category_model(self):
        """
        Test number of records in Recipe table
        """

        # create test recipe_category
        recipe = RecipeCategory(reci_name="Rolex", description="Chapati and egg")

        # save recipe category to database
        db.session.add(recipe)
        db.session.commit()

        self.assertEqual(RecipeCategory.query.count(), 1)

    def test_recipe_model(self):
        """
        Test number of records in Recipes table
        """

        # create test recipe
        recicipe = Recipe(recipe_name="Mugoyo", ingredient="Sweet potato and beans",maki_steps="boil and mingle")

        # save role to database
        db.session.add(recipe)
        db.session.commit()

        self.assertEqual(Recipe.query.count(), 1)

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """
        Test that logout link is inaccessible without login
        and redirects to login page then to logout
        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_admin_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('home.admin_dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_recipe_categories_view(self):
        """
        Test that recipe categories page is inaccessible without login
        and redirects to login page then to recipe categories page
        """
        target_url = url_for('chef.list_recipe_categories')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_recipes_view(self):
        """
        Test that roles page is inaccessible without login
        and redirects to login page then to roles page
        """
        target_url = url_for('chef.list_recipes')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

  

if __name__ == '__main__':
    unittest.main()
