#!/usr/bin/env python3

from tkinter import *
import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_srvs.srv import Empty

frame = Tk()
frame.geometry("300x200")
frame.title("MOTIONLOG")
rospy.init_node('MotionLog')
rate = rospy.Rate(10)
rate.sleep()
# pub = rospy.Subscriber("Turtle_Control", String ,queue_size=10)

def Reset():
   
    print("Reset")
    rospy.wait_for_service('/reset')  # รอให้บริการ "reset" พร้อมใช้งาน
    try:
        reset_service = rospy.ServiceProxy('/reset', Empty)
        response = reset_service()
        rospy.loginfo("Reset Turtlesim Service Response: %s", response)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

def readS1(num):
    text = num.data 
    L1.config(text = str(text))## รับข้อความ
    print("Motion = " + text)
sub= rospy.Subscriber("Turtle_Control", String ,callback=readS1)

L1 = Label(frame,font = ('Arial',20),text ="",bg="black")
L1.place(x=20, y=50)

B1 = Button(text = "RESET", command=Reset)
B1.place(x=100, y=150)

frame.mainloop()