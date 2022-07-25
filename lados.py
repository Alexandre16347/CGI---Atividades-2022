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
    (0, 6),
    (0, 7),
    (0, 8),
    (1, 2),
    (1, 4),
    (2, 3),
    (3, 4),
    (5, 6),
    (5, 8),
    (6, 7),
    (7, 8)
)

superficie = (
    (0, 1, 2, 3),
    (0, 3, 4, 1),
    (0, 5, 6, 7),
    (0, 7, 8, 5),
    (1, 2, 3, 4),
    (5, 6, 7, 8)

)

normals = [
    (0,  1,  0),
    (0, -1,  0),
    (0,  0,  1),
    (1,  0,  0),
    (0,  1,  0),
    (0,  0, -1),
    (-1,  0,  0),
    (0,  0,  1),
    (1,  0,  0),
    (0, -1,  0)
]

cores = (
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 1),
    (0, 0, 1),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 1),
    (0, 0, 1)
)

textureCoordinates = (
    (0, 0),
    (0, 1),
    (1, 1),
    (1, 0)
)


def carregaTextura():
    textureSurface = pygame.image.load('vidro.jpg')
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


def Ampulheta():
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(superficie):
        x = 0
        glNormal3fv(normals[i_surface])
        for i_vertex, vertex in enumerate(surface):
            x += 1
            # glColor3fv(cores[x])
            glTexCoord2fv(textureCoordinates[i_vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3fv(cores[0])
    glBegin(GL_LINES)       # Inicia o OpenGL e inidica q la
    # vem instruções
    for aresta in arestas:
        for vertex in aresta:

            glVertex3fv(vertices[vertex])  # Informa o vertice
            # para a aresta
    glEnd()


def main():
    global superficie

    pygame.init()
    display = (1024, 760)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()

    # glMatrixMode(GL_PROJECTION)
    glMatrixMode(GL_MODELVIEW)
    gluPerspective(75, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)

    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

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

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        carregaTextura()
        Ampulheta()

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        clock.tick(60)


main()
