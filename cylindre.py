__author__ = 'Bertrand'


class EnigmaCylindre:
    _cylindre = ['abcdefghijklmnopqrstuvwxyz', 'WQAXSZCDEVFRBGTNHYJUKILOMP']

    def _reset_cylindre(self, initial_char):
        while self._cylindre[0][0] != initial_char :
            self._rotate()

    def _rotate(self):
        temp = self._cylindre[0][1:]
        temp += self._cylindre[0][0]
        self._cylindre[0] = temp
        return temp

    def _strip(self,str):
        return ''.join(c for c in str if c in self._cylindre[0])

    def _packetize(self, str):
        reste = len(str) % 5
        if reste == 0:
            reste = 5
        for i in range(len(str) - reste, 0, -5):
            str = str[0:i] + " " + str[i:]
        return str

    def _encode_char(self, char_to_encode):
        found = self._cylindre[0].find(char_to_encode)
        if found != -1:
            encoded = self._cylindre[1][found]
            return encoded
        return char_to_encode

    def _decode_char(self, char_to_decode):
        found = self._cylindre[1].find(char_to_decode)
        if found != -1:
            encoded = self._cylindre[0][found]
            return encoded
        return char_to_decode

    def encode_string(self, str_to_encode):
        encoded = ''
        for c in str_to_encode:
            encoded += self._encode_char(c)
            self._rotate()
        return encoded

    def decode_string(self, str_to_decode):
        decoded = ''
        for c in str_to_decode:
            decoded += self._decode_char(c)
            self._rotate()
        return decoded

    def _setup(self):
        print("Saisissez la position initiale du cylindre \n")
        pos = input().lower()
        while pos not in self._cylindre[0]:
            print("caractère inconnu, veuillez réessayer, merci")
            pos = input("nouvel essai").lower()

        self._reset_cylindre(pos)
        print(self._cylindre)

    def encode(self,str_to_encode):
        self._setup()
        striped = self._strip(str_to_encode)
        packetized = self._packetize(striped)
        encoded = self.encode_string(packetized)
        return encoded

    def decode(self, str_to_decode):
        self._setup()
        encoded = self.decode_string(str_to_decode)
        return encoded










