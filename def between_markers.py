def between_markers(text: str, begin: str, end: str) -> str:
    
    if (begin not in text) and (end not in text):
        return text
    elif begin not in text:
        return text[:text.index(end)]
    elif end not in text:
        return text[text.index(begin)+len(begin):]    
    else:
        return text[text.index(begin)+len(begin):text.index(end)]