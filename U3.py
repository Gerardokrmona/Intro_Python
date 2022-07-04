# LIST, TUPLES, SETS, Dictionaries 

# LIST: Las listas empiezan con [] se cuenta desde el elem 0

friends = ["Rolf", "Bob", "Anne"]
print(friends[0])
print(friends[1])
print(friends[2])

print(len(friends))

amigos = [ ["Gerardo",10], ["Leon", 15], ["David",20] ]
print(amigos[1][0])

amigos.append(["lewis",23])
print(amigos)

amigos.remove(["lewis",23])
print(amigos)

#TUPLES: es común usar paréntesis al rededor aunque no se necesita
#Las tuples no cuentan con Append ni remove

short_tuple = ("Rolf", "Bob", "Anne")

nombres = ("ger","eunice","ana")
nombres = nombres + ("luis",)
print(nombres)

#SET: No mantienen el orden ni repiten elementos


art_friends = {"Rolf","Hugo","Luis"}
science_friends = {"Luis", "Armando"}

art_friends.add("Luis")
print(art_friends)

art_friends.remove("Luis")
print(art_friends)

# función   ---difference---

set1 = art_friends.difference(science_friends)
print(set1)

set2 = science_friends.difference(art_friends)
print(set2)

# #function    --symmetric_difference---

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

#function    ---intersection---
both = science_friends.intersection(art_friends)
print(both)

# #function       -union---

all_friends = art_friends.union(science_friends)
print(all_friends)


# DICTIONARIES: Mantienen el orden, no tiene duplicados

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20 #agrego
friend_ages["Adam"] = 31 #modifica
print(friend_ages)

#podemos convertir una lista de tupples a un diccionario

friends = [("Rolf",24), ("Adam",30), ("Luis", 22)]
friends_dict = dict(friends)
print(friends_dict)