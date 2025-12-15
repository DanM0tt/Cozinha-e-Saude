from funcoes.hashing_algorithm import get_password_hash, verify_password_hash

def test_get_password_hash():
    senha = "123456"
    hash_senha = get_password_hash(senha)

    assert hash_senha != senha
    assert isinstance(hash_senha, str)
    assert len(hash_senha) > 0


def test_verify_password_hash_correct():
    senha = "minha_senha"
    hash_senha = get_password_hash(senha)

    assert verify_password_hash(senha, hash_senha) is True


def test_verify_password_hash_incorrect():
    senha = "minha_senha"
    hash_senha = get_password_hash(senha)

    assert verify_password_hash("outra_senha", hash_senha) is False
