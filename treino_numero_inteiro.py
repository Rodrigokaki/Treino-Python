def main():
    usuario = input('Digite um numero por inteiro: ')
    if usuario.isnumeric():
        pass
    else:
        print('Voce deve digitar apenas numeros')
        main()
    numero = ""
    casas = 0
    numero_1 = False

    for i in usuario:
        casas += 1

    if casas >= 4:
            conversor0000 = {1:'mil', 2:'dois mil', 3:'tres mil', 4:'quatro mil', 5:'cinco mil', 6:'seis mil', 7:'sete mil', 8:'oito mil', 9:'nove mil'}
            numero += conversor0000[int(usuario[-4])]

    if casas >= 3:
        conversor000 = {1:'cento', 2:'duzentos', 3:'trezentos', 4:'quatrocentos', 5:'quinhentos',6:'seiscentos', 7:'setecentos', 8:'oitocentos', 9:'novecentos', 0:''}
        if casas > 3 and usuario[-3] != '0':
            numero += ' '
        numero += conversor000[int(usuario[-3])]

    if casas >= 2:
        conversor00 = {2:'vinte', 3:'trinta', 4:'quarenta', 5:'cinquenta',6:'sessenta', 7:'setenta', 8:'oitenta', 9:'noventa', 0:''}
        if casas > 2 and usuario[-2] != '0' and usuario[-2] != '1':
            numero += ' e '
        if usuario[-2] != '1':
            numero += conversor00[int(usuario[-2])]
        else:
            numero_1 = True
            pass

    if casas >= 1:
        conversor0 = {1:'um', 2:'dois', 3:'tres', 4:'quatro', 5:'cinco',6:'seis', 7:'sete', 8:'oito', 9:'nove', 0:""}
        conversor1 = {1:'onze', 2:'doze', 3:'treze', 4:'quatorze', 5:'quinze',6:'dezesseis', 7:'dezessete', 8:'dezoito', 9:'dezenove',0:"dez"}
        if numero_1 == True:
            if casas > 2:
                numero += ' e '
            numero += conversor1[int(usuario[-1])]
        else:
            if usuario[-2] == '2':
                numero += ' '
            elif usuario[-1] != '0':
                numero += ' e '
            numero += conversor0[int(usuario[-1])]

    if usuario == '100':
        numero = 'cem'

    print(numero)

main()