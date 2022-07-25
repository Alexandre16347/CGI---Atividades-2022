# from syslog import openlog
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    #   (x,  y,  z)
    (1, -1, -1),  # 00
    (1, 1, -1),  # 01
    (-1, 1, -1),  # 02
    (-1, -1, -1),  # 03
    (1, -1,  1),  # 04
    (1,  1,  1),  # 05
    (-1, -1, 1),  # 06
    (-1, 1,  1),  # 07

    (0,  0,  2),  # 08
    (0,  2,  0),  # 09
    (2,  0,  0),  # 10

    (-2, 0,  0),  # 11
    (0, -2,  0),  # 12
    (0,  0, -2),  # 13




)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),

    # (6, 8),
    # (5, 8),
    # (7, 8),
    # (4, 8),

    (1, 9),
    (2, 9),
    (5, 9),
    (7, 9),

    # (1, 10),
    # (4, 10),
    # (5, 10),
    # (0, 10),

    # (2, 11),
    # (3, 11),
    # (7, 11),
    # (6, 11),

    # (0, 12),
    # (3, 12),
    # (4, 12),
    # (6, 12),

    # (0, 13),
    # (3, 13),
    # (2, 13),
    # (1, 13),

)

arestas = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),

    # (6, 8),
    # (5, 8),
    # (7, 8),
    # (4, 8),

    # (1, 9),
    # (2, 9),
    # (5, 9),
    # (7, 9),

    (1, 10),
    (4, 10),
    (5, 10),
    (0, 10),

    # (2, 11),
    # (3, 11),
    # (7, 11),
    # (6, 11),

    # (0, 12),
    # (3, 12),
    # (4, 12),
    # (6, 12),

    # (0, 13),
    # (3, 13),
    # (2, 13),
    # (1, 13),




)
superfice = (

    # (4, 5, 1, 9),  # T Esquerdo
    # (0, 1, 2, 9),  # T Atrás
    # (6, 7,  5, 9),  # T Frente
    # (7, 2, 3, 9),  # T Direita

    (5, 7, 2, 9),  # Cima
    (2, 1, 5, 9),

    (6, 7, 5, 8),   # Frente
    (6, 4, 5, 8),

    (4, 5, 1, 10),  # Direita
    (1, 0, 4, 10),

    (2, 7, 6, 11),  # Esquerda
    (6, 3, 2, 11),

    (3, 6, 4, 12),  # Baixo
    (4, 0, 3, 12),

    (3, 2, 1, 13),  # Atrás
    (1, 0, 3, 13),

    # (0, 1, 2, 3),  # Atrás
    # (3, 2, 7, 6),  # Direita
    # (6, 7, 5, 4),  # Frente
    # (4, 5, 1, 0),  # Esquerdo

    # (1, 5, 7, 2),  # Cima
    # (4, 0, 3, 6),  # Baixo
    # (8, 2, 3),
    # (8, 3, 0),
    # (8, 2, 1),
    #  (8, 1, 0),
    # (9, 7, 2),
    # (9, 1, 2),
    # (9, 5, 7),
    # (9, 2, 1),






)

normals = (
    (0, 0, -1),
    (-1, 0, 0),
    (0, 0, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),

    (0, 0, -1),
    (-1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
    (-1, 0, 0),
    (0, 0, 1),
)

cores = (
    ((0, 0, 1),
     (0, 1, 0),
     (0, 0, 1),
     (0, 1, 0),
     (1, 0, 1),
     (0, 0, 1),
     (0, 0, 1),
     (0, 1, 0),
     (0, 0, 1),
     (0, 1, 0),
     (1, 0, 1),
     (0, 0, 1),
     (0, 0, 1),
     (0, 1, 0),
     (0, 0, 1),
     (0, 1, 0),
     (1, 0, 1),
     (0, 0, 1),)
)


def loadTexture():
    textureSurface = pygame.image.load('v.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def Cube():
    # glBegin(GL_LINES)
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(superfice):
        x = 0
        glNormal3fv(normals[i_surface])
        for vertex in surface:
            x += 1
            glColor3fv(cores[x])
            glVertex3fv(verticies[vertex])
    glEnd()

    glColor3fv(cores[0])
    glBegin(GL_LINES)

    for edge in arestas:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    global superfice

    pygame.init()
    display = (800, 600)
    # display = (400, 300)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    glTranslatef(0.0, 0.0, -5)

    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
    glLight(GL_LIGHT0, GL_AMBIENT, (10, 0, 0, 1))
    glLight(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # Navegando na pagina
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)

                if event.key == pygame.K_UP:
                    glTranslatef(0.0, 0.5, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0.0, -0.5, 0)

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

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        Cube()

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)
        pygame.display.flip()
        pygame.time.wait(10)


main()
