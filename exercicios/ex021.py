from playsound3 import playsound

sound = playsound("C:/Users/BRAVO/Documents/Estudos/python/[004] Kerosene [(Crystal Castles official)].m4a")
if sound.is_alive():
    print("Sound is still playing!")