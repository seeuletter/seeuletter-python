import seeuletter

# Replace this API key with your own.
seeuletter.api_key = "API_KEY_HERE"

# Creating a Letter Electronic
example_letter = seeuletter.Letter.createElectronic(
    description='Test Electronic Letter from Python Bindings',
    to_address={
        'email': 'erlich.dumas@example.com',
        'first_name': 'Erlich',
        'last_name': 'Dumas',
        'status': 'individual'
    },
    content='Please review the attached documents:',
    source_file="""<html>Hello {{name}},</html>""",
    source_file_type="html",
    variables={
        'name': 'Erlich'
    },
    postage_type="lre"
)

print "Electronic letter Response : "
print "\n"
print example_letter
print "\n"
