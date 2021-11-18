#!/usr/bin/env python3

import rospy
import random
from threading import Event
from std_msgs.msg import String
from casino.srv import bet


consolations = ["Поражения случаются( В следующий раз повезет\n",
                "#@!$%& рот этого казино! Не расстраивайся ❤\n",
                "Не повезло( Попробуй еще раз\n"]


def result_handler(result):
    global event

    # Ожидание вывода win/lose в консоль
    rospy.sleep(0.1)

    result = result.data

    if result == 'win':
        message = '🌈🌈🌈 Congrats! ‍🌈🌈🌈\n'

    else:
        message = random.choice(consolations)

    # rospy.loginfo(message)
    print(message)
    event.set()


if __name__ == '__main__':
    rospy.init_node('casino_client')

    play = rospy.ServiceProxy('roulette', bet)
    rospy.Subscriber('game_result', String, result_handler)

    # Для вывода сообщений в нужном порядке
    event = Event()

    while not rospy.is_shutdown():
        event.clear()

        print('Enter color and number)')
        try:
            color, number = str(input()).split(sep=' ')
            number = int(number)

            print(play(color, number).response)
        except Exception:
            print('Incorrect input\n')
            event.set()

        event.wait(timeout=3)
