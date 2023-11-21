import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Git Connexion established
# Fonction pour générer un signal ECG simulé
def generate_ecg_signal():
    fs = 1000  # Fréquence d'échantillonnage en Hz
    t = np.arange(0, 10, 1 / fs)  # Temps en secondes
    ecg_signal = 0.5 * np.sin(2 * np.pi * 5 * t) + 0.2 * np.sin(2 * np.pi * 12 * t)
    return ecg_signal


# Fonction pour détecter les QRS avec la transformée multi-ondelettes
def qrs_detection(signal):
    # Exemple de détection simple des QRS en utilisant la transformée en ondelettes
    # Vous devez remplacer cela par l'algorithme réel que vous souhaitez utiliser
    # dans le cadre de la détection des QRS avec transformée multi-ondelettes.
    # Par exemple, vous pourriez utiliser la bibliothèque PyWavelets.
    pass


# Fonction principale Streamlit
def main():
    st.title("Projet de Détection des QRS avec Transformée Multi-Ondelettes")

    # Étape 1: Lecture et génération de signal
    ecg_signal = generate_ecg_signal()

    # Affichage temporel
    st.subheader("Affichage Temporel du Signal ECG")
    st.line_chart(ecg_signal)

    # Tester l'effet de l'échantillonnage et de la quantification
    # Vous pouvez ajouter le code pour tester ces effets ici

    # Étape 2: Calcul de FFT
    st.subheader("Calcul de FFT")
    fft_result = np.fft.fft(ecg_signal)
    frequencies = np.fft.fftfreq(len(fft_result))
    st.line_chart(np.abs(fft_result))

    # Explication textuelle
    st.write("""
    La transformée de Fourier rapide (FFT) est utilisée pour transformer le signal du domaine temporel 
    vers le domaine fréquentiel. Cette visualisation montre les composantes fréquentielles du signal.
    """)

    # Étape 3: Tronquer le signal
    truncated_signal = ecg_signal[:len(ecg_signal) // 2]

    # Étape 4: Calcul de FFT avant et après troncature
    st.subheader("Calcul de FFT après Troncature")
    fft_result_truncated = np.fft.fft(truncated_signal)
    frequencies_truncated = np.fft.fftfreq(len(fft_result_truncated))
    st.line_chart(np.abs(fft_result_truncated))

    # Explication textuelle
    st.write("""
    En tronquant le signal, nous pouvons observer comment cela affecte les composantes fréquentielles
    lorsqu'elles sont visualisées avec la FFT.
    """)

    # Étape 5: Ajouter un bruit
    noisy_signal = ecg_signal + 0.1 * np.random.randn(len(ecg_signal))

    # Étape 6: Appliquer des calculs de corrélation et tester les retards
    # Vous pouvez ajouter le code pour ces étapes ici

    # Étape 7: Appliquer un filtrage
    st.subheader("Signal après Filtrage")
    b, a = signal.butter(4, 0.1, 'low')  # Exemple de filtre passe-bas Butterworth d'ordre 4
    filtered_signal = signal.filtfilt(b, a, ecg_signal)
    st.line_chart(filtered_signal)

    # Explication textuelle
    st.write("""
    Un filtre passe-bas Butterworth d'ordre 4 a été appliqué au signal ECG pour éliminer les hautes fréquences.
    La visualisation montre le signal après l'application du filtre.
    """)


if __name__ == "__main__":
    main()
