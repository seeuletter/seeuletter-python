import seeuletter

# Replace this API key with your own.
seeuletter.api_key = "API_KEY_HERE"

# Creating an Account for a company
example_account = seeuletter.Account.create(
  email="msb.partner@example.com",
  name="Erlich Bachman",
  phone="+33104050607",
  company_name="MSB Partner from Python Wrapper",
  address_line1='30 rue de rivoli',
  address_line2='',
  address_city='Paris',
  address_country='France',
  address_postalcode='75004'
)

print "New Account Response : "
print "\n"
print example_account
print "\n"

# Updating email of the created account
seeuletter.Account.updateEmail(
    example_account.company._id,
    "msb.partner.new@example.com",
)

print "Email Account Updated"
print "\n"

