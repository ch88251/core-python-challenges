"""
You are in charge of the cake for a child's birthday. You have decided the cake
will have one candle for each year of their total age. They will only be able to
blow out the tallest of the candles. Count how many candles are tallest.
"""
import os


def birthday_cake_candles(candles):
    largest = max(candles)
    return candles.count(largest)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthday_cake_candles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
