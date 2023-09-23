import cv2
import numpy as np

class YananAlanTespit:
# Resmi yükle
 resim = cv2.imread('yanmisAlan_veri.jpg')

# HSV renk uzayına dönüştür
 hsv_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)

# Yeşil renk için eşikleme yapın (örnek olarak, yeşil için eşik değeri ayarlayın)
 lower_green = np.array([35, 100, 100])  # Düşük sınır
 upper_green = np.array([85, 255, 255])  # Yüksek sınır
 yeşil_alanlar = cv2.inRange(hsv_resim, lower_green, upper_green)

# Konturları bul
 contours, _ = cv2.findContours(yeşil_alanlar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Her yeşil alanı doldurun
 for contour in contours:
    cv2.drawContours(resim, [contour], -1, (0, 0, 255), thickness=cv2.FILLED)

# Alanları işaretleyin (örneğin, metinle)
 toplamAlan = 0
 for contour in contours:
    alan = cv2.contourArea(contour)
    x, y, _, _ = cv2.boundingRect(contour)
    toplamAlan += alan
    cv2.putText(resim, f"{alan:.2f}", (x, y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) 


   
 print("Kaybedilen Toplam Alan:", toplamAlan, "piksel")
 
 


# Sonucu görselleştir
 cv2.imwrite("isleme_sonrasi_resim.jpg", resim)
 cv2.waitKey(0)
 cv2.destroyAllWindows()


