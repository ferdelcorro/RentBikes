# -*- coding: utf-8 -*-


def check_empty(text):
    inserted = raw_input(text)
    if not inserted:
        print 'Debe ingresar un dato'
        return check_empty(text)
    return inserted


def check_positive_number(number):
    try:
        number = int(number)
    except ValueError:
        return False
    else:
        return number >= 0


def insert_number(text):
    inserted = check_empty(text)
    # inserted_number = raw_input(text)
    is_valid = check_positive_number(inserted)
    if not is_valid:
        print 'La cantidad ingresada no es válida'
        return insert_number(text)
    return int(inserted)
