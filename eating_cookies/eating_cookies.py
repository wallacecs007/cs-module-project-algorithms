'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache):
    # Your code here
    counter = 0

    if cache[n] > 0:
        return cache[n]

    if n == 0:
        cache[0] == 0
        return 1
    if n >= 3:
        counter += eating_cookies(n - 3, cache)
    if n >= 2:
        counter += eating_cookies(n - 2, cache)
    if n >= 1:
        counter += eating_cookies(n - 1, cache)

    cache[n] = counter

    return counter


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
