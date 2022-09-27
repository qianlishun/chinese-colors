import re
 
filepath = "/Users/mrq/Desktop/WorkSpace/code/chinese-colors/src/assets//colors.json"
txt = open(filepath, "r").read()
result=""
test_text = re.findall(r'\"hex\": (.*)\,',txt)
result = result +'\n'.join(test_text)
print(result)