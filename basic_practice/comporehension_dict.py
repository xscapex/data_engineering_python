word = 'letters'

letter_counts = {letter: word.count(letter) for letter in set(word)}

print(letter_counts)

