# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations


if __name__ == '__main__':
    string,legnth=input().split()
    for permutation in permutations(sorted(string), int(legnth)):
     print(''.join(permutation))

