value = raw_input()
print any([c.isalnum() for c in value])
print any([c.isalpha() for c in value])
print any([c.isdigit() for c in value])
print any([c.islower() for c in value])
print any([c.isupper() for c in value])