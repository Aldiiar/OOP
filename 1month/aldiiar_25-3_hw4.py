data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
datat = list(data_tuple)

letters = []
numbers = []

'''1'''
letters = [i for i in datat if type(i) == str]
numbers = [i for i in datat if type(i) != str]

'''2'''
numbers.remove(6.13)
true_ = numbers.pop(0)
letters.append(true_)
numbers.insert(1, 2)

'''3'''
numbers.sort()
letters.reverse()
letters[1] = letters[1].upper()
letters[-2] = letters[-2].lower()

'''4'''
numbers[0] = numbers[0]**2
numbers[1] = numbers[1]**2
numbers[2] = numbers[2]**2

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)
