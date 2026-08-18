import streamlit as st

# Create the board
def createBoard():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    num = 1

    for i in range(3):
        for j in range(3):
            board[i][j] = num
            num += 1

    return board


# Check winner
def checkWinner(board):

    # Rows
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]

    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]

    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]

    # Columns
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]

    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]

    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    # Diagonal
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


# Check whether board is full
def isBoardFull(board):

    for i in range(3):
        for j in range(3):

            if board[i][j] != "X" and board[i][j] != "O":
                return False

    return True


# Make a move
def makeMove(position):

    board = st.session_state.board
    player = st.session_state.player

    if position == 1:
        if board[0][0] == 1:
            board[0][0] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    elif position == 2:
        if board[0][1] == 2:
            board[0][1] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    elif position == 3:
        if board[0][2] == 3:
            board[0][2] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    elif position == 4:
        if board[1][0] == 4:
            board[1][0] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    elif position == 5:
        if board[1][1] == 5:
            board[1][1] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    elif position == 6:
        if board[1][2] == 6:
            board[1][2] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    elif position == 7:
        if board[2][0] == 7:
            board[2][0] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    elif position == 8:
        if board[2][1] == 8:
            board[2][1] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    elif position == 9:
        if board[2][2] == 9:
            board[2][2] = player
        else:
            st.session_state.message = "Position already occupied!"
            return

    # Clear previous message
    st.session_state.message = ""

    # Check winner
    winner = checkWinner(board)

    if winner is not None:
        st.session_state.winner = winner
        return

    # Check draw
    if isBoardFull(board):
        st.session_state.draw = True
        return

    # Change player
    if player == "X":
        st.session_state.player = "O"
    else:
        st.session_state.player = "X"


# Reset game
def resetGame():

    st.session_state.board = createBoard()
    st.session_state.player = "X"
    st.session_state.winner = None
    st.session_state.draw = False
    st.session_state.message = ""


# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = createBoard()

if "player" not in st.session_state:
    st.session_state.player = "X"

if "winner" not in st.session_state:
    st.session_state.winner = None

if "draw" not in st.session_state:
    st.session_state.draw = False

if "message" not in st.session_state:
    st.session_state.message = ""


# Page title
st.title("🎮 Tic Tac Toe")

st.write("### Two Player Game")


# Display winner / turn
if st.session_state.winner is not None:

    st.success(
        "🎉 Player " + st.session_state.winner + " Wins!"
    )

elif st.session_state.draw:

    st.warning("🤝 Game Draw!")

else:

    st.info(
        "Player " + st.session_state.player + "'s Turn"
    )


# Display message
if st.session_state.message != "":
    st.error(st.session_state.message)


# Board
for i in range(3):

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            str(st.session_state.board[i][0]),
            key="button_" + str(i) + "_0",
            use_container_width=True
        ):
            if st.session_state.winner is None and not st.session_state.draw:
                makeMove(st.session_state.board[i][0])
                st.rerun()

    with col2:
        if st.button(
            str(st.session_state.board[i][1]),
            key="button_" + str(i) + "_1",
            use_container_width=True
        ):
            if st.session_state.winner is None and not st.session_state.draw:
                makeMove(st.session_state.board[i][1])
                st.rerun()

    with col3:
        if st.button(
            str(st.session_state.board[i][2]),
            key="button_" + str(i) + "_2",
            use_container_width=True
        ):
            if st.session_state.winner is None and not st.session_state.draw:
                makeMove(st.session_state.board[i][2])
                st.rerun()


# Reset button
st.write("")

if st.button("🔄 Reset Game", use_container_width=True):
    resetGame()
    st.rerun()