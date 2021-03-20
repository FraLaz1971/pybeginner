#!/usr/bin/env python3
def studentsGrades():
	studname = 'John'
	math = 83
	science = 84
	english = 85
	sum = (math + science + english)
	average = sum/3
	sentence = 'Grades of '+studname+' in Math:'+str(math)+". Science:"+str(science)+". And English:"+str(english)
	print(sentence)
	sentence2 = 'Average:'+str(average)
	print(sentence2)
	return
# main
studentsGrades()

