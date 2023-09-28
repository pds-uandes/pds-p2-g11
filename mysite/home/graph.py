import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
from .models import Parameters

def get_graph_11(question):
    velocidad = question.dic['[VELOCIDAD]']
    periodo = question.dic['[PERIODO]']

    wavelength = velocidad * periodo

    # Crear datos para la onda
    x = np.linspace(0, wavelength, 1000)  # Crear puntos a lo largo de una longitud de onda
    y = np.sin(2 * np.pi * x / wavelength)  # Función sinusoidal para la onda

    # Crear el gráfico
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.title("Onda Armónica Simple")
    plt.xlabel("Posición (m)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # Marcar la longitud de onda en el gráfico
    plt.legend()
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_12(question):
    nodos = question.dic['[NODOS]']
    tiempo = question.dic['[TIEMPO]']
    longitud = question.dic['[LONGITUD]']

    f = nodos / tiempo

# Crear datos para la onda
    x = np.linspace(0, longitud, 1000)  # Crear puntos a lo largo de una longitud de onda
    t = np.linspace(0, tiempo, 1000)  # Intervalo de tiempo de 0 a 7 segundos
    y = np.sin(2 * np.pi * f * t - 2 * np.pi * x / longitud)  # Función sinusoidal para la onda

    # Crear el gráfico de la onda
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.title("Onda Armónica")
    plt.xlabel("Posición (m)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_21(question):
    frecuencia = question.dic['[FRECUENCIA]']

    t = np.linspace(0, 1, 1000)  # Intervalo de tiempo de 0 a 1 segundo
    y = np.sin(2 * np.pi * frecuencia * t)  # Función sinusoidal para la señal

    # Crear el gráfico de la señal de sonar
    plt.figure(figsize=(8, 4))
    plt.plot(t, y)
    plt.title("Señal de Sonar en el Agua")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_22(question):
    velocidad = question.dic['[VELOCIDAD]']
    tiempo = question.dic['[TIEMPO]']
    longitud = question.dic['[LONGITUD]']

    # Calculate the distance to the leading edge
    distance = velocidad * tiempo

    # Create data for the wave
    x = np.linspace(0, distance, 1000)
    y = np.sin(2 * np.pi * x / longitud)

    # Create the graph
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.title("Sound Wave")
    plt.xlabel("Distance (m)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # Mark the leading edge of the wave
    plt.legend()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_31(question):
    frecuencia = question.dic['[FRECUENCIA]']
    amplitud = question.dic['[AMPLITUD]']

    # Calcular el período (T)
    T = 1 / frecuencia

    # Crear datos para la onda armónica
    t = np.linspace(0, 2*T, 1000)  # Intervalo de tiempo de 0 a 2 períodos
    y = amplitud * np.sin(2 * np.pi * frecuencia * t)  # Función sinusoidal para la onda

    # Crear el gráfico de la onda armónica
    plt.figure(figsize=(8, 4))
    plt.plot(t, y)
    plt.title("Onda Armónica")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_32(question):
    frecuencia = question.dic['[FRECUENCIA]']
    amplitud = question.dic['[AMPLITUD]']
    periodo = question.dic['[PERIODO]']


    t = np.linspace(0, 2*periodo, 1000)  # Intervalo de tiempo de 0 a 2 períodos
    y = amplitud * np.sin(2 * 3.14 * frecuencia * t)  # Función sinusoidal para la onda

    # Crear el gráfico de la onda armónica
    plt.figure(figsize=(8, 4))
    plt.plot(t, y)
    plt.title("Onda Armónica")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_41(question):
    frecuencia = question.dic['[FRECUENCIA]']
    amplitud = question.dic['[AMPLITUD]']
    random = question.dic['[RANDOM]']

    x = np.linspace(-10, 10, 100)  # Valores de x en un rango
    t = np.linspace(0, 1, 100)  # Valores de t en un intervalo de tiempo
    x, t = np.meshgrid(x, t)
    y = amplitud * (frecuencia * np.pi * t - random * x)

    # Crear el gráfico
    fig = plt.figure(figsize=(8, 6))
    ax = fig.gca(projection='3d')
    ax.plot_surface(x, t, y, cmap='viridis')
    ax.set_title("Representación Gráfica de la Onda")
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.set_zlabel("y")

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_42(question):
    frecuencia = question.dic['[FRECUENCIA]']
    amplitud = question.dic['[AMPLITUD]']
    random = question.dic['[RANDOM]']


    x = np.linspace(-10, 10, 100)  # Valores de x en un rango
    t = np.linspace(0, 1, 100)  # Valores de t en un intervalo de tiempo
    x, t = np.meshgrid(x, t)
    y = amplitud * (frecuencia * np.pi * t - random * x)

    # Crear el gráfico
    fig = plt.figure(figsize=(8, 6))
    ax = fig.gca(projection='3d')
    ax.plot_surface(x, t, y, cmap='viridis')
    ax.set_title("Representación Gráfica de la Onda")
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.set_zlabel("y")

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_51(question):
    # Crear datos para la onda sonora
    frecuencia = question.dic['[FRECUENCIA]']
    amplitud = question.dic['[AMPLITUD]']

    t = np.linspace(0, 1, 1000)  # Intervalo de tiempo de 0 a 1 segundo
    y = amplitud * np.sin(2 * np.pi * frecuencia * t)  # Función sinusoidal para la onda

    # Crear el gráfico de la onda sonora
    plt.figure(figsize=(8, 4))
    plt.plot(t, y)
    plt.title("Onda Sonora")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_52(question):
    intensidad = question.dic['[INTENSIDAD]']
    densidad = question.dic['[DENSIDAD]']
    velocidad = question.dic['[VELOCIDAD]']
    frecuencia = question.dic['[FRECUENCIA]']

    A = np.sqrt((2 * intensidad) / (densidad * velocidad**2 * frecuencia**2))

    # Crear datos para la onda sonora
    t = np.linspace(0, 1, 1000)  # Intervalo de tiempo de 0 a 1 segundo
    y = A * np.sin(2 * np.pi * frecuencia * t)  # Función sinusoidal para la onda

    # Crear el gráfico de la onda sonora
    plt.figure(figsize=(8, 4))
    plt.plot(t, y)
    plt.title("Onda Sonora")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph(question):
    if question.theme == 1:
        if question.difficulty == 1:
            return get_graph_11(question)
        else:
            return get_graph_12(question)
    elif question.theme == 2:
        if question.difficulty == 1:
            return get_graph_21(question)
        else:
            return get_graph_22(question)
    elif question.theme == 3:
        if question.difficulty == 1:
            return get_graph_31(question)
        else:
            return get_graph_32(question)
    elif question.theme == 4:
        if question.difficulty == 1:
            return get_graph_41(question)
        else:
            return get_graph_42(question)
    elif question.theme == 5:
        if question.difficulty == 1:
            return get_graph_51(question)
        else:

            return get_graph_52(question)
    pass
