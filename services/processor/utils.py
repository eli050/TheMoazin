import base64
import cleantext


def clean_central(text):
    return cleantext.clean(text,
                           lowercase=True,
                           extra_spaces=True,
                           punct=True,
                           stopwords=True
                          )




def decode_base64(base64_string:str, format_return:str = "ascii" ) -> list:
    decoded_bytes = base64.b64decode(base64_string)
    decoded_string = decoded_bytes.decode(format_return)
    return decoded_string.lower().split(",")

def get_unique_list(input_list):
    unique_items = []
    seen = set()
    for item in input_list:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)
    return unique_items