# Definiere die Benutzer und Passwörter
users = {"user1": "password1", "jasper.v": "LaufinZone5"}

# Funktion zum Überprüfen der Anmeldedaten
def check_login(username, password):
    if username in users and users[username] == password:
        return True
    return False
