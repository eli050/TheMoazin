from utils import decode_base64
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
    def _calculate_danger(self):
        frequency = 0
        list_of_text = self.text_to_check.lower().strip().split()
        words_pair_count = 0
        for i, word in enumerate(list_of_text):
            if word in self.list_dangerous_words:
                # print(word)
                frequency += 1
            elif word in self.list_most_dangerous_words:
                # print(word)
                frequency += 2
            if i + 1 < len(list_of_text):
                if (f"{list_of_text[i]} {list_of_text[i+1]}"
                        in self.list_dangerous_words):
                    # print(f"{list_of_text[i]} {list_of_text[i+1]}")
                    frequency += 1
                    words_pair_count += 1
                elif (f"{list_of_text[i]} {list_of_text[i + 1]}"
                        in self.list_most_dangerous_words):
                    # print(f"{list_of_text[i]} {list_of_text[i + 1]}")
                    frequency += 2
                    words_pair_count += 1
        return frequency / (len(list_of_text) - words_pair_count)

    @staticmethod
    def _is_bds( num_of_dangerous:float):
        return num_of_dangerous > 0.7

    @staticmethod
    def _danger_levels(num_of_dangerous):
        if num_of_dangerous < 0.30:
            return "none"
        elif 0.30 <= num_of_dangerous <= 0.7:
            return "medium"
        else:
            return "high"


