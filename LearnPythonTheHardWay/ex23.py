# Aufruf des Scripts als python3.6 ex23.py utf-8 strict
# --> input_encoding = utf-8
# & error = strict


# import wichtiger module
import sys
# aufdröseln der zu übergebenen Parameter
script, input_encoding, error = sys.argv

# Definition der Funktion =/= Aufruf der Funktion. Hier nur Definition!
# Wenn wir sie später konkret ausführen wird language_file = languages sein,
# encoding wird input_encoding und errors wird error
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

#Funktionsdefinition die 3 parameter bekommt: line (wird durch main funktion gesetzt),
# encoding & errors werden ebenfalls von main übergeben (main() ruft print_line)
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
# languages ist ein File Object.
languages = open("languages.txt", encoding="utf-8")
#Aufruf der main funktion mit dem File Object sowie zwei Parametern die beim Aufruf des Scripts übergeben wurden
main(languages, input_encoding, error)
