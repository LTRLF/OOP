"""
ให้นําโปรแกรมตามข้อ 1 มาขยายความสามารถให้รองรับนักศึกษาหลายคน โดยให้ refactor ฟังก์ชัน
add_score ให้รับพารามิเตอร์เป็น add_score(subject_score, student, subject, score) โดย student
เป็นข้อมูลของนักศึกษาเป็น string (ในที่นี้เป็น id) และ return เป็น dictionary
Input : subject_score = { }, student = '65010001', subject = 'python', score = 50
return : { '65010001' : { 'python' : 50 } }
input : subject_score = { '65010001' : { 'python' : 50 } },
student = '65010001', subject = ‘calculus’, score = 60
return : {'65010001': {'python’: 50, 'calculus', 60} }
โดยหากชื่อมีข้อมูล key ใดที่มีใน dictionary อยู่แล้ว ให้ถือเป็นการ update ข้อมูลนั้น

ให้ refactor ฟังก์ชัน calc_average_score โดยให้ส่งคืนเป็น dictionary ของนักศึกษาและคะแนนเฉลี่ย
ของนักศึกษาคนนั้น เช่น {'65010001': '55.00' }
"""


def add_score(subject_score, student, subject, score):
  #ถ้าไม่มี id นั้นๆให้ทำการสร้างขึ้นมาใหม่เลย
  if student not in subject_score:
    subject_score[student] = {subject: score}

  subject_score[student][subject] = score
  return subject_score


def calc_average_score(subject_score):
  x = {}
  #มี ID กี่ตัว ก็ทำเท่านั้นรอบ
  for student in subject_score.keys():
    # ex. {'66010840': {'math': 90, 'oop': 90}
    #total = {'math': 90, 'oop': 90} 
    #โดย '66010840'= keys {'math': 90, 'oop': 90} = values
    total = subject_score[student].values()
    #การ sum() dictionary python จะ sum แค่ค่าvalues เท่านั้น 
    x[student] = ("{:.2f}".format(sum(total) / len(subject_score[student])))
  return x

# subject = {}
# subject = add_score(subject, '66010840', 'math', 90)
# subject = add_score(subject, '66010840', 'oop', 90)

# subject = add_score(subject, '66010942', 'math', 60)
# subject = add_score(subject, '66010942', 'math', 70)

# print(subject)
# print(calc_average_score(subject))