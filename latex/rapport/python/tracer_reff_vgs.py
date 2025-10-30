import numpy as np
import matplotlib.pyplot as plt

def tracer_Rc_vgs():
    """
    Trace la caractéristique Rc = f(Vgs) d'une résistance commandée en tension
    basée sur les mesures expérimentales
    """
    # Données expérimentales
    R = np.array([0, 518.367, 1017, 1496, 2030, 2502, 3019, 3505])
    Vds = np.array([0, 0.199, 0.214, 0.231, 0.253, 0.281, 0.317, 0.351])
    Vd = np.array([0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6])
    Vgs = np.array([0, -0.52, -1.02, -1.5, -2.01, -2.52, -2.99, -3.4])
    
    # Calculs
    Rc = 470  # Ohms (résistance de charge)
    Id = (Vd - Vds) / Rc  # Courant drain en A
    Rds = Vds / Id  # Résistance drain-source en Ohms
    Rc = Rc + Rds  # Résistance effective totale en Ohms
    
    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(Vgs, Rc, 'bo-', linewidth=2, markersize=8, label='Rc mesuré')
    
    # Marquer le point Rc = 750Ω
    Rc_cible = 750
    # Interpolation pour trouver Vgs correspondant
    Vgs_750 = np.interp(Rc_cible, Rc, Vgs)
    plt.plot(Vgs_750, Rc_cible, 'r*', markersize=15, 
             label=f'Rc = 750Ω (Vgs ≈ {Vgs_750:.2f}V)')
    
    # Ligne horizontale pour Rc = 750Ω
    plt.axhline(y=Rc_cible, color='r', linestyle='--', alpha=0.5)
    
    # Ligne verticale pour Vgs correspondant
    plt.axvline(x=Vgs_750, color='r', linestyle='--', alpha=0.5)
    
    # Mise en forme
    plt.xlabel('Vgs (V)', fontsize=12, fontweight='bold')
    plt.ylabel('Rc (Ω)', fontsize=12, fontweight='bold')
    plt.title('Caractéristique Rc = f(Vgs) - Résistance commandée en tension', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    
    # Annotations
    plt.text(Vgs_750 - 0.3, Rc_cible + 50, 
             f'Vgs = {Vgs_750:.2f}V\nRc = {Rc_cible}Ω', 
             fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()
    
    # Afficher les résultats numériques
    print("=" * 60)
    print("Tableau des résultats:")
    print("=" * 60)
    print(f"{'Vgs (V)':<10} {'Rds (Ω)':<12} {'Rc (Ω)':<12} {'Id (mA)':<10}")
    print("-" * 60)
    for i in range(len(Vgs)):
        print(f"{Vgs[i]:<10.2f} {Rds[i]:<12.0f} {Rc[i]:<12.0f} {Id[i]*1000:<10.3f}")
    print("=" * 60)
    print(f"\nPour Rc = 750Ω, Vgs ≈ {Vgs_750:.2f}V")
    print("=" * 60)

# Appeler la fonction
if __name__ == "__main__":
    tracer_Rc_vgs()