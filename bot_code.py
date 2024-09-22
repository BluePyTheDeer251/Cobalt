import tensorflow as tf
import numpy as np
import scipy as sci

print("Welcome! NOTICE: Some dependencies have been placed in the code, but they are currently useless.")

# Where the magic happens
number = input("What is you favorite number? ")

totalNum = print(f"Oh, {number} is an amazing number!")

name = input("Oh, I almost forgot. What's your name? ")

totalName = print(f"{name} is a beautiful name!")

os = input("And lastly, what is your Operating System of choice? (Windows, macOS or Linux, written like it is here.) ")

if os == "Windows":
    print("It's a nice OS, but kinda bloated, and sadly, Microsoft just keeps making it worse.")

if os == "macOS":
    print("It's nice, but, why pay so much? But oh well, opinions are opinions.")

if os == "Linux":
    print("Very nice, but depending on the distro, it can have its ups and downs.")

genres = input("Ok, so, what genres of games do you enjoy? ")

totalGenres = print(f"Oh, {genres} is/are very nice genre(s)!")


print("That's all I can do, for now, if I ever actually get improved, which is somewhat unlikely considering a lot of things, but maybe, against all odds, this could get improved!")
