numbers = []

def numberadder(loops, stepsize):
    i = 0
    while i < loops:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += stepsize
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers





loops_input = int(input("How many loops to go?"))
stepsize_input = int(input("Which stepsize?"))

print("Starting loop...")
numberadder(loops_input, stepsize_input)


print("The numbers: ")

for num in numbers:
        print(num)
