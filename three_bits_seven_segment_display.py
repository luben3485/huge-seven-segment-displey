import RPi.GPIO as GPIO
import numpy as np
import time
import sys
import random
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
hori = np.array([[1,0,0,1,0,0,1]],np.int32)
def light_line(pos,num):
    GPIO.output(pos[num],GPIO.HIGH)
def dark_line(pos,num):
    GPIO.output(pos[num],GPIO.LOW)

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

def big_cycle_1(sec):
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

def small_cycle(sec):

    for index in range(0,6):
        light(first_pins,cycle,index)
        light(second_pins,cycle,index)
        light(third_pins,cycle,index)
        time.sleep(sec)

def  big_cycle_2(sec,count):
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    light(third_pins,blank,0)

    time.sleep(0.1)

    cycle_pin = ["first_pins","second_pins","third_pins","third_pins","third_pins","third_pins","second_pins","first_pins","first_pins","first_pins"]
    cycle_index = np.array([0,0,0,1,2,3,3,3,4,4],np.int32)

    for i in  range(0,count):
        light_line(cycle_pin[i],cycle_index[i])
        time.sleep(sec)

    for i in range(count-1,-1,-1):
        dark_line(cycle_pin[i],cycle_index[i])
        time.sleep(sec)

def big_cycle_3(sec):
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    light(third_pins,blank,0)

    time.sleep(0.1)

    cycle_pin = ["first_pins","second_pins","third_pins","third_pins","third_pins","third_pins","second_pins","first_pins","first_pins","first_pins"]
    cycle_index = np.array([0,0,0,1,2,3,3,3,4,4],np.int32)
    
    count = 10
    for j in range(0,9):
        light_line(cycle_pin[0],cycle_index[0])
        time.sleep(sec)
        for i in range(1,count):
            dark_line(cycle_pin[i-1],cycle_index[i-1])
            light_line(cycle_pin[i],cycle_index[i])
            time.sleep(sec)
        count = count - 1
    light_line(cycle_pin[0],cycle_index[0])
    time.sleep(sec)

def hori_line(sec):
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    light(third_pins,blank,0)

    time.sleep(0.1)

    light(first_pins,hori,0)
    time.sleep(sec)
    light(second_pins,hori,0)
    time.sleep(sec)
    light(third_pins,hori,0)
    time.sleep(sec)
    light(first_pins,blank,0)
    time.sleep(sec)
    light(second_pins,blank,0)
    time.sleep(sec)
    light(third_pins,blank,0)
    time.sleep(sec)


def vert_line(sec):
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    light(third_pins,blank,0)

    time.sleep(0.1)
    vert_pin = ["first_pins","second_pins","third_pins"]
    for i in range(0,3): 
        light_line(vert_pin[i],1)
        light_line(vert_pin[i],5)
    time.sleep(sec)

    for i in range(0,3):
        light_line(first_pins,2)
        light_line(first_pins,4)
    time.sleep(sec)

    for i in range(0,3): 
        dark_line(vert_pin[i],1)
        dark_line(vert_pin[i],5)
    time.sleep(sec)

    for i in range(0,3):
        dark_line(first_pins,2)
        dark_line(first_pins,4)
    time.sleep(sec)

def Scrolling_digit(sec,str):
    light(first_pins,blank,0)
    light(second_pins,blank,0)
    light(third_pins,blank,0)

    time.sleep(0.1)

    num_arr = []
    for i in range(0,len(str)):
        tmp = int(str[i])
        num_arr.append(tmp)
        #print(num_arr)
    first = -3
    second = -2
    third = -1
    length = len(num_arr)

    for i in range(0,length+4):
        tmp1 = tmp2 = tmp3 = "x"
        if(first >= 0 and first < length):
            light(first_pins,number,num_arr[first])
            tmp1 = num_arr[first]
        else:
            light(first_pins,blank,0)

        if(second >= 0 and second < length):
            light(second_pins,number,num_arr[first])
            tmp2 = num_arr[second]
        else:
            light(first_pins,blank,0)

        if(third >= 0 and third < length):
            light(third_pins,number,num_arr[first])
            tmp3 =num_arr[third]
        else:
            light(first_pins,blank,0)
        print("[",tmp1,tmp2,tmp3,"]")
        time.sleep(sec)
        first += 1
        second += 1
        third += 1

def random_num(sec_for_random,sec_for_display,random_count,display_num):
    
    for i in range(0,random_count):
        num = random.randint(0,9)
        light(first_pins,number,num)
        num = random.randint(0,9)
        light(second_pins,number,num)
        num = random.randint(0,9)
        light(third_pins,number,num)
        time.sleep(sec_for_random)
    light(first_pins,number,int(display_num[0]))
    light(second_pins,number,int(display_num[1]))
    light(third_pins,number,int(display_num[2]))
    time.sleep(sec_for_display)


def dark_light(sec):
    #dark
    light(first_pins,lightall,1)
    light(second_pins,lightall,1)
    light(third_pins,lightall,1)
    time.sleep(sec)
    #light
    light(first_pins,lightall,0)
    light(second_pins,lightall,0)
    light(third_pins,lightall,0)
    time.sleep(sec)

def dark_light_num(sec,num):
    #dark
    light(first_pins,lightall,1)
    light(second_pins,lightall,1)
    light(third_pins,lightall,1)
    time.sleep(sec)
    #light
    light(first_pins,number,int(num[0]))
    light(second_pins,number,int(num[1]))
    light(third_pins,number,int(num[2]))
    time.sleep(sec)
    


# main program
while True:
    lightES_107_520_886(5)
    Scrolling_digit(1,"520107886")
    for i in range(5,0,-1):
        big_cycle_1(i/10)
    for i in range(1,6):
        small_cycle(i/10)
    for i in range(0,2):
        dark_light_num(0.5,"107")
        dark_light_num(0.5,"520")
        dark_light_num(0.5,"886")
    big_cycle_2(0.2,10)
    big_cycle_3(0.2)
    for i in range(0,4):
        hori_line(0.1)
        vert_line(0.1)
    random_num(0.1,1,10,"520")
    random_num(0.1,1,10,"107")
    random_num(0.1,1,10,"886")
    big_cycle_1(0.3)

    light(first_pins,blank,0)
    light(second_pins,blank,0)
    light(third_pins,blank,0)
    
    time.sleep(3)






'''
while True:
    for index in range(0,1):
        light(first_pins,lightall,index)
        light(second_pins,lightall,index)
        light(third_pins,lightall,index)
        time.sleep(2)	
'''

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












