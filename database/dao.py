from database.DB_connect import DBConnect
from model.album import Album
from model.artist import Artist
from model.track import Track


class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select ar.id, ar.name, count(*) as numero_album
                from artist ar, album a
                where ar.id = a.artist_id 
                group by ar.id , ar.name
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'], numero_album=row['numero_album'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result #lista di oggetti artista

    @staticmethod
    def get_connessioni():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
            select a1.artist_id as a1,  a2.artist_id as a2, count(*) as somma
            from album a1, album a2, track t1, track t2
            where (a1.id = t1.album_id or a2.id = t2.album_id)
            and t1.id = t2.id
            and a1.artist_id < a2.artist_id 
            group by  a1.artist_id, a2.artist_id
                                
                """
        cursor.execute(query)
        for row in cursor:
            result.append((row["a1"],row["a2"], row["somma"]))
        cursor.close()
        conn.close()
        return result




