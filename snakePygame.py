import pygame
import random
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, K_p


class yilan():

    def __init__(self):
        self.yX = [289, 289, 289, 289, 289]
        self.yY = [289, 269, 249, 229, 209]
        # yılan başlangıç yönü
        self.yonY = 0
        """
        yönler
        0 - Aşağı
        1 - Sağ
        2 - Yukarı
        3 - Sol
        """
        self.puan = 0
        # elmanın rastgele konumu
        self.yemPozisyonu = (random.randint(3, 588), random.randint(3, 588))
        pygame.init()
        # ekran boyutu
        self.ekran = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Yılan Oyunu')
        # elma kare boyutu
        self.yemSekli = pygame.Surface((10, 10))
        # elma rengi
        self.yemSekli.fill((0, 255, 0))
        # yilan kare boyutu
        self.yilanSekli = pygame.Surface((20, 20))
        # yılan rengi
        self.yilanSekli.fill((0, 0, 0))
        self.yaziTipi = pygame.font.SysFont('comicsansms', 20)
        # FPS saniyedki frame(kare) sayısı,hızı
        self.yilanHizi = pygame.time.Clock()

        self.enYuksekSkor(self.puan)
        self.duraklat = True

    def enYuksekSkor(self, p):
        try:
            with open("enYuksekSkor.txt", "r") as file:
                enY = int(file.readline())
            if(p > enY):
                with open("enYuksekSkor.txt", "w") as file:
                    file.write(str(p))
                return p
            else:
                return enY
        except FileNotFoundError as e:
            print(e)
            with open("enYuksekSkor.txt", "w") as file:
                file.write(str(p))
            # yılanın yanma durumunu kontrol eden fonksiyon

    def yemYilanKontrol(self, x1, x2, y1, y2, w1, w2, h1, h2):

        if x1+w1 > x2 and x1 < x2+w2 and y1+h1 > y2 and y1 < y2+h2:
            return True
        else:
            return False

    # yılan yandığında çalışan fonksiyon
    def yandiEkrani(self, ekran, puan):
        self.enYuksekSkor(puan)
        ekran.fill((0, 0, 0))
        restartButon = pygame.Rect(150, 250, 300, 80)
        rect = pygame.draw.rect(ekran, (30, 144, 255), restartButon)
        quitButon = pygame.Rect(150, 370, 300, 80)
        rect2 = pygame.draw.rect(ekran, (220, 20, 60), quitButon)

        yaziTipi = pygame.font.SysFont('comicsansms', 30)

        metin1 = yaziTipi.render('Skorunuz: '+str(puan), True, (255, 255, 255))
        enYS = yaziTipi.render(
            'En Yüksek Skor: '+str(self.enYuksekSkor(puan)), True, (255, 255, 255))
        metin2 = yaziTipi.render('Yeniden Oyna', True, (255, 255, 255))
        metin3 = yaziTipi.render('Çıkış', True, (255, 255, 255))

        ekran.blit(enYS, (150, 25))
        ekran.blit(metin1, (210, 80))
        ekran.blit(metin2, (200, 270))
        ekran.blit(metin3, (260, 390))

        pygame.display.update()
        # pygame.time.wait(20000)
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if(event.button == 1):
                        if(rect.collidepoint(event.pos)):
                            self.__init__()
                            self.game()
                            break

                        if(rect2.collidepoint(event.pos)):
                            pygame.quit()
                            sys.exit(0)

                elif(event.type == pygame.KEYDOWN):
                    if(event.key == K_SPACE):
                        self.__init__()
                        self.game()
                        break
                    elif(event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit(0)

                elif(event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit(0)

    def hareket(self, i):
        # yılanın hareketini sağlar
        while i >= 1:
            self.yX[i] = self.yX[i-1]
            self.yY[i] = self.yY[i-1]
            i -= 1

        # yılanın koordinatdaki hareketleri
        if self.yonY == 0:
            self.yY[0] += 20
        elif self.yonY == 1:
            self.yX[0] += 20
        elif self.yonY == 2:
            self.yY[0] -= 20
        elif self.yonY == 3:
            self.yX[0] -= 20

    def duraklatF(self, d, ekran):
        while(d is False):
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        d = True
                        self.duraklat = True
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)
                    elif event.type == QUIT:
                        pygame.quit()
                        sys.exit(0)
                    else:
                        while (d is not True):
                            # pygame.time.wait(10000)
                            # metin = self.yaziTipi.render("||", True, (0, 0, 0))
                            # ekran.blit(metin, (10, 400))
                            # pygame.display.update()
                            pass

    def game(self, hiz=11):

        kontrol = False
        while True:
            # FPS 10 HIZ
            if(self.puan % 10 == 0 and kontrol):
                kontrol = False
                hiz += 3
            elif(self.puan % 10 == 1):
                kontrol = True
            self.yilanHizi.tick(hiz)
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif e.type == KEYDOWN:
                    if e.key == K_UP and self.yonY != 0:  # tersi yöne gidemez!
                        self.yonY = 2
                    elif e.key == K_DOWN and self.yonY != 2:
                        self.yonY = 0
                    elif e.key == K_LEFT and self.yonY != 1:
                        self.yonY = 3
                    elif e.key == K_RIGHT and self.yonY != 3:
                        self.yonY = 1
                    elif e.key == K_p:
                        if(self.duraklat is False):
                            self.duraklat = True
                        else:
                            self.duraklat = False
                        self.duraklatF(self.duraklat, self.ekran)

                    elif e.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)

            i = len(self.yX)-1  # yılan boyutu
            # print("i:", i)
            # print("yX:", self.yX, "\nyY:", self.yY)

            # yılanın kendine çarpması
            while i >= 2:
                if self.yemYilanKontrol(self.yX[0], self.yX[i], self.yY[0], self.yY[i], 20, 20, 20, 20):
                    self.yandiEkrani(self.ekran, self.puan)
                i -= 1
                # print("while inside \nxs[i]:", xs[i], "\nys[i]:", ys[i])
                # print("while inside i:", i)

            # elmayı yemesi
            if self.yemYilanKontrol(self.yX[0], self.yemPozisyonu[0], self.yY[0], self.yemPozisyonu[1], 20, 10, 20, 10):
                self.puan += 1
                self.yX.append(700)  # yeni eklene kare
                self.yY.append(700)
                # yemin rengini rastgele değiştirme
                self.yemSekli.fill(
                    (random.randint(0, 220), random.randint(0, 225), random.randint(0, 230)))
                self.yemPozisyonu = (random.randint(3, 588), random.randint(3, 588))

            if self.yX[0] < 0 or self.yX[0] > 580 or self.yY[0] < 0 or self.yY[0] > 580:  # duvara çarpması
                self.yandiEkrani(self.ekran, self.puan)

            # hareket fonksiyonu
            i = len(self.yX)-1
            self.hareket(i)

            # arkaplan rengi
            self.ekran.fill((255, 255, 255))

            # yılanın ekrana çizdirilmesi
            for i in range(0, len(self.yX)):
                self.ekran.blit(self.yilanSekli, (self.yX[i], self.yY[i]))

            # elmanın ekrana çizdirilmesi
            self.ekran.blit(self.yemSekli, self.yemPozisyonu)

            # skorun canlı olarak yazdırılması
            metin = self.yaziTipi.render("P :"+str(self.puan)+" EYS :"+str(self.enYuksekSkor(self.puan)) +
                                         " Hız :"+str(hiz), True, (0, 0, 0))
            self.ekran.blit(metin, (10, 10))

            # ekranın güncellenmesi
            pygame.display.update()


def main():
    y = yilan()
    y.game()


if(__name__ == "__main__"):
    main()
