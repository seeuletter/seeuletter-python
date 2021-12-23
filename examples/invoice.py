import seeuletter

# Replace this API key with your own.
seeuletter.api_key = "API_KEY_HERE"

# Listing all invoices with filters
example_list = seeuletter.Invoice.list(
  # Filter only paid invoice
  status="paid",
  # Invoice date must be greater than 01-01-2020
  date_start="2020-01-01"
)

print "List Invoice Response : "
print "\n"
print example_list
print "\n"

# Retrieve a single invoice by id
example_invoice = seeuletter.Invoice.retrieve(
    example_list.invoices[0]._id,
)

print "Invoice Response : "
print "\n"
print example_invoice
print "\n"
