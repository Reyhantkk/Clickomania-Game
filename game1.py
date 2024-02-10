import pygame
import random
import sys


pygame.init()


ekran_genisligi = 400
ekran_yuksekligi = 500
ekran = pygame.display.set_mode((ekran_genisligi, ekran_yuksekligi))


arkaplan_rengi = (255, 255, 255)
blok_renkleri = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]


blok_boyutu = 40
sutun_sayisi = ekran_genisligi // blok_boyutu
satir_sayisi = ekran_yuksekligi // blok_boyutu
bloklar = [[random.choice(blok_renkleri) for _ in range(sutun_sayisi)] for _ in range(satir_sayisi)]

def bloklari_ciz():
    for y in range(satir_sayisi):
        for x in range(sutun_sayisi):
            blok_rengi = bloklar[y][x]
            pygame.draw.rect(ekran, blok_rengi, (x*blok_boyutu, y*blok_boyutu, blok_boyutu, blok_boyutu))

def bloklari_kaldir(konum):
    
    x, y = konum
    secilen_renk = bloklar[y][x]
    
    
    kontrol_listesi = [(x, y)]
    kaldirilacaklar = []
    
    while kontrol_listesi:
        x, y = kontrol_listesi.pop()
        if (x, y) not in kaldirilacaklar:
            kaldirilacaklar.append((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < sutun_sayisi and 0 <= ny < satir_sayisi and bloklar[ny][nx] == secilen_renk:
                    kontrol_listesi.append((nx, ny))
    
    
    for x, y in kaldirilacaklar:
        bloklar[y][x] = arkaplan_rengi

    
    for x in range(sutun_sayisi):
        sütun = [bloklar[y][x] for y in range(satir_sayisi) if bloklar[y][x] != arkaplan_rengi]
        sütun = [arkaplan_rengi] * (satir_sayisi - len(sütun)) + sütun
        for y in range(satir_sayisi):
            bloklar[y][x] = sütun[y]

def oyunu_baslat():
    clock = pygame.time.Clock() 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                konum = pygame.mouse.get_pos()
                x = konum[0] // blok_boyutu
                y = konum[1] // blok_boyutu
                bloklari_kaldir((x, y))

        ekran.fill(arkaplan_rengi)
        bloklari_ciz()
        pygame.display.flip()

        clock.tick(60)  

oyunu_baslat()
