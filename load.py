from models import engine, db_session, Base, CoffeeBar, Comment
Base.metadata.create_all(bind=engine)

# Fill the tables with some data
coffeebar_01 = CoffeeBar(name='Bistro Louis',
    intro='''
Ontdek een sfeervolle Franse bistro en maak kennis met gerechten die op klassieke, Franse wijze worden geserveerd.
''',
    description='''
                        Ontdek een sfeervolle Franse bistro en maak kennis met gerechten die op klassieke, Franse wijze worden geserveerd. Oeh, là,là! Is het iets wat je aanspreekt? Een menu met bijna uitsluitend Franse gerechten die misschien een klein snufje van iets anders hebben, maar die zó op het menu van een Parijs’ restaurant kunnen staan. Durf te ontdekken en durf te genieten. Alles kan en laat je meevoeren door deze fameuze keuken!
_Openingstijden_

Maandag t/m zondag 17.00 - 23.00 uur (zaterdag vanaf 14.00u)
''',
    image='images/bistro-louis-het-restaurant-d8483.jpg')

db_session.add(coffeebar_01)


comment_01 = Comment(
    coffeebar=coffeebar_01,
    message='''
Als paddenstoelen schieten ze uit de grond. De koffiespots in Eindhoven. Een aangename toevoeging is CoffeeLab. Qua interieur leuk, maar ook een beetje standaard (zoek maar eens op coffeebar op Pinterest). Maar goed de koffie. Ik kon kiezen uit 2 soorten bonen. Douwe Egberts en CoffeeLab's eigen bonen. Helaas werd me niet duidelijk wat voor bonen (herkomst / branding) dat dan was. Ik ging voor de cappuccino (met uiteraard de huisboon). Absoluut een mooi staaltje latte-art, maar daar gaat het de die-hard koffiekenner natuurlijk niet om. Mijn koffie smaakte goed, absoluut, maar wel anders dan anders. Niet je standaard koffie. Wellicht kwam dat door mijn keuze koffieboon, maar dan had ik toch graag iets van de afkomst geweten (ik gok Afrikaans trouwens).
''')
db_session.add(comment_01)

comment_02 = Comment(
    coffeebar=coffeebar_01,
    message='''
Beste Bart, dank voor je bezoek! Goede tip van je om de samenstelling van onze huisblend duidelijker aan te geven. We zijn nog 'under construction' ;)
''')
db_session.add(comment_02)


# Fill the tables with some data
coffeebar_02 = CoffeeBar(
    name='Coffeelab',
    intro='''
Kei lekkere koffie, toast en super gastvrije barista's! FREE WIFI. Producten Hele lekkere Koffie Hele lekkereThee Hele Dikke toast En uiteraard onze zelfgebakken taarten, brownies en blondies. Glutenvrij en Vegan! Het maakt ons niet uit!
''',
    description='''
Kei lekkere koffie, toast en super gastvrije barista's! FREE WIFI. Producten Hele lekkere Koffie Hele lekkereThee Hele Dikke toast En uiteraard onze zelfgebakken taarten, brownies en blondies. Glutenvrij en Vegan! Het maakt ons niet uit!
''',
    image='images/coffeelab.jpg'
)

db_session.add(coffeebar_02)

comment_01 = Comment(
    coffeebar=coffeebar_02,
    message='''
Heerlijke cappuccino die steeds met aandacht en veel liefde wordt bereid. Sinds de zomer van 2016 geniet ik bij Coffeelab van speciale koningscappuccino die wordt geserveerd metcaffeinevrije koffie, soyamelk of met cocosmelk. mmmme
''')
db_session.add(comment_01)

comment_02 = Comment(
    coffeebar=coffeebar_02,
    message='''
terwijl ik bovenstaande reactie schrijf zoek ik waar ik m'n puntwaardering kan geven. zie ik na de enter dat er automatisch een 6 gegeven wordt. Daarmee geef ik deze koffiewaardering-site een 4 voor gebruiksvriendelijkheid.
''')
db_session.add(comment_02)


db_session.commit()
