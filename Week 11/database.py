
import sqlite3

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect('Software Bootcamp/Week 11/filmflix.db')
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def add_record(self, film):
        sql = '''INSERT INTO tblFilms(title, yearReleased, rating, duration, genre)
                 VALUES(?,?,?,?,?)'''
        self.cursor.execute(sql, film)
        self.conn.commit()

    def delete_record(self, film_id):
        sql = 'DELETE FROM tblFilms WHERE id = ?'
        self.cursor.execute(sql, (film_id,))
        self.conn.commit()

    def update_record(self, film_id, film):
        sql = '''UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ?
                 WHERE id = ?'''
        self.cursor.execute(sql, film + (film_id,))
        self.conn.commit()

    def fetch_all_records(self):
        sql = 'SELECT * FROM tblFilms'
        return self.execute_query(sql)

    def fetch_records_by_genre(self, genre):
        sql = 'SELECT * FROM tblFilms WHERE genre = ?'
        return self.execute_query(sql, (genre,))

    def fetch_records_by_year(self, year):
        sql = 'SELECT * FROM tblFilms WHERE yearReleased = ?'
        return self.execute_query(sql, (year,))

    def fetch_records_by_rating(self, rating):
        sql = 'SELECT * FROM tblFilms WHERE rating = ?'
        return self.execute_query(sql, (rating,))

    def close(self):
        self.conn.close()

