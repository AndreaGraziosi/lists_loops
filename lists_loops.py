#Q1
songs = ["ROCKSTAR", "Do It", "For The Night"]
#Q2  print out "do it"and "for the night"
print(songs[1:3])
#Q3 update the last element
songs[2] = "Miles Away"
#print the list
print(songs)
#Q4
songs.extend(["Lemon Grove Avenue", "And Buddha Too", "Segue o Seco"])
print(songs)
songs.remove("Do It")
print(songs)
#Q6
animals = ["monkey","dolphin","Tucan"]
print(animals)
#append an animal
animals.append("Turtle")
print(animals)
#print out 3rd animal
print(animals[2])
del animals[0]
print(animals)
# use aloop to print out all animals
for animal in animals:
    print(animal)