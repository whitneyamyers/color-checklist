#initial test
# print("Hello World")

#how checklists work
checklist = list()
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

#create
def create(item):
    checklist.append(item)

#read (simplified)
def read(index):
    print(checklist[index])
    # item = checklist[index]
    # return item

#test update
# checklist = ['Blue', 'Orange']
# checklist[1] = 'Cats'
# print(checklist)

#update
def update(index, item):
    checklist[index] = item

#test destroy
# checklist = ['Blue', 'Cats']
# checklist.pop(1)
# print(checklist)

#destroy
def destroy(index):
    checklist.pop(index)

#show all items in list
def list_all_items():
    index = 0
    for list_item in checklist:
        # print(str(index) + item)
        print(str(index) + " " + list_item)
        #calling format method on a string
        # print("{} {}".format(index, item))
        index += 1

#marking items completed
def mark_completed(index):
    item = checklist[index]
    print("{} {}".format("v", item))

#prompting the user to provide input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

#updating a value with a new value
def select(function_code):
    # print(function_code)
    #use the create function
    if function_code.lower() == "c":
        input_item = user_input("Create item:")
        create(input_item)

    #using the read function
    elif function_code.lower() == "r":
        #added int() because error said index must be integer
        item_index = int(user_input("Index number to read:"))
        read(item_index)

    #update items using update function
    elif function_code.lower() == "u":
        item_index = int(user_input("Index number to update:"))
        item_update = user_input("Updated item:")
        update(item_index, item_update)

    #using the print all items function
    elif function_code.lower() == "p":
        # print("print")
        list_all_items()

    #stop running while loop
    elif function_code.lower() == "q":
        return False

    #catch all
    else:
        print("Unknown option")
    return True

#test code
# def test():
#     create("purple sox")
#     create("red cloak")
#     create("green scarf")
#
#     print(read(0))
#     print(read(1))
#
#     update(0, "purple socks")
#
#     destroy(1)
#
#     print(read(0))
#     print(read(1))
#
#     mark_completed(0)
#
#     select("C")
#
#     list_all_items()
#
#     select("R")
#
#     list_all_items()
#
#     select("P")
#
#     list_all_items()
#
#     select("lslkdjf")
#
#     list_all_items()
#
#     user_value = user_input("Please enter a value:")
#     print(user_value)
#
# #run tests
# test()

#while loop
running = True
while running:
    selection = user_input("""Press C - to add to list,
    R - to read from list,
    P - to print list,
    U - to update an item,
    Q - to quit.
    > """)
    running = select(selection)
