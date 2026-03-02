#
# Thermostat - Final Project working code
# Buttons: Cycle=GPIO24, Up=GPIO25, Down=GPIO21
#

from time import sleep
from datetime import datetime
from threading import Thread
from math import floor

from statemachine import StateMachine, State

import board
import adafruit_ahtx0

import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

import serial

from gpiozero import Button, PWMLED

DEBUG = True

# -------------------------
# I2C Sensor Setup
# -------------------------
i2c = board.I2C()
thSensor = adafruit_ahtx0.AHTx0(i2c)

# -------------------------
# Serial (UART) Setup
# -------------------------
ser = serial.Serial(
    port='/dev/ttyS0',      # /dev/ttyAMA0 on older Pi models
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# -------------------------
# LEDs (PWM)
# -------------------------
redLight = PWMLED(18)
blueLight = PWMLED(23)

# -------------------------
# LCD Display Manager
# -------------------------
class ManagedDisplay():
    def __init__(self):
        self.lcd_rs = digitalio.DigitalInOut(board.D17)
        self.lcd_en = digitalio.DigitalInOut(board.D27)
        self.lcd_d4 = digitalio.DigitalInOut(board.D5)
        self.lcd_d5 = digitalio.DigitalInOut(board.D6)
        self.lcd_d6 = digitalio.DigitalInOut(board.D13)
        self.lcd_d7 = digitalio.DigitalInOut(board.D26)

        self.lcd_columns = 16
        self.lcd_rows = 2

        self.lcd = characterlcd.Character_LCD_Mono(
            self.lcd_rs, self.lcd_en,
            self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7,
            self.lcd_columns, self.lcd_rows
        )
        self.lcd.clear()

    def cleanupDisplay(self):
        self.lcd.clear()
        self.lcd_rs.deinit()
        self.lcd_en.deinit()
        self.lcd_d4.deinit()
        self.lcd_d5.deinit()
        self.lcd_d6.deinit()
        self.lcd_d7.deinit()

    def clear(self):
        self.lcd.clear()

    def updateScreen(self, message: str):
        self.lcd.clear()
        self.lcd.message = message


screen = ManagedDisplay()

# -------------------------
# Thermostat State Machine
# -------------------------
class TemperatureMachine(StateMachine):
    off = State(initial=True)
    heat = State()
    cool = State()

    setPoint = 72
    endDisplay = False
    forceShowState = False
    cycle = (
        off.to(heat) |
        heat.to(cool) |
        cool.to(off)
    )

    def on_enter_heat(self):
        if DEBUG:
            print("* Changing state to heat")
        self.updateLights()

    def on_exit_heat(self):
        # Stop any red pulsing as we leave heat
        redLight.off()

    def on_enter_cool(self):
        if DEBUG:
            print("* Changing state to cool")
        self.updateLights()

    def on_exit_cool(self):
        # Stop any blue pulsing as we leave cool
        blueLight.off()

    def on_enter_off(self):
        if DEBUG:
            print("* Changing state to off")
        redLight.off()
        blueLight.off()

    def processTempStateButton(self):
        if DEBUG:
            print("Cycling Temperature State")
        self.cycle()
        self.updateLights()
        self.forceShowState = True
    def processTempIncButton(self):
        if DEBUG:
            print("Increasing Set Point")
        self.setPoint += 1
        self.updateLights()
        self.forceShowState = True
    def processTempDecButton(self):
        if DEBUG:
            print("Decreasing Set Point")
        self.setPoint -= 1
        self.updateLights()
        self.forceShowState = True
    def run(self):
        myThread = Thread(target=self.manageMyDisplay, daemon=True)
        myThread.start()

    def getFahrenheit(self) -> float:
        t_c = thSensor.temperature
        return ((9 / 5) * t_c) + 32

    def setupSerialOutput(self) -> str:
        # Format: state,tempF,setPoint
        tempF = floor(self.getFahrenheit())
        output = f"{self.current_state.id},{tempF},{self.setPoint}\n"
        return output

    def updateLights(self):
        temp = floor(self.getFahrenheit())

        # Always start from a known state
        redLight.off()
        blueLight.off()

        if DEBUG:
            print(f"State: {self.current_state.id}")
            print(f"SetPoint: {self.setPoint}")
            print(f"Temp: {temp}")

        if self.current_state == self.off:
            # Both off
            redLight.off()
            blueLight.off()

        elif self.current_state == self.heat:
            # Heat: red fades if temp < setPoint, else solid
            blueLight.off()
            if temp < self.setPoint:
                redLight.pulse(fade_in_time=1, fade_out_time=1, background=True)
            else:
                redLight.on()

        elif self.current_state == self.cool:
            # Cool: blue fades if temp > setPoint, else solid
            redLight.off()
            if temp > self.setPoint:
                blueLight.pulse(fade_in_time=1, fade_out_time=1, background=True)
            else:
                blueLight.on()

    def _fmt16(self, s: str) -> str:
        # Ensure exactly 16 chars (LCD width)
        s = s[:16]
        return s.ljust(16)

    def manageMyDisplay(self):
        counter = 1
        altCounter = 1

        while not self.endDisplay:
            if DEBUG:
                print("Processing Display Info...")

            current_time = datetime.now()

            # Line 1: Date + Time (16 chars)
            # Example: "02/24 10:15:30"
            line1 = current_time.strftime("%m/%d %H:%M:%S")
            lcd_line_1 = self._fmt16(line1) + "\n"

            # Line 2 alternates between temp and state/setpoint
            tempF = floor(self.getFahrenheit())
            if self.forceShowState:
                altCounter = 6
                self.forceShowState = False 
            if altCounter < 6:
                # Show current temp
                # Example: "Temp: 72F      "
                line2 = f"Temp:{tempF:>3}F"
                lcd_line_2 = self._fmt16(line2)

                altCounter += 1
            else:
                # Show state + setpoint
                # Example: "HEAT SP: 72F   "
                state = self.current_state.id.upper()
                if state == "OFF":
                    state_txt = "OFF "
                elif state == "HEAT":
                    state_txt = "HEAT"
                else:
                    state_txt = "COOL"

                line2 = f"{state_txt} SP:{self.setPoint:>3}F"
                lcd_line_2 = self._fmt16(line2)

                altCounter += 1
                if altCounter >= 11:
                    self.updateLights()
                    altCounter = 1

            screen.updateScreen(lcd_line_1 + lcd_line_2)

            # Every 30 seconds: send UART update
            if DEBUG:
                print(f"Counter: {counter}")

            if (counter % 30) == 0:
                try:
                    out = self.setupSerialOutput()
                    ser.write(out.encode("utf-8"))
                    if DEBUG:
                        print(f"UART Sent: {out.strip()}")
                except Exception as e:
                    print(f"UART send failed: {e}")
                counter = 1
            else:
                counter += 1

            sleep(1)

        # Cleanup display when exiting
        screen.cleanupDisplay()


# -------------------------
# Start machine + buttons
# -------------------------
tsm = TemperatureMachine()
tsm.run()

# Buttons (BCM)
# Green = cycle (GPIO24)
greenButton = Button(24, pull_up=True, bounce_time=0.05)
greenButton.when_pressed = tsm.processTempStateButton

# Red = setpoint up (GPIO25)
redButton = Button(25, pull_up=True, bounce_time=0.05)
redButton.when_pressed = tsm.processTempIncButton

# Blue = setpoint down (GPIO21)  <-- your new wiring
blueButton = Button(21, pull_up=True, bounce_time=0.05)
blueButton.when_pressed = tsm.processTempDecButton

repeat = True
while repeat:
    try:
        sleep(30)
    except KeyboardInterrupt:
        print("Cleaning up. Exiting...")
        repeat = False
        tsm.endDisplay = True
        redLight.off()
        blueLight.off()
        try:
            ser.close()
        except:
            pass
        sleep(1)
