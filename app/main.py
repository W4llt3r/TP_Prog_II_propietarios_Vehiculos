from app.entidades.vehiculo import Vehiculo 
from app.entidades.propietario import Propietario 
from app.repositorios.repositorio_memoria import ( RepositorioMemoria ) 
from app.servicios.servicio_registros import ( ServicioRegistros ) 
from app.interfaz.aplicacion import Aplicacion 

def main(): 
    # 1. REPOSITORIOS # ========================================== 
    repositorio_vehiculos = RepositorioMemoria() 
    repositorio_propietarios = RepositorioMemoria() 
    # 2. SERVICIO # ========================================== 
    servicio = ServicioRegistros( repositorio_vehiculos, repositorio_propietarios ) 
    # 3. DATOS DE PRUEBA # ========================================== 
    vehiculo1 = Vehiculo( "Toyota", "Corolla", "ABC123", 2012 ) 
    propietario1 = Propietario( "Juan", "Perez", "30111222", "3415555555" ) 
    servicio.crear_registro_completo( vehiculo1, propietario1 ) 
    vehiculo2 = Vehiculo( "Ford", "Focus", "DEF456", 2015 ) 
    propietario2 = Propietario( "Pedro", "Gomez", "28444555", "3414444444" ) 
    servicio.crear_registro_completo( vehiculo2, propietario2 ) 

    # Prueba visual en terminal 
    print("VEHICULOS:")
    print(repositorio_vehiculos.obtener_todos())

    print("PROPIETARIOS:")
    print(repositorio_propietarios.obtener_todos())

    print("REGISTROS COMPLETOS:")
    print(servicio.obtener_registros_completos())


    # 4. APLICACIÓN # ========================================== 
    aplicacion = Aplicacion( servicio ) 
    # 5. EJECUTAR # ========================================== 
    aplicacion.ejecutar() 

if __name__ == "__main__": 
    main()












# from app.entidades.vehiculo import Vehiculo 
# from app.entidades.propietario import Propietario 
# from app.repositorios.repositorio_memoria import RepositorioMemoria 
# from app.servicios.servicio_registros import ServicioRegistros 
# from app.interfaz.aplicacion import Aplicacion 

# def main(): ## 1. CREAR REPOSITORIOS # ===================================== 
#     repositorio_vehiculos = RepositorioMemoria()
#     repositorio_propietarios = RepositorioMemoria() 
#     # # 2. CREAR SERVICIO # ===================================== 
    
#     servicio = ServicioRegistros( repositorio_vehiculos, repositorio_propietarios ) 

#     ## 3. CREAR VEHÍCULO 1 # ===================================== 
    
#     vehiculo1 = Vehiculo( "Toyota", "Corolla", "ABC123", 2012 )

#     ## 4. CREAR PROPIETARIO 1 # ===================================== 
#     propietario1 = Propietario( "Juan", "Perez", "30111222", "3415555555" ) 
#     ## 5. GUARDAR REGISTRO COMPLETO 1 # ===================================== 
    
#     servicio.crear_registro_completo( vehiculo1, propietario1 ) 
#     ## 6. CREAR VEHÍCULO 2 # ===================================== 
    
#     vehiculo2 = Vehiculo( "Ford", "Focus", "DEF456", 2015 ) 
#     ## 7. CREAR PROPIETARIO 2 # ===================================== 
#     propietario2 = Propietario( "Pedro", "Gomez", "28444555", "3414444444" ) 
#     ## 8. GUARDAR REGISTRO COMPLETO 2 # ===================================== 
#     servicio.crear_registro_completo( vehiculo2, propietario2 ) 
#     ## 9. CREAR APLICACIÓN # ===================================== 
#     aplicacion = Aplicacion( servicio ) 
#     ## 10. INICIAR LA APLICACIÓN # ===================================== 
#     aplicacion.ejecutar() 
#     ## PUNTO DE ENTRADA DEL PROGRAMA 
#     ## ========================================= 
# if __name__ == "__main__": 
#     main()

