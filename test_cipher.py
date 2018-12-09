import pytest
import cipher

def test_encrypt_success():
    assert cipher.encrypt("ABC", 1) == "BCD"    
    assert cipher.encrypt("ABC", 0) == "ABC"
    assert cipher.encrypt("abc", -1) == "ZAB"

def test_encrypt_success_with_spaces():
    assert cipher.encrypt("a bc", 1) == "B CD"

def test_encrypt_fail():
    with pytest.raises(TypeError):
        cipher.encrypt('abc', 'q')  

def test_decrypt_success():
    assert cipher.decrypt("BCD", 1) == "ABC"
    assert cipher.decrypt("BCD", 0) == "BCD"
    assert cipher.decrypt("ZAB", -1) == "ABC"

def test_decrypt_encrypt_output_success():
    raw_string = "ALPHABETLETTERS"
    rotation_amount = 1
    encrypted_word = cipher.encrypt(raw_string, rotation_amount)
    decrypted_word = cipher.decrypt(encrypted_word, rotation_amount)
    assert decrypted_word == raw_string

def test_decrypt_encrypt_letters_and_spaces_large_negative_success():
    raw_string = "ALPHABETLEAHGEAIHGETT E RS"
    rotation_amount = -23849
    encrypted_word = cipher.encrypt(raw_string, rotation_amount)
    decrypted_word = cipher.decrypt(encrypted_word, rotation_amount)
    assert decrypted_word == raw_string