def count_words(text: str, words: set) -> int:
    count = 0
    
    for word in words:
        if word.lower() in text.lower():
            count += 1
    
    
    return count