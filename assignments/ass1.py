
### Importing packages

import urllib.request
from json import dumps, loads  
from urllib.parse import quote

try:
    # Asking for user input
    object_search = input("Enter an object for your search: ")

    # Make sure the user input is a valid query string value
    safe_query = quote(object_search)

    webUrl = urllib.request.urlopen('https://www.europeana.eu/api/entities/suggest?wskey=apidemo&text=' + safe_query + '&type=agent')                                 

    # load JSON from the URL into a variable
    data = loads(webUrl.read())

    # dump the JSON object as a string
    print(dumps(data))
    
except Exception as e:
    print("Hey hey foute boel, iets ging mis.")


quote()