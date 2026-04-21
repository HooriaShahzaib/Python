# Practice 3: string functions

# len function
st = input("Enter a string:")
print("The length of the string is: ", len(st))

# capitalizw the string
print("Capitalizing your string: ", st.capitalize())

# lower casing the string
print("Your string in lower case is: ", st.lower())

# upper casing the string
print("Your string in upper case is: ", st.upper())

# counting a letter in your string
ch = input("Enter the character you want to count in your string: ")
print("The number of times the character appears in your string is: ", st.count(ch))

# title case the string
print("Your string in title case is: ", st.title())

# replacing a word with another word in the string
r1 = input("Enter the word that you want to replace: ")
r2 = input("Enter the word that you want to replace with: ")
print("Now your string is: ", st.replace(r1,r2).replace("my","his"))

# greeting the user
name = input("Enter your name: ")
print("Good Afternoon, " + name + "!")   #This is one way
print(f"Good Morning, {name}!")   #using this f string you can easily write everything in one line without using + operator.

# finding the index of a character in the string
s = "hi  there"
print("This is the current string: ", s)
print("The index for the double spacing is:", s.find("  "))
print("Replacing that double spaceing with single space: ", s.replace("  ", " "))

# or we can do
s2 = "Yoo   baby"
print(f"right now the string is: {s2}, \n the index for the triple spacing is: {s2.find("   ")},\n after replacing that with single space your sting now is: {s2.replace("   ", " ")}") 
print(f"But the original string is still the same: {s2} bcz we didn't change the original string, we just printed the changed string. If you want to change the original string then you have to assign the changed string to the original string like this: s2 = s2.replace("   ", " ")")


print("This is the original letter: Hi there! Its soo nice to see you. bye!")
print("Use of escape letters.")
print("Hi there!\n\t Its soo nice to see you.\nbye!")