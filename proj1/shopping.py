# my_list = []
# stop_shopping = False
#
# while stop_shopping == False:
#     keep_shopping = bool(input("Keep shopping? "))
#
#     if keep_shopping == True:
#         print("You have " ,my_list)
#         new_item = "{}".format(input("Please choose item"))
#         print(new_item)
#     else:
#         print("You don't want to shop", keep_shopping)

# my_list = ["Bacon", "Cat", "Dinosaur"]
#
# for item in my_list:
#     print(my_list)

# make a list hold onto our items
# shopping_list = []
# #print out intstructions on how to us app
# print("What should we pick up at the store. ")
# print("Enter 'Done' to stop adding item. ")
#
# while True:
#     # ask for new items
#     new_item = input("> ")
#     new_item = new_item.upper()
#     # be able to quit the app
#     if new_item == 'DONE':
#         break
#     # add for new items
#     shopping_list.append(new_item)
#
#
# # print out the list
# print("Here's your list: ")
#
# for item in shopping_list:
#     print(item)


my_list = []

def show_help():
    print("What should we pick up at the store. ")
    print("""
        Enter DONE to stop app
        Enter 'HELP' for this help
        Enter 'LIST' to see list
    """)

def show_list(my_list):
    for list in my_list:
        print(list)
    #my_list = ", ".join(my_list)
    print("Your list includes {} and has {} items".format(my_list, len(my_list)))

def add_new_item(new_item):
    my_list.append(new_item)
    print("Added {}. List has {} items".format(new_item, len(my_list)))

print("What to pick up at the store")
show_help()

while True:
        new_item = input(">")
        new_item = new_item.upper()

        if new_item == "DONE":
            break
        elif new_item == "HELP":
            show_help()
            continue
        elif new_item == "LIST":
            show_list(my_list)
            continue
        add_new_item(new_item)


show_list(my_list)
















#
