# Print Twinkle Twinkle Little Star
print(''' Twinkle, twinkle, little star
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')

# installing numpy module and importing it
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
result = np.add(arr1, arr2)
print("The sum of the two arrays is:", result)

# installing pyttsx3 module and importing it to convert text to speech
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()

# printing the content of dictionary using os module
import os
path = '/'
print("This is the content of current directory: ", os.listdir(path))
