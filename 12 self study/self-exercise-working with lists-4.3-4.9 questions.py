twenty = [value for value in range(1,21)]
print(twenty)

million = [value for value in range(1,10000001)]
print(min(million))
print(max(million))
print(sum(million))

odd_number = [value for value in range(1, 21, 2)]
print(odd_number)

three = [value * 3 for value in range(1,11)]
print(three)

cube = [value **3 for value in range(1,11)]
print(cube)

names = ['mk', 'shakir', 'boko', 'josh', 'yasin']
print(names[0:2]) # [0:2] tells python to print items from names list, it starts from position zero and stops before reaching position 2
print(names[:3]) # [0:3] tells python to print items from names list, it starts from position zero and stops before reaching position 3
print(names[2:]) 