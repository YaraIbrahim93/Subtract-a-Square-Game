# 1.this is a simple substract a square game 
# 2.import num , import time 
# 3.the first player is asked if he\she wanted to play first or not
# 3.for loop to choose a number from random number
# 4.chek if sqr for number is bigger than random number
#   4.a.true , print(" Enter correct number")  
#   4.b.false, complete in loop 
# to know the remider of random number we substract him from sqr of choosen number 
# if number equal 0 , end the game


player1 = input('please inter your name......')
print('Hello', player1)
player2 = input('please inter your name......')
print('Hello',player2)
print('Rules of this game:\n','1.A number is selected \n','2.you are asked if you want to play first\n','3.you enter a number\n','4.another player selected number\n','5.the process is repeated\n','6.the first who complete that last move wins \n ','------------------------------')


import time
from random import randrange
num = randrange(1 , 1000)
print(" number of coins is :" + str(num))

while (num>0):
    for i in range(1, (num + 1)):
        num1 = int(input("enter the first number:"))
        while True:
            start = time.time()
            T = input('you have only 5 seconds to enter\n')
            print('after',int(time.time()-start),'seconds Great job')
            if int(time.time()-start)>=5:
                print('you have been late please re enter')
            else:
                break    
        while (num1**2 > num ):
            num1 = int(input("Enter the correct number..."))
        num-=(num1**2)
        print (num)
        if num == 0:
            print('player1 is wins')
            break
        num2 = int(input("enter the seconed number:"))
        while True:
            start = time.time()
            T = input('you have only 5 seconds to enter\n')
            print('after',int(time.time()-start),'seconds Great job')
            if int(time.time()-start)>=5:
                print('you have been late please re enter')
            else:
                break     
        while (num2**2>num):
            num2 = int(input("Enter the correct number..."))
        num -= num2 ** 2
        print(num)
        if num ==0:
                print("the player 2 wins")
                break