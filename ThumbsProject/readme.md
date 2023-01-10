### This project uses the Jetbot image.

## Packages
Use of the [Jetson.GPIO](https://github.com/NVIDIA/jetson-gpio) package. 
Install using pip on the Jetbot and follow the instructions on the GitHub

## Steps:
1. Run all of the cells in the notebook.
2. Collect data.
3. Create a model. Using 10 epochs is usually sufficient.
4. Run live model to see predictions
5. If working, connect a wire from pin on Arduino to Jetson pin. Default is 12 on Jetson and 8 on Arduino.
6. Ardunio Serial output should mimic prediction.

## Common Troubleshooting

# Camera has multiple instances
Camera is being used in another module. Try camera.stop(). If this doesn't work, reset Kernel. If this doesn't work, reset Jetbot.

# GPIO Ports already decleared
Comment out the GPIO setup lines. Or, restart Kernal/Jetbot.
