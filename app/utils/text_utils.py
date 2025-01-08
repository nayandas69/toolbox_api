from collections import Counter

def word_count(text: str) -> int:
    return len(text.split())

def is_palindrome(text: str) -> bool:
    sanitized = text.replace(" ", "").lower()
    return sanitized == sanitized[::-1]

def char_frequency(text: str) -> dict:
    return dict(Counter(text))

def summarize_text(text: str) -> str:
    # Dummy summarization
    sentences = text.split('.')
    return '. '.join(sentences[:2]) if len(sentences) > 2 else text

def extract_keywords(text: str) -> list:
    # Dummy keyword extraction
    words = text.split()
    return list(set(words[:5])) if len(words) > 5 else list(set(words))
