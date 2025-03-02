import pygame
import math
import random
from pygame.math import Vector2

# Inicializar Pygame
pygame.init()

# Configuración
ANCHO, ALTO = 400, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sistema de Colisiones Avanzado")
FUENTE = pygame.font.Font(None, 24)

# Clases
class Pelota:
    def __init__(self, pos, color, radio=20, masa=1):
        self.pos = Vector2(pos)
        self.vel = Vector2(random.uniform(-300, 300), random.uniform(-300, 300))
        self.radio = radio
        self.color = color
        self.masa = masa
        self.angulo_colision = None

    def actualizar(self, delta_time):
        self.pos += self.vel * delta_time

        # Rebotar en bordes
        if self.pos.x < self.radio:
            self.pos.x = self.radio
            self.vel.x *= -1
        elif self.pos.x > ANCHO - self.radio:
            self.pos.x = ANCHO - self.radio
            self.vel.x *= -1
        
        if self.pos.y < self.radio:
            self.pos.y = self.radio
            self.vel.y *= -1
        elif self.pos.y > ALTO - self.radio:
            self.pos.y = ALTO - self.radio
            self.vel.y *= -1

    def dibujar(self, superficie):
        pygame.draw.circle(superficie, self.color, self.pos, self.radio)
        
        if self.angulo_colision:
            # Línea de dirección del ángulo
            dx = math.cos(math.radians(self.angulo_colision)) * 30
            dy = math.sin(math.radians(self.angulo_colision)) * 30
            pygame.draw.line(superficie, (255, 255, 255), self.pos, (self.pos.x + dx, self.pos.y + dy), 3)

class Particula:
    def __init__(self, pos, color):
        self.pos = Vector2(pos)
        self.vel = Vector2(random.uniform(-200, 200), random.uniform(-200, 200))
        self.color = color
        self.tiempo_vida = 1.0  # 1 segundo
        self.radio = 3

    def actualizar(self, delta_time):
        self.pos += self.vel * delta_time
        self.tiempo_vida -= delta_time

    def dibujar(self, superficie):
        alpha = int(self.tiempo_vida * 255)
        color = (*self.color, alpha)
        pygame.draw.circle(superficie, color, (int(self.pos.x), int(self.pos.y)), self.radio)

# Funciones de colisiones
def manejar_colisiones(pelota1, pelota2, particulas):
    delta = pelota2.pos - pelota1.pos
    distancia = delta.length()
    radio_total = pelota1.radio + pelota2.radio

    if distancia < radio_total and distancia != 0:
        # Calcular ángulo de colisión
        angulo = math.degrees(math.atan2(-delta.y, delta.x)) % 360
        pelota1.angulo_colision = angulo
        pelota2.angulo_colision = (angulo + 180) % 360

        # Separación posicional
        overlap = (radio_total - distancia) / 2
        direccion = delta.normalize()
        pelota1.pos -= direccion * overlap
        pelota2.pos += direccion * overlap

        # Física de colisión (con masa)
        v1 = pelota1.vel
        v2 = pelota2.vel
        m1, m2 = pelota1.masa, pelota2.masa

        n = direccion
        k = v1 - v2
        p = 2 * n.dot(k) / (m1 + m2)

        pelota1.vel = v1 - p * m2 * n
        pelota2.vel = v2 + p * m1 * n

        # Generar partículas
        for _ in range(10):
            particulas.append(Particula(
                pos=(pelota1.pos + pelota2.pos) / 2,
                color=random.choice([pelota1.color, pelota2.color])
            ))

# Bucle principal
def main():
    pelotas = [
        Pelota((300, 300), (255, 0, 0), masa=1.5),
        Pelota((600, 300), (0, 255, 0), masa=0.8),
        Pelota((900, 300), (0, 0, 255), masa=1.2),
        Pelota((450, 500), (255, 255, 0), masa=1.0),
        Pelota((750, 500), (255, 0, 255), masa=1.0),
        Pelota((600, 700), (0, 255, 255), masa=1.0),
        Pelota((600, 900), (255, 255, 255), masa=1.0),
    ]

    particulas = []
    reloj = pygame.time.Clock()
    ejecutando = True

    while ejecutando:
        delta_time = reloj.tick(60) / 1000.0

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        # Actualizar pelotas
        for pelota in pelotas:
            pelota.actualizar(delta_time)
            pelota.angulo_colision = None  # Resetear ángulo

        # Verificar todas las combinaciones de colisiones
        for i in range(len(pelotas)):
            for j in range(i + 1, len(pelotas)):
                manejar_colisiones(pelotas[i], pelotas[j], particulas)

        # Actualizar y filtrar partículas
        for particula in particulas:
            particula.actualizar(delta_time)
        particulas = [p for p in particulas if p.tiempo_vida > 0]

        # Dibujar
        VENTANA.fill((30, 30, 30))

        for pelota in pelotas:
            pelota.dibujar(VENTANA)

        for particula in particulas:
            particula.dibujar(VENTANA)

        # Mostrar FPS
        fps = int(reloj.get_fps())
        texto = FUENTE.render(f"FPS: {fps} | Partículas: {len(particulas)}", True, (255, 255, 255))
        VENTANA.blit(texto, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()