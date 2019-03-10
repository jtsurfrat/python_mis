# have a HELP command
# have a SHOW command
# clean code up in general

shopping_list = []
# #print out intstructions on how to us app


def show_help():
    print("What should we pick up at the store. ")
    print("""
        Enter DONE to stop app
        Enter 'HELP' for this help
        Enter 'SHOW' to see list
    """)
def show_list():
    print("Here's your list: ")

    for item in shopping_list:
        print(item)

def add_list_item():
    shopping_list.append(new_item)
    print("Added {} in list, your list as {} items ".format(new_item, len(shopping_list)))

show_help()

while True:
    # ask for new items
    new_item = input("> ")
    new_item = new_item.upper()
    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    # add for new items
    add_list_item()


# print out the list
show_list()
#
# items = ['abc', 'efg', 'ha']
#
# def loopy(items):
#     for item in items:
#         if "a" in item:
#             continue
#         else:
#             print(item)
#
#
# loopy(items)
