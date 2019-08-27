disdict = {} #symptoms to disease dictionary
meddict = {} #diseases to medicine dictionary
name = input("Enter your name: ")
name = name.capitalize()
age  = input("Please, enter your age: ")
print ("How can I help you?") #Welcome message
symptoms = input(name + ", please enter your symptoms: ")
disease = disdict[symptoms]
print(meddict[disease])


