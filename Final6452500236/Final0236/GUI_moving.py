#!/usr/bin/env python3

from tkinter import*
import rospy
from geometry_msgs.msg import Twist
# from turtlesim.srv import SetPen
# import turtle
from std_srvs.srv import Empty
from std_msgs.msg import String
from std_msgs.msg import Int16

frame = Tk()
frame.title("REMOTE")
frame.geometry("480x500")
rospy.init_node("Turtle_Control")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
# sub= rospy.Subscriber("arduino_comand", Int16,callback=arduino_move)
pubtext = rospy.Publisher("MotionLog",String, queue_size=10)
# pub1 = rospy.Publisher("/turtle1/cmd_vel",turtle, queue_size=10)


def fw():
    print("FORWARD")
    text1 = "FORWARD"
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
    pubtext.publish(text1)

def bw():
    print("BACKWARD")
    text2 = "BACKWARD"
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
    pubtext.publish(text2)

def arduino_move(num):
    print("TURN RIGHT")
    sensor1=num.data
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= sensor1
    pub.publish(cmd)
sub= rospy.Subscriber("arduino_comand", Int16,callback=arduino_move)

# def rt():
#     print("rt")
#     cmd = Twist()
#     # cmd.linear.x = 1.0
#     # cmd.angular.z= -1.0
#     cmd.linear.y = 1.0
#     cmd.angular.z= -1.0
#     pub.publish(cmd)

def tr():
    print("TURN LEFT")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= -1.0
    pub.publish(cmd)

def tl():
    print("TURN RIGHT")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 1.0
    pub.publish(cmd)

def Penon():
    print("PEN ON")
    # my_turtle = turtle.Turtle(visible=False)
    # turtle.pen(shown = False, outline=2)
    # st = SetPen()
    # pub.publish(my_turtle)

def Penoff():
    print("PEN OFF")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 0.0
    pub.publish(cmd)

# def rs():
#     print("Reset")
#     rospy.wait_for_service('/reset')  # รอให้บริการ "reset" พร้อมใช้งาน
#     try:
#         reset_service = rospy.ServiceProxy('/reset', Empty)
#         response = reset_service()
#         rospy.loginfo("Reset Turtlesim Service Response: %s", response)
#     except rospy.ServiceException as e:
#         rospy.logerr("Service call failed: %s", e)

B1 = Button(text = "FW", command=fw)
B1.place(x=240, y=200)

B2 = Button(text = "BW", command=bw)
B2.place(x=240, y=300)

B3 = Button(text = "TL", command=tl)
B3.place(x=150, y=250)

B4 = Button(text = "TR", command=tr)
B4.place(x=330, y=250)

# B5 = Button(text = "Rotate L", command=rtl)
# B5.place(x=90, y=80)

# B6 = Button(text = "Rotate R", command=rtr)
# B6.place(x=190, y=80)

B5 = Button(text = "PEN ON", command=Penon)
B5.place(x=90, y=80)

B6 = Button(text = "PEN OFF", command=Penoff)
B6.place(x=190, y=80)


# B7 = Button(text = "RESET", command=rs)
# B7.place(x=20, y=200)



frame.mainloop()