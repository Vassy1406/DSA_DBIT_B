def char_frequencies(s):
    freq ={}
    for char in s:
        if char != "": #ignore spaces
            freq[char] = freq.get(char, 0) +1
            return freq
        s="data structure and algorithms"
        print(char_frequencies(s))
