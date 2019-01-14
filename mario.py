from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
import socket
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
appname = 'master' // set your name here
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, SIMPLE_MOVEMENT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

done = True
for step in range(5000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    print("d70518ac-3efe-424b-b2aa-467b45380b08.{}.score {}\n".format(appname, info.get('score')))
    sock.sendto("d70518ac-3efe-424b-b2aa-467b45380b08.{}.score {}\n".format(appname, info.get('score')).encode('utf-8'), ("carbon.hostedgraphite.com", 2003))
    env.render()

conn.close()
env.close()
