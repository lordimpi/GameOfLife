# Juego de la Vida de Conway en Pygame
Este proyecto implementa el Juego de la Vida de Conway, un autómata celular desarrollado por el matemático John Horton Conway. El juego es un ejemplo clásico de cómo patrones complejos pueden evolucionar a partir de reglas simples. Este proyecto utiliza Pygame para la visualización y NumPy para la gestión de estados.

# Características
- Visualización en tiempo real de la evolución del Juego de la Vida.
- Interacción con el usuario mediante teclado para pausar, reiniciar y modificar el estado del juego.
- Configuración inicial con patrones conocidos como osciladores y naves espaciales.

# Requisitos Previos
Para ejecutar este proyecto, necesitas tener Python y Pygame instalados. Asegúrate de tener Python 3.6 o superior. Puedes instalar Pygame a través de pip:

`pip install pygame`
`pip install numpy`

# Estructura de Archivos
- `main.py`: Punto de entrada del juego que inicializa y ejecuta el bucle principal.
- `game.py`: Contiene la lógica del juego y la clase GameOfLife.
- `settings.py`: Define las configuraciones básicas como las dimensiones de la pantalla y los colores.

# Cómo Ejecutar
Para iniciar el juego, simplemente ejecuta el archivo `main.py` usando Python. Por ejemplo: `python main.py`

![image](https://github.com/lordimpi/GameOfLife/assets/53197926/d18eefc5-f364-4d19-81b2-053121848c9c)

# Controles
- Espacio: Pausa o reanuda la simulación.
- R: Reinicia el juego con la configuración inicial.
- T: Reinicia el juego con un estado aleatorio.
- Q: Amuenta la velocidad.
- W: Disminuye la velocidad.
- ESC: Salir del juego.
- Click izquierdo: Agrega una célula viva en la posición del cursor.
- Click derecho: Elimina una célula viva en la posición del cursor.

# Contribuir
Este es un proyecto de código abierto y las contribuciones son bienvenidas. Si tienes mejoras o correcciones, por favor siente libre de forkear el repositorio y enviar un pull request. Si encuentras errores, por favor reporta los problemas en el sistema de issues del repositorio.

# Licencia
Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.
