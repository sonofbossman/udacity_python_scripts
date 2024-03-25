filepath = "pi_digits.txt"
# with open(filepath) as fileObject:
#     content = fileObject.read()
#     print(content.strip())

# with open(filepath) as fileObject:
#     for line in fileObject:
#         print(line.rstrip())

with open(filepath) as fileObject:
    content = fileObject.readlines()
str = ''
for line in content:
    str += line.rstrip()
print(str)