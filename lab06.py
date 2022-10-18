score_obj = open('scores.txt', 'r')
score = open('outscores.txt', 'w')




count = 0
student_list = []
total_list = [0,0,0,0]

print("{:21s}{:6s}{:6s}{:6s}{:6s}{:>9s}".format('Name', 'Exam1', 'Exam2', 'Exam3', 'Exam4', 'Mean'))

for line in score_obj:
    count = count + 1
    line = line.strip('\n').strip()
    line = line.split()
    
    name = line[0] + ' ' + line[1]
    exam_1 = int(line[2])
    exam_2 = int(line[3])
    exam_3 = int(line[4])
    exam_4 = int(line[5])
    mean = (exam_1 + exam_2 + exam_3 + exam_4)/4
    mean_d = round(mean,2)
    total_list[0] += exam_1
    total_list[1] += exam_2
    total_list[2] += exam_3
    total_list[3] += exam_4
    tup = (name, exam_1, exam_2, exam_3, exam_4, mean_d)
    student_list.append(tup)
student_list_sort = sorted(student_list)
for i in student_list_sort:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(i[0],i[1],i[2],i[3],i[4], i[5]))
mean_list =[total_list[0]/count, total_list[1]/count, total_list[2]/count, total_list[3]/count]
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format('Exam Mean', mean_list[0],mean_list[1]
,mean_list[2], mean_list[3]))

score_obj.close()
score.close()