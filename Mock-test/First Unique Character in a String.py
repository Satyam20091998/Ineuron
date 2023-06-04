def firstUniqChar(s):
    # Step 1: Create a dictionary to store the frequency of characters
    char_freq = {}

    # Step 2: Update the frequency count in the dictionary
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    # Step 3: Check the frequency of each character
    for i in range(len(s)):
        if char_freq[s[i]] == 1:
            return i

    # Step 4: No non-repeating character found
    return -1
print(firstUniqChar("leetcode"))  # Output: 0
print(firstUniqChar("loveleetcode"))  # Output: 2
print(firstUniqChar("aabb"))  # Output: -1
