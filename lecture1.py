# first lecture todaty 12 january 2023.


# Lazy evaluation similar to c/c++ the boolean operator are lazily tested.

a = False
b = True


def truthy():
    print("it's true!")
    return b


def false():
    print("it's false!")
    return a


print("true opr false result: ")
truthy() or false()

print("\nfalse or ture result: ")
false() or truthy()

print("\ntrue and false result: ")
truthy() and false()

print("\nfalse and true result: ")
false() and truthy()

print("true opr false result: ")

print('non'[::-1])  # reverse string
# string is immutable.

non_list = ['non', 'aom', 'ok']
print(non_list[::-1])

# list when you assign a variable list to another list variable,
# duplicates are not made, instead they are simply
# different names referring to the same list.
# This is similar to how we might think about array assignment in c/C+

list1 = [1, 23, 4, 5]
print(list1)
list2 = list1
list2[0] = 60

print(list1, list2)

# ab = 3000
# bb = 3000
# ab == bb

# True

# ab is bb
# false

# bb = [1, 2, 3]
# ab == bb

# a is b
key1 = 10
my_dic = {key1: 5, "key2": 6, 8: 15}
print(my_dic[key1])


def wins_rock_scissors_paper(p1, p2):
    # rock beats scissors
    # paper beats rock
    # scissos beats paper
    print('Start Rock Game')
    f = False
    player = p1
    opponent = p2

    player = player.lower()
    opponent = opponent.lower()

    if player == opponent:
        print('ties!')
        return f

    if player == "rock" and opponent == "scissors":
        print("player win!")
        f = True

    if player == "scissors" and opponent == "paper":
        print("player win!")
        f = True

    if player == "paper" and opponent == "rock":
        print("player win!")
        f = True

    else:
        print("return false opponent win!")

    return f


wins_rock_scissors_paper('rock', 'paper')



