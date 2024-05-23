
# Digimon World: Next Order Fishing Bot

This project provides a Python script to automate fishing in the video game **Digimon World: Next Order**. Using this script, your character will automatically fish when near a fishing zone, detecting the exclamation sign to catch fish.

## Requirements

Before running the script, ensure you have the following Python dependencies installed:

- `opencv-python`
- `numpy`
- `mss`
- `pynput`
- `pyopengl`

You can install all dependencies using pip:

```sh
pip install opencv-python numpy mss pynput pyopengl
```

## Usage

1. Clone this repository or download the files to your local machine.
2. Ensure you have the images `pesca.png` and `pesca_signo.png` in the `img` folder within the script directory.
3. Run the main script `scriptdigimon.py`.

### Running the Script

Open a terminal in the directory where you downloaded the script and run:

```sh
python scriptdigimon.py
```

The script will wait 5 seconds to allow you to position the game correctly and then start looking for the fishing area and the exclamation sign to initiate automatic fishing.

## Project Structure

```
.
├── img
│   ├── pesca.png
│   └── pesca_signo.png
│       
├── scriptdigimon.py
└── README.md
```

## Script Description

- **screenshot(region)**: Captures a full-screen or a specific region of the screen.
- **find_fishing_area(template_path, threshold, method, region)**: Searches for the fishing area on the screen.
- **find_exclamation_sign(template_path, threshold, method, region)**: Searches for the exclamation sign in a specific region.
- **fish(exclamation_region)**: Executes the fishing process, simulating key presses to catch the fish.
- **main()**: Main function that runs the fishing cycle.

## Contribution

If you want to contribute to this project, please open an issue or submit a pull request with your improvements.

## Important Warning

This script only works through screen detection, so the programmed fishing zone will depend on the reference file in pesca.png; in this case, it is programmed for fishing pond #2 in Floatia's entertainment zone with Seadramon. If you want to change the programmed place, follow these steps:

1. Go to the fishing zone you want in Digimon World: Next Order.
2. Capture the full screen when the fishing icon appears and the Digimon have their health bars on the screen.
3. Replace the pesca.png file with the screenshot you just took and rename it to pesca.png or change the code path in the following lines:

```sh
template_path = r'C:\Users\juane\Desktop\Programas Samir\scriptspython\img\pesca.png'
signo_path = r'C:\Users\juane\Desktop\Programas Samir\scriptspython\img\ruta.png'
```

4. Ensure that *signo_path* is the capture of the exclamation sign when it shows that you can fish in the new zone you just changed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Additional Notes

1. **Security**: Make sure your game is in the foreground and in the fishing zone when you run the script.
2. **Administrator Permissions**: Run the terminal or development environment as an administrator to ensure the script has the necessary permissions.
3. **Resolution Settings**: Adjust the resolutions of `screen_width` and `screen_height` in the script according to your screen.

If you have more questions or need help, feel free to open an issue in the repository. Happy fishing in the world of Digimon!
