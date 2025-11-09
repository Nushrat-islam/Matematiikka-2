# Matematiikkaa Pythonilla – Tehtävät 1–3
# Tehtävä: yksikköympyrä, sinikäyrä ja kosinikäyrä
# Kirjoittaja: Nushrat

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

# -------------------------------
# 1. Yksikköympyrä ja annetut kulmat
# -------------------------------

kulmat_ast = np.array([30, 45, 60, 90, 120, 150, 180, 270])  # kulmat asteina
kulmat_rad = np.radians(kulmat_ast)  # muutetaan radiaaneiksi

x = np.cos(kulmat_rad)
y = np.sin(kulmat_rad)

fig, ax = plt.subplots(figsize=(5,5))
ax.add_patch(patches.Circle((0, 0), radius=1, fill=False))

# Keskitetään akselit
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_aspect('equal')
ax.scatter(x, y, color='red')

# Lisätään kulma-annotaatiot
for i, kulma in enumerate(kulmat_ast):
    ax.annotate(f"{kulma}°",
                (x[i], y[i]),
                textcoords="offset points",
                xytext=(10, 5),
                ha='left',
                fontsize=10)

plt.title("1 Yksikköympyrä ja merkityt kulmat")
plt.show()

# -------------------------------
# 2. Sinikäyrä ja kosinikäyrä välillä -3π ... 3π
# -------------------------------

X = np.linspace(-3*np.pi, 3*np.pi, 512)
C = np.cos(X)
S = np.sin(X)

plt.figure(figsize=(19.2, 4.8))  # kolminkertainen leveys (6.4 * 3)
plt.plot(X, C, 'g--', label='cos(x)')  # vihreä katkoviiva
plt.plot(X, S, 'r:', label='sin(x)')   # punainen pisteviiva
plt.legend()

# -------------------------------
#  3. Akselit π-yksiköissä
# -------------------------------

plt.xticks(
    [-3*np.pi, -2*np.pi, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 2*np.pi, 3*np.pi],
    [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$-\frac{\pi}{2}$',
     r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$2\pi$', r'$3\pi$']
)

plt.title("2–3 Sini- ja kosinifunktiot välillä −3π ... 3π")
plt.grid(True)
plt.show()
