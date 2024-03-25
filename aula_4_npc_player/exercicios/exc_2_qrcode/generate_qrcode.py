# https://github.com/Python-World/python-mini-projects/tree/master/projects/Qr_code_generator
# run python3 generate_qrcode.py

# qr_code_generator.py

import qrcode

def generate_qr_code(url, filename="url_qrcode.png", fill_color="red", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    return filename  # Retornando o nome do arquivo para facilitar a verificação no teste

if __name__ == "__main__":
    input_URL = "https://www.google.com/"
    generate_qr_code(input_URL)