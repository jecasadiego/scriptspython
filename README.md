
# Digimon World: Next Order Fishing Bot

Este proyecto proporciona un script en Python para automatizar la pesca en el videojuego **Digimon World: Next Order**. Usando este script, tu personaje pescará automáticamente cuando estés cerca de una zona de pesca, detectando el signo de exclamación para capturar peces.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias de Python:

- `opencv-python`
- `numpy`
- `mss`
- `pynput`
- `pyopengl`

Puedes instalar todas las dependencias usando pip:

```sh
pip install opencv-python numpy mss pynput pyopengl
```

## Uso

1. Clona este repositorio o descarga los archivos a tu máquina local.
2. Asegúrate de tener las imágenes `pesca.png` y `pesca_signo.png` en la carpeta `img` dentro del directorio del script.
3. Ejecuta el script principal `fishing_script.py`.

### Ejecución del Script

Abre una terminal en el directorio donde descargaste el script y ejecuta:

```sh
python fishing_script.py
```

El script esperará 5 segundos para permitirte colocar el juego en la posición correcta y luego comenzará a buscar el área de pesca y el signo de exclamación para iniciar la pesca automática.

## Estructura del Proyecto

```
.
├── img
│   ├── pesca.png
│   └── pesca_signo.png
│       
├── scriptdigimon.py
└── README.md
```

## Descripción del Script

- **screenshot(region)**: Captura una pantalla completa o una región específica de la pantalla.
- **find_fishing_area(template_path, threshold, method, region)**: Busca el área de pesca en la pantalla.
- **find_exclamation_sign(template_path, threshold, method, region)**: Busca el signo de exclamación en una región específica.
- **fish(exclamation_region)**: Ejecuta el proceso de pesca, simulando pulsaciones de teclas para capturar el pez.
- **main()**: Función principal que ejecuta el ciclo de pesca.

## Contribución

Si deseas contribuir a este proyecto, por favor, abre un issue o envía un pull request con tus mejoras.

## Licencia

Este proyecto está licenciado bajo la MIT License. Consulta el archivo [LICENSE](LICENSE) para más detalles.

### Notas Adicionales

1. **Seguridad**: Asegúrate de que tu juego esté en primer plano y en la zona de pesca cuando ejecutes el script.
2. **Permisos de Administrador**: Ejecuta la terminal o el entorno de desarrollo como administrador para asegurar que el script tenga los permisos necesarios.
3. **Ajustes de Resolución**: Ajusta las resoluciones de `screen_width` y `screen_height` en el script según tu pantalla.

Si tienes más preguntas o necesitas ayuda, no dudes en abrir un issue en el repositorio. ¡Feliz pesca en el mundo de Digimon!
