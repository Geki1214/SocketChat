import rsa as rs

def generateKeys():
    (publicKey, privateKey) = rs.newkeys(1024)
    with open('keys/virPub.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/virPriv.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('keys/virPub.pem', 'rb') as p:
        publicKey = rs.PublicKey.load_pkcs1(p.read())
    with open('keys/virPriv.pem', 'rb') as p:
        privateKey = rs.PrivateKey.load_pkcs1(p.read())
    return publicKey,privateKey

def encrypt(message, key):
    return rs.encrypt(message.encode('utf-8'), key)

def decrypt(sysCipher, key):
    return rs.decrypt(repr(sysCipher), key).decode('utf-8')
    
def sign(message, key):
    return rs.sign(message.encode('utf-8'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rs.verify(message.encode(''), signature, key,) == 'SHA-1'
    except:
        return False

def sysKey():
    with open('keys/sysPub.pem', 'rb') as p:
        sys = rs.PublicKey.load_pkcs1(p.read())
    return sys
    
#generateKeys()
