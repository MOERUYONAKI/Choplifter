# Choplifter

## I - Gereksinimler

**Python 3** veya daha yeni bir sürüm
> Kütüphane "**Pygame 2.5.0**"  
> Paket "**PyInstaller 6.7.0**"  
  
## II - CHPrompt Komutları

**1 - /clear**  
> CHPrompt'u temizler  
  
**2 - /exit**  
> CHPrompt'u kapatır  
  
**3 - /help**  
> Komut listesini gösterir 
  
**4 - /play** *[ -f ]* *[ -s ]*  
> Choplifter'ı başlatır  
> [ -f ] - Tam ekran modu *(deneysel)*  
> [ -s ] - Hayatta kalma modu 
  
**5 - /repo**  
> Repository bağlantısını döndürür  
  
## III - Oyun  
  
### Tanıtım
  
> *Choplifter* oyunu, bir helikopterle rehineleri kurtarma simülasyonudur. Oyuncu, düşmanlardan kaçınmalı ve mümkün olduğunca çok rehine kurtarmalıdır. Bu oyun için Python ve Pygame kütüphanesi gereklidir.  
  
### Oyun Mantığı
  
> **Başlatma**: Oyun penceresinin yapılandırılması, resimlerin yüklenmesi ve oyun değişkenlerinin başlatılması.  
> **Ana Döngü**: Oyuncu girişlerinin yönetilmesi, oyun durumunun güncellenmesi ve grafiklerin çizilmesi.  
> **Çarpışma Yönetimi**: Helikopter, düşmanlar, rehineler ve mermiler arasındaki çarpışmaları algılamak ve etkileşimleri yönetmek.  
> **Rehine Kurtarma**: Helikopterin rehineleri kurtarmak için yaklaşması gerekir. Rehineler, helikopter yerdeyken ona doğru hareket eder.  
> **Oyunun Sonu**: Tüm rehineler kurtarıldığında veya helikopter yok edildiğinde oyun biter.  
  
### Oyun Elemanları
  
> **Helikopter**: Oyuncunun aracı. Tüm yönlere hareket edebilir ve mermi atabilir.  
> **Düşmanlar**: Tanklar, jetler ve helikopteri yok etmeye çalışan uzaylılar.  
> **Rehineler**: Kurtarılacak siviller. Helikopter indiğinde ona doğru hareket ederler.  
> **Üs**: Rehinelerin başlangıçta bulunduğu yapılar.  
> **Mermiler**: Helikopter tarafından düşmanları yok etmek için ateşlenir.  
  
### Oyunun Sonu
  
> Oyun, tüm rehinelerin kurtarılması veya helikopterin yok edilmesiyle sona erer. Son puan, kurtarılan rehine sayısı ve yok edilen düşman sayısına dayanarak ekranda gösterilir.  
  
## IV - Geliştiriciler
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  