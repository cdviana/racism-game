pip install qrcode[pil]

import os
import re
from typing import Iterable, Tuple
import qrcode
from qrcode.constants import ERROR_CORRECT_M

SAFE_NAME = re.compile(r'[^A-Za-z0-9._-]')

def sanitize_filename(name: str) -> str:
    """Mantém apenas letras, números, ponto, _ e -, trocando o resto por _."""
    cleaned = SAFE_NAME.sub('_', name.strip())
    return cleaned or "qr"

def make_qr(data: str, box_size: int = 10, border: int = 4):
    """
    Cria um objeto PIL com o QR Code.
    - ERROR_CORRECT_M: aguenta ~15% de dano
    - box_size: tamanho de cada “quadradinho” (pixels)
    - border: margem (módulos) ao redor do QR
    """
    qr = qrcode.QRCode(
        version=None,  # ajusta automaticamente
        error_correction=ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def generate_qrs(items: Iterable[Tuple[str, str]], out_dir: str = "qrs",
                 box_size: int = 10, border: int = 4, suffix: str = ".png"):
    """
    Gera QR codes para cada (id, url) em 'items'.
    Salva como <out_dir>/<id><suffix>.
    """
    os.makedirs(out_dir, exist_ok=True)
    for item_id, url in items:
        fname = sanitize_filename(str(item_id)) + suffix
        path = os.path.join(out_dir, fname)

        img = make_qr(url, box_size=box_size, border=border)
        img.save(path)
        print(f"✔️  salvo: {path}")

if __name__ == "__main__":
    #Lista embutida com o link de todos os marcos
    pares = [
        ("NA", "https://cdviana.github.io/racism-game/?s=NA"),
        ("NB", "https://cdviana.github.io/racism-game/?s=NB"),
        ("NC", "https://cdviana.github.io/racism-game/?s=NC"),
        ("ND", "https://cdviana.github.io/racism-game/?s=ND"),
        ("LA", "https://cdviana.github.io/racism-game/?s=LA"),
        ("LB", "https://cdviana.github.io/racism-game/?s=LB"),
        ("LC", "https://cdviana.github.io/racism-game/?s=LC"),
        ("LD", "https://cdviana.github.io/racism-game/?s=LD"),
        ("CA", "https://cdviana.github.io/racism-game/?s=CA"),
        ("CC", "https://cdviana.github.io/racism-game/?s=CC"),
        ("CD", "https://cdviana.github.io/racism-game/?s=CD"),
        ("OA", "https://cdviana.github.io/racism-game/?s=OA"),
        ("OB", "https://cdviana.github.io/racism-game/?s=OB"),
        ("OC", "https://cdviana.github.io/racism-game/?s=OC"),
        ("OD", "https://cdviana.github.io/racism-game/?s=OD"),
        ("SA", "https://cdviana.github.io/racism-game/?s=SA"),
        ("SB", "https://cdviana.github.io/racism-game/?s=SB"),
        ("SC", "https://cdviana.github.io/racism-game/?s=SC"),
        ("SD", "https://cdviana.github.io/racism-game/?s=SD"),
        ("CB", "https://cdviana.github.io/racism-game/map.html?r=volta-negra-centro"),
    ]

    # Gera os PNGs em ./qrs (mude box_size/border se quiser)
    generate_qrs(pares, out_dir="qrs", box_size=10, border=4)
