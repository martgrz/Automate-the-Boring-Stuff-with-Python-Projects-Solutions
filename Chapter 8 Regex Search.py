import re, os

AreaCodeRegex = re.compile(r'\d\d-\d\d\d')

AreaCodes=[]

for filename in os.listdir():
    if filename.endswith('txt'):
        file = open(filename)
        file = file.read()
        mo = AreaCodeRegex.findall(file)
        AreaCodes.append(mo)

print(AreaCodes)
       

