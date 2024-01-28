nombres=["Ana","Pablo","Carmen","Diego"]

for nombre in nombres:
    print(nombre)

personas=[]
a={"nombre":"Ana","edad":28}
b={"nombre":"Pablo","edad":36}
personas.append(a)
personas.append(b)
for persona in personas:
    print(persona["nombre"],persona["edad"])

print(personas)


lista=[1,2,3,4]
for indice,numero in enumerate(lista):
    lista[indice] *=2
    print(lista)