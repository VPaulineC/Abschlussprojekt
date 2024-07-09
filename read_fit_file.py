import fitparse
import pandas as pd
import plotly.express as px

def read_heart_rate_from_fit(file_path):
    '''Liest die Herzfrequenzdaten aus einer FIT-Datei und gibt sie als DataFrame zurück.'''
    # Öffne die FIT-Datei mit fitparse
    fitfile = fitparse.FitFile(file_path)

    # Listen zum Speichern der Daten
    timestamps = []
    heart_rates = []

    # Iteriere über alle Nachrichten in der FIT-Datei
    for record in fitfile.get_messages("record"): # record = Datensatz / get_messages = gibt alle Nachrichten des Typs "record" zurück
        record_data = {} # leeres Dictionary für die Daten des Datensatzes
        for data in record:
            # Speichere die Daten in einem Dictionary
            record_data[data.name] = data.value # data.name = Name des Datensatzes / data.value = Wert des Datensatzes

        # Extrahiere den Timestamp und die Herzrate, falls vorhanden
        if 'timestamp' in record_data and 'heart_rate' in record_data:
            timestamps.append(record_data['timestamp'])
            heart_rates.append(record_data['heart_rate'])

    # Erstelle einen DataFrame aus den Daten
    df = pd.DataFrame({
        'timestamp': timestamps,
        'heart_rate': heart_rates
    })

    # Füge eine Spalte im df hinzu, die nur die Sekunden enthält mit der Funktion dt.second
    # df['seconds'] = df['timestamp'].dt.second Falsch!

    # Berechne die Sekunden seit dem Start der Aufzeichnung
    start_time = df['timestamp'].iloc[0]
    df['seconds'] = (df['timestamp'] - start_time).dt.total_seconds() 

    # Rückgabe des DataFrames
    return df


# Erstelle die interaktive Grafik
def plot_fit_file(file_path):
    '''Plottet die Herzfrequenzdaten aus einer FIT-Datei in einer interaktiven Grafik.'''
    df = read_heart_rate_from_fit(file_path)
    #fig = px.line(df, x = 'seconds', y ='heart_rate')
    fig = px.line(df, x='seconds', y='heart_rate', title='Herzfrequenz über Zeit')
    return fig

# Beispielverwendung
if __name__ == "__main__":
    #file_path = 'fit-files/long_endurance_ride.fit'
    #file_path = 'fit-files/tempo_blocks_training.fit'
    file_path = 'fit-files/vo2_max_training.fit'
    df = read_heart_rate_from_fit(file_path)
    fig = plot_fit_file(file_path)
    fig.show()




    
