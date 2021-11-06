print("    █  █▀ ▄█ ▄█▄    █  █▀    ▄▄▄▄▀  ▄  █ ▄███▄   █▀▄▀█  ████▄   ▄      ▄▄▄▄▀█▄█   ██ █▀ ▀▄  █▄█   ▀▀▀ █    █   █ █▀   ▀  █ █ █  █   █    █  ▀▀▀ ██▀▄   ██ █   ▀  █▀▄       █    ██▀▀█ ██▄▄    █ ▄ █  █   █ █   █     ██  █  ▐█ █▄  ▄▀ █  █     █     █   █ █▄   ▄▀ █   █  ▀████ █   █    █ █    ▐ ▀███▀    █     ▀         █  ▀███▀      █         █▄ ▄█   ▀ ▀               ▀               ▀             ▀           ▀▀▀")


import sys
#import socket


def main():
   menu()


#################################


def menu():
    print()

    print("devlop by : @kk.6c")
    print()
    print("************ Welcome **************")
    print()

    choice = input("""
      1: Pizza system 
      2: Average calc
      3: Area calc
      4: Numbers above 70
      Q: Logout

   Please enter your choice: """)

    if choice == "1" or choice =="١":
        pizza()
    elif choice == "2" or choice =="٢":
        login()
    elif choice == "3" or choice =="٣":
        area()
    elif choice == "4" or choice =="٤":
        above()
    elif choice=="q" or choice=="Q":
        print("Thx for using my script ")
        sys.exit

    else:
        print("You must only select Numbers")
        print("Please try again")
        menu()


#########################################


def pizza():
    print("")
    print("************ pizza system **************")

    print("")


   
    pittza = input("How many pittza you want  : ")
    taxn   = input("Enter Tax Rate            : ")

    pittza = int(pittza)
    taxn=float(taxn)


    ff = taxn / 100
    pizpris = 25
    befortax = pizpris * pittza
    tax = befortax * ff
    aftertax = tax + befortax

    print("")

    print("**************************************")
    print("")



    print("Pizza number    : " ,pittza)
    print("Price for each  : " , pizpris)
    print("Price befor tax : "  , befortax)
    print("Tax             : ",tax)
    print("Price After Tax : ",aftertax)
    print("")


#################################################



def login():

    print("")
    print("*************** Average calc ***************")
    print("")



    number2 = input("How many Number do you want to calc : ")
    number2 = int(number2)
    print("")



   #func to cal
    def cal (l,w):
     area = l * w
     return area

    box1_l = 20
    box2_l = 25
    box_w = 30

    box1_area = cal(box1_l, box_w)
    box2_area = cal(box2_l,box_w)
   


    # a function that Calcutta tha scueer of number
    def square_number(number):
     return number**2


    # display from 1 to 10 and their squares
    for i in range (1,11):
     i_square = square_number(i)
    #print(i,"square is ", i_square)


    total  = 0

    for I in range(number2):
     student_mark = input("Enter Number : ")
     student_mark   = int(student_mark)


    total = total + student_mark
    avg_mark = total / number2
    print("Average Mark :  ",avg_mark)

########################################################

def above():
    print("")
    print("************ above  **************")
    print("")
    print("Max 5 Number ")
    print("")

    con = 0

    for i in range (5):
        num=input("Enter Numbers :  ")
        num=float(num)

        if(num >= 70):
           con = con + 1

    print("the number of student  with marks greater than 70 is " ,con)


 ########################################################

def area():

    print("")
    print("*************** Area calc ***************")
    print("")

    heiht = input("Enter the height : ")

    width   = input("Enter the width : ")


    heiht = float(heiht)
    width   = float(width)



    print("")
    print()


    area = heiht*heiht/2
    area2 = heiht*width
    total = area + area2

    print("Area shape   : ",area)
    print("Second area  : ",area2)
    print("Total        : ",total)
        


main()
