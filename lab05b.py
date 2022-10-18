infile = open("data.txt","r")
outfile = open("output.txt","w")

lines = infile.readlines()
min_height,min_weight,min_BMI=100000,100000,100000
max_height,max_weight,max_BMI=-100,-100,-100
sum_height,sum_weight,sum_BMI=0,0,0
count=0
print(lines[0][0:12]+lines[0][12:24]+lines[0][24:36]+"BMI         ")
outfile.write(lines[0][0:12]+lines[0][12:24]+lines[0][24:36]+"BMI         \n")
for line in lines[1:]:
  count=count+1
  name=line[0:12]
  height=float(line[12:24])
  weight=float(line[24:36])
  BMI=weight/(height**2)
  sum_height=sum_height+height
  sum_weight=sum_weight+weight
  sum_BMI=sum_BMI+BMI

  if min_height>height:
    min_height=height
  if min_weight>weight:
    min_weight=weight
  if min_BMI>BMI:
    min_BMI=BMI
  #Max values
  if max_height<height:
    max_height=height
  if max_weight<weight:
    max_weight=weight
  if max_BMI<BMI:
    max_BMI=BMI
  print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(name,height,weight,BMI))
  outfile.write("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}\n".format(name,height,weight,BMI))
print()
outfile.write("\n")
print("Average     {:<12.2f}{:<12.2f}{:<12.2f}".format(sum_height/count,sum_weight/count,sum_BMI/count))
outfile.write("Average     {:<12.2f}{:<12.2f}{:<12.2f}\n".format(sum_height/count,sum_weight/count,sum_BMI/count))
print("Max         {:<12.2f}{:<12.2f}{:<12.2f}".format(max_height,max_weight,max_BMI))
outfile.write("Max         {:<12.2f}{:<12.2f}{:<12.2f}\n".format(max_height,max_weight,max_BMI))
print("Min         {:<12.2f}{:<12.2f}{:<12.2f}".format(min_height,min_weight,min_BMI))
outfile.write("Min         {:<12.2f}{:<12.2f}{:<12.2f}\n".format(min_height,min_weight,min_BMI))
outfile.close()
