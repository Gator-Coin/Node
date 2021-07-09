from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import BestAvailableEncryption, PrivateFormat, Encoding, PublicFormat, NoEncryption, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey 
import cryptography.exceptions

class Key_Ring(object):

    def private_key(self) -> Ed25519PrivateKey:
        """
        :returns: Ed25519PrivateKey
        """
        return self.secret

    def public_key(self) -> Ed25519PublicKey:
        """
        :returns: Ed25519PublicKey
        """
        return self.private_key().public_key()

    def generate(self) -> None:
        """
        Generate an Ed25519 private key

        :returns: Ed25519PrivateKey
        """
        self.secret = Ed25519PrivateKey.generate()


    def load_key(self, data) -> None:
        """
        this is the method to create a key pair from a bytes object loaded form a file.

        :param data: a bytes like 32 bit private key

        :returns: Ed25519PrivateKey
        
        """
        
        self.secret = load_pem_private_key(data, password=None)

    def sign(self, data: bytes) -> bytes:
        """
        :params data: a bytes primative to encypt
        :returns: a 64 byte signature
        """

        return self.private_key().sign(data)

    def private_bytes(self) -> bytes:
        """
        serializes the private key to bytes 

        :returns: Serialized Key
        """

        private_bytes = self.private_key().private_bytes(
            encoding=Encoding.PEM, 
            format=PrivateFormat.PKCS8, 
            encryption_algorithm=NoEncryption()
        )

        if private_bytes == None:
            raise Exception()
        return private_bytes
    
    def public_bytes(self) -> bytes:
        """
        serializes the public key to bytes

        :returns: Serialized Key
        """
        return self.public_key().public_bytes(
            encoding=Encoding.Raw,
            format=PublicFormat.Raw
        )

    def verify(self, signature, data) -> None:
        """
        Allows serialization of the key to bytes. 
        :param signature: The signature to verify
        :param data: the data to verify

        :raises cryptography.exceptions.InvalidSignature: Raised when the signature cannot be verified.
        """
        self.public_key().verify(signature, data)


if __name__=="__main__":
    # example of how to use this modual
    key = Key_Ring()
    key.generate()
    signature = key.sign(b"Sign Here")


    # how to verify a signature
    try:
        key.verify(signature, b"Sign Here")

    except cryptography.exceptions.InvalidKey as e:
        print(e)
    else:
        print("valid Key")

    # how to print the key
    print("==================================")
    print(key.private_bytes().decode("utf8"))
    print(key.public_bytes().decode("utf8"))
    print("==================================")
    # how to load a key
    saved_key = key.private_bytes()
    key2 = Key_Ring()
    key2.load_key(saved_key)
    print(key2.private_bytes().decode("utf8"))