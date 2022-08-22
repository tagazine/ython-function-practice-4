from operator import truediv


def max_num(nums): #function 1
    return max(nums)

list = {1, 5, 10, 6}
print(max_num(list))


def mult_list(list): #function 2
    product = 1
    for num in list:
        product = product * num
    return product

list = [2, 2, 6, 7]
print(mult_list(list))


def rev_string(string): #function 3
    return string[::-1]

print(rev_string("Hiya, Folks!"))


def num_within(num, begin, end): #function 4
    for i in range(begin, end):
        if i == num:
            return True
    return False

print(num_within(3, 2, 9))


def pascal(n): #function 5
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')

        num = 1
        for j in range(1, i+1):
            print(' ', num, sep='', end='')
            num = num * (i - j) // j
        print()

pascal(5)