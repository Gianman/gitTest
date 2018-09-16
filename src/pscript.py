
user_nums = list()


def funct(a, b):
    return a + b


def prompt():
    a = raw_input('Enter a number: ')
    return int(a)


def main():
    for i in range(0, 2):
        temp = prompt()
        user_nums.append(temp)

    result = funct(user_nums[0], user_nums[1])
    print('Result is {}'.format(result))


if __name__ == '__main__':
    main()
