from secrets import token_bytes
from typing import Tuple 

def random_key(length: int) -> int:

    random_bytes: bytes = token_bytes(length)

    return int.from_bytes(random_bytes, "big") 

def encrypt(original: str) -> Tuple[int, int]:

    original_bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    
    original_key: int = int.from_bytes(original_bytes, 'big')
    encrypted: int = original_key ^ dummy

    return dummy, encrypted

def decrypt(key_1: int, key_2: int) -> str:

    decrypted: int = key_1 ^ key_2
    decrypted_bytes: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')

    return decrypted_bytes.decode()

if __name__ == '__main__':

    str_to_encrypt = 'rodrigo bernardo medeiros'
    key_1, key_2 = encrypt(str_to_encrypt)

    result: str = decrypt(key_2, key_1)

    print(result)


