from tabulate import tabulate

#Exam_calc
student_list=["vaibhav","raj","shankar"]
maths_1=[50,40,30]
biology_1=[40,30,50]
chemistry_1=[40,50,30]
physics_1=[70,80,90]
IT_1=[90,70,80]
Total_1=[290,270,280]
percentage_1=[]

#taking index as var
maths=maths_1.index(max(maths_1))
biology=biology_1.index(max(biology_1))
chemistry=chemistry_1.index(max(chemistry_1))
physics=physics_1.index(max(physics_1))
IT=IT_1.index(max(IT_1))

#append into table
n=3;
data=[];
for i in range(n):
    data.append([student_list[i], maths_1[i],biology_1[i],chemistry_1[i],physics_1[i],IT_1[i],Total_1[i]])

data.append(["toppers",student_list[maths],student_list[biology],student_list[chemistry],student_list[physics],student_list[IT],student_list[Total_1.index(max(Total_1))]])

col_names = ["stud_Names", "maths_mrks","biology_mrks","chemistry_mrks","physics_mrks","IT_mrks","Total"]
  
print(tabulate(data, headers=col_names))

#print a specific students score
def ind_score():
    boolean=str(input("do you want to search yours details/score(y/n): "))
    if boolean=='y' or boolean=='Y' :
        name_stud=student_list.index(str(input("enter your name: ")));
        print("the student name is: ",student_list[name_stud]);
        print("maths marks: ",maths_1[name_stud]);
        print("biology marks: ",biology_1[name_stud]);
        print("chemistry marks: ",chemistry_1[name_stud]);
        print("physics marks: ",physics_1[name_stud]);
        print("IT marks: ",IT_1[name_stud]);
        print("total marks: ",Total_1[name_stud]);
        ind_score();
    else:
        print("Thank you")

ind_score();




