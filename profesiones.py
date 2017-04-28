#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Autor: Fulanito de Tal
# Programa: modelo.py
# Fecha: Sat May 17 14:54:18 COT 2014
# Descripcion: este programa hace blablablabla

# Constantes
UNIVERSIDAD = 0
CIUDAD = 1
PROGRAMA = 2
SEMESTRES = 3
VALOR = 4
HOMBRES = 5
MUJERES = 6

profesiones = {
  # "sigla"  : [ "universidad", "ciudad", "programa", semestres, valor, hombres, mujeres ],
    "PUJ-PRE": [ "Pontificia Universidad Javeriana", "Cali", "Pre-Escolar", 9, 3800000, 14, 12 ],
    "UCA-CNT": [ "Universidad del Cauca", "Popayan", "Contaduria", 12, 2100000, 15, 14 ],
    "UAN-ADE": [ "Universidad Antonio Nariño", "Medellin", "Administracion de Empresas", 10, 2450000, 8, 16 ],
    "USB-SOC": [ "Universidad de San Buenaventura", "Cartagena", "Trabajo Social", 10, 4200000, 17, 17 ],
    "UNC-SIS": [ "Universidad Nacional de Colombia", "Sincelejo", "Ingenieria de Sistemas", 10, 1400000, 16, 19 ],
    "UDP-IMM": [ "Universidad de Pamplona", "Pamplona", "Ingenieria Multimedia", 10, 2900000, 21, 15 ],
    "UCA-IND": [ "Universidad del Cauca", "Popayan", "Ingenieria Industrial", 12, 1280000, 18, 17 ],
    "FPS-PER": [ "Universidad Francisco de Paula Santander", "Cucuta", "Periodismo", 10, 4500000, 5, 15 ],
    "UTP-PER": [ "Universidad Tecnológica de Pereira", "Armenia", "Periodismo", 8, 1400000, 31, 14 ],
    "UTP-ADE": [ "Universidad Tecnológica de Pereira", "Pereira", "Administracion de Empresas", 10, 4500000, 33, 14 ],
    "UCA-PRE": [ "Universidad del Cauca", "Popayan", "Pre-Escolar", 9, 4200000, 4, 17 ],
    "UIS-ECO": [ "Universidad Industrial de Santander", "Tunja", "Economia", 11, 4500000, 32, 14 ],
    "UCB-MED": [ "Universidad de Córdoba", "Santa Marta", "Medicina", 12, 2800000, 14, 10 ],
    "FPS-CMS": [ "Universidad Francisco de Paula Santander", "Cucuta", "Comunicación Social", 9, 2900000, 26, 17 ],
    "UDA-PRE": [ "Universidad de Antioquia", "Bello", "Pre-Escolar", 9, 4500000, 4, 18 ],
    "UPB-PRE": [ "Universidad Pontificia Bolivariana ", "Bogota", "Pre-Escolar", 10, 4500000, 25, 15 ],
    "UDA-IND": [ "Universidad de Antioquia", "Medellin", "Ingenieria Industrial", 10, 3600000, 7, 16 ],
    "UND-ELC": [ "Universidad Nacional Abierta y a Distancia -UNAD", "Cali", "Ingenieria Electronica", 11, 3600000, 20, 15 ],
    "UNL-IMM": [ "Universidad Libre", "Medellin", "Ingenieria Multimedia", 10, 3600000, 25, 16 ],
    "CMA-VET": [ "Colegio Mayor de Antioquia", "Bello", "Veterinaria", 8, 4500000, 21, 13 ],
    "UMG-SIS": [ "Universidad del Magdalena", "Santa Marta", "Ingenieria de Sistemas", 12, 1280000, 8, 14 ],
    "UCM-SOC": [ "Universidad Católica de Manizales", "Manizales", "Trabajo Social", 8, 2650000, 18, 13 ],
    "EAF-PUB": [ "Universidad EAFIT", "Bogota", "Publicidad", 8, 1400000, 29, 12 ],
    "UDP-ADE": [ "Universidad de Pamplona", "Pamplona", "Administracion de Empresas", 10, 2900000, 7, 17 ],
    "PUJ-CNT": [ "Pontificia Universidad Javeriana", "Medellin", "Contaduria", 12, 1900000, 23, 14 ],
    "UCM-ELC": [ "Universidad Católica de Manizales", "Pereira", "Ingenieria Electronica", 10, 1900000, 26, 12 ],
    "CMA-SIS": [ "Colegio Mayor de Antioquia", "Medellin", "Ingenieria de Sistemas", 10, 2300000, 15, 17 ],
    "UND-SIS": [ "Universidad Nacional Abierta y a Distancia -UNAD", "Medellin", "Ingenieria de Sistemas", 10, 3800000, 8, 19 ],
    "EAF-ADE": [ "Universidad EAFIT", "Medellin", "Administracion de Empresas", 10, 1280000, 18, 14 ],
    "UCM-PER": [ "Universidad Católica de Manizales", "Manizales", "Periodismo", 10, 2100000, 3, 19 ],
    "UTO-CNT": [ "Universidad del Tolima", "Ibague", "Contaduria", 12, 1400000, 12, 12 ],
    "UNC-SOC": [ "Universidad Nacional de Colombia", "Ibague", "Trabajo Social", 8, 1400000, 8, 12 ],
    "USL-ECO": [ "Universidad de la Salle", "Bogota", "Economia", 11, 1900000, 31, 11 ],
    "USB-CMS": [ "Universidad de San Buenaventura", "Bogota", "Comunicación Social", 9, 2100000, 21, 11 ],
    "UNC-PRE": [ "Universidad Nacional de Colombia", "Santa Marta", "Pre-Escolar", 10, 3600000, 22, 18 ],
    "UAT-ECO": [ "Universidad del Atlántico", "Barranquilla", "Economia", 10, 3600000, 16, 17 ],
    "USL-PRE": [ "Universidad de la Salle", "Bogota", "Pre-Escolar", 10, 3600000, 18, 19 ],
    "UAN-IMM": [ "Universidad Antonio Nariño", "Cali", "Ingenieria Multimedia", 10, 4500000, 15, 17 ],
    "FPS-ELC": [ "Universidad Francisco de Paula Santander", "Bucaramanga", "Ingenieria Electronica", 10, 1400000, 18, 12 ],
    "UNC-CNT": [ "Universidad Nacional de Colombia", "Sincelejo", "Contaduria", 12, 3600000, 29, 13 ],
    "UPN-ENF": [ "Universidad Pedagógica Nacional", "Santa Marta", "Enfermeria", 8, 2900000, 25, 13 ],
    "UIS-CNT": [ "Universidad Industrial de Santander", "Cucuta", "Contaduria", 12, 2800000, 11, 19 ],
    "UNC-IMM": [ "Universidad Nacional de Colombia", "Pereira", "Ingenieria Multimedia", 10, 2650000, 22, 17 ],
    "UPB-CNT": [ "Universidad Pontificia Bolivariana ", "Cali", "Contaduria", 12, 2450000, 37, 10 ],
    "UND-SOC": [ "Universidad Nacional Abierta y a Distancia -UNAD", "Bogota", "Trabajo Social", 10, 1900000, 22, 17 ],
    "UDA-CNT": [ "Universidad de Antioquia", "Medellin", "Contaduria", 12, 2300000, 17, 17 ],
    "INC-ENF": [ "Universidad Incca de Colombia", "Medellin", "Enfermeria", 8, 3800000, 19, 18 ],
    "UNL-CMS": [ "Universidad Libre", "Cartagena", "Comunicación Social", 9, 1400000, 17, 19 ],
    "UNC-PER": [ "Universidad Nacional de Colombia", "Barranquilla", "Periodismo", 8, 2800000, 18, 16 ],
    "UNC-VET": [ "Universidad Nacional de Colombia", "Medellin", "Veterinaria", 10, 2100000, 19, 10 ],
    "CMA-ECO": [ "Colegio Mayor de Antioquia", "Bello", "Economia", 10, 3800000, 38, 10 ],
    "UNC-ADE": [ "Universidad Nacional de Colombia", "Cartagena", "Administracion de Empresas", 10, 2900000, 35, 13 ],
    "UNL-PUB": [ "Universidad Libre", "Cali", "Publicidad", 10, 2900000, 19, 14 ],
    "FPS-SOC": [ "Universidad Francisco de Paula Santander", "Cucuta", "Trabajo Social", 8, 2900000, 4, 16 ],
    "UNL-ADE": [ "Universidad Libre", "Bogota", "Administracion de Empresas", 10, 1900000, 31, 15 ],
    "UCB-SOC": [ "Universidad de Córdoba", "Sincelejo", "Trabajo Social", 8, 4500000, 24, 10 ],
    "UTO-ENF": [ "Universidad del Tolima", "Ibague", "Enfermeria", 8, 4500000, 28, 12 ],
    "UCM-SIS": [ "Universidad Católica de Manizales", "Manizales", "Ingenieria de Sistemas", 12, 2800000, 17, 12 ],
    "UIS-IND": [ "Universidad Industrial de Santander", "Bucaramanga", "Ingenieria Industrial", 10, 1400000, 19, 11 ],
    "UAT-ENF": [ "Universidad del Atlántico", "Barranquilla", "Enfermeria", 8, 2450000, 22, 19 ],
    "UPN-ELC": [ "Universidad Pedagógica Nacional", "Cartagena", "Ingenieria Electronica", 11, 2100000, 1, 19 ],
    "CMA-MED": [ "Colegio Mayor de Antioquia", "Bello", "Medicina", 12, 3800000, 29, 11 ],
    "UMG-PER": [ "Universidad del Magdalena", "Sincelejo", "Periodismo", 8, 4500000, 18, 15 ],
    "UCM-CMS": [ "Universidad Católica de Manizales", "Manizales", "Comunicación Social", 9, 4200000, 1, 19 ],
    "UNL-PER": [ "Universidad Libre", "Pereira", "Periodismo", 8, 2800000, 7, 19 ],
    "UCM-MED": [ "Universidad Católica de Manizales", "Armenia", "Medicina", 10, 1900000, 23, 11 ],
    "UDC-PUB": [ "Universidad de Cartagena", "Cartagena", "Publicidad", 8, 2650000, 36, 13 ],
    "USB-MED": [ "Universidad de San Buenaventura", "Cali", "Medicina", 10, 1900000, 8, 13 ],
    "UDP-PER": [ "Universidad de Pamplona", "Tunja", "Periodismo", 10, 1900000, 29, 14 ],
    "UCB-SIS": [ "Universidad de Córdoba", "Monteria", "Ingenieria de Sistemas", 10, 4200000, 16, 15 ],
    "INC-VET": [ "Universidad Incca de Colombia", "Cali", "Veterinaria", 8, 3600000, 6, 17 ],
    "EAF-PRE": [ "Universidad EAFIT", "Bello", "Pre-Escolar", 9, 4500000, 14, 19 ],
    "UDC-IMM": [ "Universidad de Cartagena", "Conveñas", "Ingenieria Multimedia", 10, 4200000, 24, 12 ],
    "UTP-IMM": [ "Universidad Tecnológica de Pereira", "Pereira", "Ingenieria Multimedia", 10, 2900000, 32, 10 ],
    "UPN-ECO": [ "Universidad Pedagógica Nacional", "Cali", "Economia", 11, 1400000, 13, 10 ],
    "UNC-CMS": [ "Universidad Nacional de Colombia", "Neiva", "Comunicación Social", 9, 1400000, 10, 13 ],
    "UMG-MED": [ "Universidad del Magdalena", "Riohacha", "Medicina", 10, 1900000, 30, 11 ],
    "UTP-PUB": [ "Universidad Tecnológica de Pereira", "Pereira", "Publicidad", 10, 2800000, 23, 15 ],
    "UDC-CMS": [ "Universidad de Cartagena", "Tolu", "Comunicación Social", 9, 1900000, 17, 12 ],
    "USB-ELC": [ "Universidad de San Buenaventura", "Cali", "Ingenieria Electronica", 12, 2800000, 20, 10 ],
    "UDP-IND": [ "Universidad de Pamplona", "Pamplona", "Ingenieria Industrial", 10, 4500000, 38, 10 ],
    "INC-MED": [ "Universidad Incca de Colombia", "Bogota", "Medicina", 12, 1900000, 4, 18 ],
    "FPS-SIS": [ "Universidad Francisco de Paula Santander", "Tunja", "Ingenieria de Sistemas", 10, 1400000, 20, 10 ],
    "UMG-CMS": [ "Universidad del Magdalena", "Santa Marta", "Comunicación Social", 9, 4200000, 10, 17 ],
    "UCB-ELC": [ "Universidad de Córdoba", "Cartagena", "Ingenieria Electronica", 10, 1280000, 9, 11 ],
    "UNC-ECO": [ "Universidad Nacional de Colombia", "Pasto", "Economia", 11, 4500000, 22, 15 ],
    "UTO-VET": [ "Universidad del Tolima", "Neiva", "Veterinaria", 10, 2800000, 12, 14 ],
    "UCA-ADE": [ "Universidad del Cauca", "Popayan", "Administracion de Empresas", 10, 2800000, 30, 13 ],
    "UAN-PUB": [ "Universidad Antonio Nariño", "Bogota", "Publicidad", 8, 3600000, 20, 15 ],
    "UNC-ENF": [ "Universidad Nacional de Colombia", "Bogota", "Enfermeria", 8, 1900000, 37, 12 ],
    "UNC-IND": [ "Universidad Nacional de Colombia", "Popayan", "Ingenieria Industrial", 12, 4200000, 33, 14 ],
    "UDC-PER": [ "Universidad de Cartagena", "Cartagena", "Periodismo", 10, 2800000, 28, 16 ],
    "UPN-MED": [ "Universidad Pedagógica Nacional", "Popayan", "Medicina", 14, 3600000, 22, 19 ],
    "UNC-MED": [ "Universidad Nacional de Colombia", "Cali", "Medicina", 14, 2300000, 4, 16 ],
    "UDP-PUB": [ "Universidad de Pamplona", "Cucuta", "Publicidad", 10, 1900000, 6, 14 ],
    "UTP-CMS": [ "Universidad Tecnológica de Pereira", "Armenia", "Comunicación Social", 9, 1400000, 29, 11 ],
    "UCB-VET": [ "Universidad de Córdoba", "Barranquilla", "Veterinaria", 8, 1900000, 32, 15 ],
    "UPN-VET": [ "Universidad Pedagógica Nacional", "Sincelejo", "Veterinaria", 10, 2800000, 25, 17 ],
    "UNC-PUB": [ "Universidad Nacional de Colombia", "Armenia", "Publicidad", 10, 2800000, 28, 14 ],
    "UTO-ECO": [ "Universidad del Tolima", "Ibague", "Economia", 11, 1900000, 26, 16 ],
    "UMG-ELC": [ "Universidad del Magdalena", "Santa Marta", "Ingenieria Electronica", 10, 2800000, 29, 17 ],
    "USB-SIS": [ "Universidad de San Buenaventura", "Medellin", "Ingenieria de Sistemas", 11, 2650000, 29, 18 ],
    "EAF-IND": [ "Universidad EAFIT", "Medellin", "Ingenieria Industrial", 12, 2900000, 18, 18 ],
    "UCB-ENF": [ "Universidad de Córdoba", "Valledupar", "Enfermeria", 8, 1900000, 29, 17 ],
    "PUJ-IND": [ "Pontificia Universidad Javeriana", "Bogota", "Ingenieria Industrial", 12, 3600000, 12, 15 ],
    "UAT-VET": [ "Universidad del Atlántico", "Cartagena", "Veterinaria", 8, 4500000, 30, 11 ],
    "UIS-PRE": [ "Universidad Industrial de Santander", "Bucaramanga", "Pre-Escolar", 10, 1400000, 6, 15 ],
    "UDC-ADE": [ "Universidad de Cartagena", "Cartagena", "Administracion de Empresas", 10, 2100000, 16, 11 ],
    "UPB-IND": [ "Universidad Pontificia Bolivariana ", "Medellin", "Ingenieria Industrial", 12, 3600000, 22, 18 ],
    "USL-CNT": [ "Universidad de la Salle", "Bogota", "Contaduria", 12, 3800000, 12, 19 ],
    "EAF-IMM": [ "Universidad EAFIT", "Medellin", "Ingenieria Multimedia", 10, 2800000, 16, 16 ],
    "UDM-ENF": [ "Universidad de América", "Manizales", "Enfermeria", 8, 1900000, 23, 19 ],
    "CMA-ELC": [ "Colegio Mayor de Antioquia", "Bello", "Ingenieria Electronica", 11, 4500000, 31, 14 ],
    "UDM-ECO": [ "Universidad de América", "Pereira", "Economia", 11, 3600000, 5, 19 ],
    "UDM-VET": [ "Universidad de América", "Armenia", "Veterinaria", 10, 4500000, 26, 16 ],
    "UCA-IMM": [ "Universidad del Cauca", "Pasto", "Ingenieria Multimedia", 10, 1900000, 20, 19 ],
    "CMA-ENF": [ "Colegio Mayor de Antioquia", "Medellin", "Enfermeria", 8, 2300000, 14, 14 ],
    "UCA-PUB": [ "Universidad del Cauca", "Neiva", "Publicidad", 8, 1900000, 6, 15 ] }

def sumar(profesiones, campo):
    """ (dicc, int) -> int

    Retorna la suma de todos los valores en un campo

    >>> sumar(profesiones, HOMBRES)
    2281
    >>> sumar(profesiones, MUJERES)
    1741

    """
    total = 0
    for codigo in profesiones.keys():
        total += profesiones[codigo][campo]
    return total

def seleccionar(profesiones, campo, valor):
    """ (dicc, int, any) -> dicc

    Seleccionar los registros cuyo campo sea igual a valor y
    retorna un diccionario con ellos

    """
    dicc = dict()
    for codigo in profesiones.keys():
        if profesiones[codigo][campo] == valor:
            dicc[codigo] = profesiones[codigo]
    return dicc

def total_hombres(profesiones):
    """ (diccionario) -> int

    Retorna el total de hombres

    >>> total_hombres(profesiones)
    2281

    """
    return sumar(profesiones, HOMBRES)

def total_mujeres(profesiones):
    """ (diccionario) -> int

    Retorna el total de mujeres

    >>> total_mujeres(profesiones)
    1741

    """
    return sumar(profesiones, MUJERES)

# Pruebas
if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Principal

# Total hombres y mujeres
print("Total Hombres :", total_hombres(profesiones))
print("Total Mujeres:", total_mujeres(profesiones))

# Oferta de programas en Popayan, y Total hombres
popayan = seleccionar(profesiones, CIUDAD, 'Popayan')
print(popayan)
print("Cuanta oferta hay en Popayan :", len(popayan))
print("Total Hombres en Popayan :", total_hombres(popayan))

# Total de Programas por Ciudad
# Total de Hombres y de Mujeres por Ciudad
# Promedio del valor de la Matricula por Ciudad
# Total de Hombres y de Mujeres por Universidad
# Total de Hombres y de Mujeres por Programa
# Promedio de Hombres y de Mujeres por Programas
# Promedio del valor de la Matricula por Programas