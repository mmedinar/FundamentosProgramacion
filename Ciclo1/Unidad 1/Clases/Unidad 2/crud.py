from typing import List


students = "mario, fernando"

def menu():
    print("--APLICACION CRUD: INSCRIPCION ESTUDIANTES--")
    print("="*50)
    print("Escoja su opción: ")
    print("[C] - Crear estudiante" )
    print("[R] - Listar estudiantes" )
    print("[U] - Actualizar estudiante" )
    print("[D] - Borrar estudiante" )
    print("[S] - Salir" )


def get_student_name():
    return input("Ingrese nombre estudiante: ")


def create_student(student_name):
    global students
    if student_name not in students:
        students  += student_name + ','
    else:
        print(f'El estudiante {student_name} ya existe.')


def list_students():
    global students
    print(students)

def update_student(student_name, update_student_name):
    global students
    if student_name in students:
        students = students.replace(student_name + ',', update_student_name +',')
    else:
        print(f"El estudiante {student_name} no se encuentra en la lista. ")
    
def delete_student(student_name):
    global students
    if student_name in students:
        students = students.replace(student_name + ',', '')
    else:
        print(f"El estudiante {student_name} no se encuentra en la lista. ")


if __name__ == '__main__':
    menu()
    command = input().upper()
    while command != 'S':
        if command == 'C':
            student_name = get_student_name()
            create_student(student_name)
            list_students()
        elif command == 'R':
            list_students()
        elif command == 'U':
            list_students()
            student_name = get_student_name()
            update_student_name = input('Nuevo nombre: ')
            update_student(student_name, update_student_name)
        elif command == 'D':
            list_students()
            student_name = get_student_name()
            delete_student(student_name)
            list_students
        else:
            print("COMANDO INVALIDO")
        menu()
        command = input().upper()
    print("Ha finalizado su trabajo. GRACIAS  ")

