import numpy as np
import matplotlib.pyplot as plt

# Paramètres
omega_0 = 1  # Fréquence de résonance normalisée
R = 1000  # Résistance en ohms (exemple)
C = 1e-6  # Capacité en farads (exemple)
omega_0 = 1 / (R * C)  # Fréquence de résonance

# Plage de fréquences
x = np.logspace(-2, 2, 1000)  # x = omega/omega_0
omega = x * omega_0

# Fonction de transfert
def beta(x):
    return 1 / (3 + 1j * (x - 1/x))

# Calcul du module et de la phase
H = beta(x)
module_dB = 20 * np.log10(np.abs(H))
phase_deg = np.angle(H, deg=True)

# Asymptotes pour le module
module_asymptote_BF = -20 * np.log10(x)  # Basse fréquence: -20dB/dec
module_asymptote_HF = 20 * np.log10(x)   # Haute fréquence: +20dB/dec
module_asymptote_0 = -20 * np.log10(3) * np.ones_like(x)  # À omega_0

# Asymptotes pour la phase
phase_asymptote = np.zeros_like(x)
phase_asymptote[x < 0.1] = 90   # Basse fréquence: +90°
phase_asymptote[x > 10] = -90   # Haute fréquence: -90°
mask = (x >= 0.1) & (x <= 10)
phase_asymptote[mask] = 90 - 180 * np.log10(x[mask] / 0.1) / np.log10(100)

# Tracé
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Diagramme de gain
ax1.semilogx(x, module_dB, 'b-', linewidth=2, label='Courbe réelle')
ax1.semilogx(x, module_asymptote_BF, 'r--', linewidth=1.5, label='Asymptote BF (-20dB/dec)')
ax1.semilogx(x, module_asymptote_HF, 'g--', linewidth=1.5, label='Asymptote HF (+20dB/dec)')
ax1.axvline(x=1, color='k', linestyle=':', alpha=0.5, label='ω = ω₀')
ax1.grid(True, which='both', alpha=0.3)
ax1.set_xlabel('x = ω/ω₀')
ax1.set_ylabel('|β| (dB)')
ax1.set_title('Diagramme de Bode - Module')
ax1.legend()

# Diagramme de phase
ax2.semilogx(x, phase_deg, 'b-', linewidth=2, label='Courbe réelle')
ax2.semilogx(x, phase_asymptote, 'r--', linewidth=1.5, label='Asymptotes')
ax2.axhline(y=90, color='r', linestyle=':', alpha=0.5)
ax2.axhline(y=0, color='k', linestyle=':', alpha=0.5)
ax2.axhline(y=-90, color='r', linestyle=':', alpha=0.5)
ax2.axvline(x=1, color='k', linestyle=':', alpha=0.5, label='ω = ω₀')
ax2.grid(True, which='both', alpha=0.3)
ax2.set_xlabel('x = ω/ω₀')
ax2.set_ylabel('Phase (°)')
ax2.set_title('Diagramme de Bode - Phase')
ax2.set_ylim([-100, 100])
ax2.legend()

plt.tight_layout()
plt.show()

# Affichage des valeurs clés
print(f"À ω = ω₀ (x = 1):")
print(f"  Module: {module_dB[np.argmin(np.abs(x - 1))]:.2f} dB")
print(f"  Phase: {phase_deg[np.argmin(np.abs(x - 1))]:.2f}°")
print(f"\nModule théorique à ω₀: {20*np.log10(1/3):.2f} dB")