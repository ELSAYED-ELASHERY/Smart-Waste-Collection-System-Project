# استيراد المكتبات اللازمة
import RPi.GPIO as GPIO     # مكتبة التحكم في منافذ Raspberry Pi
import time                 # مكتبة لإضافة تأخير زمني

# اختيار نظام ترقيم الدبابيس BCM (أي رقم GPIO نفسه)
GPIO.setmode(GPIO.BCM)

# تحديد البن الذي سنوصل عليه السيرفو
SERVO_PIN = 18

# ضبط البن كمخرج
GPIO.setup(SERVO_PIN, GPIO.OUT)

# إنشاء PWM على البن 18 بتردد 50Hz
# أغلب السيرفو يعمل على تردد 50
pwm = GPIO.PWM(SERVO_PIN, 50)

# بدء PWM بقيمة 0
pwm.start(0)

try:

    while True:

        # في السيرفو 360 درجة:
        # 7.5 تقريباً = توقف
        # أقل من 7.5 = دوران عكس عقارب الساعة
        # أكثر من 7.5 = دوران مع عقارب الساعة

        print("السيرفو يدور يمين")
        pwm.ChangeDutyCycle(9)   # دوران يمين
        time.sleep(3)

        print("توقف السيرفو")
        pwm.ChangeDutyCycle(7.5) # توقف
        time.sleep(2)

        print("السيرفو يدور شمال")
        pwm.ChangeDutyCycle(6)   # دوران شمال
        time.sleep(3)

        print("توقف السيرفو")
        pwm.ChangeDutyCycle(7.5) # توقف
        time.sleep(2)

# عند الضغط على Ctrl+C
except KeyboardInterrupt:

    # إيقاف PWM
    pwm.stop()

    # إعادة ضبط جميع المنافذ
    GPIO.cleanup()

    print("تم إيقاف البرنامج")