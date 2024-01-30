import ast
import os
import time
import numpy as np
import joblib

def get_info(data, key):
    return data.get(key, "Bilgi bulunamadı.")

def read_input_file(file_path):
    with open(file_path, "r") as file:
        input_data = file.read()
    return ast.literal_eval(input_data)

def clear_input_file(file_path):
    with open(file_path, "w") as file:
        file.truncate(0)

def tahmin_yap(model, input_verileri):
    model = joblib.load(model)
    tahmin = model.predict(input_verileri)
    return tahmin

# Dosyaları açıp içeriklerini okuma
with open("il_avg_label.txt", "r") as file:
    il_avg_content = file.read()
with open("il_id_label.json", "r") as file:
    il_id_content = file.read()

with open("ilce_avg_label.txt", "r") as file:
    ilce_avg_content = file.read()
with open("ilce_id_label.json", "r") as file:
    ilce_id_content = file.read()

with open("mahalle_avg_label.txt", "r") as file:
    mahalle_avg_content = file.read()
with open("mahalle_id_label.json", "r") as file:
    mahalle_id_content = file.read()

with open("konut_tipi_id_label.json", "r") as file:
    konut_tipi_id_content = file.read()

with open("bulundugu_kat_id_label.json", "r") as file:
    bulundugu_kat_id_content = file.read()

with open("konut_kat_kombinasyon_id_label.json", "r") as file:
    konut_kat_kombinasyon_id_content = file.read()

# Dosya içeriğini bir sözlüğe çevirme (string olarak kaydedilmiş bir dict olduğu varsayılarak)
il_avg_dict = ast.literal_eval(il_avg_content)
il_id_dict = ast.literal_eval(il_id_content)
ilce_avg_dict = ast.literal_eval(ilce_avg_content)
ilce_id_dict = ast.literal_eval(ilce_id_content)
mahalle_avg_dict = ast.literal_eval(mahalle_avg_content)
mahalle_id_dict = ast.literal_eval(mahalle_id_content)
konut_tipi_id_dict = ast.literal_eval(konut_tipi_id_content)
bulundugu_kat_id_dict = ast.literal_eval(bulundugu_kat_id_content)
konut_kat_kombinasyon_id_dict = ast.literal_eval(konut_kat_kombinasyon_id_content)

# İlgili dosya adını ve yolunu güncelleyin
input_file_path = "input_verileri.txt"

while True:
    # Check if the input file has new data
    if os.path.exists(input_file_path) and os.path.getsize(input_file_path) > 0:
        input_veriler = read_input_file(input_file_path)

        # Kullanıcıdan il, ilçe ve mahalle isimlerini al
        il_input = input_veriler['il_input']
        ilce_input = input_veriler['ilce_input']
        mahalle_input = input_veriler['mahalle_input']
        konut_tipi_input = input_veriler['konut_tipi_input']
        bulundugu_kat_input = input_veriler['bulundugu_kat_input']

        # İlgili isimlerle sözlükten değerleri çekme
        il_id = il_id_dict.get(il_input, "Bilgi bulunamadı.")
        il_info = il_avg_dict.get(il_input, {})
        ilce_id = ilce_id_dict.get(ilce_input, "Bilgi bulunamadı.")
        ilce_info = ilce_avg_dict.get(ilce_input, {})
        mahalle_id = mahalle_id_dict.get(mahalle_input, "Bilgi bulunamadı.")
        mahalle_info = mahalle_avg_dict.get(mahalle_input, {})
        konut_tipi_id = konut_tipi_id_dict.get(konut_tipi_input, "Bilgi bulunamadı.")
        bulundugu_kat_id = bulundugu_kat_id_dict.get(bulundugu_kat_input, "Bilgi bulunamadı.")
        konut_kat_kombinasyon_id = konut_kat_kombinasyon_id_dict.get(konut_tipi_input + bulundugu_kat_input, "Bilgi bulunamadı.")

        # Model için uygun şablonu hazırlama
        Il = il_id
        Ilce = ilce_id
        Mahalle = mahalle_id
        Konut_Tipi = konut_tipi_id
        Bulundugu_Kat = bulundugu_kat_id
        Metrekare = input_veriler['Metrekare']
        metrekare_araligi = (
            0 if 0 < Metrekare <= 50 else
            5 if 50 < Metrekare <= 100 else
            1 if 100 < Metrekare <= 150 else
            2 if 150 < Metrekare <= 200 else
            3 if 200 < Metrekare <= 400 else
            4 if 400 < Metrekare <= 800 else
            6 if Metrekare > 800 else
            None)
        if metrekare_araligi is None:
            print("Metrekare Sıfır veya Negatif olamaz!")
            Metrekare = float(input("Metrekareyi Giriniz "))
        else:
            pass
        OdaSayisi = input_veriler['OdaSayisi']
        SalonSayisi = input_veriler['SalonSayisi']
        ToplamOdaSayisi = OdaSayisi + SalonSayisi
        Konut_Kat_Kombinasyonu = konut_kat_kombinasyon_id
        Il_Ortalama_Fiyat = il_info['Ortalama Fiyat']
        Il_Std_Fiyat = il_info['Std Fiyat']
        Ilce_Ortalama_Fiyat = ilce_info['Ortalama Fiyat']
        Ilce_Std_Fiyat = ilce_info['Std Fiyat']
        Mahalle_Ortalama_Fiyat = mahalle_info['Ortalama Fiyat']
        Mahalle_Std_Fiyat = mahalle_info['Std Fiyat']
        ToplamOdaSayisiMetrekareOrani = ToplamOdaSayisi / Metrekare
        SalonSayisiMetrekareOrani = SalonSayisi / Metrekare
        OdaSayisiMetrekareOrani = OdaSayisi / Metrekare

        # Kullanıcıdan alınan verileri bir sözlükte topla
        input_verileri = {
            'Il': Il,
            'Ilce': Ilce,
            'Mahalle': Mahalle,
            'Konut_Tipi': Konut_Tipi,
            'Bulundugu_Kat': Bulundugu_Kat,
            'Metrekare': Metrekare,
            'OdaSayisi': OdaSayisi,
            'SalonSayisi': SalonSayisi,
            'ToplamOdaSayisi': ToplamOdaSayisi,
            'Konut_Kat_Kombinasyonu': Konut_Kat_Kombinasyonu,
            'Metrekare_Araligi': metrekare_araligi,
            'Il_Ortalama_Fiyat': Il_Ortalama_Fiyat,
            'Il_Std_Fiyat': Il_Std_Fiyat,
            'Ilce_Ortalama_Fiyat': Ilce_Ortalama_Fiyat,
            'Ilce_Std_Fiyat': Ilce_Std_Fiyat,
            'Mahalle_Ortalama_Fiyat': Mahalle_Ortalama_Fiyat,
            'Mahalle_Std_Fiyat': Mahalle_Std_Fiyat,
            'ToplamOdaSayisiMetrekareOrani': ToplamOdaSayisiMetrekareOrani,
            'SalonSayisiMetrekareOrani' : SalonSayisiMetrekareOrani,
        }

        # Modelinizi yükleyip tahmin yapın
        model_tahmini = tahmin_yap('gradient_boosting_model_2.pkl', [list(input_verileri.values())])

        # Tahmin sonucunu yazdırın
        print("Tahmin Edilen Fiyat: ", 1000000 * model_tahmini[0])

        # Yeni bir dosya oluşturun ve tahmin edilen fiyatı bu dosyaya yazın
        output_file_path = "predicted_price.txt"
        with open(output_file_path, "w") as output_file:
            output_file.write(str(model_tahmini))

        print(f"Tahmin Edilen Fiyat, '{output_file_path}' dosyasına yazıldı.")

        # Dosyanın içeriğini temizle
        clear_input_file(input_file_path)

    # Pause for a moment before checking again
    time.sleep(1)

    # Check if the user wants to exit the loop
    stop_signal = input("Enter '0' to stop, or press Enter to continue: ")
    if stop_signal == "0":
        break
    else :
        pass
