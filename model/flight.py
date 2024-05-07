from datetime import datetime
from dataclasses import dataclass


@dataclass
class Flight:
    _id: int
    _airline_id: int
    _flight_number: int
    _tail_number: str
    _origin_airport_id: int
    _destination_airport_id: int
    _scheduled_departure_date: datetime
    _departure_delay: float
    _elapsed_time: float
    _distance: int
    _arrival_date: datetime
    _arrival_delay: float

    @property
    def id(self):
        return self._id

    @property
    def airline_id(self):
        return self._airline_id

    @property
    def flight_number(self):
        return self._flight_number

    @property
    def tail_number(self):
        return self.tail_number

    @property
    def origin_airport_id(self):
        return self._origin_airport_id

    @property
    def destination_airport_id(self):
        return self._destination_airport_id

    @property
    def scheduled_departure_date(self):
        return self._scheduled_departure_date

    @property
    def departure_delay(self):
        return self._departure_delay

    @property
    def elapsed_time(self):
        return self._elapsed_time

    @property
    def distance(self):
        return self._distance

    @property
    def arrival_date(self):
        return self._arrival_date

    @property
    def arrival_delay(self):
        return self._arrival_delay

    def __str__(self):
        return f"Flight {self.id} #{self.flight_number} from {self.origin_airport_id} to {self.destination_airport_id}"

    def __hash__(self):
        return hash(self.id)
