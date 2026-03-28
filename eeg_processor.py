import mne
import numpy as np
from config import FREQ_BANDS, DATA_PATH

def load_and_prepare_data(file_path):
    raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
    raw.filter(l_freq=1.0, h_freq=40.0)
    return raw

def get_band_power_per_channel(raw, band_name):
    fmin, fmax = FREQ_BANDS[band_name]
    
    spectrum = raw.compute_psd(method='welch', fmin=fmin, fmax=fmax, n_fft=2048)
    psds = spectrum.get_data() 
    
    band_powers = np.mean(psds, axis=1)
    
    results = {ch_name: power for ch_name, power in zip(raw.ch_names, band_powers)}
    return results

def run_analysis():
    raw_data = load_and_prepare_data(DATA_PATH)
    alpha_results = get_band_power_per_channel(raw_data, 'alpha')
    beta_results = get_band_power_per_channel(raw_data, 'beta')
    
    combined = []
    for ch in raw_data.ch_names:
        combined.append({
            'channel': ch,
            'alpha': alpha_results[ch],
            'beta': beta_results[ch],
            'ratio': alpha_results[ch] / beta_results[ch] if beta_results[ch] != 0 else 0
        })
    return combined