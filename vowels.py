def count_vowels(s):
    count = 0
    for char in s:
        if char in "aeiouAEIOU":
            count += 1
    return count
s = input()
vowel_count = count_vowels(s)
print(vowel_count(s))


