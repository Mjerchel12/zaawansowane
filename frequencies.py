import re

def word_frequencies(text: str) -> dict:
    words = re.findall(r"\b\w+\b", text.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq