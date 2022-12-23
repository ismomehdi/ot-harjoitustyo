from db.config import connect


class HighScoreRepository:
    def __init__(self):
        connection = connect()
        self.cursor = connection.cursor()

    def check_if_top_ten(self, score, level):
        if self.count_rows() < 10:
            return True

        self.delete_excess_rows()
        lowest_high_score = 'SELECT score FROM high_scores WHERE level = :level ORDER BY score LIMIT 1'
        lowest_high_score = self.cursor.execute(
            lowest_high_score, {'level': level}).fetchone()

        if lowest_high_score is None:
            return True
        
        elif score > lowest_high_score['score']:
            return True

    def count_rows(self):
        self.cursor.execute('SELECT COUNT(*) FROM high_scores')
        count = self.cursor.fetchone()[0]

        return count

    def delete_excess_rows(self):
        high_scores = 'SELECT id FROM high_scores ORDER BY score DESC LIMIT 10'
        self.cursor.execute(
            f'DELETE FROM high_scores WHERE id NOT IN ({high_scores})')

    def add(self, level, name, score):
        self.cursor.execute('INSERT INTO high_scores (level, name, score) VALUES (:level, :name, :score)', {
                            'level': level, 'name': name, 'score': score})

        self.cursor.connection.commit()

    def get_top_ten(self, level):
        high_scores = 'SELECT name, score FROM high_scores \
            WHERE level = :level ORDER BY score DESC, id DESC LIMIT 10'
        high_scores = self.cursor.execute(
            high_scores, {'level': level}).fetchall()

        return high_scores
