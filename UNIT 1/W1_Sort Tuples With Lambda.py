cows = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
list = list(zip(cows.keys(), cows.values()))
sorted_by_second = sorted(list, key=lambda tup: tup[1], reverse=True)
print(sorted_by_second)