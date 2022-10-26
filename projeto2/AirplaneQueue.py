from Airplane import Airplane
from random import randint


class AirplaneQueue:
    def __init__(self, queue_id):
        self.queue_id = queue_id
        self.queue = []

    def generate_airplanes(self, ap_status: str):
        waiting_queue = len(self.queue)
        waiting_queue_limit = 3

        if waiting_queue == 0:
            for i in range(randint(0, waiting_queue_limit)):
                self.queue.append(Airplane(airplane_status=ap_status))
        elif waiting_queue == 1:
            for i in range(randint(0, waiting_queue_limit - 1)):
                self.queue.append(Airplane(airplane_status=ap_status))
        elif waiting_queue == 2:
            self.queue.append(Airplane(airplane_status=ap_status))
        else:
            pass

    def get_queue_icon(self):
        if self.queue_id == 1:
            return "🟦"
        elif self.queue_id == 2:
            return "🟩"
        elif self.queue_id == 3:
            return "🟪"
        else:
            return "🛫"

    def show_queue_info(self):
        # Exibir informações as pistas de pouso
        landing_queue = self.queue_id == 1 or self.queue_id == 2 or self.queue_id == 3

        if landing_queue:
            print(f"Fila de pouso {self.queue_id}: {self.get_queue_icon()} {len(self.queue)} aviões na fila")
            for index, airplane in enumerate(self.queue):
                if index == 0:
                    if airplane.ap_fuel == 0:
                        pass
                    else:
                        print(f"{airplane.show_airplane_info()} -> Pouso previsto")
                else:
                    print(airplane.show_airplane_info())
        else:
            print(f"Fila de decolagem {self.get_queue_icon()}: -> {len(self.queue)} aviões na fila")
            for airplane in self.queue:
                print(airplane.show_airplane_info())

    def remove_airplane(self):
        removed_airplane = self.queue.pop()
        print(removed_airplane)

    def waiting_time(self):
        if self.queue:
            return self.queue[0].ap_time
        else:
            return 0

    def update_queue(self):
        if self.queue:
            if self.queue_id == "take off":
                print(f'O avião {self.queue[0].ap_id} decolou!')
            else:
                print(f'O avião {self.queue[0].ap_id} pousou!')
            if len(self.queue) > 1:
                for i in range(0, len(self.queue) - 1):
                    self.queue[i] = self.queue[i + 1]

        self.queue = self.queue[: -1]



