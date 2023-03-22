hat_list = [1, 2, 3, 4, 5]
number = int(input("Введіть число, щоб замінити його в списку:"))
hat_list[int(len(hat_list) // 2)] = number
print(hat_list)

del hat_list[len(hat_list) - 1]
print(hat_list)

print(len(hat_list))


my_list = [1, 7, 23, 34, 0]
n = len(my_list)

for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(my_list)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(my_list)
print("The list with unique elements only:", new_list)


chess_board = [["_" for i in range(8)] for j in range(8)]
chess_board[0][0] = "R"
chess_board[0][7] = "R"
chess_board[7][0] = "R"
chess_board[7][7] = "R"
for row in chess_board:
    chess = " ".join(row)
    print(chess)



