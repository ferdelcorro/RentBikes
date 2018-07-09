# -*- coding: utf-8 -*-

from rent import Rent
from general import check_positive_number, insert_number, check_empty


def main():
    obj = Rent()
    option = '0'
    while option != '4':
        print '\n' * 3
        print '=' * 30
        print 'Vamos a alquilar una bici'
        print '1) Alquilar bicis'
        print '2) Ver bicicletas alquiladas'
        print '3) Ver precios'
        print '4) Salir'
        print '=' * 30
        option = raw_input('Ingrese la opcion: ')
        is_valid_option = check_positive_number(option)

        if is_valid_option:
            if option == '1':
                bikes = insert_number('Ingrese la cantidad de bicicletas: ')
                hours = insert_number('Ingrese la cantidad de horas: ')
                family = check_empty('¿Es una familia? (Y/N): ')
                is_family = family.upper() == "Y"
                if is_family:
                    surname = check_empty('Ingrese el apellido: ')
                else:
                    surname = None
                rent = obj.rent_bikes(bikes, hours, family=is_family, surname=surname)
                print 'El precio a abonar es $%s' % rent["price"]
                raw_input('Presione enter para continuar')
            elif option == '2':
                rents = obj.show_rents()
                if rents:
                    for rent in rents:
                        bikes = rent["bikes"]
                        hours = rent["hours"]
                        return_time = rent["return_time"]
                        surname = rent["family_surname"]
                        msg = '\nSe alquilardon %s bicicletas por %s horas\na devolver el %s\n' % (bikes, hours, return_time)
                        if surname:
                            msg += 'a la familia %s\n' % surname
                        print msg
                else:
                    print 'Aún no se alquiladó ninguna bicicleta'
                raw_input('Presione enter para continuar')
            elif option == '3':
                prices = obj.show_prices()
                print '\nLos precios son:'
                print '$%s la hora' % prices["hour"]
                print '$%s el día' % prices["day"]
                print '$%s la semana\n' % prices["week"]
                raw_input('Presione enter para continuar')
            elif option == '4':
                confirmacion = check_empty('Está seguro? Y/N: ')
                if confirmacion.upper() == 'N':
                    option = 0
                    print 'Se cancelo la salida'
                    raw_input('Presione enter para continuar')
            else:
                print ('No es una opción válida')
                raw_input('Presione enter para continuar')
        else:
            print 'No es una opción válida'
            raw_input('Presione enter para continuar')


if __name__ == '__main__':
    main()
