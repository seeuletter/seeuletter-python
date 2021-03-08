import seeuletter

# Replace this API key with your own.
seeuletter.api_key = "test_726e0bec-90f7-4ae4-8910-e5d12920320c"

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
