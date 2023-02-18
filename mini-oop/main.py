import students
import groups

def main():
    gr1 = groups.Groups("ИВТАПбд-21")
    gr2 = groups.Groups("ИВТАПбд-22")
    st1 = students.Students("Ренжина","Александра","ИВТАПбд-22")
    st2 = students.Students("Узлов","Андрей","ИВТАПбд-21")

    if(st1.group == gr1.name_group):
        gr1.amount+=1
    else:
        gr2.amount+=1
    if(st2.group == gr2.name_group):
        gr2.amount+=1
    else:
        gr1.amount+=1
    st1.print_inf()
    st2.print_inf()

    gr1.print_inf()
    gr2.print_inf()
if __name__ == '__main__':
    main()
