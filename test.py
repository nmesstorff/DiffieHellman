#!/usr/bin/env python
"""
example diffie-hellman keyexchange

for more information about DH see:
http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
"""
from DH import DH

PRIMITIVE_ROOT = 42
PRIME = 44318

ALICE = DH(PRIMITIVE_ROOT, PRIME)
print "ALICE: g=%i, p=%i" % (ALICE.in_g, ALICE.in_p)
print "ALICE: secret: %i" % ALICE.prvsecret
print "ALICE: pubkey: %s\n" % ALICE.gen_pubkey()

BOB = DH(PRIMITIVE_ROOT, PRIME)
print "BOB: g=%i, p=%i" % (BOB.in_g, BOB.in_p)
print "BOB: secret: %i" % BOB.prvsecret
print "BOB: pubkey: %s\n" % BOB.gen_pubkey()

print "keyexchange..."
ALICE.set_shared_secret(BOB.gen_pubkey())
BOB.set_shared_secret(ALICE.gen_pubkey())

print "ALICE shared: %s" % ALICE.sharedsecret
print "BOB shared: %s" % BOB.sharedsecret
