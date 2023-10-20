from FollowerBot import FollowerBot, RobotOutOfBounds, Timeout

def test_run(robot: FollowerBot) -> None:
    
    """Make the robot move, doesn't matter how much, just as long as it has moved from the starting position.
    :param FollowerBot robot: instance of the robot that you need to make move
    """
    try:
        robot.set_wheels_speed(25)
        robot.sleep(1)
        robot.done()
    except FollowerBot.RobotOutOfBounds:
        print("The robot has moved out of bounds. Make sure to keep the robot within the track image.")
        return
    except FollowerBot.Timeout:
        print("The robot has taken too long to complete the task. Make sure to keep the robot moving efficiently.")
        return
    else:
        print("The robot has successfully moved from the starting position.")


def drive_to_line(robot: FollowerBot):
    try:
        while True:
            all_sensor = robot.get_line_sensors()
            if all_sensor !=[0,0,0,0,0,0]:
                break
            robot.set_wheels_speed(20)
            robot.sleep(0.05)
            print(robot.get_position(),all_sensor)
            
        while True:
            sensor_3= robot.get_left_line_sensor()  # sensor 3
            sensor_4 = robot.get_right_line_sensor()  # sensor 4
            print(robot.get_position())
            if sensor_3 == sensor_4 and sensor_4 <50 :
                print("Black Line detected")
                break
            robot.set_wheels_speed(20)
            robot.sleep(0.05)
            print(robot.get_position(), robot.get_line_sensors())
        
        robot.set_wheels_speed(0)
        robot.sleep(0.01)
        robot.set_wheels_speed(100)
        robot.sleep(0.3)
        print(robot.get_position(), robot.get_line_sensors())
        
        robot.set_wheels_speed(0)
        # If the robot goes out of bounds, stop and raise an exception
        robot.done()
    except RobotOutOfBounds:
        robot.done()
        print("Robot Out of Bounds")
        


def follow_the_line(robot: FollowerBot):
    
    try:
        
        while True:
            all_sensor = robot.get_line_sensors()
            if all_sensor !=[0,0,0,0,0,0]:
                break
            robot.set_wheels_speed(20)
            robot.sleep(0.05)
            print(robot.get_position(),all_sensor)
        while True:
            all_sensor = robot.get_line_sensors()
            if all_sensor !=[1024,1024,1024,1024,1024,1024]:
                break
            robot.set_wheels_speed(20)
            robot.sleep(0.05)
            print(robot.get_position(),all_sensor)
        while True:
            all_sensor = robot.get_line_sensors()
            print(robot.get_position(),all_sensor)
            left_sensors = robot.get_left_line_sensors()
            right_sensors = robot.get_right_line_sensors()
            if all(sensor > 500 for sensor in left_sensors) and all(sensor > 500 for sensor in right_sensors):
                robot.done()
                break
            elif all_sensor ==[1024,0,0,0,0,1024] or all_sensor ==[1024,1024,0,0,1024,1024] or all_sensor==[0,0,0,0,0,0]:
                robot.set_left_wheel_speed(40)
                robot.set_right_wheel_speed(40)
                robot.sleep(0.001)
            # Turn Right
            elif left_sensors.count(0)+2<=right_sensors.count(0):
                robot.set_left_wheel_speed(15)
                robot.set_right_wheel_speed(-15)
                robot.sleep(0.001)
            elif left_sensors.count(0)+1 < right_sensors.count(0):
                robot.set_left_wheel_speed(8)
                robot.set_right_wheel_speed(-8)
                robot.sleep(0.0001)
            
            elif left_sensors.count(0)>=right_sensors.count(0)+2:
                robot.set_left_wheel_speed(-15)
                robot.set_right_wheel_speed(15)
                robot.sleep(0.001)
            elif left_sensors.count(0) > right_sensors.count(0)+1:
                robot.set_left_wheel_speed(-8)
                robot.set_right_wheel_speed(8)
                robot.sleep(0.0001)
            
            elif left_sensors[0]==0 and right_sensors.count(0)==0:
                robot.set_left_wheel_speed(-15)
                robot.set_right_wheel_speed(15)
                robot.sleep(0.001)
            
            elif right_sensors[2] ==0 and left_sensors.count(0) ==0:
                robot.set_left_wheel_speed(15)
                robot.set_right_wheel_speed(-15)
                robot.sleep(0.001)
            
            #Turn Left
            else:
                robot.set_left_wheel_speed(40)
                robot.set_right_wheel_speed(40)
                robot.sleep(0.0001)
            
        robot.set_wheels_speed(0)
        robot.done()
    except RobotOutOfBounds:
        print("Robot Out of bounds")
        robot.done()



def the_true_follower(robot: FollowerBot):
    try:
        startPoint = robot.get_position();
        isreturn = False
        count =0
        while True:
        
            all_sensor = robot.get_line_sensors()
            if all_sensor !=[0,0,0,0,0,0]:
                break
            robot.set_wheels_speed(100)
            robot.sleep(0.1)
            print(robot.get_position(),all_sensor)
            
        while True:
            all_sensor = robot.get_line_sensors()
            if all_sensor !=[1024,1024,1024,1024,1024,1024]:
                break
            robot.set_wheels_speed(100)
            robot.sleep(0.3)
            print(robot.get_position(),all_sensor)
            
        
        while True:
            all_sensor = robot.get_line_sensors()
            # print(robot.get_position(),all_sensor)
            left_sensors = robot.get_left_line_sensors()
            right_sensors = robot.get_right_line_sensors()
            
            if robot.get_position() == startPoint and isreturn:
                robot.done()
                break
            if(642 in all_sensor):
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(-100)
                robot.sleep(.2)
                # print("Hi")
                count=0
            elif all_sensor ==[1024,1024,1024,1024,1024,1024] :
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(100)
                count+=1
                if count==3:
                    robot.sleep(0.1)
                else:
                    robot.sleep(0.008)
            elif all_sensor ==[1024,0,0,0,0,1024]  or all_sensor==[0,0,0,0,0,0] :
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(100)
                robot.sleep(0.01)
                isreturn = True
            # Turn Right
            elif all_sensor ==[1024,1024,0,0,1024,1024]:
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(100)
                robot.sleep(0.1)
                isreturn = True
                
            elif left_sensors.count(0)+2<right_sensors.count(0):
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(-100)
                robot.sleep(0.001)
            elif left_sensors.count(0)+2==right_sensors.count(0):
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(-100)
                robot.sleep(0.0002)
            elif left_sensors.count(0)+1 < right_sensors.count(0):
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(-100)
                robot.sleep(0.0001)
            
            elif left_sensors.count(0)>right_sensors.count(0)+2:
                robot.set_left_wheel_speed(-100)
                robot.set_right_wheel_speed(100)
                robot.sleep(0.001)
            
            elif left_sensors.count(0)==right_sensors.count(0)+2:
                robot.set_left_wheel_speed(-100)
                robot.set_right_wheel_speed(100)
                robot.sleep(0.005)
            elif left_sensors.count(0) > right_sensors.count(0)+1:
                robot.set_left_wheel_speed(-100)
                robot.set_right_wheel_speed(100)
                print(all_sensor)
                robot.sleep(0.0002)
            
            elif left_sensors[0]==0 and right_sensors.count(0)==0:
                robot.set_left_wheel_speed(-100)
                robot.set_right_wheel_speed(100)
                robot.sleep(0.008)
            
            elif right_sensors[2] ==0 and left_sensors.count(0) ==0:
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(-100)
                robot.sleep(0.008)
            
            elif all_sensor.count(0)==5:
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(100)
                robot.sleep(0.01)
                # isreturn = True
            else:
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(100)
                robot.sleep(0.001)
            
            
        robot.set_wheels_speed(0)
        robot.done()
    except RobotOutOfBounds:
        print("Robot Out of bounds")
        robot.done()
    except Timeout:
        print("TimeOut")
        robot.done()


robot = FollowerBot("robot_path_6.png",90, 265,300)
# test_run(robot)
# drive_to_line(robot)
# follow_the_line(robot)
the_true_follower(robot)
# robot.done()