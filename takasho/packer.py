import base64
import hashlib
import hmac
import secrets
import zlib
from typing import Tuple


class Cipher:
    """This is the symmetric block cipher class used by Takasho (player API) for
    custom encryption/decryption.
    """

    def __init__(self, key: bytes, nonce: bytes):
        """Initialize the block cipher with the supplied key and nonce.

        Args:
            key: 32 bytes long.
            nonce: 12 bytes long.
        """
        self._state = [0] * 16
        for i in range(4):
            self._state[i] = int.from_bytes(
                self._sigma[4*i : 4*(i+1)], 'little')
        for i in range(8):
            self._state[i + 4] = int.from_bytes(key[4*i : 4*(i+1)], 'little')
        for i in range(3):
            self._state[i + 13] = int.from_bytes(nonce[4*i : 4*(i+1)], 'little')
        u = (((self._state[9] + self._state[4]) ^ self._state[11])
             + ((self._state[14] + self._state[13]) ^ self._state[15]))
        self._round_gap = self._round_gaps[
            ((u >> 7) & 2) | ((u >> 2) & 1) | ((u >> 13) & 4) | ((u >> 2) & 8)]
    
    def transform(self, body: bytes, counter: int = 0) -> bytes:
        """Encrypt/Decrypt the body and return the result.

        Args:
            body: Data to be encrypted/decrypted.
            counter: Optional state initialization for the block cipher.
        Returns:
            The resulting data after encryption/decryption.
        """
        def _int32(value: int):
            """Truncate a python int into a 32-bit unsigned int."""
            return value & 0xffffffff
        
        def _rotate_right(value: int, n_bits: int):
            """Perform a bitwise rotate right on a 32-bit unsigned int."""
            return _int32((value >> n_bits) | (value << (32 - n_bits)))
        
        result = bytearray()
        length = len(body)
        body_offset = 0
        while length > 0:
            l = length if length < 0x40 else 0x40
            state = self._state.copy()
            state[12] = counter
            rounds = 10 - self._round_gap
            if self._round_gap < 10:
                rounds = rounds if rounds > 1 else 1
                for i in range(rounds):
                    state[0] = _int32(state[0] + state[4])
                    state[12] = _rotate_right(state[12] ^ state[0], 0x10)
                    state[8] = _int32(state[8] + state[12])
                    state[4] = _rotate_right(state[4] ^ state[8], 0x14)
                    state[0] = _int32(state[0] + state[4])
                    state[12] = _rotate_right(state[12] ^ state[0], 0x18)
                    state[8] = _int32(state[8] + state[12])
                    state[4] = _rotate_right(state[4] ^ state[8], 0x19)
                    state[1] = _int32(state[1] + state[5])
                    state[13] = _rotate_right(state[13] ^ state[1], 0x10)
                    state[9] = _int32(state[9] + state[13])
                    state[5] = _rotate_right(state[5] ^ state[9], 0x14)
                    state[1] = _int32(state[1] + state[5])
                    state[13] = _rotate_right(state[13] ^ state[1], 0x18)
                    state[9] = _int32(state[9] + state[13])
                    state[5] = _rotate_right(state[5] ^ state[9], 0x19)
                    state[2] = _int32(state[2] + state[6])
                    state[14] = _rotate_right(state[14] ^ state[2], 0x10)
                    state[10] = _int32(state[10] + state[14])
                    state[6] = _rotate_right(state[6] ^ state[10], 0x14)
                    state[2] = _int32(state[2] + state[6])
                    state[14] = _rotate_right(state[14] ^ state[2], 0x18)
                    state[10] = _int32(state[10] + state[14])
                    state[6] = _rotate_right(state[6] ^ state[10], 0x19)
                    state[3] = _int32(state[3] + state[7])
                    state[15] = _rotate_right(state[15] ^ state[3], 0x10)
                    state[11] = _int32(state[11] + state[15])
                    state[7] = _rotate_right(state[7] ^ state[11], 0x14)
                    state[3] = _int32(state[3] + state[7])
                    state[15] = _rotate_right(state[15] ^ state[3], 0x18)
                    state[11] = _int32(state[11] + state[15])
                    state[7] = _rotate_right(state[7] ^ state[11], 0x19)
                    state[0] = _int32(state[0] + state[5])
                    state[15] = _rotate_right(state[15] ^ state[0], 0x10)
                    state[10] = _int32(state[10] + state[15])
                    state[5] = _rotate_right(state[5] ^ state[10], 0x14)
                    state[0] = _int32(state[0] + state[5])
                    state[15] = _rotate_right(state[15] ^ state[0], 0x18)
                    state[10] = _int32(state[10] + state[15])
                    state[5] = _rotate_right(state[5] ^ state[10], 0x19)
                    state[1] = _int32(state[1] + state[6])
                    state[12] = _rotate_right(state[12] ^ state[1], 0x10)
                    state[11] = _int32(state[11] + state[12])
                    state[6] = _rotate_right(state[6] ^ state[11], 0x14)
                    state[1] = _int32(state[1] + state[6])
                    state[12] = _rotate_right(state[12] ^ state[1], 0x18)
                    state[11] = _int32(state[11] + state[12])
                    state[6] = _rotate_right(state[6] ^ state[11], 0x19)
                    state[2] = _int32(state[2] + state[7])
                    state[13] = _rotate_right(state[13] ^ state[2], 0x10)
                    state[8] = _int32(state[8] + state[13])
                    state[7] = _rotate_right(state[7] ^ state[8], 0x14)
                    state[2] = _int32(state[2] + state[7])
                    state[13] = _rotate_right(state[13] ^ state[2], 0x18)
                    state[8] = _int32(state[8] + state[13])
                    state[7] = _rotate_right(state[7] ^ state[8], 0x19)
                    state[3] = _int32(state[3] + state[4])
                    state[14] = _rotate_right(state[14] ^ state[3], 0x10)
                    state[9] = _int32(state[9] + state[14])
                    state[4] = _rotate_right(state[4] ^ state[9], 0x14)
                    state[3] = _int32(state[3] + state[4])
                    state[14] = _rotate_right(state[14] ^ state[3], 0x18)
                    state[9] = _int32(state[9] + state[14])
                    state[4] = _rotate_right(state[4] ^ state[9], 0x19)
            for i in range(16):
                state[i] = _int32(state[i] + self._state[i])
            state[12] = _int32(state[12] + counter)
            for i in range(l):
                result.append(body[body_offset + i]
                              ^ state[i // 4].to_bytes(4, 'little')[i % 4])
            length -= l
            body_offset += l
            counter += 1
        return bytes(result)
    
    _sigma = b'zG]RTQVC{zkpV]/T'
    _round_gaps = [1, 3, 4, 1, 1, 3, 3, 2, 4, 3, 2, 2, 1, 4, 4, 2]


class Packer:
    """This is the packer/unpacker class used by Takasho (player API) to
    pack (deflate and encrypt) serialized gRPC data before transmission, and
    unpack (decrypt and inflate) received gRPC data before deserialization.
    """

    def __init__(self, key: bytes):
        """Initialize the packer class.
        
        Args:
            key: Used as the key for the symmetric block cipher.
        """
        self._nonce_buffer = self._NonceBuffer()
        self._key_buffer = bytearray(key)
    
    def compute_hash(self, nonce: bytes, body: bytes) -> bytes:
        """Compute hash for the supplied nonce and body.
        
        Args:
            nonce: Used as part of the key for the hash algorithm.
            body: Data to be hashed.
        Returns:
            The computed hash value.
        """
        key = self._key_buffer + bytearray(nonce)
        h = hmac.new(key, body, hashlib.sha256)
        return h.digest()
    
    def unpack(self, encrypted: bytes) -> bytes:
        """Unpack (decrypt and inflate) the supplied data.
        
        Args:
            encrypted: Encrypted data to be decrypted and inflated.
        Returns:
            The resulting data after decryption and inflate.
        """
        self._nonce_buffer.parse(encrypted)
        cipher = Cipher(self._key_buffer, self._nonce_buffer.buffer)
        decrypted = cipher.transform(encrypted[12:])
        body, header = self._inflate(decrypted)
        hash = self.compute_hash(self._nonce_buffer.buffer, body)
        if hash != header:
            raise RuntimeError('Invalid MAC code detected.')
        return body
    
    def pack(self, body: bytes) -> bytes:
        """Pack (deflate and encrypt) the supplied data using a random nonce.
        
        Args:
            body: Data to be deflated and encrypted.
        Returns:
            The resulting data after deflate and encryption.
        """
        self._nonce_buffer.refresh()
        return self.pack_with_nonce(self._nonce_buffer.buffer, body)
    
    def pack_with_nonce(self, nonce: bytes, body: bytes) -> bytes:
        """Pack (deflate and encrypt) the supplied data using the suppiled
        nonce.
        
        Args:
            nonce: Nonce used for the symmetric block cipher and hash
                computation.
            body: Data to be deflated and encrypted.
        Returns:
            The resulting data after deflate and encryption.
        """
        result = bytearray(nonce)
        hash = self.compute_hash(nonce, body)
        deflated = self._deflate(body, hash)
        cipher = Cipher(self._key_buffer, nonce)
        result += bytearray(cipher.transform(deflated))
        return bytes(result)
    

    class _NonceBuffer:
        """This is the nonce buffer class used by the packer class to manage
        nonce creation."""
        
        def __init__(self):
            """Initialize an empty 12-byte-long nonce."""
            self.buffer = bytearray(12)
        
        def refresh(self):
            """Generate a random 12-byte-long nonce."""
            self.buffer = bytearray(secrets.token_bytes(12))
        
        def parse(self, array: bytearray):
            """Use the first 12 bytes of the supplied bytearray as nonce."""
            self.buffer = bytearray(array)[:12].copy()
    

    def _deflate(
            self, body: bytes, content_header: bytes,
            result_header: bytes = None) -> bytes:
        """Deflate the supplied data.
        
        Args:
            body: The main body to be deflated.
            content_header: The header to be deflated (placed in front of body
                before deflate).
            result_header: The header placed as-is in front of the result (not
                deflated).
        Returns:
            The resulting data after deflate.
        """
        result = bytearray(result_header) if result_header else bytearray()
        content = bytearray(content_header) + bytearray(body)
        result += bytearray(zlib.compress(content)[2:-4])
        return bytes(result)
    
    def _inflate(self, body: bytes) -> Tuple[bytes, bytes]:
        """Inflate the supplied data.
        
        Args:
            body: The data to be inflated.
        Returns:
            A tuple with two elements.
            The first element is the inflated main body (without header).
            The second element is the inflated header.
        """
        decompressor = zlib.decompressobj(-zlib.MAX_WBITS)
        content = decompressor.decompress(body)
        header = content[:0x20]
        body = content[0x20:]
        return body, header


packer = Packer(b'ZA1Cu0eZosC3o8YTFuGjloxRkCg6ugVv')


if __name__ == '__main__':
    # Test case for Cipher
    key = bytes([
        0x7c, 0xf8, 0xb8, 0xbe, 0xf6, 0x61, 0x1a, 0xc7,
        0x03, 0x05, 0x18, 0xe8, 0xf1, 0x06, 0xd7, 0xa1,
        0x26, 0x54, 0x9b, 0x5b, 0x91, 0x41, 0xe3, 0x19,
        0xff, 0xf2, 0xbf, 0x24, 0xc8, 0xb3, 0x64, 0x42
    ])
    nonce = bytes([
        0x7a, 0x44, 0x92, 0x5c, 0x2f, 0xc6, 0x13, 0x83,
        0x2c, 0xdf, 0xf4, 0x5e
    ])
    cipher = Cipher(key, nonce)
    assert base64.b64encode(cipher.transform(bytes([
        0xce, 0x01, 0xb3, 0xe9, 0x71, 0x9f, 0x82, 0xcb,
        0x96, 0x5e, 0xdb, 0xeb, 0x49, 0xa4, 0x10, 0x0e,
        0xa3, 0x71, 0x58, 0x8a, 0x84, 0x8d, 0x48, 0xf0,
        0xd9, 0x9c, 0x13, 0x61, 0x6c, 0xbe, 0x54, 0x8d
        ]))) == b'm4hXJUSxgBtI/hLhNtkOXBZqca7NdcDTiDunnA+JJa4='
    # Test cases for Packer
    proto_hex = ('0a0f4f444d47656e657269635f426f6f740a154f444d47656e657269635f5'
        + '36563757265486173680a144f444d47656e657269635f5369676e6174757265')
    assert bytes.hex(packer.unpack(bytes.fromhex(
        '87deaf4ba0958a38dab01da2ee358fac144b45e3cccdf195dabd38a4ec9429a621f559'
        + '71b9e48fc3fa850ee1b8f467a8cbc4a1c32287ed20dc32682b1f6d17587390e657d0'
        + 'a7fa91c5e0a6e1cc1169e9961d51a6aef3a19aca873f80'
        ))) == proto_hex
    assert bytes.hex(packer.unpack(packer.pack(bytes.fromhex(proto_hex)))
        ) == proto_hex

