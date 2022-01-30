'''
What is a Break statement

- used to break out of of a loop statemet.(stop the loop)
- it will break the loop even if condition is still true.
'''
print("1 to 10 break on 5")
print(" ")
i = 1

while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

'''
Continue Statement

what is a continue statement

used to stop the current iteration and continue with the 
next iteration of the loop.

'''
print(" ")
print("1 to 10 skip 4 and continue")
print(" ")
i = 0

while i < 10:
    i += 1
    if i == 4:
        continue
    print(i)
