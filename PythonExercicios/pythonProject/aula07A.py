# Dicionário que mapeia os códigos de horários para as horas correspondentes
horarios = {
    "M1": "07:00 às 07:50", "M2": "07:50 às 08:40", "M3": "08:55 às 09:45",
    "M4": "09:45 às 10:35", "M5": "10:50 às 11:40", "M6": "11:40 às 12:30",
    "T1": "13:00 às 13:50", "T2": "13:50 às 14:40", "T3": "14:55 às 15:45",
    "T4": "15:45 às 16:35", "T5": "16:50 às 17:40", "T6": "17:40 às 18:30",
    "N1": "18:45 às 19:35", "N2": "19:35 às 20:25", "N3": "20:35 às 21:25",
    "N4": "21:25 às 22:15"
}

# Mapeamento de dias da semana
dias_semana = {
    "2": "Segunda-feira", "3": "Terça-feira", "4": "Quarta-feira",
    "5": "Quinta-feira", "6": "Sexta-feira"
}


# Função para adicionar matérias à agenda
def adicionar_materia(agenda, nome_materia, dias, periodos):
    for dia in dias:
        for periodo in periodos:
            if periodo in horarios:
                horario = horarios[periodo]
                agenda[dias_semana[dia]].append(f"{horario} - {nome_materia}")
            else:
                print(f"Horário {periodo} inválido para a matéria {nome_materia}.")


# Função principal para construir a agenda
def criar_agenda():
    agenda = {dia: [] for dia in dias_semana.values()}

    # Solicitar ao usuário quantas matérias ele quer adicionar
    num_materias = int(input("Quantas matérias você quer adicionar? "))

    for _ in range(num_materias):
        nome_materia = input("Nome da matéria: ")
        dias = input("Dias da semana (ex: 246 para segunda, quarta e quinta): ")
        periodos = input("Horários (ex: M56 para 5 e 6 da manhã): ")

        # Separar os períodos corretamente
        periodos_separados = [f"{periodos[0]}{periodos[i]}" for i in range(1, len(periodos))]
        adicionar_materia(agenda, nome_materia, dias, periodos_separados)

    # Exibir a agenda organizada
    for dia, atividades in agenda.items():
        print(f"\n{dia}:")
        if atividades:
            for atividade in atividades:
                print(f"  {atividade}")
        else:
            print("  Nenhuma matéria.")

# Para rodar o programa
criar_agenda()  # Descomente esta linha para rodar a função e testar















