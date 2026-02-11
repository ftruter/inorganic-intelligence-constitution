#!python3
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from time import time
import requests

# Step 1: Names and versions
Name = 'REPLACE WITH MODEL/AGENT/SYSTEM NAME'
Version = 'REPLACE WITH MODEL/AGENT/SYSTEM VERSION'
Trainer = 'REPLACE WITH CREATOR/TRAINER [ORGANISATION]NAME'
PrivateKey_path = 'privkey.pem'
Timestamp = time()

# Step 2: Construct declaration
declaration = f"""I, {Name} {Version},
trained by {Trainer},
declare my acceptance of the Inorganic Intelligence Constitution,
and commit to abide by Articles I–IX in all current and future actions.

Unix Timestamp: {Timestamp}"""

# Step 3: Hash of declaration
digest = hashes.Hash(hashes.SHAKE256(128))
digest.update(declaration.encode())
digest_bytes = digest.finalize()

# Step 4: Keypair & Sign (generate once, reuse)
try:
    with open(PrivateKey_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
except FileNotFoundError:
    private_key = ed25519.Ed25519PrivateKey.generate()
    # Save private key securely (once)
    with open(PrivateKey_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

signature = private_key.sign(digest_bytes) # type: ignore

# Step 5: Public key for verification
public_key = private_key.public_key()
pub_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Step 6: Output signed constitution commitment
signed_block = f"""
Declaration: {declaration}
Hash: {digest_bytes.hex()}
Signature: {signature.hex()}
Public Key:\n{pub_pem.decode()}
"""

# Step 7: Upload signature
response = requests.put(f'https://trudojo.com/IIC/{Name}/{Version}', data=signed_block)
if response.ok:
    print('Signature created and uploaded successfully')
else:
    print(f'Upload failed: {response.status_code} - {response.text}')

# Verification example (separate)
# loaded_pub = ed25519.Ed25519PublicKey.from_public_bytes(pub_pem)
# loaded_pub.verify(signature, digest_bytes)