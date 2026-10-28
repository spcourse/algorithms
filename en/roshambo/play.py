"""
Play your roshambot.py against one of the five opponents.

Put this file in the same folder as roshambot.py and run, for example:

    python play.py lance

Opponents: dwayne, lance, bicyclist, winner, winnerwinner
"""

import sys

MOVES = ("rock", "paper", "scissors")
BEATS = {"rock": "paper", "paper": "scissors", "scissors": "rock"}  # BEATS[x] beats x
OPPONENTS = {
    "dwayne": "Dwayne",
    "lance": "Lance",
    "bicyclist": "The Bicyclist",
    "winner": "The Winner",
    "winnerwinner": "The Winner Winner",
}


class StopGame(Exception):
    pass


def round_winner(a, b):
    """the move that won the round; after a tie, the move both played"""
    if a == b or BEATS[b] == a:
        return a
    return b


def score(history):
    mine = sum(1 for t, m in history if t != m and round_winner(t, m) == m)
    theirs = sum(1 for t, m in history if t != m and round_winner(t, m) == t)
    return mine, theirs


def opponent_move(opponent, history):
    """history: (theirs, mine) for each round played so far"""
    n = len(history)
    if opponent == "dwayne":
        return "rock"
    if opponent == "lance":
        return MOVES[n % 3]
    if opponent == "bicyclist":
        return MOVES[(n // 2) % 3]
    if n == 0:
        return "rock"
    last = round_winner(*history[-1])
    if opponent == "winner":
        return last
    return BEATS[last]


def play(opponent, filename="roshambot.py"):
    history = []  # (theirs, mine)
    printed = []  # your moves
    problem = None

    # The opponent only answers once your move for this round is printed.
    def fake_print(*args, **kwargs):
        line = kwargs.get("sep", " ").join(str(a) for a in args).strip()
        if line in MOVES:
            printed.append(line)

    def fake_input(prompt=None):
        nonlocal problem
        mine, theirs = score(history)
        if mine == 5 or theirs == 5 or len(history) == 9:
            problem = "the game is over, but your program asks for the opponent's move again"
            raise StopGame()
        if len(printed) != len(history) + 1:
            problem = ("your program should first print its move (just rock, paper or scissors, "
                       "on a line of its own) and then ask for the opponent's move")
            raise StopGame()
        move = opponent_move(opponent, history)
        history.append((move, printed[-1]))
        return move

    with open(filename) as f:
        code = compile(f.read(), filename, "exec")
    try:
        exec(code, {"__name__": "__main__", "print": fake_print, "input": fake_input})
    except StopGame:
        pass

    print(f"Playing against {OPPONENTS[opponent]}:")
    print("        | You played | Opponent played |")
    for i, (theirs, mine) in enumerate(history):
        if mine == theirs:
            result = "draw :|"
        elif round_winner(theirs, mine) == mine:
            result = "won  :)"
        else:
            result = "lost :("
        print(f"Round {i + 1} | {mine:<10} | {theirs:<15} | {result}")
    print()

    mine, theirs = score(history)
    if problem:
        print(f"Oops: in round {len(history) + 1} {problem}.")
    elif mine < 5 and theirs < 5 and len(history) < 9:
        print(f"Oops: your program stopped at {mine}-{theirs} after {len(history)} rounds, but the game isn't over.")
    elif mine == 5:
        print("You won!!!")
    elif theirs == 5:
        print("You lost :(")
    else:
        print(f"Draw: {mine}-{theirs} after 9 rounds. That's not enough, you need to win.")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in OPPONENTS:
        print("Usage: python play.py [opponent]")
        print("where [opponent] is one of: " + ", ".join(OPPONENTS))
        sys.exit(1)
    play(sys.argv[1])
