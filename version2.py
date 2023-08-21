import logo_funciones as lf
class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []     
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)
    def verDatosPacientes(self, c):
        # Se busca paciente por paciente
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                print("Nombre: " + p.verNombre())
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
                break
    def verNumeroPacientes(self):
        print("En el sistema hay " + str(len(self.__lista_pacientes)) + " pacientes")              
def main():
    mi_sistema = Sistema()
    print(lf.logo1)
    print("Bienvenido al sistema de registro de pacientes\n")
    while True:
        opcion = lf.intChecker(" - 1. Ingresar paciente\n - 2. Buscar paciente\n - 3. Ver número de pacientes ingresados\n - 4. Salir  \n")
        if opcion == 1:
            print("Ingrese los datos del paciente\n")
            nombre = input("Nombre: ")
            cedula = lf.intChecker("Cedula: ")
            genero = input("Genero: ")
            servicio = input("Servicio: ")
            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            sis.ingresarPaciente(pac)
        elif opcion == 2:
            c = lf.intChecker("Ingrese la cedula del paciente: ")
            if mi_sistema.verDatosPacientes(c) == None:
                print("No se encontró el paciente")
            else:
                p = sis.verDatosPacientes(c)
                print(f"Datos del paciente con cedula {c}:\n")
                print("Nombre: " + p.verNombre())
                print("Genero: " + p.verGenero())
                print("Servicio: " + p.verServicio())
        elif opcion == 3:
            mi_sistema.verNumeroPacientes()
            print()
        elif opcion == 4:
            print("Gracias por usar el sistema")
            print(lf.logo2)
            break
        else:
            print("Opcion invalida\n")
            
if __name__ == "__main__":
    main()