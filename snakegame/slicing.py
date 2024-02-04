letters = ["a","b","c","d","e","f"]

print(f"list to be manipulated{letters}")


print(f"from position 2 to position 5{letters[2:5]}")
print(f"from position 2 till end{letters[2:]}")
print(f"everything except last one{letters[:5]}")
print(f"incremented by 2 {letters[2:5:2]}")
print(f"incremented by 2 but from start to finish(every second item) {letters[::2]}")
print(f"negative increment for reverse list{letters[::-1]}")