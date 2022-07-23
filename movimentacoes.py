import pygame
#import OpenGL

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (        # Um cubo tem 8 vertices
    # (-0.5, -0.5, -0.5),
    # (0.5, -0.5, -0.5),
    # (0.5, 0.5, -0.5),
    # (-0.5, -0.5, 0.5),
    # (0.5, -0.5, 0.5),
    # (0.5, 0.5, 0.5)

    (0, 0, 0),
    (1, 1, 2),
    (-1, 1, 2),
    (-1, -1, 2),
    (1, -1, 2),
    (1, 1, -2),
    (-1, 1, -2),
    (-1, -1, -2),
    (1, -1, -2)

)

arestas = (         # Um cubo possui 12 arestas
                    # Ligando um vertice a outro
    # (0, 1),         # Aresta [0]  [0--1]
    # (0, 3),         # Aresta [1]  [0--3]
    # (0, 4),         # Aresta [2]  [0--4]
    # (2, 1),         # Aresta [3]  [2--1]
    # (2, 3),         # Aresta [4]  [2--3]
    # (2, 7),         # Aresta [5]  [2--7]
    # (6, 3),         # Aresta [6]  [6--3]
    # (6, 4),         # Aresta [7]  [6--4]
    # (6, 7),         # Aresta [8]  [6--7]
    # (5, 1),         # Aresta [9]  [5--1]
    # (5, 4),         # Aresta [10] [5--4]
    # (5, 7)          # Aresta [11] [5--7]

    # (0, 1),
    # (0, 2),
    # (1, 2),
    # (0, 3),
    # (3, 4),
    # (3, 5),
    # (4, 5),
    # (1, 4),
    # (2, 5),

    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    # (0, 6),
    # (0, 7),
    # (0, 8),
    # (1, 2),
    # (1, 4),
    # (2, 3),
    # (3, 4),
    # (5, 6),
    # (5, 8),
    # (6, 7),
    # (7, 8)
)


def Ampulheta():
    glBegin(GL_LINES)       # Inicia o OpenGL e inidica q la
    # vem instruções
    for aresta in arestas:
        for vertice in aresta:
            glVertex3fv(vertices[vertice])  # Informa o vertice
            # para a aresta
    glEnd()                 # Fecha e encerras as intruções OpenGL


def main():
    pygame.init()
    display = (1024, 760)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_MODELVIEW)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(1, 3, 1, 1)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.1, 0, 0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(0.1, 0, 0)

            if event.key == pygame.K_UP:
                glTranslatef(0, 0.2, 0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0, -0.2, 0)

            if event.key == pygame.K_s:
                glRotatef(5, 5, 0, 0)
            if event.key == pygame.K_w:
                glRotatef(-5, 5, 0, 0)
            if event.key == pygame.K_d:
                glRotatef(-5, 0, -5, 0)
            if event.key == pygame.K_a:
                glRotatef(5, 0, -5, 0)

            if event.key == pygame.K_p:
                glScalef(0.9, 0.9, 0.9)
            if event.key == pygame.K_l:
                glScalef(1.1, 1.1, 1.1)

            if event.key == pygame.K_z:
                glFrustum(-10.0, 10.0, -10.0, 10.0, 1.0, 2.0)
            if event.key == pygame.K_x:
                glFrustum(1/-5.0, 1/5.0, 1/-5.0, 1/5.0, 1.0, 2.0)
            if event.key == pygame.K_c:
                gluLookAt(0, 0, 0, 1, 0, 1, 0, 0, 1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Ampulheta()
        pygame.display.flip()
        pygame.time.wait(10)


main()
