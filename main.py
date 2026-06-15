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
    print("Início do Santo Terço")
    play("inicio_santo_terco.mp3")
    
    print("Credo")
    play("Credo.mp3")
    
    print("Pai Nosso")
    play("Pai_Nosso.mp3")

    print("Três Ave Marias")
    for i in range(1, 4):
        print(f" - Ave Maria {i}/3")
        play("Ave_Maria.mp3")

    print("Glória ao Pai")
    play("Glória_ao_Pai.mp3")
    time.sleep(0.5)

    for i in range(5):
        print(f"\n--- {ORDINAIS[i].capitalize()} Mistério ---")
        print(f"Anúncio do {ORDINAIS[i]} mistério")
        play(f"anuncio_{ORDINAIS[i]}_misterio.mp3")
        
        print("Pai Nosso")
        play("Pai_Nosso.mp3")

        print("Dez Ave Marias")
        for j in range(1, 11):
            print(f" - Ave Maria {j}/10")
            play("Ave_Maria.mp3")

        print("Glória ao Pai")
        play("Glória_ao_Pai.mp3")
        
        print("Jaculatórias")
        play("Jaculatórias.mp3")
        
        print("Rogai por nós")
        play("rogai_por_nos.mp3")

    print("\n--- Encerramento ---")
    print("Salve Rainha")
    play("salve_rainha.mp3")
    
    print("Ladainha de Nossa Senhora")
    play("Ladainha de Nossa Senhora.mp3")
    
    print("Pai Nosso")
    play("Pai_Nosso.mp3")
    
    print("Ave Maria")
    play("Ave_Maria.mp3")
    
    print("Glória ao Pai")
    play("Glória_ao_Pai.mp3")
    
    print("Fim do Santo Terço")
    play("fim_do_santo_terco.mp3")


if __name__ == "__main__":
    rezar_terco_mariano()
