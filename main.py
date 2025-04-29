from tkinter import *
import random

root = Tk()
root.title("Hangman")
root.geometry("800x600")
root.config(bg="teal")

'''MODEL'''
# FUNCTIONS


# GLOBAL VARIABLES
# creates a list of seven images
images = []
for i in range(1,8):
    images.append(PhotoImage(file=f"images/{i}.png"))

# creates a list of 58110 words
words = open("wordbank.txt","r") #opens text file for reading
wordbank = words.read() #stores contents of txt file in variable
wordbank = wordbank.split() #place words into a list.







'''CONTROLLER'''


'''VIEW'''




root.mainloop()
