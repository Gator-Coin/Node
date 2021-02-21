from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import PrivateFormat, Encoding
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey 
import cryptography.exceptions

class Key(Ed25519PrivateKey):

    def generate(self) -> Ed25519PrivateKey:
        """
        Generate an Ed25519 private key

        :returns: Ed25519PrivateKey
        """
        return super().generate()

    def from_private_bytes(self, data) -> Ed25519PrivateKey:
        """
        this is the method to create a key pair from a bytes object loaded form a file.

        :param data: a bytes like 32 bit private key

        :returns: Ed25519PrivateKey
        """
        return super().from_private_bytes(data)

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

if __name__=="__main__":
    # example of how to use this modual
    crypto = Crypto().generate()    # Generate a new key pair and assign that to the variable crypto
    signature = crypto.sign(b"Sign Here")       # Signs a byte string with the private key
    public_key = crypto.public_key()            # generate the public key object
    try:
        public_key.verify(signature, b"Sign Here")
    except cryptography.exceptions.InvalidKey as e:
        print(e)
    else:
        print("valid Key")

