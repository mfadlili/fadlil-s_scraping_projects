import gempaterkini

if __name__ == '__main__':
    print("Melihat Gempa Terbaru di Indonesia")
    result = gempaterkini.ambil_data()
    gempaterkini.baca_hasil(result)