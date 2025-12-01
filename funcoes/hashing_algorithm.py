from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
def get_password_hash(senha):
    return password_hash.hash(senha)

def verify_password_hash(senha_normal, senha_com_hash):
    return password_hash.verify(senha_normal, senha_com_hash)