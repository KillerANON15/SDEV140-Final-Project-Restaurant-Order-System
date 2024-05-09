import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

prices = {
    "Fried Calamari" : 10,
    "Beach Burger" : 14,
    "Salmon Wonder" : 23,
    "Shrimp Tacos" : 15,
    "Sushi Platter" : 25,
    "Empanadas" : 10,
}

root  = Tk()

root.title("Zach White - Auspicious Bits")


# ------------------------------------FUNCTIONS--------------------------------------------- #

#region Generating a random Order ID when starting a new order
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "BIN_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id
#endregion

#region Add to Order Button
def add():
    # updating the transaction label
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    # updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")
#endregion

#region Remove Button Function
def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if dish_to_remove in transaction_list:
        # update transaction label
        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        # update transaction total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#endregion

#region Display Button Functions
def displayCalamari():
    calamariDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style = "DishFrame.TFrame")
    empanadasDishFrame.configure(style= "DishFrame.TFrame")
    sushiDishFrame.configure(style = "DishFrame.TFrame")
    shrimpDishFrame.configure(style = "DishFrame.TFrame")
    burgerDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        image = calamariImage,
        text = "Fried Calamari",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
    )

def displayBurger():
    burgerDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Beach Burger",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = burgerImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displaySalmon():
    salmonDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    calamariDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Salmon Wonder",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = salmonImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayTacos():
    shrimpDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Shrimp Tacos",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = shrimpImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayEmpanadas():
    empanadasDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Empanadas",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = empanadasImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displaySushi():
    sushiDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image = sushiImage,
        text = "Sushi Platter",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )
#endregion

#region Generating Receipt from Order Button
def order():
    order_id = orderIDLabel.cget("text").replace("ORDER ID : ", "").strip()  # Ensures any extra whitespace is removed
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list = [item.strip() for item in transaction_list if item]  # Ensures no empty strings are processed

    order_day = date.today()
    order_time = datetime.now()

    receipt_filename = f"{order_id}.txt"  # Makes sure the file name is derived from order_id
    with open(receipt_filename, 'w') as file:
        file.write("Auspicious Bits\n")
        file.write("________________________________________________________\n")
        file.write(order_day.strftime("%x") + "\n")
        file.write(order_time.strftime("%X") + "\n\n")
        for item in transaction_list:
            file.write(item + " $\n")  # Ensure formatting is consistent for readability
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text") + "\n")

    # Reset the order details
    orderTotalLabel.configure(text="TOTAL : 0$")
    orderIDLabel.configure(text="ORDER ID : " + ORDER_ID())  # Updates the label with a new ORDER ID
    orderTransaction.configure(text="")

# Ensure ORDER_ID function is called only when resetting
def reset_order_id():
    new_id = ORDER_ID()
    orderIDLabel.configure(text="ORDER ID : " + new_id)
    return new_id
#endregion


# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")  # Configures the background color for the main frame
s.configure('MenuFrame.TFrame', background = "#4A4A48")  # Configures the background color for the menu frame
s.configure('DisplayFrame.TFrame', background = "#0F1110")  # Configures the background color for the display frame
s.configure('OrderFrame.TFrame', background = "#B7C4CF")  # Configures the background color for the order frame
s.configure('DishFrame.TFrame', background = "#4A4A48", relief = "raised")  # Configures the background color and relief style for dish frames
s.configure('SelectedDish.TFrame', background = "#C4DFAA")  # Configures the background color for selected dish frames
s.configure('MenuLabel.TLabel',
            background = "#0F1110",  # Configures the background color for menu labels
            font = ("Arial", 13, "italic"),  # Configures the font for menu labels
            foreground = "white",  # Configures the foreground color for menu labels
            padding = (5, 5, 5, 5),  # Configures the padding for menu labels
            width = 21  # Configures the width for menu labels
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",  # Configures the background color for the order total label
            font = ("Arial", 10, "bold"),  # Configures the font for the order total label
            foreground = "white",  # Configures the foreground color for the order total label
            padding = (2, 2, 2, 2),  # Configures the padding for the order total label
            anchor = "w"  # Configures the anchor for the order total label
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",  # Configures the background color for the order transaction label
            font = ('Helvetica', 12),  # Configures the font for the order transaction label
            foreground = "white",  # Configures the foreground color for the order transaction label
            wraplength = 170,  # Configures the wrap length for the order transaction label
            anchor = "nw",  # Configures the anchor for the order transaction label
            padding = (3, 3, 3, 3)  # Configures the padding for the order transaction label
            )
#endregion


# region Images
# Top Banner images
LogoImageObject = Image.open("ZachWhiteSDEV140_Project\Images\Bits Logo.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("ZachWhiteSDEV140_Project\Images/restaurant top banner.jpg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Menu images
displayDefaultImageObject = Image.open("ZachWhiteSDEV140_Project\Images/display - Default.png").resize((350,360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

calamariImageObject = Image.open("ZachWhiteSDEV140_Project\Images/menu/fried calamari.png").resize((350,334))
calamariImage = ImageTk.PhotoImage(calamariImageObject)

burgerImageObject = Image.open("ZachWhiteSDEV140_Project\Images/menu/beach burger.png").resize((350,334))
burgerImage = ImageTk.PhotoImage(burgerImageObject)

salmonImageObject = Image.open("ZachWhiteSDEV140_Project\Images/menu/salmon wild rice.png").resize((350,334))
salmonImage = ImageTk.PhotoImage(salmonImageObject)

shrimpImageObject = Image.open("ZachWhiteSDEV140_Project\Images/menu/shrimp tacos.png").resize((350,334))
shrimpImage = ImageTk.PhotoImage(shrimpImageObject)

sushiImageObject = Image.open("ZachWhiteSDEV140_Project\Images/menu/sushi platter.png").resize((350,334))
sushiImage = ImageTk.PhotoImage(sushiImageObject)

empanadasImageObject = Image.open("ZachWhiteSDEV140_Project\Images/menu/empanadas.png").resize((350,334))
empanadasImage = ImageTk.PhotoImage(empanadasImageObject)


#endregion

#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

# Dish Frames
calamariDishFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
calamariDishFrame.grid(row = 1, column = 0, sticky = "NSEW")

burgerDishFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
burgerDishFrame.grid(row = 2, column = 0, sticky ="NSEW")

salmonDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
salmonDishFrame.grid(row = 3, column = 0, sticky ="NSEW")

shrimpDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
shrimpDishFrame.grid(row = 4, column = 0, sticky ="NSEW")

sushiDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
sushiDishFrame.grid(row = 5, column = 0, sticky ="NSEW")

empanadasDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
empanadasDishFrame.grid(row = 6, column = 0, sticky ="NSEW")

#endregion

# region Top Banner Section

LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

# endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

CalamariDishLabel = ttk.Label(calamariDishFrame, text ="Fried Calamari ..... 10$", style ="MenuLabel.TLabel")
CalamariDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

BurgerDishLabel = ttk.Label(burgerDishFrame, text ="Beach Burger ..... 14$", style ="MenuLabel.TLabel")
BurgerDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SalmonDishLabel = ttk.Label(salmonDishFrame, text ="Salmon Wonder ..... 23$", style ="MenuLabel.TLabel")
SalmonDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

ShrimpDishLabel = ttk.Label(shrimpDishFrame, text ="Shrimp Tacos ..... 15$", style ="MenuLabel.TLabel")
ShrimpDishLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

SushiDishLabel = ttk.Label(sushiDishFrame, text ="Sushi Platter ..... 25$", style ="MenuLabel.TLabel")
SushiDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

EmpanadasDishLabel = ttk.Label(empanadasDishFrame, text ="Empanadas .... 10$", style ="MenuLabel.TLabel")
EmpanadasDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Buttons
CalamariDisplayButton = ttk.Button(calamariDishFrame, text ="Display", command = displayCalamari)
CalamariDisplayButton.grid(row = 0, column = 1, padx = 10)

BurgerDisplayButton = ttk.Button(burgerDishFrame, text ="Display", command = displayBurger)
BurgerDisplayButton.grid(row = 0, column = 1, padx = 10)

SalmonDisplayButton = ttk.Button(salmonDishFrame, text ="Display", command = displaySalmon)
SalmonDisplayButton.grid(row = 0, column = 1, padx = 10)

ShrimpDisplayButton = ttk.Button(shrimpDishFrame, text ="Display", command = displayTacos)
ShrimpDisplayButton.grid(row = 0, column = 1, padx = 10)

SushiDisplayButton = ttk.Button(sushiDishFrame, text ="Display", command = displaySushi)
SushiDisplayButton.grid(row = 0, column = 1, padx = 10)

EmpanadasDisplayButton = ttk.Button(empanadasDishFrame, text ="Display", command = displayEmpanadas)
EmpanadasDisplayButton.grid(row = 0, column = 1, padx = 10)

# endregion

#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")


# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

#endregion



#----------------------------- GRID CONFIGURATIONS -------------------------------------------#
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)


if __name__ == "__main__":
    reset_order_id()  # Ensure a new Order ID is ready at startup
    root.mainloop()


