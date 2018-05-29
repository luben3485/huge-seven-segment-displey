import RPi.GPIO as GPIO
import numpy as np
import time
import sys
GPIO.setmode(GPIO.BOARD)

#one bit
'''
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
'''
first_pins = np.array([3,5,7,11,13,15,19],np.int32)
second_pins = np.array([21,23,29,31,33,35,37],np.int32)
third_pins = np.array([8,10,12,16,18,22,24],np.int32)
for i in range (0,7):
    GPIO.setup(first_pins[i],GPIO.OUT)
    GPIO.setup(second_pins[i],GPIO.OUT)
    GPIO.setup(third_pins[i],GPIO.OUT)

number       = np.array([[1,1,1,1,1,1,0],  # = 0
                         [0,1,1,0,0,0,0],  # = 1
                         [1,1,0,1,1,0,1],  # = 2
                         [1,1,1,1,0,0,1],  # = 3
                         [0,1,1,0,0,1,1],  # = 4
                         [1,0,1,1,0,1,1],  # = 5
                         [1,0,1,1,1,1,1],  # = 6
                         [1,1,1,0,0,0,0],  # = 7
                         [1,1,1,1,1,1,1],  # = 8
                         [1,1,1,0,0,1,1]],np.int32) # = 9
cycle        = np.array([[1,0,0,0,0,0,0],  # = 
                         [0,1,0,0,0,0,0],  # = 
                         [0,0,1,0,0,0,0],  # = 
                         [0,0,0,1,0,0,0],  # = 
                         [0,0,0,0,1,0,0],  # = 
                         [0,0,0,0,0,1,0]],np.int32)
blank = np.array([[0,0,0,0,0,0,0]],np.int32)
lightall = np.array([[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]],np.int32)
ES = np.array([[1,0,0,1,1,1,1],[1,0,1,1,0,1,1]],np.int32)
unique_one = np.array([[0,0,0,0,1,1,0]],np.int32)

def light(pos,digit_array,num):
    for index in range(0,7):
       # is_light = seven_digits[num,index]
        is_light = digit_array[num,index] 
        pin = int(pos[index])
       # print(pin)
        if is_light == 1:
            GPIO.output(pin,GPIO.HIGH)
        else:
            GPIO.output(pin,GPIO.LOW)

def lightES_107_520_886(sec):
    light(first_pins,ES,0)
    light(second_pins,ES,1)
    light(third_pins,blank,0)
    time.sleep(sec)
    light(first_pins,unique_one,0)
    light(second_pins,number,0)
    light(third_pins,number,7)
    time.sleep(sec)
    light(first_pins,number,5)
    light(second_pins,number,2)
    light(third_pins,number,0)
    time.sleep(sec)
    light(first_pins,number,8)
    light(second_pins,number,8)
    light(third_pins,number,6)
    time.sleep(sec)


def light_num_p(sec,a,b,c):
    for i in range(0,a+1):
        for j in range(0,b+1):
            for k in range(0,c+1):
                light(first_pins,number,i)
                light(second_pins,number,j)
                light(third_pins,number,k)
                print(i,j,k)
                time.sleep(sec)

def light_num_n(sec,a,b,c):
    for i in range(a,-1,-1):
        for j in range(b,-1,-1):
            for k in range(c,-1,-1):
                light(first_pins,number,i)
                light(second_pins,number,j)
                light(third_pins,number,k)
                print(i,j,k)
                time.sleep(sec)
'''
def big_cycle(sec):
    light(first_pins,cycle,0)
    light(second_pins,blank,0)
    light(third_pins,blank,0)
    time.sleep(sec)
    light(second_pins,cycle,0)
    light(first_pins,blank,0)
    light(third_pins,blank,0)
    time.sleep(sec)
    light(third_pins,cycle,0)
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    time.sleep(sec)
    light(third_pins,cycle,1)
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    time.sleep(sec)
    light(third_pins,cycle,2)
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    time.sleep(sec)
    light(third_pins,cycle,3)
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    time.sleep(sec)
    light(second_pins,cycle,3)
    light(first_pins,blank,0)
    light(third_pins,blank,0)
    time.sleep(sec)
    light(first_pins,cycle,3)
    light(second_pins,blank,0)
    light(third_pins,blank,0)
    time.sleep(sec)
    light(first_pins,cycle,4)
    light(second_pins,blank,0)
    light(third_pins,blank,0)
    time.sleep(sec)
    light(first_pins,cycle,5)
    light(second_pins,blank,0)
    light(third_pins,blank,0)
    time.sleep(sec)
'''
    


'''
while True:
    lightES_107_520_886(5)
'''

while True:
    for index in range(0,1):
        light(first_pins,lightall,index)
        light(second_pins,lightall,index)
        light(third_pins,lightall,index)
        time.sleep(2)	

'''
while True:
    light_num_n(0.2,9,9,9)
'''

'''
while True:
    for index in range(0,1):
        light(first_pins,lightall,index)
        light(second_pins,lightall,index)
        light(third_pins,lightall,index)

        time.sleep(1)	
'''

'''
while True:
    input1_str=input('enter:')
    input1_list=input1_str.split()
    for i in range(len(input1_list)):
        input1_list[i]=int(input1_list[i])
        print(type(input1_list))
        print(input1_list)
        for index in range(len(input1_list)):
            is_light = input1_list[index]
            pin = int(first_pins[index])
            if is_light == 1:
                GPIO.output(pin,GPIO.HIGH)
            else:
                GPIO.output(pin,GPIO.LOW)
'''












