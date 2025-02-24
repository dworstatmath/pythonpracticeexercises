# movies=["The Thing", "Animal House", "Rush Hour", "Rush Hour 2"]
# num=0
# for movie in movies:
#     num=num+1
#     print(str(num)+". "+movie)

# movies.sort()#sorts alphabetically
# print(movies)
# movies.append("Fantastic 4")#adds item to end of list
# print(movies)
# movies.pop()#removes last item
# movies.pop()
# print(movies)
# movies.remove("Animal House")#removes first instance of item
# print(movies)
# movies.insert(1, "Deadpool")#adds item to index 1 of list
# print(movies)
# print(len(movies))
# print(movies[len(movies)-1])

# #removing nuber from a list
# numbers=[1,2,2,9,2,2,9,12]
# while 2 in numbers:
#     numbers.remove(2)
# print(numbers)
# name="ian ng"
# for letter in name:
#     print(letter)

groceries=["cheez its","nerds gummy clusters", "doritos","cocoa puffs","pepsi","dr. pepper", "mountain dew"]
string="You have "
for grocery in groceries[0:len(groceries)-1]:
    string+=(grocery+", ")
string+=("and "+groceries[len(groceries)-1]+".")
print(string)
while 1>0:
    remove=input("What item do you want to remove? \n")
    if remove in groceries:
        groceries.remove(remove)
        string="You have "
        for grocery in groceries[0:len(groceries)-2]:
            string+=(grocery+", ")
        string+=("and "+groceries[len(groceries)-1]+".")
        print(string)
    elif remove in ["stop","halt", "none","nothing"]:
        break
    else:
        print("You don't have that item")