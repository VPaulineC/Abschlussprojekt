import json
import pandas as pd
from person import Person
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

    @staticmethod
    def load_by_id(such_id):
    # für alle ekg test über alle personen
    # for pereon in prsons
    #for ekgtest in test    def load_by_id(such_id):

        person_data = Person.load_person_data()

        if such_id == "None":
            return {}
        
        for eintrag in person_data:
            for ekg_test in eintrag["ekg_tests"]:
                if ekg_test["id"] == such_id:
                    return ekg_test
        return {}

    @staticmethod
    def find_peaks(series, threshold, respacing_factor=5):
        """
        A function to find the peaks in a series
        Args:
            - series (pd.Series): The series to find the peaks in
            - threshold (float): The threshold for the peaks
            - respacing_factor (int): The factor to respace the series
        Returns:
            - peaks (list): A list of the indices of the peaks
        """
        # Respace the series
        series = series.iloc[::respacing_factor]
        
        # Filter the series
        series = series[series>threshold]


        peaks = []
        last = 0
        current = 0
        next = 0

        for index, row in series.items():
            last = current
            current = next
            next = row

            if last < current and current > next and current > threshold:
                peaks.append(index-respacing_factor)

        return peaks

    @staticmethod
    def plot_ekg(df, peaks):
        df.loc[:, "is_peak"] = False
        df.loc[peaks, "is_peak"] = True
        fig = px.scatter(df, x='Time in s', y='EKG in mV', color='is_peak') 
        return fig
    
    @staticmethod
    def plot_hr(df_hr): 
        fig = px.line(df_hr, x='Time in s', y='Heart Rate in bpm')
        return fig
    
## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]


    def get_df(self):
        df = pd.read_csv(self.data, sep='\t', header=None, names=['EKG in mV','Time in ms',])
        df['Time in s'] = df['Time in ms'] / 1000
        return df    
        
    
    @staticmethod
    def estimate_hr(peaks, sampling_rate):
        # Calculate time differences between peaks
        time_difference = np.array([(peaks[i] - peaks[i-1]) / sampling_rate for i in range(1, len(peaks))])
        # Calculate average time difference
        # avg_time_difference = sum(time_difference) / len(time_difference)
        # Calculate heart rate (beats per minute)
        heart_rate = 60. / time_difference
        time_array = np.array(peaks[1:]) / sampling_rate
        

        # Create dataframe
        df_hr = pd.DataFrame({'Time in s': time_array, 'Heart Rate in bpm': heart_rate})
        return df_hr
    
   
if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    #------------------------------------------------------------
    id_from_selectionbox = 1
    ekg_dict = EKGdata.load_by_id(id_from_selectionbox)
    print("Eintrag von gewählter ID EKG:", ekg_dict) #id
    ekg_data = EKGdata(ekg_dict)
    #------------------------------------------------------------
    df = ekg_data.get_df()
    print(df.head())
    peaks = EKGdata.find_peaks(df['EKG in mV'], 340, 5)
    #------------------------------------------------------------
    fig = EKGdata.plot_ekg(df, peaks,)
    fig.show()
    
    #------------------------------------------------------------
    df_hr = EKGdata.estimate_hr(peaks, 1000)
    print(df_hr.head())
    #------------------------------------------------------------
    fig = EKGdata.plot_hr(df_hr)
    fig.show() 
    #------------------------------------------------------------


# %%
