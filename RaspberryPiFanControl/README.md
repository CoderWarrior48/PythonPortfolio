
# Fan Control - Raspberry Pi 4

Ever get annoyed of the fan on your Pi? Following this amazing tutorial [here](https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/) to automatically regulate your fan speed based on the temperature of your CPU.

For me however, that wasn't enough. I added a control gui with python to switch the fan from automatic to manual mode. This control can easily be accessed from the taskbar and runs on python with tkinter: 

[!WARNING]
These programs access eachother in your system! File paths must be configured to your system and permissions enabled to execute bash files.

## Configuration

Start by updating the file paths in the files below

`launcher.sh`
`fan-control-app/launcher.sh`
`fan_ctrl.py`

Replace the */yournamehere/* sections with your pi's name, or 'pi' if you haven't specified one. (ex. /home/pi/Desktop/fan-control-app)

Once complete you need to move these files into the correct places.

- The *Script* file goes in place of the original from the tutorial
- The fan-control-app goes in the *Desktop* folder
- The fan-control.desktop goes in */.local/share/applications (This location might be hidden so try View > Show Hiden)

After everything has been configured you should be successfully able to run the 


main menu > new item > app launcher > add