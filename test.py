import json

# JSON-Daten werden direkt als Python-Objekt (Liste von Diktaten) definiert
patients = [
    # Hier kommen die Patientendaten rein
]

def get_ekg_result_link(patients, ekg_id):
    for patient in patients:
        for test in patient["ekg_tests"]:
            if test["id"] == ekg_id:
                return test["result_link"]
    return None

# Funktion zum Plotten der Herzfrequenz über Zeit für .fit-Dateien
def plot_fit_file(file_path):
    # Annahme: Das .fit-File enthält Daten im CSV-Format für das Beispiel
    # Hier müssen Sie die Daten laden und plotten (z.B. mit pandas und matplotlib)
    print(f"Plotting interactive heart rate over time from .fit file: {file_path}")
    # Beispiel-Code (ohne tatsächliche Implementierung):
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # data = pd.read_csv(file_path)  # Beispiel: Einlesen der .fit-Datei als CSV
    # plt.plot(data['time'], data['heart_rate'])
    # plt.show()

# Funktion zum Durchführen von Berechnungen für .txt-Dateien
def process_txt_file(file_path):
    # Hier kommen die normalen EKG-Berechnungen rein
    print(f"Processing EKG data from .txt file: {file_path}")
    # Beispiel-Code (ohne tatsächliche Implementierung):
    # with open(file_path, 'r') as file:
    #     data = file.readlines()
    #     # EKG-Berechnungen durchführen

# Beispielaufruf der Funktion
ekg_id = 1  # Die ID des gewünschten EKG-Tests
result_link = get_ekg_result_link(patients, ekg_id)

if result_link:
    if result_link.endswith('.fit'):
        plot_fit_file(result_link)
    elif result_link.endswith('.txt'):
        process_txt_file(result_link)
    else:
        print(f"Unbekannter Dateityp für den Result Link: {result_link}")
else:
    print(f"EKG-Test mit ID {ekg_id} nicht gefunden.")
