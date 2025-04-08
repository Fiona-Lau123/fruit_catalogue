import easygui
import number_range as c
import csv


# Reads the file 
f = open("fruit.txt", "r")

reader = csv.reader(f)

fruits = {}

# To make the file into a nested dictionary 
for row in reader:
    if len(row) == 5:
        fruits[row[0]] = {"Potassium": row[1],
                          "Phosphorus": row[2],
                          "Sugar": row[3],
                          "Calories": row[4]}


def options():
    """Display option boxes the user can choose from"""
    
    options ={
        "Add fruit": add_fruit,
        "Search": search,
        "Show fruits": display_fruits,
        "Delete": delete,
        "Exit": exit_fully,
    }


    input = "pick"

    # This while loop will continue until it returns as "start"
    while input != "start":

        msg = "Welcome to Fruit Mix\n What would it be today?"
        title =  "Fruit mix"
        choices = []
        for button in options:
            choices.append(button)
         
        selection = easygui.buttonbox(msg, title, choices)

        # Will go through the function the user pressed
        input = options[selection]()


def add_fruit():
    """Goes through the search function, to search for a fruit detail"""

    # Asks user which fruit they want to add
    title = "Adding fruit"
    msg = "What fruit do you want to add?"
    added_fruit = easygui.enterbox(msg, title)
    
    # When user pressed cancel when adding fruit then 
    # it would go through cancel function
    if added_fruit == None:
        added_fruit = cancel()
        
    # While loop is to make sure a appropriate name is entered
    while added_fruit == "" or added_fruit == 0 \
        or added_fruit.isalpha() == False:
        added_fruit = verify(added_fruit)
   
    # Changes to what the addeed_fruit return as, to all capital letters
    added_fruit = added_fruit.upper()

    # Checks if the fruit exist or not. Goes through existence function
    fruit_check = existence(added_fruit)

    # Goes through if statement if user entered a fruit that
    # is in the nested dictionary

    if fruit_check in fruits.keys():
        msg = added_fruit + " ALREADY EXIST"
        title = "FRUIT EXISTS"
        easygui.msgbox(msg, title)
        return add_fruit() # Goes back to add_fruit funtion
    
    # Goes through elif statement when user entered a appropriate fruit
    # name that does not exist in the dictionary
    elif added_fruit.isalpha():

        # Goes through each value function to get a value
        potassium_value = potassium_value_check()
        phosphorus_value = phosphorus_value_check()
        sugar_value = sugar_value_check()
        calories_value = calories_value_check()
    
    # When user did not enter a appropriate name the user is made 
    # sure to go through verify function to enter name again
    else:
        added_fruit = verify(added_fruit) # Goes through verify function

    # Makes the fruit added into a dictionary with the values
    fruits[added_fruit] = {
        "Potassium": potassium_value,
        "Phosphorus": phosphorus_value,
        "Sugar": sugar_value,
        "Calories": calories_value
    }


    fruit_details(added_fruit) # Display the fruit details


def potassium_value_check():
    """Add a potassium value, as well as making sure the 
    value enter is in the range"""
   
   # Add potassium value 
    msg = "Add a potassium(mg) value"
    title = "Add value"
    potassium_value = easygui.enterbox(msg, title)

    # If user pressed cancel button. User goes through cancel function
    if potassium_value == None:
        potassium_value = cancel()

    # What the user entered is made sure the user has entered something. 
    # It will go through empty_value function
    potassium_value = empty_value(potassium_value)

    # User will go through if function when value is not in range
    if potassium_value.isdigit() == True or potassium_value != "":

        # User will be looped until potassium value is in the range
        while potassium_value == "" or \
            potassium_value.isdigit() == False or \
                int(potassium_value) < c.MIN_POTASSIUM or \
                    int(potassium_value) > c.MAX_POTASSIUM:
            
            msg = "Value entered for potassium needs to be in between " \
                  + str(c.MIN_POTASSIUM) + " to " + str(c.MAX_POTASSIUM)
            title = "Value Error"
            potassium_value = easygui.enterbox(msg, title)

            # Goes through cancel function when user press cancel
            if potassium_value == None:
                potassium_value = cancel()

        return(potassium_value) # return with the value
    return(potassium_value) # return with the value

def phosphorus_value_check():
    """Add a phosphorus value. 
    As well as checking that the value entered is in the range"""

    # Allow user to add a phosphorus value
    msg = "Add a phosphorus(mg) value"
    title = "Add value"
    phosphorus_value = easygui.enterbox(msg, title)

    # Goes through cancel function when user press cancel
    if phosphorus_value == None:
        added_fruit = cancel()

    # It will go through empty_value function
    phosphorus_value = empty_value(phosphorus_value)

    # When user entered a value
    if phosphorus_value.isdigit() == True or phosphorus_value != "":

        # User is looped if value entered is not in the range
        while phosphorus_value == "" or phosphorus_value.isdigit() == False\
            or int(phosphorus_value) < c.MIN_PHOSPHORUS or \
                int(phosphorus_value) > c.MAX_PHOSPHORUS:
            
            msg = "Value entered for phosphorus needs to be in between " \
                + str(c.MIN_PHOSPHORUS) + " to " + str(c.MAX_PHOSPHORUS)
            title = "Value Error"
            phosphorus_value = easygui.enterbox(msg, title)

            # Goes through cancel function when user press cancel
            if phosphorus_value == None:
                phosphorus_value = cancel()

        return(phosphorus_value) # return with the value
    return(phosphorus_value) # return with the value


def sugar_value_check():
    """Add a sugar value. 
    As well as checking that the value entered is in the range"""

    # Asking user for a value
    msg = "Add a sugar(g) value"
    title = "Add value"
    sugar_value = easygui.enterbox(msg, title)

    # User pressed cancel, the cancel function is called
    if sugar_value == None:
        added_fruit = cancel()

    # To check if the user entered anythhing. Calls empty_value function
    sugar_value = empty_value(sugar_value)

    # When user entered a value
    if sugar_value.isdigit() == True or sugar_value != "":

        # While loop is used until value entered is in the range
        while sugar_value == "" or sugar_value.isdigit() == False \
            or int(sugar_value) < c.MIN_SUGAR or \
                int(sugar_value) > c.MAX_SUGAR:
            
            # Asks user to enter within the value range
            msg = "Value entered for sugar needs to be in between " \
                + str(c.MIN_SUGAR) + " to " + str(c.MAX_SUGAR)
            title = "Value Error"
            sugar_value = easygui.enterbox(msg, title)

            # Calls cancel function when cancel is pressed
            if sugar_value == None:
                sugar_value = cancel()

        return(sugar_value) # return with the value
    return(sugar_value) # return with the value

def calories_value_check():
    """User add a calorie value and checks the range of calorie value"""

    # Asks user for a calorie value
    msg = "Add a calories(kcal) value"
    title = "Add value"
    calories_value = easygui.enterbox(msg, title)

    # Cancel function is called when cancel is pressed
    if calories_value == None:
        added_fruit = cancel()

    # To check if the user entered nothing for a value
    calories_value = empty_value(calories_value)

    # When user has entered a value 
    if calories_value.isdigit() == True or calories_value != "":

        # Checks if value is in range. 
        # If not user will be looped until value entered is in the range
        while calories_value == "" or calories_value.isdigit() == False \
            or int(calories_value) < c.MIN_CALORIES or \
                int(calories_value) > c.MAX_CALORIES:
            
            # Asks user to enter within the range
            msg = "Value entered for calories needs to be in between " \
                + str(c.MIN_CALORIES) + " to " + str(c.MAX_CALORIES)
            title = "Value Error"
            calories_value = easygui.enterbox(msg, title)


            # Cancel function is called when user press cancel
            if calories_value == None:
                calories_value = cancel()

        return(calories_value) # return with the value
    return(calories_value) # return with the value

def empty_value(value):
    """When user has entered nothing, 
    this function is called until user entered a value"""

    # When user doesn't enter a valid value, 
    # the user is looped back until value entered is valid
    while value == "" or value == 0 or value.isdigit() == False:
        msg = "Please add a valid value"
        title = "No value"
        value = easygui.enterbox(msg, title)

        # Calls cancel function when cancel is pressed
        if value == None:
            value = cancel()

    return value # return with the value

def search():
    """Searches for a fruit and should display fruit details when it exist"""

    # Asks user what they want to search for
    title = "Searching for a fruit"
    msg = "What fruit do you want to search for?"
    fruit_searched = easygui.enterbox(msg, title)

    # Cancel function called when user pressed cancel
    if fruit_searched == None :
        fruit_searched = cancel()

    # User is looped until a valid name is entered
    while fruit_searched == "" or fruit_searched == 0 or \
        fruit_searched.isalpha() == False:
        fruit_searched = verify(fruit_searched)

    
    # Changes fruit_searched to capital letters
    fruit_searched = fruit_searched.upper()
   
    # Goes through the existence function to check
    # whether the fruit exist or not
    fruit_check = existence(fruit_searched)

    # To check whether the fruit exist or not from what the user entered
    if fruit_check:
        fruit_details(fruit_check)

    else:
        # Message for user when fruit does not exist
        msg = fruit_searched + " does not exist"
        title = "Non-existing"
        easygui.msgbox(msg, title)

        return search()
       
def display_fruits():
    """Display the fruit details"""

    for fruit_id, fruit_value in fruits.items():
        print("\nFruit name: " + fruit_id)
       
        for fruit_key in fruit_value:
            print(fruit_key + ":", fruit_value[fruit_key])



def verify(fruit_name):
    """To check whether the name entered is valid 
    or needs to be asked for a name again"""

    # User is looped when there is no valid/suitable name
    while fruit_name == "" or str(fruit_name).isalpha() == False \
        or fruit_name == None:

        # Asks user to enter a fruit name again
        msg = "Please enter a fruit name"
        title = "Fruit name error"
        new_searched = easygui.enterbox(msg, title)

        # Cancel function is called when user pressed cancel
        if new_searched == None:
            new_searched = cancel()

        # When there is a valid/suitable name it would 
        # return back to what they searched(new_searched)
        elif new_searched.isalpha():
            return new_searched


def existence(fruit_check):
    """To check if the fruit entered is in the nested dictionary or not"""

    # Checks if fruit entered is in the dictionary or not
    for fruit in fruits.keys():
        if fruit_check == fruit:
            return fruit
    return 0

def fruit_details(fruit_name):
    """Displaying the fruit details"""

    details = [fruit_name + "\n"]

    # Goes through the details in the dictionary
    for detail in fruits[fruit_name]:
        value = fruits[fruit_name][(detail)]
        all_details = detail + " : " + value
        details.append(all_details)

    # Asks user whether they want to make changes or not
    msg = "Do you want to make any changes"
    title = "Fruit details"
    choices = ["No", "Change"]
    changes = easygui.buttonbox("\n".join(details) \
                                + "\n\n" + msg, title, choices)
    
    # Goes through make_changes function when user press change
    if changes == "Change":
        make_changes(fruit_name)
    
    else:
        return details # returns with the detail

def make_changes(fruit_name):
    """When user wants to make changes to value"""

    # Options for user to choose from
    edit_boxes = {"Potassium": potassium_value_check,
                  "Phosphorus": phosphorus_value_check,
                  "Sugar": sugar_value_check,
                  "Calories": calories_value_check,
                  }
    
    # Asks user what they want to change 
    msg = "What value do you want to change?"
    title = "Changing value"
    boxes = []

    # Shows the different boxes, the user can choose
    for edit_options in edit_boxes:
        boxes.append(edit_options)

    # Display boxes 
    box_choosed = easygui.buttonbox(msg, title, boxes)

    # Goes through the function of what the user pressed
    value = edit_boxes[box_choosed]()

    # Updates the value to what the user entered
    fruits[fruit_name].update({box_choosed: value})

    fruit_details(fruit_name) # Shows fruit details

def delete():
    """Allow user to deleta a fruit"""

    # Asks user what fruit they want to delete
    msg = "What fruit would you like to delete?"
    title = "Delete fruit"
    delete_fruit = easygui.enterbox(msg, title)

    # Cancel function is called when user presses cancel
    if delete_fruit == None :
        delete_fruit = cancel()

    # When fruit name entered is not valid/suitable.
    # It would be looped going to verify fuction
    while delete_fruit == "" or delete_fruit == 0 \
        or delete_fruit.isalpha() == False:

        delete_fruit = verify(delete_fruit)

    # Changes delete_fruit to capital letters
    delete_fruit = delete_fruit.upper()

    # Checks whether the fruit exist or not as 
    # it goes through existence function
    check_delete = existence(delete_fruit)

    # When user entered a existing fruit, 
    # it would go through this if statement. For confirmation
    if check_delete in fruits.keys():
        msg = "ARE YOU SURE YOU WANT TO DELETE " + check_delete
        title = "confirm delete"
        confirm_delete = easygui.ynbox(msg, title)

        # Deletes the fruit when user has confirmed
        if confirm_delete:
            del fruits[delete_fruit]

    # When user entered a fruit that does not exist
    else:
        msg = delete_fruit + \
            " DOES NOT EXIST.\n Do you still want to delete a fruit?"
        title = "non-existing"
        fruit_delete = easygui.ynbox(msg, title)

        # Return back to delete function to search again 
        if fruit_delete:
            return delete()
        
        else:
            return options() # Return to the main/start page


def cancel():
    """When user has pressed cancel button. 
    Allow them to exit if they want to"""

    # Asks for confirmation if they want to leave
    msg = "Do you want to leave?"
    title = "Leave"
    leave = easygui.ynbox(msg, title)

    # When user want to leave, if statement is called. 
    # To return to the start/main page
    if leave:
        return options()
    
    else:
        return 0 # returns as 0
   
def exit_fully():
    """Exiting the program, as well as updating the file"""

    # Asks user for confirmation, if they want to exit
    msg = "Are you sure you want to exit?"
    title = "Exiting?"
    exit = easygui.ynbox(msg,title)

    # When user wants to exit
    if exit:

        # Updates file before it completely ends the program
        f = open("fruit.txt", "w")

        for fruit in fruits:
            f = open("fruit.txt", "a")
            change_file =  fruit + "," + \
                ",".join(fruits[fruit].values()) + "\n"
            print(change_file)
            f.write(change_file)
            f.close()

        return "start" # Program ends 
   
    else:
        # Returns back to option when user doesn't want to exit
        return options
   
options() # Program starts here