import re 
x = "This is a sentence. (once a day) [twice a day]"
x = re.sub("[\(\[].*?[\)\]]", "", x)
x = x.replace('  ','')
print(x)