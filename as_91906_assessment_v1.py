import easygui
import number_range as c
import csv

f = open("fruit.txt", "r")

reader = csv.reader(f)

fruits = {}


for row in reader:
    if len(row) == 5:
        fruits[row[0]] = {"Potassium": row[1],
                          "Phosphorus": row[2],
                          "Sugar": row[3],
                          "Calories": row[4]}


def options():
    options ={
        "Add fruit": add_fruit,
        "Search": search,
        "Show fruits": display_fruits,
        "Delete": delete,
        "Exit": exit_fully,
    }


    input = "pick"


    # Loop below continues until user selects "Exit" from options and
    # get_input is set as "N"
    while input != "start":


        msg = "Welcome to Fruit Mix\n What would it be today?"
        title =  "Fruit mix"
        choices = []
        for button in options:
            choices.append(button)
         
        selection = easygui.buttonbox(msg, title, choices)

        input = options[selection]()


def add_fruit():
    title = "Adding fruit"
    msg = "What fruit do you want to add?"
    added_fruit = easygui.enterbox(msg, title)


    if added_fruit == "":
        added_fruit = verify(added_fruit)
   
    added_fruit = added_fruit.upper()
    print(added_fruit)
    # if added_fruit == None:
    #     added_fruit = cancel()


    # while added_fruit == None:
    #     added_fruit = cancel()
    fruit_check = existence(added_fruit)


    if fruit_check in fruits.keys():
        msg = added_fruit + " ALREADY EXIST"
        title = "FRUIT EXISTS"
        easygui.msgbox(msg, title)
        return add_fruit()
    

    elif added_fruit.isalpha():
        potassium_value = potassium_value_check()
        phosphorus_value = phosphorus_value_check()
        sugar_value = sugar_value_check()
        calories_value = calories_value_check()
        print(added_fruit)
    

    else:
        added_fruit = verify(added_fruit)


    fruits[added_fruit] = {
        "Potassium": potassium_value,
        "Phosphorus": phosphorus_value,
        "Sugar": sugar_value,
        "Calories": calories_value
    }
    print(fruits)
    print(fruits[added_fruit])


    # fruits[added_fruit][]
    # f = open("fruits.txt", "w")
    # f.write(added_fruit + ",")
    # f.close
    fruit_details(added_fruit)

def potassium_value_check():
   
    msg = "Add a potassium(mg) value"
    title = "Add value"
    potassium_value = easygui.enterbox(msg, title)

    if potassium_value == None:
        added_fruit = cancel()
        print(potassium_value)
        print(added_fruit)


    elif potassium_value.isdigit() == True or potassium_value != "":
        while potassium_value == "" or int(potassium_value) < c.MIN_POTASSIUM or int(potassium_value) > c.MAX_POTASSIUM:
            msg = "Value entered for potassium needs to be in between " + str(c.MIN_POTASSIUM) + " to " + str(c.MAX_POTASSIUM)
            title = "Value Error"
            new_value = easygui.enterbox(msg, title)

            if int(new_value) >= c.MIN_POTASSIUM and int(new_value) <= c.MAX_POTASSIUM:
                print(new_value)
                return(new_value)
    print(potassium_value)
    return(potassium_value)
           
def phosphorus_value_check():
    msg = "Add a phosphorus(mg) value"
    title = "Add value"
    phosphorus_value = easygui.enterbox(msg, title)


    if phosphorus_value.isdigit() == True or phosphorus_value != "":
        while phosphorus_value == "" or int(phosphorus_value) < c.MIN_PHOSPHORUS or int(phosphorus_value) > c.MAX_PHOSPHORUS:
            msg = "Value entered for phosphorus(mg) needs to be in between " + str(c.MIN_PHOSPHORUS) + " to " + str(c.MAX_PHOSPHORUS)
            title = "Value Error"
            new_value = easygui.enterbox(msg, title)


            if int(new_value) >= c.MIN_PHOSPHORUS and int(new_value) <= c.MAX_PHOSPHORUS:
                print(new_value)
                return(new_value)
    return(phosphorus_value)


def sugar_value_check():
    msg = "Add a sugar(g) value"
    title = "Add value"
    sugar_value = easygui.enterbox(msg, title)


    if sugar_value.isdigit() == True or sugar_value != "":
        while sugar_value == "" or int(sugar_value) < c.MIN_SUGAR or int(sugar_value) > c.MAX_SUGAR:
            msg = "Value entered for sugar(g) needs to be in between " + str(c.MIN_SUGAR) + " to " + str(c.MAX_SUGAR)
            title = "Value Error"
            new_value = easygui.enterbox(msg, title)




            if int(new_value) >= c.MIN_SUGAR and int(new_value) <= c.MAX_SUGAR:
                print(new_value)
                return(new_value)
           
    return(sugar_value)


def calories_value_check():
    msg = "Add a phosphorus(mg) value"
    title = "Add value"
    calories_value = easygui.enterbox(msg, title)


    if calories_value.isdigit() == True or calories_value != "":
        while calories_value == "" or int(calories_value) < c.MIN_CALORIES or int(calories_value) > c.MAX_CALORIES:
            msg = "Value entered for calories(kcal) needs to be in between " + str(c.MIN_CALORIES) + " to " + str(c.MAX_CALORIES)
            title = "Value Error"
            new_value = easygui.enterbox(msg, title)


            if int(new_value) >= c.MIN_CALORIES and int(new_value) <= c.MAX_CALORIES:
                print(new_value)
                return(new_value)
           
    return(calories_value)

def search():
    title = "Searching for a fruit"
    msg = "What fruit do you want to search for?"
    fruit_searched = easygui.enterbox(msg, title).upper()

    if fruit_searched == "":
        fruit_searched = verify(fruit_searched)
   
    fruit_searched = fruit_searched.upper()
    print(fruit_searched)
   
    # Goes through the existence function to check whether the fruit exist or not
    fruit_check = existence(fruit_searched)
    print(fruit_check)


    if fruit_check:
        fruit_details(fruit_check)


    else:
        msg = fruit_searched + " does not exist"
        title = "Non-existing"
        easygui.msgbox(msg, title)
        return search()
       
def display_fruits():

    for fruit_id, fruit_value in fruits.items():
        print("\nFruit name: " + fruit_id)
       
        for fruit_key in fruit_value:
            print(fruit_key + ":", fruit_value[fruit_key])

def verify(fruit_name):

    while fruit_name == "" or fruit_name.isalpha() == False:
        msg = "Please enter a fruit name"
        title = "Fruit name error"
        new_searched = easygui.enterbox(msg, title)
       
        if new_searched.isalpha():
            return new_searched


        # if new_searched =!


def existence(fruit_check):

    for fruit in fruits.keys():
        if fruit_check == fruit:
            return fruit
    return 0

def fruit_details(fruit_name):
    details = [fruit_name + " DETAILS \n"]


    for value in fruits[fruit_name]:
        price = fruits[fruit_name][(value)]
        all_details = value + " : " + price
        full_details = details.append(all_details)
    print(details)
   
    msg = "Do you want to make any changes"
    title = "Fruit details"
    choices = ["No", "Change"]
    changes = easygui.buttonbox("\n".join(details) + "\n\n" + msg, title, choices)


    if changes == "Change":
        make_changes(fruit_name, details)

def make_changes(fruit_name, details):
    edit_boxes = {"Potassium": potassium_value_check,
                  "Phosphorus": phosphorus_value_check,
                  "Sugar": sugar_value_check,
                  "Calories": calories_value_check,
                  }
    msg = "What value do you want to change?"
    title = "Changing value"
    boxes = []
    for edit_options in edit_boxes:
        boxes.append(edit_options)
    print(edit_options)


    box_choosed = easygui.buttonbox(msg, title, boxes)
    print(box_choosed)

# value = fruits[fruit_name][box_choosed]
#     print(value)
   
    value = edit_boxes[box_choosed]()
    print(edit_boxes)
    print(value)

    fruits[fruit_name].update({box_choosed: value})
    print(fruits)

    fruit_details(fruit_name)

def delete():
    msg = "What fruit would you like to delete?"
    title = "Delete fruit"
    delete_fruit = easygui.enterbox(msg, title).upper()


    check_delete = existence(delete_fruit)
    print(check_delete)
    print(fruits.keys())


    if check_delete in fruits.keys():
        msg = "Are you sure you want to delete " + check_delete
        title = "confirm delete"
        delete = easygui.ynbox(msg, title)


        if delete:
            del fruits[delete_fruit]
            print(fruits)


def cancel():
    msg = "Do you want to leave?"
    title = "Leave"
    leave = easygui.ynbox(msg, title)

    if leave:
        return options()
    else:
        return 0
   
def exit_fully():
    msg = "Are you sure you want to exit?"
    title = "Exiting?"
    exit = easygui.ynbox(msg,title)


    if exit:
        return "start"
   
    else:
        return options
   
options()
