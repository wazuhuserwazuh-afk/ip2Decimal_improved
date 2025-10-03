# ip2Decimal_improved
Un script inspirado en II104567, ususario de THL




## Conversor de Dirección IP (IPv4) a Número Entero (32-bit)

`ip2num_improved.py` es un *script* de Python diseñado para convertir una dirección **IPv4** de su formato estándar de puntos y decimales (`A.B.C.D`) a su representación numérica entera única de **32 bits**. Esta conversión es esencial para almacenar, indexar o realizar cálculos de subredes eficientes en entornos de red y bases de datos.

## ✨ Características Principales

  * **Validación Robusta:** Utiliza la librería estándar `ipaddress` para garantizar que la dirección ingresada no solo tenga el formato correcto (`X.X.X.X`), sino que también cada octeto esté dentro del rango válido (`0-255`).
  * **Cálculo Preciso:** Realiza la conversión matemática estándar (base 256) de manera precisa y segura.
  * **Fácil de Usar:** Interfaz de línea de comandos simple y directa.

-----

## 🚀 Requisitos

Este *script* utiliza bibliotecas estándar que generalmente vienen preinstaladas con Python 3.

  * **Python 3.x**
  * **Librerías:** `sys`, `ipaddress` (Estándar de Python)

-----

## ⚙️ Uso

El *script* debe ejecutarse desde la línea de comandos, pasando la dirección IP deseada como único argumento.

### Sintaxis

```bash
python3 ip2num_improved.py <dirección_ip_v4>
```

### Ejemplos

| Comando | Salida | Descripción |
| :--- | :--- | :--- |
| `python3 ip2num_improved.py 192.168.1.1` | `3232235777` | Conversión exitosa de una IP privada. |
| `python3 ip2num_improved.py 8.8.8.8` | `134744072` | Conversión exitosa de una IP pública conocida. |
| `python3 ip2num_improved.py 256.0.0.1` | `256.0.0.1' no es una dirección IP válida (IPv4).` | Manejo de error: el octeto `256` es inválido. |

-----

## ❓ ¿Cómo funciona la Conversión?

La dirección IPv4 (`A.B.C.D`) es esencialmente un número de 32 bits dividido en cuatro segmentos de 8 bits (octetos). La conversión a un único número entero se logra mediante la siguiente fórmula, basada en el sistema de numeración posicional de base 256:

$$\text{Entero} = (A \times 256^3) + (B \times 256^2) + (C \times 256^1) + (D \times 256^0)$$

El *script* utiliza la clase `ipaddress.IPv4Address(ip_str).int` para realizar este cálculo internamente de forma eficiente.
