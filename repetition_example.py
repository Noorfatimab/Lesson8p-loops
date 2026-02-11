# repetition_example.py
# Lesson 8: Loops in Python

def main():
    print("Counting from 1 to 5 using a for loop:")
    for i in range(1, 6):
        print("This is repetition number", i)

    print("\nCounting from 5 down to 1 using a while loop:")
    count = 5
    while count > 0:
        print("Countdown:", count)
        count -= 1

main()
