"""
Exercise 6:
The final grade of a student is calculated from three grades assigned in the range of 0 to 10, respectively:
a laboratory work, a semestral evaluation, and a final exam.
The mean of the three mentioned grades follows the weights:
    - Laboratory Work: 2;
    - Semestral Evaluation: 3;
    - Final Exam: 5.
According to the result, display on the screen if the student has failed (mean between 0 and 2.9), 
is in remediation (between 3 and 4.9) or has passed. Make all necessary checks.


Exercício 6 (PT-BR):
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente,
a um trabalho de laboratório, a uma avaliação semestral e a um exame final. 
A média das três notas mencionadas anteriormente obedece aos pesos: 
    - Trabalho de Laboratório: 2;
    - Avaliação Semestral: 3;
    - Exame Final: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de 
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

lab_grade = float(input("Enter the grade for the Laboratory Work: "))
if 0 <= lab_grade <= 10:
    ev_grade = float(input("Enter the grade for the Semestral Evaluation: "))
    if 0 <= ev_grade <= 10:
        exam_grade = float(input("Enter the grade for the Final Exam: "))
        if 0 <= exam_grade <= 10:
            mean = ((lab_grade*2) + (ev_grade*3) + (exam_grade*5))/10  # weighted average
            if mean < 3:
                print(f"Mean: {mean:.2f}.\nThe student has failed.")
            elif mean < 5:
                print(f"Mean: {mean:.2f}.\nThe student is in remediation.")
            else:
                print(f"Mean: {mean:.2f}.\nThe student has passed.")
        else:
            print("The grade for the Final Exam is invalid.")
    else:
        print("The grade for the Semestral Evaluation is invalid.")
else:
    print("The grade for the Laboratory Work is invalid.")
