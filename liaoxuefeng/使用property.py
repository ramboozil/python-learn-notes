class Student(object):
    # score = None

    def get__score(self):
        return self.score

    def set__score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer!')
        elif score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        else:
            self.score = score


s = Student()
# s.set__score(101)
print(dir(s))
# print(Student.score)


class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer!')
        elif score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100')
        else:
            self._score = score


s2 = Student2()
s2.score = '101'
print(s2.score)