NroEmpleados = 0

TotalNetos = 0


while NroEmpleados < 4 :
        Identificacion  = input ("Digite la identificacion del Empleado: ")

        NombreApellido = input ("Digite los Nombre y apellidos del empleado: ")

        ValorHora = int(input("Digite el valor de la hora trabajada: "))

        NumeroHoras = int(input("Digite el numero de horas trabajadas en el mes: "))

        SueldoNeto = ValorHora * NumeroHoras 

        NroEmpleados = NroEmpleados + 1

        TotalNetos = TotalNetos + SueldoNeto

        print ("El señor de nombre: " + NombreApellido)

        print ("Devengo este mes el valor de: " +  str(SueldoNeto))


        
        
        
        
print ("El total final de los pagos de todos los empleados es: " + str(TotalNetos))