import ctypes
import lupa
import sound_synthizer
from sound_synthizer import synthizer
import sound
import random
import time
CGTRuntime = lupa.LuaRuntime()
import accessible_output2.outputs.auto
def addfunc(name, ref):
    CGTRuntime.globals()[name] = ref

def sound3d(name):
    return sound_synthizer.sound_synthizer(name, ctx)

def luaexec(code):
    CGTRuntime.execute(code)


def init():
    global o
    global ctx
    o = accessible_output2.outputs.auto.Auto()
    addfunc("luaexec", luaexec)
    addfunc("pyexec", exec)
    addfunc("luaeval", CGTRuntime.eval)
    addfunc("urlsound", sound.urlsound)
    addfunc("pyeval", eval)
    addfunc("sound", sound.sound)
    addfunc("sound3d", sound3d)
    addfunc("elapsed", time.time)
    addfunc("speak", o.output)#It does braille too
    addfunc("wait", time.sleep)
    with synthizer.initialized(
            log_level=synthizer.LogLevel.DEBUG, logging_backend=synthizer.LoggingBackend.STDERR):

        ctx = synthizer.Context()

        ctx.default_panner_strategy.value = synthizer.PannerStrategy.HRTF
        main()


def runcode(b):
    try:
        CGTRuntime.execute(b)
    except Exception as e:
        print("An error occured: "+str(e)+". Press enter to continue")
        
        input()


def console():
    print("Welcome to the cgt debugging console.")
    while True:
        print(">")
        runcode(input())


def main():
    while True:
        print("Select something to do: run, or console", end="\r\n")
        s = input()
        if s == "run":
            b = input("Enter a file to run lua code from it")
            f = open(b)
            runcode(f.read())
        if s == "console":
            console()


init()