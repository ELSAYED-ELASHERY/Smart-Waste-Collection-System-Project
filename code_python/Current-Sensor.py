# استيراد المكتبات اللازمة
import time                   # لإنشاء تأخيرات
import board                  # للوصول إلى دبابيس Raspberry Pi
import busio                  # للتواصل عبر I2C
import adafruit_ads1x15.ads1115 as ADS    # مكتبة ADS1115
from adafruit_ads1x15.analog_in import AnalogIn  # قراءة القنوات التناظرية

# إنشاء واجهة I2C (SDA و SCL على Pi)
i2c = busio.I2C(board.SCL, board.SDA)

# تهيئة محول ADS1115
ads = ADS.ADS1115(i2c)

# اختيار القناة A0 من ADS1115
channel = AnalogIn(ads, ADS.P0)

# حساسية حساس ACS712 20A
sensitivity = 0.100   # 100mV لكل أمبير

# جهد الخمول (2.5V عند صفر تيار)
offset_voltage = 2.5

# حلقة لقراءة التيار باستمرار
while True:
    # قراءة الجهد من الحساس
    voltage = channel.voltage

    # حساب التيار من الجهد
    current = (voltage - offset_voltage) / sensitivity

    # طباعة الجهد والتيار
    print(f"جهد الحساس: {voltage:.3f} V")
    print(f"التيار المقاس: {current:.3f} A")
    print("----------------------------")

    # الانتظار ثانية واحدة قبل القراءة التالية
    time.sleep(1)