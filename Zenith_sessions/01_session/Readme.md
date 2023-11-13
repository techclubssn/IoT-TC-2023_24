## Script and general instruction for basic GPIO programming
- Usually, the python library `RPi.GPIO` will be pre-installed with Raspberry Pi OS, but just in case if you get `Module Not found error` . You can install it by using the command,
    
    ```bash
    pip install RPi.GPIO
    ```
    
- The below code is a script for toggling LED every 1 second:
    
    To start typing in code, you can use the Geany editor or use `nano` to write the script.
    
    - For nano, open up the terminal and type in `nano <file_name>.py` and then start typing in the script given below.
    
    ```python
    # import the necessary packages
    import RPi.GPIO as GPIO 
    from time import sleep
    
    # GPIO configurations
    GPIO.setmode(GPIO.BOARD) # This is used to inform the GPIO module that you will be 
    # using the pin mapping with respect to the board.
    GPIO.setup(40,GPIO.OUT,initial=0) # Here you're setting the GPIO pin number 40 to be
    # an output port with the initial value of Logic zero (or) 0V
    
    try: # Runs the try block until an exception like (Ctrl+C) to stop the code occurs.
      while True:
      	GPIO.output(40,1) # We are setting the GPIO pin 40 to High
      	sleep(1) # 1 second of delay
      	GPIO.output(40,0) # We are setting the GPIO pin 40 to Low
      	sleep(0) # 1 second of delay
    except: # This segment of code runs on exit
    	GPIO.cleanup() # This is used to clear the hardware configuration (registers) that was made during the GPIO configuration
    ```
    
    In order to execute this file, use
    
    ```bash
    python3 <file_name>.py
    ```
    
- You should see the LED in pin number 40 blinking (hopefully you didn’t burn anything :) Congrats if this your first time programming the Raspberry Pi!
