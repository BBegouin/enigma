from cylindre import EnigmaCylindre


class EnigmaMachine:
    _codec = EnigmaCylindre()

    def code(self, str_to_code):
        return self._codec.encode(str_to_code)


    def decode(self, str_to_decode):
        return self._codec.decode(str_to_decode)


