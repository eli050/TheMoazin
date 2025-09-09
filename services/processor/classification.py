from utils import decode_base64
from config import MOST_DANGEROUS_WORDS, DANGEROUS_WORDS
import re


class Classification:
    def __init__(self, text_to_check:str):
        self.text_to_check = text_to_check
        self.list_most_dangerous_words:list[str] = decode_base64(MOST_DANGEROUS_WORDS)
        self.list_dangerous_words:list[str] = decode_base64(DANGEROUS_WORDS)
    def calculate_danger(self):
        danger_count = 0
        for word in self.list_dangerous_words:
            if re.search(r'\b' + re.escape(word) + r'\b',self.text_to_check):
                danger_count += 1

        for word in self.list_most_dangerous_words:
            if re.search(r'\b' + re.escape(word) + r'\b',self.text_to_check):
                danger_count += 2
        return (danger_count* 100)/ len(self.text_to_check.split())

    def is_bds(self):
        pass
    def danger_levels(self):
        pass

