tareas=[]
options=["y","Y","n","N"]

def newTarea():
    tarea={}
    tarea["nombre"]=input("inserte nombre ")
    tarea["descipcion"]=input("inserte una descipcion dela tarea ")
    tarea["fecha limite"]=input("inserte la fecha de entrega ")
    tarea["nivelde importancia"]=input("inserte una medida del 1 al 10 de que tan inportate es esta tarea ")

def onliYN():
    Otratarea=""
    while (Otratarea in options)==False:
        Otratarea=input("quiere agregar otra tarea? (Y/N) ")
    return Otratarea
otraTarea=onliYN()

while otraTarea=="Y" or otraTarea=="y":
    tareas.append(newTarea())
    otraTarea=onliYN()
print(tareas)