# import whois
from whois import whois

# create variable
lookupDomain = whois('kaptencreative.com')

# print result
print(lookupDomain.text)
