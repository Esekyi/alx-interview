#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of each round of the game and returns
        the player with the most wins.
    """
    if not nums or x < 1:
        return None

    max_number = max(nums)

    is_prime = [True] * (max_number + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_number**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_number + 1, i):
                is_prime[j] = False

    count_primes = [0] * (max_number + 1)
    for i in range(1, max_number + 1):
        count_primes[i] = count_primes[i - 1] + is_prime[i]

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if count_primes[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
