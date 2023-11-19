import csv

# 클래스 생성
class Student:
    def __init__(self, name, korean, math, english):    # 생성자
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    def calculate_average(self):   # 클래스 안에서 평균 점수를 계산하는 함수
        return (self.korean + self.math + self.english) / 3

def loadData(file_path):
    student_dict = {}
    with open(file_path, "r", encoding="utf8") as fp:
        csv_reader = csv.reader(fp)
        
        # 첫 번째 행은 과목 이름이므로 무시
        next(csv_reader)
        
        for row in csv_reader:
            student_name = row[0]
            korean, math, english = map(float, row[1:])
            student = Student(student_name, korean, math, english)
            student_dict[student_name] = student

    return student_dict

file_path = "student.csv"
students_data = loadData(file_path)

# 각 학생의 평균 점수 출력
for student_name, student in students_data.items():
    average = student.calculate_average()
    print(f"{student_name}의 평균 점수는 {average} 입니다.")