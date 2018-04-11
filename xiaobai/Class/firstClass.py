class CocaCola:
    formula = ['sugar', 'caffeine', 'soda', 'water']


cola_for_you = CocaCola()
print(CocaCola.formula)
print(cola_for_you.formula)

for element in cola_for_you.formula:
    print(element)

coke_for_China = CocaCola()
coke_for_China.local_logo = '可口可乐'
print(coke_for_China.local_logo) 