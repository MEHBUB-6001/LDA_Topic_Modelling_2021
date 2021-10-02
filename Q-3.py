def ReverseSting(original_string):
    index = -1 
    for i in range(len(original_string)-1, int(len(original_string)/2), -1):      
        if original_string[i].isalpha():
            temp = original_string[i]
            while True:
                index += 1
                if original_string[index].isalpha():
                    original_string[i] = original_string[index]
                    original_string[index] = temp
                    break
    return original_string
string ="ab$24%736(849ldj"
print ("Given Input string Is : ", string)
string = ReverseSting(list(string))
print ("Accepted Output string Is: ", "".join(string))
