# seeuletter-python

[![PyPI version](https://badge.fury.io/py/seeuletter.svg)](http://badge.fury.io/py/seeuletter)



Seeuletter.com Python bindings is a simple but flexible wrapper for the [Seeuletter.com](https://www.seeuletter.com) API.

See full Seeuletter.com documentation [here](https://docs.seeuletter.com/?python#).

For best results, be sure that you're using the latest version of the Seeuletter API and the latest version of the Python wrapper.

#### French
Un module Python pour envoyer du courrier postal en ligne depuis votre application Python.

Seeuletter propose une API permettant d'envoyer très facilement du courrier postal depuis votre ERP, CRM ou application web.

Pas de frais d'installation. Pas d'engagement. Vous payez ce que vous consommez.

Documentation : https://docs.seeuletter.com/?python

Bien démarrer : https://www.seeuletter.com/guide/bien-demarrer-avec-l-api-d-envoi-de-courrier

## Table of Contents

- [Getting Started](#getting-started)
  - [Registration](#registration)
  - [Installation](#installation)
  - [Usage](#usage)
- [Examples](#examples)

## Getting Started

Here's a general overview of the Seeuletter services available, click through to read more.


Please read through the official [API Documentation](https://docs.seeuletter.com/?python#) to get a complete sense of what to expect from each endpoint.

### Registration

First, you will need to first create an account at [Seeuletter.com](https://www.seeuletter.com/signup) and obtain your Test and Live API Keys.

Once you have created an account, you can access your API Keys from the [API Keys Panel](https://www.seeuletter.com/app/dashboard/keys).


### Installation

seeuletter-python can be installed through the `pip` or `easy_install`:

```
pip install seeuletter
easy_install seeuletter
```

### Usage

#### Create a new letter
```python
import seeuletter
seeuletter.api_key = 'your-api-key'

example_letter = seeuletter.Letter.create(
    description='Test Letter from Python Bindings',
    to={
        'name': 'Erlich',
        'address_line1': '30 rue de rivoli',
        'address_city': 'Paris',
        'address_postalcode': '75004',
        'address_country': 'France'
    },
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
```

#### List all letters
```python
import seeuletter
seeuletter.api_key = 'your-api-key'

list_letters = seeuletter.Letter.list()

print "List Letters : "
print "\n"
print list_letters
print "\n"
```

#### Retrieve a specific letter
```python
import seeuletter
seeuletter.api_key = 'your-api-key'

get_letter = seeuletter.Letter.retrieve('ID_OF_THE_LETTER')

print "Get Letter : "
print "\n"
print get_letter
print "\n"
```


## Examples

We've provided various examples for you to try out [here](https://github.com/seeuletter/seeuletter-python/tree/master/examples).


=======================

Copyright &copy; 2017 Seeuletter.com

Released under the MIT License, which can be found in the repository in `LICENSE.txt`.
