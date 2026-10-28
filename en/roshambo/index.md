# Roshambo

When you play RoShamBo (rock-paper-scissors) you win as often as you lose... *if* the opponent plays randomly. But people rarely play randomly. If they have a strategy you can try to beat it.

Mark Rober made a robot that has a 75% chance of winning against most humans:

![embed](https://www.youtube.com/embed/qgZReY9jnj4)

Rober's solution assumes a fixed strategy, but in principle different people can have different strategies. Your goal is to write a smart RoShamBo bot that figures out which strategy the opponent uses and then beats it.

You will play against these 5 opponents:

| opponent | how it plays |
|---|---|
| Dwayne | always `rock` |
| Lance | cycles: `rock`, `paper`, `scissors`, `rock`, `paper`, `scissors`, ... |
| The Bicyclist | cycles: `rock`, `rock`, `paper`, `paper`, `scissors`, `scissors`, `rock`, `rock`, ... |
| The Winner | starts with `rock`; after that it plays the move that won the previous round |
| The Winner Winner | starts with `rock`; after that it plays the move that beats the move that won the previous round |

Your goal is to write a program called `roshambot.py` that tries to figure out with which opponent you are playing and then beat it.

Each interaction consists of your program making a guess (prints either `"rock"`, `"paper"` or `"scissors"`), and then asking what the opponent played. Example:

	paper
	The opponent played: rock

So, after this interaction our program won (paper beats rock).

You repeat these interactions until one of the players has won 5 rounds, or a total of 9 rounds has been played. If the opponent is Dwayne, the interaction might look something like this:

	paper
	The opponent played: rock
	scissors
	The opponent played: rock
	scissors
	The opponent played: rock
	scissors
	The opponent played: rock
	rock
	The opponent played: rock
	scissors
	The opponent played: rock
	scissors
	The opponent played: rock
	The opponent won :(

In this case the opponent won :(

With this program you have to type in yourself what the opponent plays. This might become tedious, so we made a file `play.py` ([download here](play.py)) that will automatically test your code against any of the 5 players. Put it in the same folder as your `roshambot.py` file and run it using:

    python play.py [opponent]

Where [opponent] can be any of `dwayne`, `lance`, `bicyclist`, `winner`, `winnerwinner`. The output will look something like this:

    Playing against Lance:
            | You played | Opponent played |
    Round 1 | rock       | rock            | draw :|
    Round 2 | rock       | paper           | lost :(
    Round 3 | rock       | scissors        | won  :)
    Round 4 | paper      | rock            | won  :)
    Round 5 | scissors   | paper           | won  :)
    Round 6 | rock       | scissors        | won  :)
    Round 7 | paper      | rock            | won  :)

    You won!!!

Keep in mind that this only works if your program meets the exact specifications as laid out above: first make your own guess (and print it) and then ask what the opponent played.

## Specification summary

* Create a file called `roshambot.py`.

* Each round, your program first prints its move on a line of its own: just `rock`, `paper` or `scissors`. Then it reads the opponent's move with `input`.

* Rock beats scissors, scissors beats paper and paper beats rock. Two of the same is a tie: it counts as a round, but nobody gets a win.

* The game ends as soon as one of the players has 5 wins, or after 9 rounds. Then print who won.

* Your program beats an opponent if it gets **5 wins** first.

* Beat each strategy using a single program (so you need to guess which opponent you are facing). The game could theoretically end in a draw. That is not enough, you need to win.

### Constraints

* **You are only allowed to use the programming concepts discussed so far.** So, *no* lists, dicts, sets or other data structures. (If you already know more advanced concepts, consider it a challenge to limit yourself to this minimal set of operations.)

* You are *not* allowed to use the `import` or `break` statements.

## Testing

First play against your program yourself: pick one of the opponents and type in its moves. Then test it with `play.py`. 

You can also use `checkpy`, which tests all five opponents:

	checkpy roshambot
