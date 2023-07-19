# Time:
# O(m*n)
# Space:
# O(m+n)

#the arguments are the image itself, the selected x, y, the amount of row, col, the previous color, and new color.
#we need the rows, columns, and previous color as base cases
def floodfill(screen, source_row, source_col, row, col, prev_num, new_num):
  #checking edges
  if source_row < 0 or source_row >= row or source_col < 0 or source_col >= col:
    return
  #checking if the selected index is the same as prev color. if it isnt that means we stop
  if screen[source_row][source_col] != prev_num:
    return
  #change the color of the selected x and y from what it was to the new color
  screen[source_row][source_col] = new_num
  #recursively go through each index from the selected x and y.
  floodfill(screen, source_row + 1, source_col, row, col, prev_num, new_num)
  floodfill(screen, source_row - 1, source_col, row, col, prev_num, new_num)
  floodfill(screen, source_row, source_col + 1, row, col, prev_num, new_num)
  floodfill(screen, source_row, source_col - 1, row, col, prev_num, new_num)






screen = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 0, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

r = 9 #rows
c = 9 #columns


#selected coordinates
x = 1
y = 2

#variable to indicate what the last color was
prev_num = screen[x][y]

#arbitrary color/new number
new_num = 5

#method call
floodfill(screen, x, y, r, c, prev_num, new_num)

#print results
for i in range(r):
  print(screen[i])

# output = [
#   [1, 1, 1, 1, 1, 1, 1, 1, 1]
#   [1, 1, 5, 5, 5, 5, 5, 5, 1]
#   [1, 1, 5, 5, 5, 5, 5, 5, 1]
#   [1, 1, 5, 5, 1, 1, 5, 5, 1]
#   [1, 1, 5, 5, 1, 1, 5, 5, 1]
#   [1, 1, 5, 5, 1, 1, 5, 5, 1]
#   [1, 1, 5, 5, 5, 5, 5, 5, 1]
#   [1, 1, 5, 5, 5, 5, 5, 5, 1]
#   [1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]








#trying to recall from memory
# image = [
#   [1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 1, 0, 0, 0, 0, 0, 0, 1],
#   [1, 1, 0, 0, 0, 0, 0, 0, 1],
#   [1, 1, 0, 0, 1, 1, 0, 0, 1],
#   [1, 1, 0, 0, 1, 1, 0, 0, 1],
#   [1, 1, 0, 0, 1, 1, 0, 0, 1],
#   [1, 1, 0, 0, 0, 0, 0, 0, 1],
#   [1, 1, 0, 0, 0, 0, 0, 0, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# rows = 9
# columns = 9

# x_co = 4
# y_co = 4

# new_color = 3
# old = screen[x_co][y_co]

# def fillflood(screen, rows, columns, x, y, old_color, new_color):
#   if x < 0 or x >= rows or y < 0 or y >= columns:
#     return
#   if screen[x][y] != old_color:
#     return
#   screen[x][y] = new_color
#   fillflood(screen, rows, columns, x - 1, y, old_color, new_color)
#   fillflood(screen, rows, columns, x + 1, y, old_color, new_color)
#   fillflood(screen, rows, columns, x, y - 1, old_color, new_color)
#   fillflood(screen, rows, columns, x, y + 1, old_color, new_color)


# fillflood(image, rows, columns, x_co, y_co, old, new_color)

# for i in range(rows):
#   print(image[i])