#  1. Start with an array of numbers and compute the sum of all the numbers.
#     For example, [5, 10, 8, 3] becomes 26.

# list = [5, 10, 8, 3]
# sum = sum(list)
# print(sum)

#  2. Start with an array of strings and combine them all into a single string.
#     For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

# list = ["volleyball", "basketball", "badminton"]
# string = ""
# for x in list:
#   string += x

# print(string)

#  3. Start with an array of hashes and compute the sum of the prices (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

products = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
# prices = [x["price"] for x in products]
# # print(prices)
# print(sum(prices))

#  4. Start with an array of numbers and compute the the minumum number.
#     For example, [5, 10, 8, 3, 9] becomes 3.

# nums = [5, 10, 8, 3, 9]
# min = min(nums)
# print(min)

#  5. Start with an array of strings and compute the total length of all the strings.
#     For example, ["volleyball", "basketball", "badminton"] becomes 29.

# sports = ["volleyball", "basketball", "badminton"]
# sum = 0
# for sport in sports:
#   sum += len(sport)

# print(sum)

#  6. Start with an array of hashes and find the hash with the lowest price (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.

# cheapest_product = products[0]
# for item in products:
#   if item["price"] < cheapest_product["price"]:
#     cheapest_product = item

# print(cheapest_product)

#  7. Start with an array of numbers and compute product of all the numbers.
#     For example, [5, 10, 8, 3] becomes 1200.

# nums = [5, 10, 8, 3]
# math_product = 1
# for num in nums:
#   math_product *= num

# print(math_product)

#  8. Start with an array of strings and combine them all into a single string, separated by dashes.
#     For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

# sports = ["volleyball", "basketball", "badminton"]
# string = "-"
# for sport in sports:
#   string += sport + "-"

# print(string)

#  9. Start with an array of hashes and find the hash with the shortest name (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

# shortest = min(products, key=lambda x: len(x["name"]))
# print(shortest)

# 10. Start with an array of numbers and compute the maximum number.
#     For example, [5, 10, 8, 3] becomes 10.

# nums = [5, 10, 8, 3]
# print(max(nums))


# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/376c8931a48549889eb3c9bc091e9f43
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/379c9945774f51027750c59d6e4395df
# SOLUTIONS (using .reduce shortcut): https://gist.github.com/peterxjang/b69183e2d555964ce3936893f423ef35