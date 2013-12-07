import unittest
from DH import DH


class TestDH(unittest.TestCase):
    # create a DH object and
    # set a fixed prvsecret instead of a random number
    def setUp(self):
        self.alice = DH(321, 2203)
        self.alice.prvsecret = 12
        self.bob = DH(321, 2203)
        self.bob.prvsecret = 19

    def test_gen_pubkey(self):
        self.assertEqual(self.alice.gen_pubkey(), 486)
        self.assertEqual(self.bob.gen_pubkey(), 1876)

    def test_gen_shared_secret(self):
        self.assertEqual(self.alice.gen_shared_secret(1876), 956)
        self.assertEqual(self.bob.gen_shared_secret(486), 956)

    def test_set_shared_secret(self):
        self.alice.set_shared_secret(1876)
        self.bob.set_shared_secret(486)
        self.assertEqual(self.alice.sharedsecret, self.bob.sharedsecret)

    def test_DH_init(self):
        self.assertRaises(ValueError, DH, 2, 2)
