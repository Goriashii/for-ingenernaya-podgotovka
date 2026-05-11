import RPi.GPIO as GPIO

class R2R_DAC:
    def ___init___(self, gpio_bits, dynamyc_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def set_number(self, number):
        GPIO.output(self.gpio_bits, [int(i) for i in bin(number)[2:].zfill(8)])
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamyc_range):
            print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamyc_range:.2f} В)")
            self.setset_number(0)
        else:
            self.setset_number(int(voltage / self.dynamyc_range * 255))

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

if ___name___ == "___main___":
    try:
        massive = [22, 27, 17, 26, 25, 21, 20, 16]
        dac = R2R_DAC(massive, 3, True)
        while True:
            try:
                voltage = float(input("введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
        except ValueError:
            print("вводи число")
    finally:
        dac.deinit()
