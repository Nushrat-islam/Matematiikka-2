import numpy as np

# 1a) 
a1 = 2.493
b1 = 0.911
print("1a) rad → asteiksi:")
print(np.degrees(a1))
print(np.degrees(b1))

# 2a)
a2 = 137.7
b2 = 62.3
print("\n2a) asteet → radiaaneiksi:")
print(np.radians(a2))
print(np.radians(b2))

# 3. Taulukko kulmista
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("\n3) Taulukko asteet → radiaanit:")
for i in A:
    print(f"{i:>3}° = {np.radians(i):.3f} rad")

# 2. SUORAKULMAISET KOLMIOT

# 1) Hypotenuusa, kun kateetit 1,6 m ja 2,3 m
a = 1.6
b = 2.3
c = np.hypot(a, b)  # numpy-funktio hypotenuusan laskuun
print("\nSuorakulmaisen kolmion hypotenuusa:", round(c, 2), "m")

# 2) Suorakulmion sivut, kun lävistäjä 6,4 m ja sivujen suhde 3:2
d = 6.4
ratio = np.array([3, 2])
x = d / np.sqrt(np.sum(ratio**2))
sides = ratio * x
print("\nSuorakulmion sivut:")
print("Pidempi sivu:", round(sides[0], 2), "m")
print("Lyhyempi sivu:", round(sides[1], 2), "m")