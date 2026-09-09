space = [["#", "#", "#"],["#", "#", "#"], ["#", "#", "#"]]
print (f"{space[0]} \n{space[1]} \n{space[2]} ")
number = input ("Enter a number of line and column: ")
line = int(number[0])
column = int(number[1])
space[line-1][column-1] = "X"
print(f"{space[0]}\n{space[1]}\n{space[2]}")
