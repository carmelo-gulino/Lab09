from database.DB_connect import DBConnect
from model.flight import Flight
from model.airport import Airport


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_all_airports():
        """
        Interroga il database e recupera tutti i voli
        """
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        result = []
        query = "SELECT * FROM airports"
        cursor.execute(query)
        for row in cursor:
            result.append(
                Airport(row["ID"], row["IATA_CODE"], row["AIRPORT"], row["CITY"], row["STATE"],
                       row["COUNTRY"], row["LATITUDE"], row["LONGITUDE"], row["TIMEZONE_OFFSET"])
            )
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_all_flights():
        """
        Interroga il database e recupera tutti i voli
        """
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        result = []
        query = "SELECT * FROM flights"
        cursor.execute(query)
        for row in cursor:
            result.append(
                Flight(row["ID"], row["AIRLINE_ID"], row["FLIGHT_NUMBER"], row["TAIL_NUMBER"], row["ORIGIN_AIRPORT_ID"],
                       row["DESTINATION_AIRPORT_ID"], row["SCHEDULED_DEPARTURE_DATE"], row["DEPARTURE_DELAY"],
                       row["ELAPSED_TIME"], row["DISTANCE"], row["ARRIVAL_DATE"], row["ARRIVAL_DELAY"])
            )
        cursor.close()
        cnx.close()
        return result


if __name__ == '__main__':
    result = DAO.get_all_airports()
    for a in result:
        print(a)
