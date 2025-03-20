tareas=[]
tareas.append({"nombre":"","descripción":"","fecha limite":"","nivel de importancia":""})
tareas[len(tareas)-1]["nombre"]=input("inserte nombre ")
tareas[len(tareas)-1]["descipcion"]=input("inserte una descipcion dela tarea ")
tareas[len(tareas)-1]["fecha limite"]=input("inserte la fecha de entrega ")
tareas[len(tareas)-1]["nivelde importancia"]=input("inserte una medida del 1 al 10 de que tan inportate es esta tarea ")
options=["y","Y","n","N"]
def onliYN():
    Otratarea=""
    while (Otratarea in options)==False:
        Otratarea=input("quiere agregar otra tarea? (Y/N) ")
    return Otratarea
otraTarea=onliYN()
while otraTarea=="Y" or otraTarea=="y":
    tareas.append({"nombre":"","descripción":"","fecha limite":"","nivel de importancia":""})
    tareas[len(tareas)-1]["nombre"]=input("inserte nombre ")
    tareas[len(tareas)-1]["descipcion"]=input("inserte una descipcion dela tarea ")
    tareas[len(tareas)-1]["fecha limite"]=input("inserte la fecha de entrega ")
    tareas[len(tareas)-1]["nivelde importancia"]=input("inserte una medida del 1 al 10 de que tan inportate es esta tarea ")
    otraTarea=onliYN()