import seeuletter


# Replace this API key with your own.
seeuletter.api_key = "test_726e0bec-90f7-4ae4-8910-e5d12920320c"


# Creating a Letter
example_letter = seeuletter.Letter.create(
    description='Test Letter from Python Bindings',
    to_address={
        'name': 'Erlich',
        'address_line1': '30 rue de rivoli',
        'address_city': 'Paris',
        'address_postalcode': '75004',
        'address_country': 'France'
    },
    from_address={
        'name': 'Erlich',
        'address_line1': '30 rue de rivoli',
        'address_city': 'Paris',
        'address_postalcode': '75004',
        'address_country': 'France'
    },
    #    source_file=open('/path/to/your/file.pdf', 'rb'),
    source_file="""<html>Hello {{name}},</html>""",
    source_file_type="html",
    variables={
        'name': 'Erlich'
    },
    postage_type="prioritaire",
    color="bw"
)

print "Letter Response : "
print "\n"
print example_letter
print "\n"
