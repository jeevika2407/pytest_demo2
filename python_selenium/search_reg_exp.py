# import re
# text="alam iam a good good good girl london"
# # res=re.search("^alam.*london$",text)
# res=re.search("good",text)
# print("result: {} and start and position of end={}".format(res,res.span()))

# res1=re.findall("good",text)
# print("result= {}".format(res1))

# print(res)
# if(res1):
#     print("yes")
# else:
#     print("no")











# import re

# text = "alam iam a good good good girl london"

# # Search using re.search
# res = re.search("^alam.*london$", text)

# # Find all occurrences of "good" using re.findall
# res1 = re.findall("good", text)

# print("result= {}".format(res1))

# # Print the result of re.search
# print(res)

# # Check if any match was found for "good"
# if res1:
#     print("yes")
# else:
#     print("no")

# Using re.split() to split the text wherever there's a space (or other pattern)
# split_result = re.split(r"\s", text)  # Splits based on spaces
# print("Split result:", split_result)

# # Using re.sub() to replace "good" with "excellent"
# sub_result = re.sub(r"good", "excellent", text)
# print("Sub result:", sub_result)



# import re
# text="alam iam a good good good girl london"
# res=re.search("goo",text)
# print("result: {} and start and position of end={}".format(res,res.span()))

# res = re.split("iam", text)  # Splits based on spaces
# print("Split result: {}".format(res))

# pattern = "^a.*d$"
# sample_text = "abcd"
# match = re.search(pattern, sample_text)

# print("Pattern {}", bool(match))

# sub_result = re.sub("good", "excellent", text)
# print("Sub result:", sub_result)


import re
text = "Hello, this is a test message."

# Replace only if it starts with 'H' and ends with '.'
new_text = re.sub(r"^H.*\.$", "Modified line", text)

print(new_text)
