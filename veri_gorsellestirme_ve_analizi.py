#pip install pandas numpy matplotlib seaborn
import pandas as pd # Veri analizi için
import numpy as np # Sayısal işlemler için
import matplotlib.pyplot as plt # Grafik çizmek için
import seaborn as sns # Daha güzel grafikler için

#1. Veri Kümesi Oluşturma veya Yükleme

data = {
    "Ad" : ["Ali","Ayşe","Mehmet","Zeynep","Can"],
    "Yaş" : [24,23,22,12,26],
    "Maaş" : [5000, 7000, 8000, 10000, 3000]
}

df = pd.DataFrame(data) #datayı dataframe'e dönüştür
print(df)


#2. Veri Analizi

print(df.describe()) #sayısal özet istatistikleri
print(df.info()) #veri türleri hakkında bilgi

###ortalama yaş hesaplama
print("Ortalama yaş:", df["Yaş"].mean())

###en yüksek maaşı alan kişiyi hesaplama
print(df[df["Maaş"] == df["Maaş"].max()])


#3. Matplotlib ile Basit Grafik Çizme

plt.plot(df["Yaş"], df["Maaş"], marker="o", linestyle="--", color="r")
plt.xlabel("Yaş")
plt.ylabel("Maaş")
plt.title("Yaş ve Maaş İlişkisi")
plt.show()


#4. Seaborn ile Daha İyi Grafikler

sns.scatterplot(x="Yaş", y="Maaş", data=df)
plt.title("Yaş ve Maaş Dağılımı")
plt.show()

###histogram çizme
sns.histplot(df["Yaş"], bins=5, kde=True)
plt.title("Yaş Dağılımı")
plt.show()


#5. Korelasyon Analizi

df_numeric = df.select_dtypes(include=["number"]) # Sadece sayısal sütunları seç
corr = df_numeric.corr() # Korelasyon matrisini hesapla

#### Korelasyon ısı haritasını çiz
plt.figure(figsize=(6,4))  # Grafik boyutunu ayarla
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

plt.title("Korelasyon Matrisi")
plt.show()

























