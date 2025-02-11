# Conway

Create a file called `conway.py` that implements Conway's Game of Life: [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

You don't need anything fancy, you can just animate this in the terminal:

![](conway.gif)

### Some tips:

* Define a field a 2D-list of strings:

	    X = "#" # on
	    o = " " # off

	    field = [
	        [o, o, o, o, o, o, o, o, o, o],
	        [o, X, o, o, o, o, o, o, o, o],
	        [o, o, X, X, o, o, o, o, o, o],
	        [o, X, X, o, o, o, o, o, o, o],
	        [o, o, o, o, o, o, o, o, o, o],
	        [o, o, o, o, o, o, o, o, o, o],
	        [o, o, o, o, o, o, o, o, o, o],
	        [o, o, o, o, o, o, o, o, o, o],
	        [o, o, o, o, o, o, o, o, o, o],
	        [o, o, o, o, o, o, o, o, o, o],
	    ]


* Print the field with a space between each element to make it (sort of) square.

* Use this to clear the screen between frames:

	    ### clear screen
	    print(chr(27) + "[2J")

* Use the time library to pauze between frames:

	    import time

	    time.sleep(0.1)

* Each iteration, compute a new frame in a new variable called `new_field` using the rules of the game. Only once you're completely done applying the rules, you set `field = new_field`. This way you avoid loosing information that you might need for applying the game rules.
