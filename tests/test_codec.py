from cylindre import EnigmaCylindre


def test_strip():
    cyl = EnigmaCylindre()
    striped = cyl._strip("toto é s&fà")
    assert striped == "totosf"


def test_packetize():
    cyl = EnigmaCylindre()
    striped = cyl._packetize("salutlescopains,çava?")
    assert striped == "salut lesco pains ,çava ?"


def test_encode_char():
    cyl = EnigmaCylindre()
    encoded = cyl._encode_char("b")
    assert encoded == "Q"
    encoded = cyl._encode_char("r")
    assert encoded == "Y"


def test_rotate():
    cyl = EnigmaCylindre()
    cyl._rotate()
    assert cyl._cylindre == ['bcdefghijklmnopqrstuvwxyza', 'WQAXSZCDEVFRBGTNHYJUKILOMP']
    cyl._rotate()
    assert cyl._cylindre == ['cdefghijklmnopqrstuvwxyzab', 'WQAXSZCDEVFRBGTNHYJUKILOMP']


def test_reset_cylindre():
    cyl = EnigmaCylindre()
    cyl._reset_cylindre("a")
    assert cyl._cylindre == ['abcdefghijklmnopqrstuvwxyz', 'WQAXSZCDEVFRBGTNHYJUKILOMP']

"""
def test_encode_string():
    cyl = EnigmaCylindre()
    cyl._reset_cylindre("a")
    encoded = cyl.encode("salut les copains !! comment ça va ? ")
    assert encoded == 'JPVYN ZOFUS XGKMA FIJYE NKWKM'


def test_decode_string():
    cyl = EnigmaCylindre()
    cyl._reset_cylindre("a")
    encoded = cyl.decode("JPVYN ZOFUS XGKMA FIJYE NKWKM")
    assert 'salut lesco pains comme ntava' == encoded
"""
