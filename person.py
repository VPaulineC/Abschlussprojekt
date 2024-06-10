import json
from datetime import datetime

class Person:
    
    @staticmethod
    def load_person_data():
        """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list(person_data):
        """A Function that takes the persons-dictionary and returns a list auf all person names"""
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
        return list_of_names
    
    @staticmethod
    def find_person_data_by_name(suchstring):
        """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
        und die die Person als Dictionary zurück gibt"""

        person_data = Person.load_person_data()
        if suchstring == "None":
            return {}

        two_names = suchstring.split(", ")
        vorname = two_names[1]
        nachname = two_names[0]

        for eintrag in person_data:
            if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
                
                return eintrag
        else:
            return {}
        
    @staticmethod   
    def load_by_id(such_id):
        person_data = Person.load_person_data()
        
        if such_id == "None":
            return {}

        for eintrag in person_data:
            if (eintrag["id"] == such_id):
                return eintrag
        else:
            return {}
        
    def __init__(self, person_dict) -> None:
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]
        self.max_heart_rate = self.calc_max_heart_rate()
        self.age = self.calc_age()
        self.ekg_data = person_dict["ekg_tests"]
        self.ekg_result_link = person_dict["ekg_tests"][0]["result_link"]


    def calc_age(self):
        current_year = datetime.now().year
        birth_year = int(self.date_of_birth)
        age = current_year - birth_year
        return age
    
    def calc_max_heart_rate(self):
        age = self.calc_age()
        max_heart_rate = 220 - age 
        return max_heart_rate
    
# ----------------------------------------
if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    print(person_names)
    print(Person.find_person_data_by_name("Huber, Julian"))

    person_1_dict = Person.find_person_data_by_name("Huber, Julian")
    person_1 = Person(person_1_dict)

    alter = person_1.calc_age()
    max_herzfrequenz = person_1.calc_max_heart_rate()
    choosen_id = Person.load_by_id(1)
    print("Alter:", alter)
    print("Maximale Herzfrequenz:", max_herzfrequenz)
    print("Eintrag von gewählter ID:", choosen_id)
    
    