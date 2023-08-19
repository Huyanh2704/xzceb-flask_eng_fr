"""This is program for translation"""
from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    """This is module for translate E to F"""
    frenchtext = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(englishtext)
    print(frenchtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    """This is module for translate F to E"""
    englishtext = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchtext)
    print(englishtext)
    return englishtext
