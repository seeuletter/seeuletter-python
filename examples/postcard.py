import seeuletter

# Replace this API key with your own.
seeuletter.api_key = "API_KEY_HERE"


# Creating a Postcard
example_postcard = seeuletter.Postcard.create(
    description='Test Postcard from Python Bindings',
    to={
        'name': 'Erlich',
        'address_line1': '30 rue de rivoli',
        'address_city': 'Paris',
        'address_postalcode': '75004',
        'address_country': 'France'
    },
    source_file_front="""<html>Hello {{name}}, i'm the front.</html>""",
    source_file_front_type="html",
    source_file_back="""<html>Hello {{name}}, i'm the back.</html>""",
    source_file_back_type="html",
    merge_variables={
        'name': "Erlich"
    }
)

print "Postcard Response : "
print "\n"
print example_postcard
print "\n"
