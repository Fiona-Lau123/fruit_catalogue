import easygui


fruit = {"Strawberry":
    {"Potassium": 153,
     "Phosphorus": 24,
     "Sugar": 5,
     "Calories": 33},
     "Watermelon":
     {"Potassium": 112,
     "Phosphorus": 11,
     "Sugar": 6,
     "Calories": 30},
     "Grape":
     {"Potassium": 191,
     "Phosphorus": 20,
     "Sugar": 16,
     "Calories": 69},
     "Feijoa":
     {"Potassium": 172,
     "Phosphorus": 19,
     "Sugar": 8,
     "Calories": 55},
}


def options():
    options ={
        "Search": search,
        # "Add fruit": add_fruit,
        "Show fruits": display_fruits,
        # "Delete": delete,
        "Exit": exit_fully,
    }


    get_input = "Y"


    # Loop below continues until user selects "Exit" from options and
    # get_input is set as "N"
    while get_input != "N":


        msg = "Welcome to Fruit Mix\n What would it be today?"
        title =  "Fruit mix"
        choices = []
        for i in options:
            choices.append(i)
         
        selection = easygui.buttonbox(msg, title, choices)


        # Calls a specific function, based on the user's selection from
        # the menu.
        # For example, if user clicks on "Delete" button, it will be
        # get_input = options[leave()]
        get_input = options[selection]()

def search():
    title = "Searching for a fruit"
    msg = "What fruit do you want to seach for?"
    fruit_searched = easygui.enterbox(msg, title)




def display_fruits():

    for fruit_id, fruit_value in fruit.items():
        print("\nFruit name: " + fruit_id)
        
        for fruit_key in fruit_value:
            print(fruit_key + ":", fruit_value[fruit_key])
    # f = open("fruit").read()            
    # print(f)


def exit_fully():
    msg = "Are you sure you want to exit?"
    title = "Exiting?"
    exit = easygui.ynbox(msg,title)


    if exit:
        return "N"
   
    else:
        return options
   
options()







