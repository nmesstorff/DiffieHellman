"""
File: DH.py
Author: Norman Messtorff
Email: normes@normes.org
Github: https://github.com/nmesstorff
Description: Diffie-Hellman keyexchange example in python
    for more information about DH see:
    http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
"""
import random


class DH(object):
    """
    Diffie-Hellman keyexchange example in python
    """
    def __init__(self, in_g, in_p):
        """check & set primitive root and prime; generate private secret"""
        if self.verify_gp(in_g, in_p):
            self.in_g = in_g
            self.in_p = in_p
        else:
            raise ValueError('g=%i and p=%i have to be: 2 <= g <= (p-2)'
                             % (in_g, in_p))
        self.prvsecret = self.get_random()
        self.sharedsecret = None

    @staticmethod
    def verify_gp(in_g, in_p):
        """ (int, int) -> boolean

        Verify that selected base in_g is greater than or equal 2
        and less than or equal prime in_p minus 2.
        Does not check if in_p is really a prime number.

        >>> DH.verify_gp(in_g=10, in_p=11)
        False
        >>> DH.verify_gp(in_g=2, in_p=13)
        True
        """
        if 2 <= in_g <= (in_p - 2):
            return True
        return False

    def get_random(self):
        """
        generate (secret) random number
        WARNING: this is only a pseudo random number!
        """
        return random.randint(1, (self.in_p - 2))

    def gen_pubkey(self):
        """generate public key"""
        return (self.in_g ** self.prvsecret) % self.in_p

    def gen_shared_secret(self, otherpublic):
        """generate shared secret"""
        return (otherpublic ** self.prvsecret) % self.in_p

    def set_shared_secret(self, otherpublic):
        """set shared secret"""
        self.sharedsecret = self.gen_shared_secret(otherpublic)
