import ctypes
import pathlib
import time

AUDIO_DIR = pathlib.Path(__file__).parent / "audios"

winmm = ctypes.windll.winmm


def play(filename):
    path = str(AUDIO_DIR / filename)
    alias = "audio"
    winmm.mciSendStringW(f'open "{path}" type mpegvideo alias {alias}', None, 0, 0)
    winmm.mciSendStringW(f"play {alias} wait", None, 0, 0)
    winmm.mciSendStringW(f"close {alias}", None, 0, 0)


ORDINAIS = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]


def rezar_terco_mariano():
    play("inicio_santo_terco.mp3")
    play("Credo.mp3")
    play("Pai_Nosso.mp3")

    for _ in range(3):
        play("Ave_Maria.mp3")

    play("Glória_ao_Pai.mp3")
    time.sleep(0.5)

    for i in range(5):
        play(f"anuncio_{ORDINAIS[i]}_misterio.mp3")
        play("Pai_Nosso.mp3")

        for _ in range(10):
            play("Ave_Maria.mp3")

        play("Glória_ao_Pai.mp3")
        play("Jaculatórias.mp3")
        play("rogai_por_nos.mp3")

    play("salve_rainha.mp3")
    play("Ladainha de Nossa Senhora.mp3")
    play("Pai_Nosso.mp3")
    play("Ave_Maria.mp3")
    play("Glória_ao_Pai.mp3")
    play("fim_do_santo_terco.mp3")


if __name__ == "__main__":
    rezar_terco_mariano()
