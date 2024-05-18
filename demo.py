import datetime
import os
from campania import Campania
from anuncio import Video, SubTipoInvalidoError
from error import LargoExcedidoError

def escribir_log(excepcion):
    """
    Escribe un error en un log diario. El log incluye la fecha, hora del error y su descripción.
    
    Parámetros:
    -----------
    excepcion : Exception
        La excepción que se ha lanzado y necesita ser registrada.
    """
    try:
        archivo = f"log.{datetime.date.today()}.log"
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.abspath('logs/'+archivo), 'a') as log:
            log.write(f"[{fecha_hora}]  ERROR:  {str(excepcion)}\n")
    except OSError as e:
        print(f"Error al intentar crear y/o escribir el archivo log: {str(e)}")

try:
    anuncios_data = [("Video",{"url_archivo": "archivo1", "url_clic": "clic1", "sub_tipo": "instream","duracion":10})]
    campania = Campania("Campaña prueba","2024-01-01","2024-02-01", anuncios_data)

    try:
        nombre_campania = input("Ingrese el nuevo nombre para la campaña:\n")
        campania.nombre = nombre_campania
        print(campania)
        
    except LargoExcedidoError as e:
        escribir_log(e)
        print("El nombre de la campaña excede el largo permitido")
    except Exception as e:
        escribir_log(e)
        print("Error no especificado")
        
    try:   
        print(f"Formato de anuncio: {campania.anuncios[0].sub_tipo}")
        sub_tipo = input("Ingrese el nuevo subtipo para el anuncio:\n")
        campania.anuncios[0].sub_tipo = sub_tipo
        
    except SubTipoInvalidoError as e:
        escribir_log(e)
        print("El subtipo ingresado no coincide con el formato")
    except Exception as e:
        escribir_log(e)
        
except Exception as e:
    escribir_log(e)
    print("Error no especificado")
