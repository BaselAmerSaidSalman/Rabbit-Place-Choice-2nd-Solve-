print("Welcome to place the rabbit")
field = [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
print(f"{field[0]}\n{field[1]}\n{field[2]}")
place = input("Where should the rabbit go? 🐇\nPlease choose a row and a column: ")
row = int(place[0])
column = int(place[1])
field[row-1][column-1] = "🐇"
while int(place) > 33 or int(place) < 11:
  print("Please enter a number between 11 and 33")
  place = input("Where should the rabbit go? 🐇\nPlease choose a row and a column: ")
print("""Success...\n"""
,field[0],"""\n""",field[1],"""\n""",field[2],
)

