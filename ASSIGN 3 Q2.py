#Write a Python program to reverse a string.?



def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)
 
s = "1234abcd"
 
print("The original string  is : ", s)
 
print("The reversed string(using reversed) is : ", reverse(s))