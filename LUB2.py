name="vivek"
print(name.upper())
print(name.capitalize())
print(name.index('i'))
print(name[3])
print(name.count("v"))

# list assignmant
lst=["my","name","is","vivek",]
print(type(lst))

lst.append("nagre")
print(lst.index("my"))
lst.reverse()
lst.remove("is")
lst.insert(0,"so what")
# del lst
print(lst)

# assignment number 3 dictionary
dit={"name":"vivek"}
print(dit)
print(dit['name'])
print(dit.keys())
print(dit.values())
dit.update({"name2":"sham"})
print(dit.items())