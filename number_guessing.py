from ast import While
import random

top_range = input("Type a number:")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
r= random.randint(0, top_range)
times =0

while True:
    times += 1
    guess = int(input("Make a guess: "))
    if r == guess:
        print(f"Exact Number {r}")
        print("Amazing good job!")
        break
    else:
        print("Ngu!")
        if r > guess:
            print("Chọn số lớn hơn đi thằng ngu!")
        else:
            print("Chọn nhỏ lại chút")
        
print(times)
if times <=2:
    print(f"Đoán chỉ trong {times} lần, gắt đấy!")
else:
    print(f"Đoán tới {times} lần, ngu vl!")
        
