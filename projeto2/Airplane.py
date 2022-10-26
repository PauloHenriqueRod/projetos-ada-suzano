import string
from random import randint, choice


def generate_id() -> str:
    generated_id = ""
    # Gera a sequencia de letras aleatórias
    for i in range(3):
        generated_id += choice(string.ascii_uppercase)
    # Gera se sequência de números aleatórios
    for i in range(3):
        generated_id += str(randint(0, 9))

    return generated_id


class Airplane:
    def __init__(self, airplane_status: str):
        self.ap_id = generate_id()
        self.ap_status: str = airplane_status
        self.ap_fuel = self.generate_airplane_fuel()
        self.ap_time = 0

    def decrement_fuel(self):
        if self.ap_fuel == 0:
            self.ap_fuel = 0
        else:
            self.ap_fuel -= 1

    def increment_time(self):
        self.ap_time += 1

    def check_emergency_status(self):
        if self.ap_fuel < 3:
            return True
        else:
            return False

    def generate_airplane_fuel(self) -> int:
        if self.ap_status == "landing":
            return randint(2, 20)
        else:
            return randint(15, 22)

    def show_airplane_info(self) -> str:
        airplane_info = ""

        if self.ap_fuel > 0:
            airplane_info = f"\t🆔: {self.ap_id}\t -> {'⚠️' if self.check_emergency_status() else ''} Combustível: {self.ap_fuel} \t -> Tempo de espera {self.ap_time} \t -> Status: {self.ap_status.upper()} "
        else:
            airplane_info = f"\t🆘: Aeronave: {self.ap_id} caiu por falta de combustível"

        return airplane_info

    def check_airplane_break(self):
        if self.ap_fuel == 0:
            return 1
        else:
            return 0
