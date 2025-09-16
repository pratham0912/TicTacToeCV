import cv2 as cv


# Check if a player has won
def check_winner(board):
    # Rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

# Check for tie
def check_tie(board):
    for row in board:
        if "" in row:
            return False
    return True


board = [["","",""],["","",""],["","",""]]
player = "O"
game_over = False

def mouse_click(event, x, y, flags, param):
    global board, player, w1, w2, h1, h2,game_over

    if game_over == True:
        return
    if event != cv.EVENT_LBUTTONDOWN:
        return

    # column check
    if x < w1:
        col = 0
    elif x < w2:
        col = 1
    else:
        col = 2

    # row check
    if y < h1:
        row = 0
    elif y < h2:
        row = 1
    else:
        row = 2
    # print(f"Clicked cell: row={row}, col={col}")

    if board[row][col] == "":
        board[row][col] = player
        print(f"Player {player} clicked cell: row={row}, col={col}")

#         switch player
        player = "X" if player == "O" else "O"


cap = cv.VideoCapture(0)
cv.namedWindow('Tic Tac Toe')
cv.setMouseCallback('Tic Tac Toe', mouse_click)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    h1, h2 = h//3, 2*h//3
    w1, w2 = w//3, 2*w//3

    # Vertical lines
    cv.line(frame, (w1, 0), (w1, h), (0, 0, 0), 3)
    cv.line(frame, (w2, 0), (w2, h), (0, 0, 0), 3)

    # Horizontal lines
    cv.line(frame, (0, h1), (w, h1), (0, 0, 0), 3)
    cv.line(frame, (0, h2), (w, h2), (0, 0, 0), 3)

    #drawing circle and cross
    for row in range(3):
        for col in range(3):
            center_x = col * w1 + w1//2
            center_y = row * h1 + h1//2
            radius = min(w1,h1)//3
            if board[row][col] == "O":
                cv.circle(frame ,(center_x, center_y), radius, (0, 0, 255), 1)

            elif board[row][col] == "X":
                size = radius
                cv.line(frame,(center_x-size, center_y-size), (center_x + size, center_y+size), (0, 0, 255), 1)
                cv.line(frame,(center_x-size, center_y+size), (center_x+size, center_y-size), (0, 0, 255), 1)


    winner = check_winner(board)
    if winner :
        cv.putText(frame,f"{winner} wins!",(50,50), cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv.LINE_AA)
        game_over = True

    elif check_tie(board):
        cv.putText(frame, "Its a Tie!",(50,50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1,cv.LINE_AA)
        game_over = True
    cv.imshow('Tic Tac Toe', frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        board = [["","",""],["","",""],["","",""]]
        player = "O"
#         player = "X" if "O" else "O"
        game_over = False

cap.release()
cv.destroyAllWindows()
