from fastapi import APIRouter
from app.utils.text_utils import word_count, is_palindrome, char_frequency, summarize_text, extract_keywords

router = APIRouter()

@router.post("/word-count")
def count_words(text: str):
    return {"word_count": word_count(text)}

@router.post("/is-palindrome")
def palindrome_check(text: str):
    return {"is_palindrome": is_palindrome(text)}

@router.post("/char-frequency")
def character_frequency(text: str):
    return {"character_frequency": char_frequency(text)}

@router.post("/summarize")
def text_summarization(text: str):
    return {"summary": summarize_text(text)}

@router.post("/extract-keywords")
def keyword_extraction(text: str):
    return {"keywords": extract_keywords(text)}
