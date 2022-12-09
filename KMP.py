def kmp(pattern, text):
    # Pre-process the pattern to create the partial match table.
    table = [0] * (len(pattern) + 1)
    j = 0
    for i in range(2, len(pattern) + 1):
        while j > 0 and pattern[j] != pattern[i - 1]:
            j = table[j]
        if pattern[j] == pattern[i - 1]:
            j += 1
        table[i] = j

    # Search for the pattern in the text.
    j = 0
    for i in range(len(text)):
        while j > 0 and pattern[j] != text[i]:
            j = table[j]
        if pattern[j] == text[i]:
            j += 1
        if j == len(pattern):
            print("Found pattern at index " + str(i - len(pattern) + 1))
            j = table[j]

# Test the KMP algorithm on a sample pattern and text.
pattern = "ababac"
text = "abacababac"
kmp(pattern, text)


# This implementation of the KMP algorithm first pre-processes the pattern to create the partial match table,
# Then searches for the pattern in the text using the information in the partial match table to avoid unnecessary comparisons.

# When run on the sample pattern and text, the output would be:

#Found pattern at index 4


