iterable = ['Sprint', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)
another_iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(another_iterator))
print(next(iterator))
print(next(iterator))
