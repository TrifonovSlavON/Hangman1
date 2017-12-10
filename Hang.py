import random
slovar = ['lol', 'kek', 'cheburek', 'program', 'test']

mistakes = []
a1 = ['Mistakes: 1 of 5', '  ___', ' |   |', ' |', ' |', ' |', ' |']
a2 = ['Mistakes: 2 of 5', '  ___', ' |   |', ' |', ' |', ' |', '/|\ ']
a3 = ['Mistakes: 3 of 5', '  ___', ' |   |', ' |   O', ' |', ' |', '/|\ ']
a4 = ['Mistakes: 4 of 5', '  ___', ' |   |', ' |   O', ' |  /|\ ', ' |', '/|\ ']
a5 = ['Mistakes: 5 of 5. You lose!', '  ___', ' |   |', ' |   O', ' |  /|\ ', ' |  / \ ', '/|\ ']
mistakes.append(a1)
mistakes.append(a2)
mistakes.append(a3)
mistakes.append(a4)
mistakes.append(a5)

slovo = []
M = random.randint(0, len(slovar) - 1)
for i in range(len(slovar[M])):
    slovo.append('*')
    print('*', end='')
i = 0
while i != 5:
    if '*' not in slovo:
        print('You win!')
        break
    bukva = input()
    if bukva in set(slovar[M]):
        for j in range(len(slovo)):
            if slovar[M][j] == bukva:
                slovo[j] = bukva
        # print('\n')
        for k in slovo:
            print(k, end='')
        print('\n-------------------------------------------------------------')
    else:
        for j in range(len(mistakes[i])):
            print(mistakes[i][j], end='\n')

        print(' ')
        for k in slovo:
            print(k, end='')

        print('\n-------------------------------------------------------------')
        i += 1