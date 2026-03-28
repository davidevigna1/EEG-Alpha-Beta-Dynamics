import mne
import matplotlib.pyplot as plt

def plot_raw_signal(raw):
    fig_raw = raw.plot(n_channels=10, scalings='auto', title="Segnale EEG Grezzo (Primi 10 canali)", show=False)
    print("Grafico del segnale grezzo generato.")
    return fig_raw

def plot_psd(raw):
    fig_psd = raw.compute_psd(fmin=1.0, fmax=40.0, picks='eeg').plot(show=False)
    ax = fig_psd.axes[0]
    ax.set_title("Densità Spettrale di Potenza (PSD) - Tutti i canali EEG")
    ax.set_ylabel("Potenza (dB/Hz)") 
    print("Grafico della PSD generato.")
    return fig_psd

def show_all_plots():
    plt.show()

