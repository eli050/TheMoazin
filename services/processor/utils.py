import base64
import re


def encode_base64(base64_string:str, format_return:str = "ascii" ) -> list:
    decoded_bytes = base64.b64decode(base64_string)
    decoded_string = decoded_bytes.decode(format_return)
    decoded_list = re.split("r[ ,]+", decoded_string)
    return [item for item in decoded_list if item]