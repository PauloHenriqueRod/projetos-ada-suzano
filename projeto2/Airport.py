from AirplaneQueue import AirplaneQueue


class Airport:
    def __init__(self):
        self._QUEUE_IDS = ["take off", 1, 2, 3]
        self._AIRSTRIPS_IDS = [1, 2, 3]
        self._AIRSTRIPS_OCCUPIED = {"3": False, "2": False, "1": False}
        self.queues = self.generate_queues()
        self.airstrips = self.generate_airstrips()

    def generate_queues(self):
        queues = []

        for as_id in self._QUEUE_IDS:
            queue = AirplaneQueue(queue_id=as_id)
            queues.append(queue)

        return queues

    def generate_airstrips(self) -> list[dict[str, int]]:
        airstrips = []

        for as_id in self._AIRSTRIPS_IDS:
            airstrips.append({"id": as_id, "count": 0})

        return airstrips
