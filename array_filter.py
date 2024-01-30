#  1. Start with an array of numbers and create a new array with only the numbers less than 20.
#     For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].

# nums = [2, 32, 80, 18, 12, 3]
# small_nums = [ x for x in nums if x < 20]
# print(small_nums)

#  2. Start with an array of strings and create a new array with only the strings that start with the letter "w".
#     For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].

# strings = ["winner", "winner", "chicken", "dinner"]
# w_strings = [s for s in strings if s[0] == 'w']
# print(w_strings)

#  3. Start with an array of hashes and create a new array with only the hashes with prices greater than 5 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}].

# products = [{'name': "chair", 'price': 100}, {'name': "pencil", 'price': 1}, {'name': "book", 'price': 4}]
# expensive_products = [prod for prod in products if prod['price'] > 5]
# print(expensive_products)

#  4. Start with an array of numbers and create a new array with only the even numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [2, 4, 8].

# nums = [2, 4, 5, 1, 8, 9, 7]
# even_nums = [x for x in nums if x % 2 == 0]
# print(even_nums)

#  5. Start with an array of strings and create a new array with only the strings shorter than 4 letters.
#     For example, ["a", "man", "a", "plan", "a", "canal", "panama"] becomes ["a", "man", "a", "a"].

# strings = ["a", "man", "a", "plan", "a", "canal", "panama"]
# short_strings = [s for s in strings if len(s) < 4]
# print(short_strings)

#  6. Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].

# products = [{'name': "chair", 'price': 100}, {'name': "pencil", 'price': 1}, {'name': "book", 'price': 4}]
# short_names = [prod for prod in products if len(prod['name']) < 6 ]
# print(short_names)

#  7. Start with an array of numbers and create a new array with only the numbers less than 10.
#     For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].

# nums = [8, 23, 0, 44, 1980, 3]
# small = [x for x in nums if x < 10]
# print(small)

#  8. Start with an array of strings and create a new array with only the strings that don't start with the letter "b".
#     For example, ["big", "little", "good", "bad"] becomes ["little", "good"].

# words = ["big", "little", "good", "bad"]
# non_bs = [x for x in words if x[0] != 'b']
# print(non_bs)

#  9. Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "pencil", price: 1}, {name: "book", price: 4}].

# products = [{'name': "chair", 'price': 100}, {'name': "pencil", 'price': 1}, {'name': "book", 'price': 4}]
# cheap_products = [ prod for prod in products if prod['price'] < 10]
# print(cheap_products)

# 10. Start with an array of numbers and create a new array with only the odd numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].

# nums = [2, 4, 5, 1, 8, 9, 7]
# odds = [x for x in nums if x % 2 == 1]
# print(odds)

# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/7de16ed43ea506e98df3fa15074b84f8
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/a702894841c7018ed8c127b647ae21f8
# SOLUTIONS (using .select shortcut): https://gist.github.com/peterxjang/b8c8fb8b77b2cae7bb9cc62a3a434761