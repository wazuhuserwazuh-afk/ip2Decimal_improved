import sys
import ipaddress
import socket # Usado para la conversión de bytes a entero

def ip_to_integer(ip_address_str):
    """
    Convierte una dirección IPv4 (string) a su representación entera de 32 bits.
    Utiliza la biblioteca ipaddress para una validación completa y robusta.
    """
    try:
        # 1. Validación y creación del objeto IPv4
        # Esto verifica automáticamente el formato y el rango (0-255) de cada octeto.
        ip_obj = ipaddress.IPv4Address(ip_address_str)
        
        # 2. Conversión a entero
        # El objeto IPv4Address tiene un atributo 'packed' (los 4 bytes)
        # y un atributo 'host_mask' que es el valor entero.
        # socket.ntohl (Network To Host Long) asegura el orden correcto de los bytes, 
        # pero ipaddress.IPv4Address(ip_address_str).packed ya garantiza el formato de red (big-endian).
        
        # El método .packed devuelve los 4 bytes. socket.ntohl convierte del orden de red (big-endian) 
        # al orden del host, pero el valor entero ya está en el atributo 'int_value' o .packed.
        # La forma más simple y correcta en Python moderno es usar el atributo int
        integer_representation = int(ip_obj)
        
        return integer_representation
        
    except ipaddress.AddressValueError:
        # Captura errores si la IP no es válida (formato o rango fuera de 0-255)
        return None
    except Exception as e:
        # Captura cualquier otro error
        print(f"Error inesperado: {e}")
        return None

# =================================================================
# Lógica Principal
# =================================================================
if __name__ == "__main__":
    # Verificación de argumentos
    if len(sys.argv) != 2:
        print("Uso: python3 ip2Decimal_improved.py <dirección_ip_v4>")
        sys.exit(1)

    ip = sys.argv[1]
    
    # Intenta la conversión
    result = ip_to_integer(ip)

    if result is not None:
        print(result)
    else:
        # El mensaje de error es más específico gracias a ipaddress
        print(f"'{ip}' no es una dirección IP válida (IPv4).")
        sys.exit(2)
