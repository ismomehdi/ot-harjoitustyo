from db.config import connect


class HighScoreRepository:
    def __init__(self):
        """The HighScoreRepository class is used to interact with the
            high_scores table in the database.
        """
        connection = connect()
        self.cursor = connection.cursor()

    def check_if_top_ten(self, score, level):
        """Checks if the score is in the top ten scores.

        Args:
            score: An integer representing the score.
            level: An integer representing the level.

        Returns:
            boolean: Returns True if the score is in the top ten.
        """
        if self.count_rows() < 10:
            return True

        self.delete_excess_rows()
        lowest_high_score = 'SELECT score FROM high_scores \
            WHERE level = :level ORDER BY score LIMIT 1'
        lowest_high_score = self.cursor.execute(
            lowest_high_score, {'level': level}).fetchone()

        if lowest_high_score is None:
            return True

        if score > lowest_high_score['score']:
            return True

        return False

    def count_rows(self):
        """Counts the number of rows in the high_scores table.

        Returns:
            integer: Returns the number of rows in the high_scores table.
        """
        self.cursor.execute('SELECT COUNT(*) FROM high_scores')
        count = self.cursor.fetchone()[0]

        return count

    def delete_excess_rows(self):
        """Deletes the rows that are not in the top ten scores.
        """
        high_scores = 'SELECT id FROM high_scores ORDER BY score DESC LIMIT 10'
        self.cursor.execute(
            f'DELETE FROM high_scores WHERE id NOT IN ({high_scores})')

    def add(self, level, name, score):
        """Adds a new high score to the high_scores table.

        Args:
            level: An integer representing the level.
            name: A string representing the name.
            score: An integer representing the score.
        """
        self.cursor.execute('INSERT INTO high_scores (level, name, score) \
            VALUES (:level, :name, :score)', {'level': level, 'name': name, 'score': score})

        self.cursor.connection.commit()

    def get_top_ten(self, level):
        """Gets the top ten scores for the given level.

        Args:
            level: An integer representing the level.

        Returns:
            list: A list of dictionaries containing the name and score.
        """
        high_scores = 'SELECT name, score FROM high_scores \
            WHERE level = :level ORDER BY score DESC, id DESC LIMIT 10'
        high_scores = self.cursor.execute(
            high_scores, {'level': level}).fetchall()

        return high_scores
