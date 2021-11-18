#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import String
from casino.srv import bet


def make_bet(bet):
    global pub
    win = random.getrandbits(1)
    result = 'win' if bool(win) else 'lose'

    pub.publish(result)
    return result


if __name__ == '__main__':
    rospy.init_node('casino_server')
    rospy.Service('roulette', bet, make_bet)
    pub = rospy.Publisher('game_result', String, queue_size=10)
    rospy.loginfo('Server is running...')
    rospy.spin()

