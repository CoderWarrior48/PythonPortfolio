
# Fan Control - Raspberry Pi 4

Ever get annoyed of the fan on your Pi? Following this amazing tutorial [here](https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/) to automatically regulate your fan speed based on the temperature of your CPU.

For me however, that wasn't enough. I added a control app with python to switch the fan from automatic to manual mode. This control can easily be accessed from the taskbar and runs on python with tkinter: 

> [!WARNING]
> These programs access eachother in your system! File paths must be configured to your system and permissions enabled to execute certain bash files.

## Configuration

Start by updating the file paths in the files below

`launcher.sh`
`fan-control-app/launcher.sh`
`fan_ctrl.py`

Replace the */yournamehere/* sections with your pi's name, or 'pi' if you haven't specified one. (ex. `/home/pi/Desktop/fan-control-app`)

Once complete you need to move these files into the correct places.

- The `Scripts` folder goes in place of the original from the tutorial
- The fan-control-app goes in the `/Desktop` folder
- The fan-control.desktop goes in anywhere you prefere, *Desktop* to keep it simple

After everything has been configured you should be successfully able to run the program by double clicking the `fan-control.desktop` file. 

Finally, add this app to your taskbar. Start by right clicking the taskbar and selecting add/change items. From the panel that pops up, select add new > app launcher. A plus sign or other symbol should now appear on your taskbar. Click on it and select other > Fan Control and then add item. 

If everything works as expected you should be able to click on the icon in your taskbar and a window will pop up. Click automatic to switch to automatic mode or choose a speed on the slider and click manual to send the new speed to the fan. 


## How does it work?

The inital program begins on startup. However, a few changes to the origonal python program tells it to constantly check the text file `mode.txt`. The current mode and information is saved in this file. The `fan-control-app` uses inputs from a tkinter app to change and update the same file, providing a connection between the two separate programs. Because of this setup, you can close the app or even reboot your pi and it will save the current mode and speed.