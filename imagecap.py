import pygame
import pygame.camera
import time

pygame.camera.init()
msg = pygame.camera.list_cameras() #Camera detected or not

print(msg)

cam = pygame.camera.Camera(msg[0],(640,480))
cam.start()

time.sleep(0.1)

img = cam.get_image()
pygame.image.save(img,"filename.jpg")