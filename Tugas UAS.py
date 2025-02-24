import heapq

print("+"*22)
print("Perkiraan a star dalam game iggle pop")
print("+"*22)
print("M = Musuh")
print("P = Pemain")
print(". = Jalan")
print("* = Perkiraan Jalur musuh")
print("+"*22)
print("\n")

# Fungsi menampilkan peta
def print_peta(peta, posisi_pemain, posisi_musuh, jalur):
    for i in range(len(peta)):
        row = []
        for j in range(len(peta[i])):
            if (i, j) == posisi_pemain:
                row.append('P')  # P untuk pemain
            elif (i, j) == posisi_musuh:
                row.append('M')  # M untuk musuh
            elif (i, j) in jalur:
                row.append('*')  # Menandai jalur dengan tanda *
            elif peta[i][j] == 1:
                row.append('#')  # Menandai rintangan dengan tanda #
            else:
                row.append('.')  # Menandai jalur kosong dengan titik
        print(" ".join(row))
    print()

# Fungsi A* mencari jalur terpendek
def a_star(peta, mulai, tujuan):
    h = lambda p: abs(p[0] - tujuan[0]) + abs(p[1] - tujuan[1])
    antrian, asal, biaya = [(h(mulai), mulai)], {}, {mulai: 0}
    
    while antrian:
        _, sekarang = heapq.heappop(antrian)
        if sekarang == tujuan:
            jalur = []
            while sekarang in asal:
                jalur.append(sekarang)
                sekarang = asal[sekarang]
            return [mulai] + jalur[::-1]
        
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = sekarang[0] + dx, sekarang[1] + dy
            if 0 <= x < len(peta) and 0 <= y < len(peta[0]) and peta[x][y] != 1:
                if (x, y) not in biaya or biaya[sekarang] + 1 < biaya[(x, y)]:
                    asal[(x, y)] = sekarang
                    biaya[(x, y)] = biaya[sekarang] + 1
                    heapq.heappush(antrian, (biaya[(x, y)] + h((x, y)), (x, y)))
    
    return None

# Fungsi untuk menggerakkan pemain
def gerak_player(peta, posisi_pemain):
    print("Gerakan pemain: W (atas), A (kiri), S (bawah), D (kanan), O (keluar)")
    gerakan = input("Masukkan gerakan (W/A/S/D/O): ").upper()

    if gerakan == "O":  # Menekan O untuk keluar game
        return "keluar"
    
    x, y = posisi_pemain

    if gerakan == "W" and x > 0 and peta[x-1][y] != 1:  # Gerak atas
        return (x-1, y)
    elif gerakan == "S" and x < len(peta) - 1 and peta[x+1][y] != 1:  # Gerak bawah
        return (x+1, y)
    elif gerakan == "A" and y > 0 and peta[x][y-1] != 1:  # Gerak kiri
        return (x, y-1)
    elif gerakan == "D" and y < len(peta[0]) - 1 and peta[x][y+1] != 1:  # Gerak kanan
        return (x, y+1)
    else:
        print("Gerakan tidak valid! Coba lagi.")
        return posisi_pemain  # Jika gerakan tidak valid, posisi pemain tetap sama

# Fungsi untuk menggerakkan musuh (AI)
def gerak_musuh(peta, posisi_musuh, posisi_pemain):
    jalur = a_star(peta, posisi_musuh, posisi_pemain)
    if jalur and len(jalur) > 1:  # Memastikan jalur memiliki lebih dari satu titik
        return jalur[1]  # Musuh bergerak ke posisi berikutnya di jalur
    return posisi_musuh  # Jika tidak ada jalur, musuh tetap di tempat

# Fungsi utama
def main():
    # Peta: 0 = jalur kosong, 1 = rintangan (#)
    peta = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    posisi_pemain = (4, 4)  # Posisi awal pemain
    posisi_musuh = (0, 0)  # Posisi awal musuh

    while True:
        # Menampilkan peta dengan posisi pemain dan musuh
        jalur = a_star(peta, posisi_pemain, posisi_musuh)
        print_peta(peta, posisi_pemain, posisi_musuh, jalur if jalur else [])

        # Menggerakkan pemain
        posisi_pemain = gerak_player(peta, posisi_pemain)
        
        if posisi_pemain == "keluar":  # Jika pemain menekan O untuk keluar
            print("Anda keluar dari permainan.")
            break

        # Menggerakkan musuh
        posisi_musuh = gerak_musuh(peta, posisi_musuh, posisi_pemain)

        # Cek apakah musuh menangkap pemain
        if posisi_pemain == posisi_musuh:
            print("GAME OVER! Musuh menangkapmu!")
            break

if __name__ == "__main__":
    main()
    