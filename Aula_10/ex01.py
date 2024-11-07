x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
print(x, type(x))
print(x["RN"])
print(x["PB"])
x["AM"] = "Manaus"
x["PB"] = "J. Pessoa"
print(x)
#print(x["RJ"])

for item in x.items(): print(item)



y = [1, 2, 3]
print(y, type(y))

