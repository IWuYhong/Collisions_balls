# 🎮 Mini Proyecto de Física en Pygame

Este repositorio contiene una simulación de colisiones avanzadas usando Pygame.

## Descripción

Este proyecto simula un sistema de colisiones elásticas entre pelotas en una ventana de Pygame. Las pelotas tienen diferentes masas y colores, y al colisionar, generan partículas que se desvanecen con el tiempo. Además, se visualiza el ángulo de colisión de cada pelota mediante una línea.

## Características

* Colisiones elásticas entre pelotas con diferentes masas.
* Generación de partículas en el punto de colisión.
* Visualización del ángulo de colisión.
* Rebote de las pelotas en los bordes de la ventana.
* Visualización de FPS y contador de partículas.

## Requisitos

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5.0-orange)](https://www.pygame.org/)

## ✨ Características Principales
- **Detección de colisiones** entre múltiples pelotas.
- **Cálculo del ángulo de impacto** visualizado con líneas direccionales.
- **Física realista** con masas variables y conservación del momento.
- **Sistema de partículas** para efectos visuales en colisiones.
- **FPS estable** gracias al uso de `delta time`.

## 🧠 Detalles Técnicos
- **Motor gráfico**: Pygame (renderizado 2D).
- **Sistema de partículas**: Partículas con transparencia y tiempo de vida.
- **Optimización**: Delta time para movimiento independiente del framerate.
- **Control de versiones**: Python 3.8+ y Pygame 2.5.0.

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone [https://github.com/IWuYhong/Collisions_balls.git](https://github.com/IWuYhong/Collisions_balls.git)
    ```

2.  Navega al directorio del proyecto:

    ```bash
    cd Collisions_balls
    ```

3.  Instala Pygame (si no lo tienes instalado):

    ```bash
    pip install pygame
    ```

## Ejecución

Ejecuta el script `main.py`:

```bash
python main.py
