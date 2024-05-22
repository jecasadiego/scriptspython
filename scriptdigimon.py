
import time
import cv2
import numpy as np
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import mss

# Inicializa los controladores de mouse y teclado
mouse = MouseController()
keyboard = KeyboardController()

# Función para tomar una captura de pantalla de una región específica
def screenshot(region=None):
    with mss.mss() as sct:
        monitor = sct.monitors[0] if region is None else region
        screenshot = np.array(sct.grab(monitor))
        return cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

# Función para encontrar el área de pesca en la pantalla
def find_fishing_area(template_path, threshold=0.8, method=cv2.TM_CCOEFF_NORMED, region=None):
    print("Cargando la imagen de la plantilla...")
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print("Error: La imagen de la plantilla no se pudo cargar. Verifique la ruta del archivo.")
        return None
    print("Imagen de la plantilla cargada correctamente.")
    w, h = template.shape[::-1]

    while True:
        print("Tomando captura de pantalla...")
        screen = screenshot(region)
        gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        print("Comparando la plantilla con la captura de pantalla...")
        res = cv2.matchTemplate(gray_screen, template, method)
        loc = np.where(res >= threshold)
        
        if len(loc[0]) > 0:
            for pt in zip(*loc[::-1]):
                print("Área de pesca encontrada en:", (pt[0] + w // 2, pt[1] + h // 2))
                return (pt[0] + w // 2, pt[1] + h // 2)  # Coordenadas del centro del área de pesca
        else:
            print("No se encontró el área de pesca. Intentando nuevamente...")
        time.sleep(1)

# Función para buscar el signo de admiración en una región específica
def find_exclamation_sign(template_path, threshold=0.7, method=cv2.TM_CCOEFF_NORMED, region=None):
    # Esperar 5 segundos para permitir al usuario colocar el juego en la posición correcta
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print("Error: La imagen del signo de admiración no se pudo cargar. Verifique la ruta del archivo.")
        return

    print("Imagen del signo de admiración cargada correctamente.")
    w, h = template.shape[::-1]

    start_time = time.time()

    while True:
        screen = screenshot(region)
        gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)


        # Comparar la plantilla con la captura de pantalla
        res = cv2.matchTemplate(gray_screen, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Guardar la captura de pantalla para depuración
        cv2.imwrite('screenshot.png', screen)
        cv2.imwrite('result.png', res * 255)  # Multiplicar por 255 para hacer la imagen visible

        
        print(f"Valor mínimo: {min_val}")
        print(f"Valor máximo: {max_val}")

        elapsed_time = time.time() - start_time
        if elapsed_time > 16:
            print("Tiempo excedido buscando el signo de admiración. La captura falló.")
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            return False

        if max_val >= threshold:
            top_left = (max_loc[0] + region['left'], max_loc[1] + region['top'])
            bottom_right = (top_left[0] + w, top_left[1] + h)
            screen_with_rectangle = screenshot()  # Tomar una captura de pantalla completa para dibujar el rectángulo
            cv2.rectangle(screen_with_rectangle, top_left, bottom_right, (0, 255, 0), 2)
            cv2.imwrite('screenshot_with_detection.png', screen_with_rectangle)
            print("Signo de admiración encontrado y marcado en 'screenshot_with_detection.png'")
            return True
        else:
            print("Signo de admiración no encontrado. Reintentando")

# Función para pescar
def fish(exclamation_region):
    print("Simulando la primera pulsación de la barra espaciadora...")
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    print("Primera pulsación realizada.")
    time.sleep(2)
    print("Simulando la segunda pulsación de la barra espaciadora...")
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    print("Esperando la aparición del signo de admiración...")
    if find_exclamation_sign(signo_path, region=exclamation_region):
        print("Simulando la pulsación de la barra espaciadora para capturar")
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        print("Pulsación realizada. Pez capturado.")
        print("Esperar 3 segundos para terminar la pesca.")
        time.sleep(3)
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    else:
        print("Captura fallida. Reintentando todo el proceso...")

# Ruta al template del área de pesca
template_path = r'C:\Users\juane\Desktop\Programas Samir\scriptspython\img\pesca.png'
signo_path = r'C:\Users\juane\Desktop\Programas Samir\scriptspython\img\ruta.png'

# Función principal para ejecutar el ciclo de pesca
def main():
    screen_width = 1920  # Ajusta esto según la resolución de tu pantalla
    screen_height = 1080  # Ajusta esto según la resolución de tu pantalla

    half_screen_region = {
        "top": 0,
        "left": screen_width // 2,
        "width": screen_width // 2,
        "height": screen_height
    }

    while True:
        # Buscar el área de pesca con diferentes métodos de coincidencia
        methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF, cv2.TM_CCORR_NORMED]

        fishing_area = None
        for method in methods:
            print(f"Probando con el método de coincidencia: {method}")
            fishing_area = find_fishing_area(template_path, method=method, region=half_screen_region)
            
            if fishing_area:
                # Define la región donde esperarás ver el signo de admiración (ajusta según sea necesario)
                specific_region = {
                    "top": 500,   
                    "left": 1150, 
                    "width": 300, 
                    "height": 300
                }

                fish(specific_region)
                break
            else:
                print(f"No se encontró el área de pesca con el método: {method}")

        if not fishing_area:
            print("No se encontró el área de pesca con ningún método. Reintentando...")

if __name__ == "__main__":
    main()
 