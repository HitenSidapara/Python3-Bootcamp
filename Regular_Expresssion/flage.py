# Without Verbose Flag...
# pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

import re

pattern = re.compile("""
	^([a-z0-9_\.-]+)	#first part of email	
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""",re.VERBOSE | re.IGNORECASE)


# re.VERBOSE | re.IGNORECASE = re.X | re.I

result = pattern.search("hitensidapara@gmail.com")
print(result.group())
print(result.groups())