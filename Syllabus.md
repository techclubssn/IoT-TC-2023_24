# IoT Syllabus - TechClub 2023-24
`Progress: ====>______________________________________ - 11.628%`
### Introduction to Raspberry Pi and basic sensors  
  
- :ballot_box_with_check:  High level understanding on the architecture  
- :ballot_box_with_check:  OS booting  
- :black_square_button:  Useful Linux commands  
- :black_square_button:  Introduction to GPIO programming  
    - :ballot_box_with_check:  Basic Output scripts (LED blinking)  
    - :black_square_button:  Sensors – Theory and working  
        - :black_square_button:  Ultrasonic  
        - :black_square_button:  PIR  
        - :black_square_button:  DHT11 temperature and humidity sensor  
        - :black_square_button:  Raspberry Pi camera.  
  
### Introduction to Arduino  
  
- :black_square_button:  High level understanding of Arduino and its work environment  
- :black_square_button:  Installing Arduino IDE  
- :black_square_button:  GPIO programming  
    - :black_square_button:  Arduino UNO to interface most of the sensors mentioned  
    - :black_square_button:  PWM  
    - :black_square_button:  ADC  
    - :black_square_button:  Interrupts  
  
### ESP 32 or ESP 8266  
  
In case of hardware constraints, Web based simulators would be used.  
  
- :black_square_button:  High level understanding of ESP32 or ESP8266 architecture  
- :black_square_button:  Setting up Arduino IDE for programming ESP32 (or) ESP8266  
- :black_square_button:  Basic GPIO programming  
- :black_square_button:  Setting up ESP32 (or) ESP8266 to host a web server to control the status GPIO pins (including PWM control)  
- :black_square_button:  Hosting a basic Telegram bot on ESP32 (or) ESP8266  
- :black_square_button:  `ESP32 Specific`  
    - :black_square_button:  Exploring dual core architecture of ESP32 for real time use cases  
    - :black_square_button:  Using the inbuilt Bluetooth functionality.  
  
### Wired or Hardware Communication protocols  
  
Arduino IDE compatible microcontrollers shall be used.  
  
In case of hardware constraints, Web based simulators would be used.  
  
- :black_square_button:  UART - Universal asynchronous receiver transmitter  
    - :black_square_button:  Interfacing HC-06 Bluetooth module for serial Bluetooth communication  
- :black_square_button:  SPI - Serial Peripheral Interface  
    - :black_square_button:  Interfacing IC 74595 for serial in parallel out data transfer using SPI  
- :black_square_button:  I2C - Inter Integrated Circuit  
    - :black_square_button:  Communicating with BMP180 sensor or LCD or OLED display or simple data transfer between two Arduinos (in case of hardware constraints).  
  
### Backend server development to accumulate data from ESP32 (or) ESP8266  
  
- :black_square_button:  Introduction to the light weight flask python web framework  
- :black_square_button:  Coding session for GET and POST HTTP routes.  
- :black_square_button:  Programming ESP32 (or) ESP8266 (or Raspberry Pi 4 in case of hardware constraints) to send GET and POST requests to the server for data exchange.  
  
### MQTT protocol for bi-directional communication  
  
- :black_square_button:  General overview on MQTT protocol  
- :black_square_button:  Setting up Mosquito broker in Raspberry Pi 4  
- :black_square_button:  Programming ESP32 (or ESP8266) to publish sensor data and subscribe topics to control GPIO pins or display a message on a display.  
- :black_square_button:  Basic introduction to web sockets (if time permits).  
  
### Soldering Session  
  
- :black_square_button:  Soldering of basic circuit such as an astable multivibrator using 555 timers or LM386 based audio amplifier using THT components on a Perfboard.  
- :black_square_button:  Purpose of header pins, flux, IC base.  
  
### Introduction to Schematic and PCB design  
  
This topic was mainly included to give an exposure to students on the usage and importance of Schematic and PCB Design.  
  
This was executed in the form of a workshop during Tesla 2023.  
  
Schematic design will be thought in parallel to other classes.  
  
Resources on PCB design will be shared. If time permits, we can have a session on a simple two-layer PCB design.  
  
- :ballot_box_with_check:  Using KiCAD  
- :ballot_box_with_check:  Basic schematic design  
- :black_square_button:  Layout of a simple two-layer PCB
