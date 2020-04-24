from math import factorial
from pprint import pprint as pp

words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer in pulvinar nunc,
in rhoncus ligula. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
Etiam congue convallis dignissim. Curabitur vitae elit vel tellus mattis vulputate. Sed posuere nibh sit amet
elit porttitor, et porta urna aliquam.""".split()

# using generator to process lists
letter_counts = [len(word) for word in words]

# using generator to create empty prefilled list

# same result as empty_prefilled_list = [0] * 100? yes, because integers are immutable
empty_prefilled_list = [0 for _ in range(100)]
# test if you fill the list with refs or a ref to the same object
empty_prefilled_list[0] = 1
print(empty_prefilled_list)

# this is fine, new rows of 2D list are generated, not copied
prefilled_2d_list = [[0] * 20 for x in range(20)]
# this causes error because list is mutable. rows are copied by `* 20` statement
prefilled_2d_list_2 = [[0] * 20] * 20
prefilled_2d_list[0][0] = 1
prefilled_2d_list_2[0][0] = 1
pp(prefilled_2d_list)
pp(prefilled_2d_list_2)

# set generators
print({len(str(factorial(x))) for x in range(100)})

# dictionary generators
country_to_capital = {
    'Poland': 'Warszawa',
    'Romaina': 'Timisoara',
    'United States of America': 'Washington',
    'Serbia': 'Zagrzeb',
}

capital_to_country = {capital: country.split() for country,
                      capital in country_to_capital.items()}

pp(capital_to_country)

words = ['hi', 'hello', 'fox', 'yssss', 'alpha', 'jaguar', 'jazzy']
word_set = {x[0]: x for x in words}

# using lambda function to sort touplet elements
pp(sorted(word_set.items(), key=lambda x: x[0]))
