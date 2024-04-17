#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Recipe:
    def __init__(self, name, ingredients, cuisine, dietary_preferences, instructions):
        self.name = name
        self.ingredients = ingredients
        self.cuisine = cuisine
        self.dietary_preferences = dietary_preferences
        self.instructions = instructions

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def delete_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                self.recipes.remove(recipe)
                print(f"Recipe '{recipe.name}' deleted successfully.")
                return
        print("Recipe not found.")

    def search_recipes_by_ingredient(self, ingredient):
        found_recipes = []
        for recipe in self.recipes:
            if ingredient.lower() in recipe.ingredients.lower():
                found_recipes.append(recipe)
        if found_recipes:
            print(f"Recipes containing '{ingredient}':")
            for recipe in found_recipes:
                print(recipe.name)
        else:
            print("No recipes found containing that ingredient.")

    def search_recipes_by_cuisine(self, cuisine):
        found_recipes = []
        for recipe in self.recipes:
            if cuisine.lower() == recipe.cuisine.lower():
                found_recipes.append(recipe)
        if found_recipes:
            print(f"Recipes from {cuisine.capitalize()} cuisine:")
            for recipe in found_recipes:
                print(recipe.name)
        else:
            print("No recipes found from that cuisine.")

    def search_recipes_by_dietary_preferences(self, dietary_preference):
        found_recipes = []
        for recipe in self.recipes:
            if dietary_preference.lower() in recipe.dietary_preferences.lower():
                found_recipes.append(recipe)
        if found_recipes:
            print(f"Recipes suitable for {dietary_preference.capitalize()} diet:")
            for recipe in found_recipes:
                print(recipe.name)
        else:
            print("No recipes found suitable for that dietary preference.")

    def search_recipes_by_name(self, recipe_name):
        for recipe in self.recipes:
            if recipe_name.lower() in recipe.name.lower():
                print(f"Recipe found: {recipe.name}")
                print("Ingredients:", recipe.ingredients)
                print("Cuisine:", recipe.cuisine)
                print("Dietary Preferences:", recipe.dietary_preferences)
                print("Instructions:", recipe.instructions)
                return
        print("Recipe not found.")

    def display_all_recipes(self):
        print("All Recipes:")
        for recipe in self.recipes:
            print(recipe.name)

    def edit_recipe(self, recipe_name, new_name, new_ingredients, new_cuisine, new_dietary_preferences, new_instructions):
        for recipe in self.recipes:
            if recipe_name.lower() == recipe.name.lower():
                recipe.name = new_name
                recipe.ingredients = new_ingredients
                recipe.cuisine = new_cuisine
                recipe.dietary_preferences = new_dietary_preferences
                recipe.instructions = new_instructions
                print("Recipe updated successfully.")
                return
        print("Recipe not found.")

# Sample usage
if __name__ == "__main__":
    recipe_manager = RecipeManager()

    # Adding sample recipes
    recipe1 = Recipe("Spaghetti Carbonara", "spaghetti, eggs, bacon, parmesan cheese, black pepper", "Italian", "Non-vegetarian", "Cook spaghetti. Fry bacon. Mix eggs, cheese, and pepper. Combine.")
    recipe2 = Recipe("Vegetable Stir Fry", "mixed vegetables, soy sauce, garlic, ginger", "Asian", "Vegetarian", "Stir fry vegetables with soy sauce, garlic, and ginger.")
    recipe3 = Recipe("Chicken Curry", "chicken, onions, tomatoes, curry powder", "Indian", "Non-vegetarian", "Cook chicken with onions, tomatoes, and curry powder.")

    recipe_manager.add_recipe(recipe1)
    recipe_manager.add_recipe(recipe2)
    recipe_manager.add_recipe(recipe3)

    # Search recipes by name
    recipe_manager.search_recipes_by_name("Spaghetti Carbonara")

    # Edit a recipe
    recipe_manager.edit_recipe("Spaghetti Carbonara", "Spaghetti Carbonara with Mushrooms", "spaghetti, eggs, bacon, mushrooms, parmesan cheese, black pepper", "Italian", "Non-vegetarian", "Cook spaghetti. Fry bacon and mushrooms. Mix eggs, cheese, and pepper. Combine.")

    # Display all recipes
    recipe_manager.display_all_recipes()


# In[ ]:




