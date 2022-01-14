PLACE_HOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripe_name = name.strip()
        new_letter = letter_contents.replace(PLACE_HOLDER, stripe_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripe_name}.txt","w") as file:
            file.write(new_letter)

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp