def options_menu():
    print('1. Segundo para minuto.\n2. Minuto para hora.\n3. Hora para minuto.\n4. Minuto para segundo.\n5. Segundo para hora.\n6. Hora para segundo.')

# Calculation for conversions
def sec_min():
    sec = int(input('Insira os segundos: '))
    min = round((sec / 60), 2)
    print('A conversão de ', sec, ' segundos para minutos é igual a {0}'.format(min))

def min_hour():
    min = int(input('Insira os minutos: '))
    hour = round((min / 60), 2)
    print('A conversão de ', min, ' minutos para horas é igual a {0}'.format(hour))

def hour_min():
    hour = int(input('Insira a(s) hora(s): '))
    min = round((hour * 60), 2)
    print('A conversão de ', hour, ' hora(s) para minutos é igual a {0}'.format(min)) 


def min_sec():
    min = int(input('Insira os minutos: '))
    sec = round((min * 60), 2)
    print('A conversão de ', min, ' minutos para segundos é igual a {0}'.format(sec))

def sec_hour():
    sec = int(input('Insira os segundos: '))
    hour = round((sec / 3600), 2)
    print('A conversão de ', hour, ' hora(s) para minutos é igual a {0}'.format(hour))

def hour_sec():
    hour = int(input('Insira a(s) hora(s): '))
    sec = round((hour * 3600), 2)
    print('A conversão de ', hour, ' hora(s) para segunds é igual a {0}'.format(sec))    

options_menu()

# Choose which conversion
conversion_choice = input('Selecione o número da conversão que você gostaria de realizar: ')

while int(conversion_choice) <= 6:
    if int(conversion_choice) == 1:
        sec_min()
    elif int(conversion_choice) == 2:
        min_hour()
    elif int(conversion_choice) == 3:
        hour_min()
    elif int(conversion_choice) == 4:
        min_sec()
    elif int(conversion_choice) == 5:
        sec_hour()
    elif int(conversion_choice) == 6:
        hour_sec()
    else:
        print('Selecione uma opção válida!')
        options_menu()
    break    
