#!/usr/bin/python
#Author: Ethan Hulse
#Initial Commit: 1/5/2021
#Latest Commit: 1/2/2023
from time import time as gettime
from time import sleep as trysleep
import discord
import math

exitFlag = 0

def reversal(s):
    if len(s) == 0:
        return s
    return reversal(s[1:]) + s[0]

def getsin(term, freq, ampl):
    return round(ampl * (math.sin(term * freq)) + ampl)

def getspooky(term, freqx, freqy, coef):
    return round(5 * ( math.sin(freqx * term)  +  math.sin( (freqy * term)   + math.pi) + coef)  )

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_connect(self):
        print('[LOG] Connecting as ', self.user)

    async def on_ready(self):
        print('[LOG] Logged in as ', self.user)
        botchannel = self.get_channel(927648698224246895)
        subchannel = self.get_channel(928377776107552849)
        start_time = float(0)
        end_time = float(0)

        base = '|'
        body = '⣿'
        end = '|'
        i = 1;
 
        linestr = ""
        while i > -1:
            trysleep(0.5)
            z = getsin(i, 50, 25)
            #z = getspooky(i, 0.2, 5, 6)
            print(z)
            line = [base, body]

            for _x in range(z):
                line.append(body)
                

            line.append(end)
            
            linestr = linestr.join(line)
            rlinestr = reversal(linestr)
            await botchannel.send("<@!469959178643832853> " + linestr + "929234126681288724>" )
            linestr = ""
            line.clear()
            i += 1






client = MyClient();

#client.run("KEY")