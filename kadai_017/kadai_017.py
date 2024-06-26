# -*- coding: utf-8 -*-
"""kadai_017.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aSGj2q9aFOrE2jactyxVFihZ2cPMK5Vk
"""

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}は大人です。")
    else:
      print(f"{self.name}は大人ではありません。")

# インスタンス化
humans = [Human("Mandar", 21), Human("Shete", 20), Human("Ved", 19), Human("Abhinav", 18), Human("Makita", 34)]
for human in humans:
  human.check_adult()