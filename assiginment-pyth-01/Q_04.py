# Substring Search

# Task: Given the string s, use string methods to:


# Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.

s:str ="the quick brown fox jumps over the lazy dog"

x = s.find("fox" )
print(f"index of 'fox' is {x}")

# sub : str = ("fox")

# c = s.find(sub, 0 )
# print(f"index of 'fox' is {c}")
# if "fox" in text:
#     index = text.index("fox")
# else:
#     index = -1

# print(index)


# Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.


text = "The quick brown fox jumps over the lazy dog. The dog did not see The fox."
count_the = text.title().count("The")

print(count_the)
