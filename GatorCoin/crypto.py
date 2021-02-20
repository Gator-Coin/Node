from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import PrivateFormat, Encoding
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey

class Crypto(Ed25519PrivateKey):
    def __init__(self):
        """
        Creates key pait for a Ed25519 is an elliptic curve signing algorithm using EdDSA and Curve25519
        """
        super.__init__(self)

    def generate(self):
        """
        Generate an Ed25519 private key

        :returns: Ed25519PrivateKey
        """
        return super.generate(self)

    def from_private_bytes(data):
        """
        this is the method to create a key pair from a bytes object loaded form a file.

        :param data: a bytes like 32 bit private key

        :returns: Ed25519PrivateKey
        """

    def public_key(self) -> Ed25519PublicKey:
        """
        :returns: Ed25519PublicKey
        """
        return super().public_key()


    def sign(self, data: bytes) -> bytes:
        """
        :params data: a bytes primative to encypt
        :returns: a 64 byte signature
        """
        return super().sign(data)

    def private_bytes(self, encoding: Encoding.PEM, format: PrivateFormat.PKCS8, encryption_algorithm: EllipticCurvePrivateKey) -> bytes:
        """
        Allows serialization of the key to bytes. 
        :param encoding: A value form the Encoding Enum
        :param format: A value from the PrivateFormat Enum
        :param encryption_algorithm: An instance of an object conforming to the KeySerializationEncryption interface.

        :returns: Serialized Key
        """
        return super().private_bytes(encoding, format, encryption_algorithm)
