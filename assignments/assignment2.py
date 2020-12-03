from lxml import etree
import requests
from io import StringIO
import re


clvd = input("Please enter the c:lvd: number: ")
# parsing = requests.get("https://anet.be/oai/catgeneric/server.phtml?verb=GetRecord&metadataPrefix=marc21&identifier=c:lvd:", str(clvd))
# print(parsing)
#print("" + clvd)
website = "https://anet.be/oai/catgeneric/server.phtml?verb=GetRecord&metadataPrefix=marc21&identifier=c:lvd:"
website_and_clvd = website + clvd
print(website_and_clvd)

marc21 = re.search('marc21', website_and_clvd)
if not marc21 :
    print("This xml does not contain marc21-format metadata. Please consult different transformer.")

pip install pymarc