import re

email = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
text = "2k21cse055@kiot.ac.in"

found = re.findall(email, text)

if found:
    print(found)
else:
    print(found)



# import re

# # Email test string
# text = "2k21cse055@kiot.ac.in"

# # Original regex — matches only one domain extension
# email1 = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}\b"
# found1 = re.findall(email1, text)

# # Updated regex — matches multiple domain extensions like .ac.in
# email2 = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+\b"
# found2 = re.findall(email2, text)

# print("Original regex match:", found1)
# print("Updated regex match:", found2)

