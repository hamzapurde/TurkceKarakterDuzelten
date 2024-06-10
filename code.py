name=input(" Enter Text :  ")
turkceK="ıüçşöğ"
replace="iucsog"
for i in range(2):
        for j in range(6):
            name=name.replace(str(turkceK[j]),str(replace[j]))
        turkceK= turkceK.upper()
        replace= replace.upper()
name=name.center(10,'*')
print("New Text : {}".format(name))