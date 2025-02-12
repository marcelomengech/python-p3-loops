def happy_new_year():
    """
    Counts down from 10 to 1 and prints "Happy New Year!"
    using a while loop.
    """
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(numbers):
    """
    Squares each element in the input list and returns the new list.

    Args:
        numbers: A list of integers.

    Returns:
        A new list containing the squared values of the input list.
    """
    return [number ** 2 for number in numbers]


def fizzbuzz():
    """
    Prints numbers from 1 to 100, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)