import base64



def decode_base64(base64_string:str, format_return:str = "ascii" ) -> list:
    decoded_bytes = base64.b64decode(base64_string)
    decoded_string = decoded_bytes.decode(format_return)
    return decoded_string.lower().split(",")