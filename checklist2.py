checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    item = checklist[index]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def mark_completed(index):
    item = checklist[index]
    checklist[index] = ("v " + item)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + " " + list_item)
        index += 1

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    if function_code == "r" or "R":
        item_index = int(user_input("Index number of item to read: "))
        read(item_index)

    elif function_code == "c" or "C":
        input_item = user_input("Create item: ")
        create(input_item)

    elif function_code == "p" or "P":
        list_all_items()

    else:
        print("Unknown Option")

def test():
    create("purple sox")
    create("red shoe")
    create("green scarf")

    print(read(0))
    print(read(1))
    print(read(2))

    update(0, "purple socks")
    destroy(2)

    mark_completed(0)

    list_all_items()

    select("c")
    list_all_items()
    select("p")

test()
