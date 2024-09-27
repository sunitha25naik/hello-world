import random
st_number=random.randint(0,9)
print(st_number)

guess_nu=0
cnt=0

while guess_nu!=st_number :
    guess_num=int(input('enter the number'))
           
    if(guess_nu>st_number) :
        print("enterd number is greater number")
        cnt=cnt+1
    elif guess_nu<st_number:
        print("enterd number is lesser number")
        cnt=cnt+1
    else:
            print("U guessed right number")
print('number of test',cnt)
'''
class InvalidPercentageError():
    def __init__(self):
        super().__init__("enterd number is greater number")

class LessPercentageError():
    def __init__(self):
        super().__init__(")
'''
