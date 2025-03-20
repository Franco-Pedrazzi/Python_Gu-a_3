lista=[{"name":"Ana","years":51},{"name":"Gabriela","years":15}]
print(" ")
print("1")
print(" ")
print(lista[0],lista[0]["name"],lista[1]["years"])

print(" ")
print("1.2")
print(" ")
for dic in lista:
    print(lista.index(dic))
    for key in dic:
        print(key,dic[key])
    print(" ")