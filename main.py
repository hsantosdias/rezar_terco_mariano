import ctypes
import pathlib
import time
import datetime

AUDIO_DIR = pathlib.Path(__file__).parent / "audios"
MISTERIOS_DIR = pathlib.Path(__file__).parent / "Misterios"

winmm = ctypes.windll.winmm


def play(filename):
    path = AUDIO_DIR / filename
    if not path.exists():
        return
    path_str = str(path)
    alias = "audio"
    winmm.mciSendStringW(f'open "{path_str}" type mpegvideo alias {alias}', None, 0, 0)
    
    try:
        winmm.mciSendStringW(f"play {alias}", None, 0, 0)
        while True:
            status_buffer = ctypes.create_unicode_buffer(256)
            winmm.mciSendStringW(f"status {alias} mode", status_buffer, 256, 0)
            if status_buffer.value != "playing":
                break
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(" [Áudio pulado]")
        time.sleep(0.2) # Evita que um mesmo Ctrl+C pule vários áudios de uma vez
    finally:
        winmm.mciSendStringW(f"close {alias}", None, 0, 0)


ORDINAIS = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]


def obter_tipo_misterio():
    dia = datetime.datetime.today().weekday()
    if dia in [0, 5]: # Segunda, Sábado
        return "Gozosos"
    elif dia in [1, 4]: # Terça, Sexta
        return "Dolorosos"
    elif dia in [2, 6]: # Quarta, Domingo
        return "Gloriosos"
    elif dia == 3: # Quinta
        return "Luminosos"
    return "Gloriosos"


def extrair_anuncios(tipo_misterio):
    arquivo = MISTERIOS_DIR / f"{tipo_misterio}.txt"
    anuncios = []
    if not arquivo.exists():
        for i in range(5):
            anuncios.append(f"Anúncio do {ORDINAIS[i]} mistério {tipo_misterio.lower()}")
        return anuncios
        
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
    for i in range(5):
        prefixo = f"No {ORDINAIS[i].capitalize()}"
        encontrado = False
        for linha in linhas:
            if linha.strip().startswith(prefixo):
                anuncios.append(linha.strip())
                encontrado = True
                break
        if not encontrado:
            anuncios.append(f"Anúncio do {ORDINAIS[i]} mistério {tipo_misterio.lower()}")
            
    return anuncios


def extrair_oferecimento(tipo_misterio):
    arquivo = MISTERIOS_DIR / f"{tipo_misterio}.txt"
    oferecimento = "Oferecimento do Terço"
    if not arquivo.exists():
        return oferecimento
        
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    capturando = False
    texto_oferecimento = []
    for linha in linhas:
        l_strip = linha.strip()
        if l_strip.startswith("Creio..."):
            break
        if capturando and l_strip:
            texto_oferecimento.append(l_strip)
        if l_strip.startswith("Oferecimento:"):
            capturando = True
            
    if texto_oferecimento:
        return " ".join(texto_oferecimento)
    return oferecimento


def rezar_terco_mariano():
    tipo_misterio = obter_tipo_misterio()
    anuncios = extrair_anuncios(tipo_misterio)
    texto_oferecimento = extrair_oferecimento(tipo_misterio)

    print("Início do Santo Terço")
    play("inicio_santo_terco.mp3")
    
    print("\n--- Oferecimento ---")
    print(texto_oferecimento)
    play("Oferecimento do Terço.mp3")
    
    print("\nCredo")
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
        print(f"\n--- {ORDINAIS[i].capitalize()} Mistério ({tipo_misterio}) ---")
        print(anuncios[i])
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
