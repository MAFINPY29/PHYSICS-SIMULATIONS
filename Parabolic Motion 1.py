import numpy as np
import matplotlib.pyplot as plt

#--------
def pedir_float(mensaje,minimo = None,maximo = None):
  """
  Solicita un número flotante al usuario y lo valida.

  """
  while True:
    try:
      valor = float(input(mensaje))
      if minimo is not None and valor < minimo:
        raise ValueError(f"El valor debe ser mayor o igual a {minimo}.")

      if maximo is not None and valor > maximo:
        raise ValueError(f"El valor debe ser menor o igual a {maximo}.")
      return valor

    except ValueError as e:
      print(f"Entrada inválida: {e}")
    except Exception:
      print("Error inesperado. Intente nuevamente.")

def pedir_angulo():
  """
  Solicita el ángulo en grados sexagesimales y lo convierte a radianes.
  """
  angulo_sxg = pedir_float("Ingrese el ángulo de lanzamiento (0° – 90°):",minimo = 0, maximo = 90)
  return np.deg2rad(angulo_sxg)


###
def tiempo_de_vuelo(v0,angulo,g=9.81):
  return 2*v0*np.sin(angulo)/g

def alcance(v0,angulo,g=9.81):
  return (v0**2*np.sin(2*angulo))/g

def trayectoria(v0, angulo, g=9.81, puntos=200):
    t_f = tiempo_de_vuelo(v0, angulo, g)
    t = np.linspace(0, t_f, puntos)

    x = v0 * np.cos(angulo) * t
    y = v0 * np.sin(angulo) * t - 0.5 * g * t**2

    return x, y

def analisis_alcance(v0, g=9.81):
    angulos_sxg = np.linspace(0, 90, 181)
    angulos_rad = np.deg2rad(angulos_sxg)
    alcances = alcance(v0, angulos_rad, g)
    return angulos_sxg, alcances

### PROGRAMA PRINCIPAL
def main():
  print("*************SIMULACIÓN DE MOVIMIENTO PARABÓLICO*************")

  try:
    angulo = pedir_angulo()
    v0 = pedir_float("Ingrese la velocidad inicial (m/s): ", minimo=0)
    g = 9.81

    x, y = trayectoria(v0, angulo, g)

    plt.figure()
    plt.plot(x, y,color='r')
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trayectoria del proyectil")
    plt.grid(True)
    plt.show()

    angulos, alcances = analisis_alcance(v0, g)

    plt.figure()
    plt.plot(angulos, alcances,color='g')
    plt.xlabel("Ángulo (grados)")
    plt.ylabel("Alcance horizontal (m)")
    plt.title("Alcance vs ángulo de lanzamiento")
    plt.grid(True)
    plt.show()

    alcance_max = np.max(alcances)
    angulo_optimo = angulos[np.argmax(alcances)]

    print(f"Alcance máximo: {alcance_max:.2f} m")
    print(f"Ángulo óptimo: {angulo_optimo:.1f}°")

  except Exception as e:
    print("Error crítico en la simulación.")
    print(e)
#----
if __name__ == "__main__":
    main()
