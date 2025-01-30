# Collect

Implement a program creates a list of coins to return given sum of change.

### Example 1

	How much change is owed? 0.41
	You should return these coins: [25, 10, 5, 1]

### Example 2

	How much change is owed? 1.1
	You should return these coins: [25, 25, 25, 25, 10]

## Background

![](coinchange.png)

This assignment is based on the Greedy-assignment that you made earlier. You're going to adapt the same algorithm that finds the minimum number of coins to be returned. This time you're going to keep track of a list of actual coin values to be returned.

## Specification

* Create a file called `collect.py` and implement a program that first prompts for the number of change owed and subsequently prints the minimum number of coins required.

* Assume that the user provides a whole number (integer), or a decimal number (float). The decimals in that case represent individual cents. So `3.21` means `3` dollar and `21` cents.

* If the user provides a negative number, make sure to ask for input again. Repeat until the user gives correct input.

* Return a list of coins that returns the change using the minimum number of coins (using the same strategy as for `greedy.py`). The list should be sorted from high to low.

* Do not copy-paste the code for each coin value, but write an algorithm that uses a `for`-loop:

		for coin_value in [25, 10, 5, 1]:
			# your code

### Constraints

Just as before there are some constraints on what you're allowed to use.

* You are only allowed to use the concepts that are discussed in this module.
For an overview of those concepts have a look [here](/python/en/overview).
* You are *not* allowed to use the `import`-statement. (This hasn't been discussed yet, but if you happen to know it, don't use it.)
* You are *not* allowed to use string multiplication (i.e., `[25] * number_of_coins`)

## Testing

	checkpy collect
