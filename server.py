from tkinter import DISABLED
import redis
import random


with redis.Redis() as redis_server:
    redis_server.lpush("queue", random.randint(0, 10))