import heapq
import matplotlib.pyplot as plt

print("+"*22)
print("Perkiraan a star dalam game iggle pop")
print("+"*22)
print("\n")

# Fungsi untuk menampilkan peta
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

# Fungsi A* untuk mencari jalur terpendek
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




