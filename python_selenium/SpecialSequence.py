import re
text="Alan Turing was born on 23 June 1912 in London"
res=re.findall('\AAlan',text)
print("Result of \A :",res)
print("-"*79)

res1=re.findall(r'\bLon',text)
print("Rsult of \bLon :",res1)
print("-"*79)

res2=re.findall(r'ring\b',text)
print("Rsult of ring\b :",res2)
print("-"*79)

res2=re.findall('\Bon',text)
print("Rsult of \Bon :",res2)
print("-"*79)

res2=re.findall('\d',text)
print("Rsult of \d :",res2)
print("-"*79)

res2=re.findall('\D',text)
print("Rsult of \D :",res2)
print("-"*79)

res2=re.findall('London.\Z',text)
print(res2)