import config
from eeg_processor import load_and_prepare_data, get_band_power_per_channel
from graphics import plot_raw_signal, plot_psd, show_all_plots
from database_manager import inserisci_risultati

def run_eeg_pipeline():
    print("--- INIZIO PIPELINE ANALISI EEG PER CANALE ---")

    raw = load_and_prepare_data(config.DATA_PATH)
    
    print("Calcolo potenza bande per ogni canale...")
    alpha_results = get_band_power_per_channel(raw, 'alpha')
    beta_results = get_band_power_per_channel(raw, 'beta')
    
    id_paziente_test = 1 
    count = 0
    
    print(f"Salvataggio dati per {len(raw.ch_names)} canali...")
    for ch in raw.ch_names:
        a_pow = alpha_results[ch]
        b_pow = beta_results[ch]
        ratio = a_pow / b_pow if b_pow != 0 else 0
        
        try:
            inserisci_risultati(id_paziente_test, ch, a_pow, b_pow, ratio)
            count += 1
        except Exception as e:
            pass 
            
    print(f"[OK] Salvataggio completato: {count}/{len(raw.ch_names)} canali inseriti correttamente.")
    
    print("Generazione grafici di controllo...")
    plot_raw_signal(raw)
    plot_psd(raw)
    show_all_plots()

    print("--- PROCESSO TERMINATO ---")

if __name__ == "__main__":
    run_eeg_pipeline()