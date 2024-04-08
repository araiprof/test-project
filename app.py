import random

from flask import Flask, render_template

app = Flask(__name__)

# Example recipes
recipes = [
    {
        'title': 'Authentic Italian Tiramisu',
        'ingredients': [
            '300 g Savoiardi (Ladyfingers) - about 30 cookies',
            '500 g mascarpone cheese',
            '4 medium eggs',
            '100 g granulated sugar',
            '300 ml espresso coffee',
            '2 tablespoons Marsala Wine',
            'Unsweetened cocoa powder for decoration'
        ],
        'instructions': [
            'Make the coffee and add Marsala wine. Set aside to cool.',
            'Separate egg whites from yolks. Whip egg whites to stiff peaks. Set aside.',
            'Beat egg yolks with sugar until light and smooth.',
            'Soften mascarpone cheese and combine with the yolk mixture.',
            'Gently fold in whipped egg whites.',
            'Dip ladyfingers in coffee and layer in a dish.',
            'Alternate layers of mascarpone mixture and ladyfingers.',
            'Finish with a layer of mascarpone, then dust with cocoa powder.',
            'Refrigerate for at least 3 hours before serving.'
        ]
    },
    {'title': 'Stuffed peppers',
     'ingredients': [
         '1/2 c. uncooked white or brown rice',
         '2 tbsp. extra-virgin olive oil, plus more for drizzling',
         '1 medium yellow onion, chopped',
         '3 cloves garlic, finely chopped',
         '2 tbsp. tomato paste',
         '1 lb. ground beef',
         '1 (14.5-oz.) can diced tomatoes',
         '1 1/2 tsp. dried oregano',
         'Kosher salt',
         'Freshly ground black pepper',
         '6 bell peppers, tops and cores removed',
         '1 c. shredded Monterey jack',
         'Chopped fresh parsley, for serving'
     ],
     'instructions':[
         'Preheat oven to 400°. In a small saucepan, prepare rice according to package instructions.',
         'Meanwhile, in a large skillet over medium heat, heat oil. Cook onion, stirring occasionally, ',
         'until softened, about 7 minutes. Stir in garlic and tomato paste and cook, stirring, until fragrant, ',
         'about 1 minute more. Add ground beef and cook, breaking up meat with a wooden spoon, until no longer pink, ',
         'about 6 minutes. Drain excess fat.',
         'Stir in rice and diced tomatoes; season with oregano, salt, and pepper. Let simmer, stirring occasionally, until liquid has reduced slightly, about 5 minutes.',
         'Arrange peppers cut side up in a 13"x9" baking dish and drizzle with oil. Spoon beef mixture into each pepper. Top with cheese, then cover baking dish with foil.',
         'Bake peppers until tender, about 35 minutes. Uncover and continue to bake until cheese is bubbly, about 10 minutes more.',
         'Top with parsley before serving.'
     ]
     }
]


@app.route('/')
def homepage(name=None):
    return render_template('index.html', name=name)


@app.route('/aiga')
def aiga(name=None):
    return render_template('aiga.html', name=name)


@app.route('/recipes')
def recipe_listing():
    return render_template('recipes.html', recipes=recipes)
    # Pass the list of recipes to the template

@app.route('/randomrecipe')
def randomizer ():
    # Pass the list of recipes to the template
    return render_template('randomrecipe.html', recipes=recipes)

@app.route('/madi')
def madi(name=None):
    return render_template('madi.html', name=name)

@app.route('/getrandomrecipe')
def get_random_recipe():
    recipe = random.choice(recipes)
    return render_template('recipe_snippet.html', recipe=recipe)



if __name__ == '__main__':
    app.run()
