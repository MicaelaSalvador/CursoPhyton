# libros={"los pilares de la tierra":1989,"El codigo davinci":2003}
# for titulo in libros:
#     print(titulo)
# for key in libros :
#     print(libros[key])


peliculas =[]

a={"titulo":"start wars","ano":1977,"director":"George Lucas"}
b={"titulo":"El senor de los anillos","ano":2001,"director":"Peter Jackson"}
c={"titulo":"Psicosis","ano":1960,"director":"Alfred Hitchcock"}

peliculas.append(a)
peliculas.append(b)
peliculas.append(c)

#print(peliculas[0])

contador = 0
for pelicula in peliculas:
    if contador == 1:
        print(pelicula["titulo"],pelicula["ano"],pelicula["director"])
    contador += 1
    
