class EnigmaMachine:
    cylindres = [
            'abcdefghijklmnopqrstuvwxyz', #clear
            'WQAXSZCDEVFRBGTNHYJUKILOMP' #coded
        ]

    # ================================ Private ================================= #

    def _shift(self, cyl, index):
        """
        Permet de décaler le cylindre cyl de index positions
        :param cyl:
        :param index:
        :return:
        """
        return cyl[index:] + cyl [:index]

    def _strip(self, str_to_strip):
        """
        supprime les caractère spéciaux
        :return:
        """
        str = str_to_strip
        char_to_strip = ['.', ',', '\'', ';', '&', 'é', '"', '(', '§', 'è', '!', 'ç', 'à', ')', '-', '_', '^',
                         '¨', '$', 'ù', '%', '`', '£', '+', '=', ':', '/', '?', ' ']
        for i in char_to_strip:
            str = str.replace(i, "")
        return str

    def _packetize(self, str_to_packetize):
        """
        Permet de découper une chaîne de caractère en paquet de 5 lettre séparées par des espaces
        :return:
        """
        str = str_to_packetize
        reste = len(str_to_packetize) % 5
        if reste == 0:
            reste = 5
        for i in range(len(str_to_packetize) - reste, 0, -5):
            str = self._insertChar(str, i, " ")
        return str

    def _insertChar(self, mystring, position, chartoinsert ):
        mystring   =  mystring[:position] + chartoinsert + mystring[position:]
        return mystring

    def _set_initial_pos(self,cyl, starting_char):
        """
        Permet de paramètrer les cylindres sur la bonne position de départ
        :param cyl:
        :param starting_char:
        :return:
        """
        index = cyl.find(starting_char)
        return self._shift(cyl,index)

    def _encode_char(self, char_to_encode):
        """
        permet d'encoder un cylindre
        :param cyl:
        :return:
        """
        c = char_to_encode
        found = self.cylindres[0].find(c)
        if found is not None:
            c = self.cylindres[1][found].lower()
        return c

    def code(self, msg_to_encode):
        """
        permet d'encoder une chaine de caractère
        :param msg_to_encode:
        :return:
        """
        msg = self._strip(msg_to_encode)
        encoded = ''
        for i in range(0, len(msg)):
            encoded += self._encode_char(msg[i])
            self._shift(self.cylindres[1],1)
        encoded = self._packetize(encoded)

        return encoded

    def decode(self, msg_to_decode):
        """
        Permet de décoder une chaine de caractère
        :param msg_to_decode:
        :return:
        """
        decoded = ''
        for i in range(0, len(msg_to_decode)):
            decoded += self._decode_char(msg_to_decode[i])
            self._shift(self.cylindres,1)

        return decoded

    def _decode_char(self, char_to_decode):
        if char_to_decode == ' ':
            return ' '
        c = char_to_decode
        found = self.cylindres[1].find(c.upper())
        if found is not None:
            c = self.cylindres[0][found]
        else:
            print (c + " pas trouvé")
        return c

    def setup(self, starting_char):
        """
        positionne les cylindres sur la position initiale souhaitée
        :param starting_chars:
        :return:
        """
        self.cylindres[0] = self._set_initial_pos(self.cylindres[0],starting_char)

