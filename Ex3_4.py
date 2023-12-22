"""
เขียนฟังก์ชัน char_count(str) โดยรับพารามิเตอร์ 1 ตัว เป็นข้อมูลชนิด string และให้ส่งคืนเป็น
dictionary ที่มี key เป็นตัวอักษรแต่ละตัวของ string นั้น และ value คือ จํานวนครั้งที่ตัวอักษรนั้นปรากฏ
ใน string เช่น
Input : 'language'
return : {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'e': 1}
"""

def char_count(str):
  str = {str[x]: str.count(str[x]) for x in range(len(str))}
  return str

#print(char_count('language'))
#{'l': 1, 'a': 2, 'n': 1, 'g': 2, 'e': 1, 'u':1})
#print(char_count('aabbbccccdddddd'))
#{'a':2,'b':3,'c':4,'d':6})

"""
Oat's style

def char_count(str):
    return {i: str.count(i) for i in str}

#print(char_count("language"))
"""