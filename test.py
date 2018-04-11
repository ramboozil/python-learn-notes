class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score not in range(101):
            raise ValueError()
        if self.score >= 60 and self.score < 80:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'
