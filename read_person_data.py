#%% Import
# Kopie von Aufgabe 5
import json

# Opening JSON file
# --------------------------------function to load the person data---------------------------------
def load_person_data():
    """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
    file = open('data/person_db.json')
    person_data = json.load(file)
    return person_data

# ---------------------------------Function to get a list of all persons---------------------------------
def get_person_list(person_data):
    """A Function that takes the Persons-Dictionary and returns a List auf all person names"""
    list_of_names = []
    # search for the lastname and the firstname in the dict and append it to the names list
    for eintrag in person_data:
        list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
    return list_of_names

# ---------------------------------Function to get a list from the person data---------------------------
def find_person_data_by_name(suchstring):
    """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
    und die die Person als Dictionary zurück gibt"""
    
    person_data = load_person_data()
    if suchstring == "None":
        return {}
    
    # split the string in lastname and firstname
    two_names = suchstring.split(", ")
    vorname = two_names[1]
    nachname = two_names[0]
    # search for the person where the lastname and the firstname is the same as in dict
    for eintrag in person_data:
        print(eintrag)
        if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
            print()
            return eintrag
    else:
        return {}



