# Given a string that may or may not contain a letter of interest. Print the index
# location of the first and last appearance of f. If the letter f occurs only once,
# then output its index. If the letter f does not occur, then do not print anything.
# Don't use loops in this task.

try:
    string = "this f contains  some and one  more is here "
    substring = "f"
    x = string.index(substring)
    y = string.rindex(substring)
    if x != 0 and y != 0:
        print(x, y)
    else:
        print('None')
except ValueError:
    print('None of letters f has been found')
