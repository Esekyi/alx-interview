#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of each round of the game and returns
        the player with the most wins.
    Args:
        x: an integer representing the number of rounds
        nums: a list of n integers
    Returns:
        the name of the player that won the most rounds
    """

    def sieve_of_eratosthenes(n):
        """Generate a list of prime numbers up to n."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    def count_primes(nums, primes):
        """Count the number primes up to nums."""
        return sum(primes[:nums + 1])

    max_number = max(nums)
    primes = sieve_of_eratosthenes(max_number)

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes_count = count_primes(n, primes)
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
