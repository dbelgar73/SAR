#COMPLETO

#!/usr/bin/env python
#! -*- encoding: utf8 -*-

# 1.- Pig Latin

import re
import sys
from typing import Optional, Text
from os.path import isfile

import math

class Translator():

    def __init__(self, punt:Optional[Text]=None):
        """
        Constructor de la clase Translator

        :param punt(opcional): una cadena con los signos de puntuación
                                que se deben respetar
        :return: el objeto de tipo Translator
        """
        if punt is None:
            punt = ".,;?!"
        self.re = re.compile(r"(\w+)([" + punt + r"]*)")

    def translate_word(self, word:Text) -> Text:
        """
        Recibe una palabra en inglés y la traduce a Pig Latin

        :param word: la palabra que se debe pasar a Pig Latin
        :return: la palabra traducida
        """
        vocales = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
        signosPuntuacion = [".",",",";","2","?","!"]
        añadirAlFinal = []
        palabraNueva = ""
        cambiar = True
        primeraMayuscula = False
        todaMayuscula = False

        # caso 1: empieza por un número
        if word[0].isdigit():
            return word
        # caso 2: empieza por vocal
        if word[0].lower() in vocales:
            palabraNueva = word + "yay"
        # caso 3: empieza por consonantes
        if word[0].lower() not in vocales:
            #comprobar si la primera letra es mayuscula
            if word[0].isupper(): primeraMayuscula = True
            #comprobar si esta toda en mayusculas
            if word.isupper(): todaMayuscula = True

            for c in word:
                if cambiar:
                    if c.lower() not in vocales:
                        añadirAlFinal.append(c)
                    else:
                        cambiar = False
                if not cambiar:
                    palabraNueva += c
            palabraNueva += "".join(añadirAlFinal) + "ay"
        
            word = ""
            aux = ""
            for c in palabraNueva:
                if c in signosPuntuacion: aux += c 
                else: word += c
            palabraNueva = word + aux  
            if primeraMayuscula: palabraNueva = palabraNueva.capitalize()     
            if todaMayuscula: palabraNueva = palabraNueva.upper()
        return palabraNueva

    def translate_sentence(self, sentence:Text) -> Text:
        """
        Recibe una frase en inglés y la traduce a Pig Latin

        :param sentence: la frase que se debe pasar a Pig Latin
        :return: la frase traducida
        """
        palabras = sentence.split()
        frase_nueva = [self.translate_word(palabra) for palabra in palabras]
        return " ".join(frase_nueva)

    def translate_file(self, filename:Text):
        """
        Recibe un fichero y crea otro con su tradución a Pig Latin

        :param filename: el nombre del fichero que se debe traducir
        :return: None
        """
        
        if not isfile(filename):
            print(f'{filename} no existe o no es un nombre de fichero', file=sys.stderr)

        with open(filename, 'r') as file:
            lines = file.readlines()
        
        translated_lines = [self.translate_sentence(line.strip()) for line in lines]
        
        translated_filename = filename.split('.')[0] + '_translated.txt'
        
        with open(translated_filename, 'w') as file:
            file.write('\n'.join(translated_lines))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f'Syntax: python {sys.argv[0]} [filename]')
        exit()
    t = Translator()
    if len(sys.argv) == 2:
        t.translate_file(sys.argv[1])
    else:
        sentence = input("ENGLISH: ")
        while len(sentence) > 1:
            print("PIG LATIN:", t.translate_sentence(sentence))
            sentence = input("ENGLISH: ")
