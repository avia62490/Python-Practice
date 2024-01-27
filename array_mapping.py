# 1. Start with an array of numbers and create a new array with each number times 3.
#     For example, [1, 2, 3] becomes [3, 6, 9].

# list = [1, 2, 3]
# tripled = [x * 3 for x in list]
# print(tripled)

#  2. Start with an array of strings and create a new array with each string upcased.
#     For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

# strings = ['hello', 'goodbye']
# allcaps = [x.upper() for x in strings]
# print(allcaps)

#  3. Start with an array of hashes and create a new array of string values from each hash's :name key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].

# people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
# names = [x["name"] for x in people]
# print(names)

#  4. Start with an array of numbers and create a new array with each number plus 7.
#     For example, [1, 2, 3] becomes [8, 9, 10].

# nums = [1, 2, 3]
# added_nums = [x + 7 for x in nums]
# print(added_nums)

#  5. Start with an array of strings and create a new array with each string's length.
#     For example, ["hello", "goodbye"] becomes [5, 7].

# strings = ["hello", "goodbye"]
# lengths = [len(x) for x in strings]
# print(lengths)

#  6. Start with an array of hashes and create a new array of number values from each hash's :age key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].

# people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
# ages = [x["age"] for x in people]
# print(ages)

#  7. Start with an array of numbers and create a new array with each number divided by 2.
#     For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].

# nums = [1, 2, 3]
# halves = [x / 2 for x in nums]
# print(halves)

#  8. Start with an array of strings and create a new array with each string's first letter only.
#     For example, ["hello", "goodbye"] becomes ["h", "g"].

# words = ["hello", "goodbye"]
# first_letters = [x[0] for x in words]
# print(first_letters)

# 9.  Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].

# people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
# double_ages = [x["age"] * 2 for x in people]
# print(double_ages)

# 10. Start with an array of numbers and create a new array with each number converted into a string.
#     For example, [1, 2, 3] becomes ["1", "2", "3"].

# ints = [1, 2, 3]
# string_numbers = [str(x) for x in ints]
# print(ints)
# print(string_numbers)


# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/b9ac4390aad2301a2238efc95c904f3d
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/66598fd7cdbc67fe663624e217cebbaf
# SOLUTIONS (using .map shortcut): https://gist.github.com/peterxjang/23a8f8a51601e4288ba3a8aa6d1f1c98