import pyscreenshot

image = pyscreenshot.grab() #screenshot full window
image.show() #show after screenshot
image.save("screenshot.png")