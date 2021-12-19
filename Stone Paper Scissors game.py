from random import *
game_list=["rock","paper","sicssor"]
win_chance=[
 [0,2],
 [1,0],
 [2,1]
]

print("'1: rock' \n'2: paper' \n'3: sicssor' ")
a= int(input("pick up a number: "))
b= randint(1,3)
choices_list=[a-1,b-1]
x=0
for chance in win_chance:
    if chance == choices_list:
        x= 1
print(f"you chice {game_list[a-1]}")
print(f"computer chice {game_list[b-1]}")
if x ==1 :
    print("you win")
elif a==b:
    print ("Draw")
else:
    print("you lost")
