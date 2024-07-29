# test_qr_code_generator.py

from generate_qrcode import generate_qr_code
import os

def test_generate_qr_code():
    url = "https://www.example.com/"
    filename = "test_qrcode.png"

    # Gerar QR code
    generated_file = generate_qr_code(url, filename=filename)

    # Verificar se o arquivo foi criado
    assert os.path.exists(generated_file)

    # Limpar: remover o arquivo gerado após o teste
    os.remove(generated_file)