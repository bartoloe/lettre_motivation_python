#!/usr/bin/env python
# -*- coding: utf-8 -*-

def saut_de_ligne(n):
    for i in range(0, n - 1):
        print("\n")

def tab(n):
    result = ""
    for i in range(0, n - 1):
       result += "\t "
       return result


infos = ["nom_prenom", "adresse", "code_postal", "num_phone",\
 "email"]

title = tab(2) + "Objet   : Candidature au poste d'alternance de "

subject = "sujet"

content = tab(2) + "content"

conclusion = tab(2) + "conclusion"

def print_header():
    for v in infos:
        print(v)

def format():
    print_header()
    saut_de_ligne(2)
    print(title)
    saut_de_ligne(2)
    print(content)
    saut_de_ligne(2)
    print(conclusion)

format()