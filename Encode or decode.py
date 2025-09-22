
import random
key = 1122
#encoding
def encoding():
    '''This function will encode the word which will added '''
    a = [1,2,3,4,5,6,7,8,9,0,0,0,0,0,"#","!","@","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random_num = random.sample(a,4)
    random_num2 = random.sample(a,4)
    word = input("Enter for Encode: ")
    c = word[::-1]
    b = list(c)
    b.extend(random_num)
    new = random_num2 + b
    # print(new)
    again = "".join(map(str,new))
    again = again.upper()
    print(again)
    return again
# decoding
def decoding():
    '''This function will decode the word which will added '''
    code = input("Enter for Decode : ")
    print(code)
    confirmation = input("Are you sure you want to Decode then enter pass : ")
    
    if (confirmation == "@@@@@"):
        code = code.lower()
        code_list = list(code)
        code_list = code_list[4:-4]
        rev = code_list[::-1]
        in_str = "".join(map(str,rev))
        print(in_str)
    else:
        print("Sorry not allowed")
    return in_str
def full():
    try:
        password = int(input("Enter Code: "))
        if (password == key):
                task = input("Enter what you want to do :\n A: Encoding     B:Decoding \n              ")
                if(task == "A" or task == "a"):
                            encoding()
                elif(task == "B" or task == "b"):
                            decoding()
        else:
            print("Wrong Password")
            full()
    except:
        print("Don't add string")
        full()
full()
                