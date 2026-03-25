import os
import re

ISSUE_TITLE = os.environ.get("ISSUE_TITLE", "")

if not ISSUE_TITLE.startswith("tictactoe|"):
    exit(0)

move = ISSUE_TITLE.split("|")[1].strip().upper()

board_file = ".tictactoe_state"

# create board if not exists
if not os.path.exists(board_file):
    with open(board_file, "w") as f:
        f.write("---------")

with open(board_file, "r") as f:
    board = list(f.read().strip())

positions = {
    "A1":0, "A2":1, "A3":2,
    "B1":3, "B2":4, "B3":5,
    "C1":6, "C2":7, "C3":8
}

if move not in positions:
    exit(0)

idx = positions[move]

if board[idx] == "-":
    board[idx] = "O"

with open(board_file, "w") as f:
    f.write("".join(board))

# update README
with open("README.md", "r") as f:
    content = f.read()

new_board = f"""
<!-- tictactoe starts -->
|   | 1 | 2 | 3 |
|---|---|---|---|
| A | {board[0]} | {board[1]} | {board[2]} |
| B | {board[3]} | {board[4]} | {board[5]} |
| C | {board[6]} | {board[7]} | {board[8]} |
<!-- tictactoe ends -->
"""

content = re.sub(
    r"<!-- tictactoe starts -->.*?<!-- tictactoe ends -->",
    new_board,
    content,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(content)
