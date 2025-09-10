from utils import *
from config import MOST_DANGEROUS_WORDS, DANGEROUS_WORDS



class Classification:
    def __init__(self, text_to_check:str):
        self.text_to_check = text_to_check
        self.list_most_dangerous_words:list[str] = decode_base64(MOST_DANGEROUS_WORDS)
        self.list_dangerous_words:list[str] = decode_base64(DANGEROUS_WORDS)
    def classify(self) -> dict:
        avg_danger = self._calculate_danger()
        danger_level = Classification._danger_levels(avg_danger)
        is_danger = Classification._is_bds(avg_danger)
        return {
            "bds_percent": avg_danger,
            "bds_threat_level": danger_level,
            "is_bds": is_danger
        }
    def _calculate_danger(self) -> float:
        """
        Returns the percentage of
        dangerousness based on word lists.
        Uses a coverage method
        which checks the amount of words
        from the text that are part of the list.

        """
        count_unique_words = 0
        list_of_text = get_unique_list(clean_central(self.text_to_check).split())
        for i, word in enumerate(list_of_text):
            if word in self.list_dangerous_words:
                count_unique_words += 1
            elif word in self.list_most_dangerous_words:
                count_unique_words += 2
            if i + 1 < len(list_of_text):
                if (f"{list_of_text[i]} {list_of_text[i + 1]}"
                        in self.list_dangerous_words):
                    count_unique_words += 1
                elif (f"{list_of_text[i]} {list_of_text[i + 1]}"
                        in self.list_most_dangerous_words):
                    count_unique_words += 2
        return count_unique_words / (len(self.list_dangerous_words) + len(self.list_most_dangerous_words))

    @staticmethod
    def _is_bds( num_of_dangerous:float) -> bool:
        """Returns whether the text is dangerous or not"""
        return num_of_dangerous > 0.7

    @staticmethod
    def _danger_levels(num_of_dangerous:float) -> str:
        """Returns the level of danger"""
        if num_of_dangerous < 0.30:
            return "none"
        elif 0.30 <= num_of_dangerous <= 0.7:
            return "medium"
        else:
            return "high"


