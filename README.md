# EEG Alpha Wave Analysis Pipeline

This project analyzes EEG signals from `.edf` files to calculate the power of Alpha (8-13 Hz) and Beta (13-30 Hz) bands for each of the 64 electrodes. Results are automatically saved to a MySQL database for further analysis.

## Requirements

- **Python 3.10+**
- **MySQL Server** (e.g., XAMPP, WAMP, or standalone installation)
- Libraries listed in `requirements.txt`

## Installation

1. Clone or download the project folder.
2. Install the necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Open `config.py` and modify the connection parameters if your MySQL database has a different password or host:
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password_here",
    "database": "AlphaWaveDB"
}
```

## How to use the Project

1. **Database Setup**: Run this script once to create the database and the correct table:
   ```bash
   python database_setup.py
   ```
2. **Run Analysis**: Launch the main program to analyze the EEG file and save the data:
   ```bash
   python main.py
   ```

## Results Structure

The database will contain the `alpha_analysis` table with the following columns:
- `id_paziente`: Patient identification number.
- `nome_canale`: Electrode name (e.g., Fcz, Oz, C3).
- `potenza_alpha`: Mean power measured in the Alpha band.
- `potenza_beta`: Mean power measured in the Beta band.
- `ratio_ab`: Ratio between Alpha and Beta power.
- `data_analisi`: Analysis timestamp.
