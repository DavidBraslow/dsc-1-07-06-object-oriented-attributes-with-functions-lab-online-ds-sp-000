import copy

class School:
    def __init__(self, name = None):
        self.name = name
        self._roster = {}
    
    def get_roster(self):
        return self._roster
    
    def add_student(self, stud_name, stud_grade):
        if stud_grade not in self._roster.keys():
            self._roster[stud_grade] = []
            
        self._roster[stud_grade].append(stud_name)
        
    def grade(self, grade = 0):
        if grade in self._roster.keys():
            return self._roster[grade]
        
    def sort_roster(self):
        for grade in self._roster.keys():
            self._roster[grade] = sorted(self._roster[grade])
        return self._roster
    
    roster = property(get_roster, add_student)
