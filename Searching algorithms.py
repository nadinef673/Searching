#membership list
friend = ["Lelethu", "Amber", "Zoe", "Litha"]
x = input("Enter name of person:")
print(x in friend)
#linear search
friend = ["Lelethu", "Amber", "Zoe", "Litha"]
x = input("Enter name of person:")
for y in range(len(friend)):
    if friend[y] == x:
        answer = True
        print("Element exists")

    else:
        print("Element doesn't exist")


