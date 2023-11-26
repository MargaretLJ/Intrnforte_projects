
import random
import string


temp_passlist=[]
final_pass =""


def user_password(length,upper=False,lower=False,digit=False,char=False):
    character_set= ""

    if upper:
        character_set+=(string.ascii_uppercase) #generates uppercase characters
    if lower:
        character_set+=(string.ascii_lowercase) #generates lowercase characters
    if digit:
        character_set+=(string.digits) #generates numbers
    if char:
        character_set+=(string.punctuation) #generates special characters

    if not any([upper, lower, digit, char]):
        raise ValueError("Please select at least one character type.")

    #ensuring that atleast one character of each type is included if it is selected:
    temp_pass=""
    if upper:
        temp_pass+=random.choice(string.ascii_uppercase)
    if lower:
        temp_pass += random.choice(string.ascii_lowercase)
    if digit:
        temp_pass += random.choice(string.digits)
    if char:
        temp_pass += random.choice(string.punctuation)



    temp_pass +=''.join(random.choice(character_set) for i in range(length-len(temp_pass))) #selects the desired length of the password from the given character set
    temp_passlist =list(temp_pass) #creates a list of the generated password
    random.shuffle(temp_passlist) #shuffles the list
    final_pass=''.join(temp_passlist) #converts it into a string
    return final_pass


#handles exceptions when the password is not of desired length and when the user enters wrong information
try:
    l = int(input("enter the desired length of your  password"))
    if l<=0:
        raise ValueError("Please enter a positive integer")




    u = input("Do you want uppercase characters to be present :(True or False)")
    if u not in ['True','False']:
        raise TypeError
    v =input("Do you want lowercase characters to be present : (True or False)")
    if v not in ['True', 'False']:
        raise TypeError
    w = input("Do you want digits to be present : (True or False)")
    if w not in ['True', 'False']:
        raise TypeError
    x = input("Do you want special characters to be present : (True or False)")
    if x not in ['True', 'False']:
        raise TypeError



    p = user_password(l, u=='True', v=='True', w=='True', x=='True')
    print("Generated Password:",p)

except ValueError as e:
    print(f"Error: {e}")
except TypeError:
    print("Error: Please enter 'True' or 'False'")



