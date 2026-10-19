import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    #devo definire una funzione che gestisca l'evento quando premo il bottone
    def handleSpellCheck(self, e):
        txtCurrentSentence = self._view._txtInInput.value
        if txtCurrentSentence == "":
            self._view._txtOut.controls.clear()
            self._view._txtOut.controls.append(
                ft.Text(value="Inserisci una frase!")
            )
            return

        language = self._view._dropLingua.value
        print(language)
        modality = self._view._dropMetodo.value
        print(modality)

        if language == "":
            self._view._txtOut.controls.clear()
            self._view._txtOut.controls.append(
                ft.Text(value="Seleziona una lingua!")
            )
            return

        if modality == "":
            self._view._txtOut.controls.clear()
            self._view._txtOut.controls.append(
                ft.Text(value="Inserisci un metodo di ricerca!")
            )
            return

        #il metodo handle restituisce le parole + il tempo trascorso
        parole, elapsedTime = self.handleSentence(txtCurrentSentence, language, modality)
        #devo poi inserirlo nella grafica

        self._view._txtOut.controls.clear()
        self._view._txtOut.controls.append(ft.Text("Frase inserita: " + txtCurrentSentence))
        self._view._txtOut.controls.append(ft.Text("Parole errate: " + parole))
        self._view._txtOut.controls.append(ft.Text("Tempo richiesto alla ricerca: " + str(elapsedTime) + "s"))

        self._view.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text