ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
#split teil einen string auf. Das Trennsymbol ist das Argument von Split. --> ist das Trennsymbol nicht vorhanden ist stuff eine List der Länge 1

stuff = ten_things.split(' ')
print(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
#join macht das Gegenteil von split und erzeugt aus einer Liste einen String. Die einzelnen Listen-Elemente sind dabei
# durch den String, auf dem man die join Methode ruft, getrennt. Hier ist das ' ' .
print(' '.join(stuff)) #what? cool!
print('#'.join(stuff[3:5])) #super stellar!

#homework for myself:
# Ausprobieren ob "split" auch z.b. Punkte als Argument nimmt und dann immer beim punkt trennt
#Tut es!
