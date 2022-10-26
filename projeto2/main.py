from Airport import Airport
import csv

landing_time = 0
take_off_time = 0
landings = 0
take_offs = 0
breaks = 0
AP_STATUS_LANDING = "landing"
AP_STATUS_TAKE_OFF = "take off"

new_airport = Airport()
AIRPORT_QUEUES = new_airport.generate_queues()
AIRPORT_AIRSTRIPS = new_airport.generate_airstrips()

iteracoes = 0
is_on = True
while is_on:

    iteracoes += 1

    new_airport._AIRSTRIPS_OCCUPIED = {"3": False, "2": False, "1": False}
    # varre todos os aviões e verifica se tem emergencia
    list_ap_emergency = []

    for airplane_queue in AIRPORT_QUEUES:
        for ap in airplane_queue.queue:
            emergency_ap = ap.check_emergency_status
            if emergency_ap:
                list_ap_emergency.append(ap)
    emergency = list_ap_emergency

    if emergency:
        for airplane_queue in AIRPORT_QUEUES:
            if airplane_queue.queue_id == "take off":
                pass
            else:
                # aterrissa em emergencia
                for airplane in emergency:
                    for queue in AIRPORT_QUEUES:
                        if airplane in queue.queue and airplane.check_emergency_status():
                            # verifica pistas disponíveis
                            for airstrip in new_airport._AIRSTRIPS_OCCUPIED:

                                # pousa se não estiver ocupada
                                if not new_airport._AIRSTRIPS_OCCUPIED[airstrip]:
                                    airstrip_chosen = airstrip

                                    # ocupa a pista
                                    new_airport._AIRSTRIPS_OCCUPIED[airstrip] = True

                                    break
                            # retira avião da fila
                            queue.queue.pop(queue.queue.index(airplane))
                            print(f'O avião de matrícula {airplane.ap_id} pousou em emergência na pista {airstrip_chosen}')
                            landing_time += airplane.ap_time
                            landings += 1

    for airplane_queue in AIRPORT_QUEUES:
        # decola se não tiver ocorrido emergencias

        if (not new_airport._AIRSTRIPS_OCCUPIED["1"]) and (not new_airport._AIRSTRIPS_OCCUPIED["2"]) and (not new_airport._AIRSTRIPS_OCCUPIED["3"]):

            if airplane_queue.queue_id == "take off":
                take_off_time += airplane_queue.waiting_time()  # Soma o tempo de espera
                take_offs += 1  # Adiciona na quantidade total de decolagnes
                print('')
                airplane_queue.update_queue()
                airstrip = str((iteracoes % 2) + 1)  # alterna entre 1 e 2
                new_airport._AIRSTRIPS_OCCUPIED[airstrip] = True


        if not airplane_queue.queue_id == "take off":  # esse if é somente pouso
            if not new_airport._AIRSTRIPS_OCCUPIED[str(airplane_queue.queue_id)]:
                landing_time += airplane_queue.waiting_time()
                landings += 1
                airplane_queue.update_queue()  # pousa se não estiver ocupada a pista
                new_airport._AIRSTRIPS_OCCUPIED[str(airplane_queue.queue_id)] = True
        if airplane_queue.queue_id == "take off":
            airplane_queue.generate_airplanes(AP_STATUS_TAKE_OFF)
            airplane_queue.show_queue_info()
            for airplane in airplane_queue.queue:
                airplane.increment_time()

        else:
            airplane_queue.generate_airplanes(AP_STATUS_LANDING)
            airplane_queue.show_queue_info()
            for airplane in airplane_queue.queue:
                airplane.decrement_fuel()
                airplane.increment_time()
                breaks += airplane.check_airplane_break()

    operation = input("[1] - Executar | [2] - Parar: ").lower()

    if operation == ("2" or "parar"):
        is_on = False

dict_record = {'Pousos': landings, 'Tempo medio para pouso': round(landing_time/landings, 2),
               'Decolagens': take_offs, 'Tempo médio para decolagem': round(take_off_time/take_offs, 2),
               'Média de quedas': breaks/landings}

record = f'''POUSOS: {dict_record['Pousos']}
TEMPO MÉDIO PARA POUSO: {dict_record['Tempo medio para pouso']}
DECOLAGENS: {dict_record['Decolagens']}
TEMPO MÉDIO PARA DECOLAGEM: {dict_record['Tempo médio para decolagem']}
MÉDIA DE QUEDAS: {dict_record['Média de quedas']}
'''
print(record)

with open('aiport.txt', 'w+') as file:
    file.write(record)
