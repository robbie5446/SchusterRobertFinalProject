'''Pizza App
Author: Robert Schuster
Date:3/9/24
This code includes radio buttons, check buttons, drop downs, and a submit button
to compile a pizza for a potential customer
'''
#imports
from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox


#root window
root = Tk()

#title
root.title('Pizza Ordering App')

#size
root.geometry('640x480+300+300')
root.resizable(False, False)

# cheese label alternate text
cheesePizzaLabel = Label(root, text='Cheese Pizza')
cheesePizzaLabel.grid(row=0, column=0)#geometry

#pepperoni label alternate text
pepperoniPizzaLabel = Label(root, text='Pepperoni Pizza')
pepperoniPizzaLabel.grid(row=0, column=1)#geometry

#image 1 cheese pizza
image = (Image.open("cheesepizza.jpg"))
imageResize = image.resize((100, 100)) #resizing image
cheesePizzaImage = ImageTk.PhotoImage(imageResize)
cheeseImageLabel = Label(root, image=cheesePizzaImage)#creating label
cheeseImageLabel.grid(row=1, column=0)#geometry

#image 2 pepperoni pizza
imageTwo = (Image.open("pepperonipizza.jpg"))
imageTwoResize = imageTwo.resize((100, 100)) #resizing image
pepperoniPizzaImage = ImageTk.PhotoImage(imageTwoResize)
pepperoniImageLabel = Label(root, image=pepperoniPizzaImage)#creaing label
pepperoniImageLabel.grid(row=1, column=1)#geometry


#radio button
crustLabel = Label(root, text = 'What kind of crust would you like?')
crustLabel.grid(row=2, column=1)#geometry
crustVar = BooleanVar()#declaring variable type
crustStuffed = Radiobutton(root, text="Stuffed", value=True, variable = crustVar)#radio button
crustThin = Radiobutton(root, text="Thin", value=False, variable = crustVar)#radio button
crustStuffed.grid(row=3, column=1)#geometry
crustThin.grid(row=4, column=1)#geometry


#cheese dropdown
cheeseVar = StringVar(value = "Light") #declaring variable type
cheeseLabel = Label(root, text = "How much cheese would you like?") #creating label
cheeseLabel.grid(row=5, column=1) #geometry
cheeseOptions = ('Light Cheese', 'Extra Cheese') #defining options for the dropdown
cheeseMenu = OptionMenu(root, cheeseVar, *cheeseOptions)#creating dropdown
cheeseMenu.grid(row=6, column=1)#geometry


#ingredients checkbox
ingredientLabel = Label(root, text='Check what ingredients you would like')#creating label
ingredientLabel.grid(row=7, column=1)#geometry
mushroomVar = BooleanVar()#declaring variable type
mushroom = Checkbutton(root, text="Mushroom", variable = mushroomVar)#creating checkbutton
mushroom.grid(row=8, column=1)#geometry
pepperoniVar = BooleanVar()#declaring variable type
pepperoni = Checkbutton(root, text="Pepperoni", variable = pepperoniVar)#creating checkbutton
pepperoni.grid(row=9, column=1)#geometry
pineappleVar = BooleanVar()#declaring variable type
pineapple = Checkbutton(root, text="Pineapple", variable = pineappleVar)#creating checkbutton
pineapple.grid(row=10, column=1)#geometry


#submit function
def onSubmit(): #creating onSubmit function
    answer = messagebox.askyesno("Hello", "Are you done with your order?") #creating another window
    if answer == 1: #if statement if user clicks yes
        resultLabel = Label(root, text="Your pizza consists of: ")#creating output label
        resultLabel.grid(row=5, column=7)#geometry


        #Outputting crust selection for radio button
        crustSelect = crustVar.get()#creating variable to get the input 
        if crustSelect: #condition if true
            outputStuffed = Label(root, text="Stuffed Crust")#output label
            outputStuffed.grid(row=6, column=7)#geometry
        else: #condition if false
            outputThin = Label(root, text="Thin Crust")# output label
            outputThin.grid(row=6, column=7)#geometry


        #outputting cheese selection for dropdown
        outputCheese = Label(root, text=cheeseVar.get()) #output label that gets the input
        outputCheese.grid(row=7, column=7)#geometry


        #Outputting checkbox selections
        mushroomSelect = mushroomVar.get()#output variable that gets the input
        pepperoniSelect = pepperoniVar.get()#output variable that gets the input
        pineappleSelect = pineappleVar.get()#output variable that gets the input
        if mushroomSelect: #condition if checkbox is checked
            outputMushroom = Label(root, text="Mushrooms")#creating label
            outputMushroom.grid(row=8, column=7)#geometry
        
        if pepperoniSelect:#condition if checkbox is checked
            outputPepperoni = Label(root, text="Pepperoni")#creating label
            outputPepperoni.grid(row=9, column=7)#geometry
        
        if pineappleSelect:#condition if checkbox is checked
            outputPineapple = Label(root, text="Pineapple")#creating label
            outputPineapple.grid(row=10, column=7)#geometry
        
        confirmLabel = Label(root, text="And, it's on its way!")#creating label
        confirmLabel.grid(row=11, column=7)#geometry


    else: #if user clicks no they aren't done, returns to app
        return


#submit button
submit = Button(root, text='Submit', command=onSubmit)#button that executes function for all widgets
submit.grid(row=11, column=1) #geometry      


#finish
root.mainloop()
