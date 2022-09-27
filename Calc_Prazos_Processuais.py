# -*- coding: utf-8 -*-
# Dev to: https://github.com/willamylp


from datetime import date, timedelta
from time import strftime

# VALORES CONSTANTES
FERIADOS = ['01/01/2022', '02/01/2022', '03/01/2022', '04/01/2022', '05/01/2022', '06/01/2022',
            '28/02/2022', '01/03/2022', '02/03/2022', '13/04/2022', '14/04/2022', '15/04/2022',
            '21/04/2022', '16/06/2022', '29/06/2022', '11/08/2022', '15/08/2022', '27/08/2022',
            '28/08/2022', '29/08/2022', '30/08/2022', '31/08/2022', '01/09/2022', '02/09/2022',
            '03/09/2022', '04/09/2022', '05/09/2022', '06/09/2022', '07/09/2022', '08/09/2022',
            '09/09/2022', '10/09/2022', '11/09/2022', '03/10/2022', '12/10/2022', '28/10/2022',
            '02/11/2022', '15/11/2022', '08/12/2022', '20/12/2022', '21/12/2022', '22/12/2022',
            '23/12/2022', '24/12/2022', '25/12/2022', '26/12/2022', '27/12/2022', '28/12/2022',
            '29/12/2022', '30/12/2022', '31/12/2022']

DIAS = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
        'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']

HOJE = date.today()

#Cria uma lista de datas entre a Data Inicial e a Data Final
def CriaIntervaloDatas(dataIni, dataFim):
    delta = dataFim - dataIni
    dataList = []

    for i in range(delta.days + 1):
        dia = dataIni + timedelta(i)
        dataList.append(dia)

    return dataList

def CalculadoraCPC(dataIni, prazo):
    dataPivo = dataIni

    # Define a possivel Data Final
    dataFim = (dataIni + timedelta(prazo))

    while(dataPivo <= dataFim):
        # Se a data analisada (Data Pivô) cair no Fim de Semana
        if((DIAS[dataPivo.weekday()] == "Sábado") or (DIAS[dataPivo.weekday()] == "Domingo")):
            dataFim = (dataFim + timedelta(1))

        # Se a data analisada (Data Pivô) cair no Feriado
        elif(dataPivo.strftime("%d/%m/%Y") in FERIADOS):
            dataFim = (dataFim + timedelta(1))

        # Data Pivô +1 dia
        dataPivo = (dataPivo + timedelta(1))

    return dataFim

def CalculadoraCPP(dataIni, prazo):
    # Define a possivel Data Final
    dataFim = (dataIni + timedelta(prazo))

    # Lista de Datas entre a Data Inicial e a Data Final
    datas = CriaIntervaloDatas(dataIni, dataFim)

    # Verifica se cada data individual é Feriado
    for data in datas:
        if(data.strftime("%d/%m/%Y") in FERIADOS):
            # Se a data for Feriado, acrescente +1 dia a Data Final
            dataFim = (dataFim + timedelta(1))
            datas.append(dataFim)

    # Enquanto a Data Final dor no FDS ou Feriado, add +1 dia a Data Final
    while((dataFim.strftime("%d/%m/%Y") in FERIADOS) or (DIAS[dataFim.weekday()] == "Sábado") or (DIAS[dataFim.weekday()] == "Domingo")):
        dataFim = (dataFim + timedelta(1))
    
    return dataFim

# ———————————————————————————————————————————————————————————————————————————————————————— #

if __name__ == '__main__':   
    while(True):
        print(
        '''
        +———————————————————————————————————+
        | Calculadora de Prazos Processuais |
        +———————————————————————————————————+

        + ————————————————————————————————— +
        |   1 - Calculadora CPC             |
        |   2 - Calculadora CPP             |
        |-----------------------------------|
        |   9 - SAIR                        |
        + ————————————————————————————————— +
        ''')
        opcao = input('\tOpção: ')

        if(opcao == '9'):
            exit()

        elif((opcao == '1') or (opcao == '2')):
            # Entradas do Usuário
            dataIni = input('\nData Início: ')
            prazo = int(input('Prazo: '))

            # Formatação da Data digitada para o Padrão Computacional
            dataIni = dataIni.split('/')
            dataIni = date(day=int(dataIni[0]), month=int(dataIni[1]), year=int(dataIni[2]))
            
            if(opcao == '1'):
                dataFim = CalculadoraCPC(dataIni, prazo)
            
            elif(opcao == '2'):
                dataFim = CalculadoraCPP(dataIni, prazo)

            # Saídas / Resultados
            print('\nRESULTADO:')
            print(f'—> Data Final: {dataFim.strftime("%d/%m/%Y")}')
            print(f'—> Dia da Semana: {DIAS[dataFim.weekday()]}')
            atraso = (HOJE - dataFim).days
            
            if(atraso >= 0):
                print(f'—> Status: VENCIDO — ({atraso} DIAS)')
            else:
                print(f'—> Status: NO PRAZO — ({atraso} DIAS)')
        
        else:
            print("\n->> ERRO: INSIRA UMA OPÇÃO VÁLIDA!")
