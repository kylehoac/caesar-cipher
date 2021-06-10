from caesar_cipher.caesar_cipher import encrypt,decrypt,crack

def test_cipher_shift_1():
    encrypted = encrypt("abcd",1)
    assert encrypted == "bcde"
    assert decrypt(encrypted, 1) == "abcd"

def test_cipher_shift_2():
    encrypted = encrypt("abcd",2)
    assert encrypted == "cdef"
    assert decrypt(encrypted, 2) == "abcd"

def test_cipher_wrap():
    encrypted = encrypt("xyz",1)
    assert encrypted == "yza"
    assert decrypt(encrypted, 1) == "xyz"
    print("TEST PASSED")

def test_cipher_crack():
    encrypted = encrypt("bear", 2)
    actual = crack(encrypted).__contains__("bear")
    expected = True
    assert actual == expected

def test_cipher_crack_name():
    encrypted = encrypt("billy", 2)
    actual = crack(encrypted).__contains__("billy")
    expected = True
    assert actual == expected

def test_cipher_with_capital():
    encrypted = encrypt("KYLE", 2)
    actual = crack(encrypted).__contains__("kyle")
    expected = True
    assert actual == expected