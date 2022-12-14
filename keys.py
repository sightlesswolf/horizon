import gc
import sdl2.ext
import sdl2
keys = {
    "a": sdl2.SDLK_a,
    "b": sdl2.SDLK_b,
    "c": sdl2.SDLK_c,
    "d": sdl2.SDLK_d,
    "e": sdl2.SDLK_e,
    "f": sdl2.SDLK_f,
    "g": sdl2.SDLK_g,
    "h": sdl2.SDLK_h,
    "i": sdl2.SDLK_i,
    "j": sdl2.SDLK_j,
    "k": sdl2.SDLK_k,
    "l": sdl2.SDLK_l,
    "m": sdl2.SDLK_m,
    "n": sdl2.SDLK_n,
    "o": sdl2.SDLK_o,
    "p": sdl2.SDLK_p,
    "q": sdl2.SDLK_q,
    "r": sdl2.SDLK_r,
    "s": sdl2.SDLK_s,
    "t": sdl2.SDLK_t,
    "u": sdl2.SDLK_u,
    "v": sdl2.SDLK_v,
    "w": sdl2.SDLK_w,
    "x": sdl2.SDLK_x,
    "y": sdl2.SDLK_y,
    "z": sdl2.SDLK_z,
    "0": sdl2.SDLK_0,
    "1": sdl2.SDLK_1,
    "2": sdl2.SDLK_2,
    "3": sdl2.SDLK_3,
    "4": sdl2.SDLK_4,
    "5": sdl2.SDLK_5,
    "6": sdl2.SDLK_6,
    "7": sdl2.SDLK_7,
    "8": sdl2.SDLK_8,
    "9": sdl2.SDLK_9,
    "up": sdl2.SDLK_UP,
    "down": sdl2.SDLK_DOWN,
    "left": sdl2.SDLK_LEFT,
    "right": sdl2.SDLK_RIGHT,
    "lctrl": sdl2.SDLK_LCTRL,
    "rctrl": sdl2.SDLK_RCTRL,
    "lalt": sdl2.SDLK_LALT,
    "ralt": sdl2.SDLK_RALT,
    "space": sdl2.SDLK_SPACE,
    "f1": sdl2.SDLK_F1,
    "f2": sdl2.SDLK_F2,
    "f3": sdl2.SDLK_F3,
    "f4": sdl2.SDLK_F4,
    "f5": sdl2.SDLK_F5,
    "f6": sdl2.SDLK_F6,
    "f7": sdl2.SDLK_F7,
    "f8": sdl2.SDLK_F8,
    "f9": sdl2.SDLK_F9,
    "f10": sdl2.SDLK_F10,
    "f11": sdl2.SDLK_F11,
    "f12": sdl2.SDLK_F12,
    "tab": sdl2.SDLK_TAB,
    "slash": sdl2.SDLK_SLASH,
    "backslash": sdl2.SDLK_BACKSLASH,
    "apostrophe": sdl2.SDLK_QUOTE,
    "equals": sdl2.SDLK_EQUALS,
    "backspace": sdl2.SDLK_BACKSPACE,
    "home": sdl2.SDLK_HOME,
    "end": sdl2.SDLK_END,
    "pageup": sdl2.SDLK_PAGEUP,
    "pagedown": sdl2.SDLK_PAGEDOWN,
    "delete": sdl2.SDLK_DELETE,
    "comma": sdl2.SDLK_COMMA,
    "period": sdl2.SDLK_PERIOD,
    "lshift": sdl2.SDLK_LSHIFT,
    "rshift": sdl2.SDLK_RSHIFT,
    "semicolon": sdl2.SDLK_SEMICOLON,
    "enter": sdl2.SDLK_RETURN,
    "escape": sdl2.SDLK_ESCAPE,
    "pad0": sdl2.SDLK_KP_0,
    "pad1": sdl2.SDLK_KP_1,
    "pad2": sdl2.SDLK_KP_2,
    "pad3": sdl2.SDLK_KP_3,
    "pad4": sdl2.SDLK_KP_4,
    "pad5": sdl2.SDLK_KP_5,
    "pad6": sdl2.SDLK_KP_6,
    "pad7": sdl2.SDLK_KP_7,
    "pad8": sdl2.SDLK_KP_8,
    "pad9": sdl2.SDLK_KP_9,
    "padenter": sdl2.SDLK_KP_ENTER,






}


scans = {
    "a": sdl2.SDL_SCANCODE_A,
    "b": sdl2.SDL_SCANCODE_B,
    "c": sdl2.SDL_SCANCODE_C,
    "d": sdl2.SDL_SCANCODE_D,
    "e": sdl2.SDL_SCANCODE_E,
    "f": sdl2.SDL_SCANCODE_F,
    "g": sdl2.SDL_SCANCODE_G,
    "h": sdl2.SDL_SCANCODE_H,
    "i": sdl2.SDL_SCANCODE_I,
    "j": sdl2.SDL_SCANCODE_J,
    "k": sdl2.SDL_SCANCODE_K,
    "l": sdl2.SDL_SCANCODE_L,
    "m": sdl2.SDL_SCANCODE_M,
    "n": sdl2.SDL_SCANCODE_N,
    "o": sdl2.SDL_SCANCODE_O,
    "p": sdl2.SDL_SCANCODE_P,
    "q": sdl2.SDL_SCANCODE_Q,
    "r": sdl2.SDL_SCANCODE_R,
    "s": sdl2.SDL_SCANCODE_S,
    "t": sdl2.SDL_SCANCODE_T,
    "u": sdl2.SDL_SCANCODE_U,
    "v": sdl2.SDL_SCANCODE_V,
    "w": sdl2.SDL_SCANCODE_W,
    "x": sdl2.SDL_SCANCODE_X,
    "y": sdl2.SDL_SCANCODE_Y,
    "z": sdl2.SDL_SCANCODE_Z,
    "0": sdl2.SDL_SCANCODE_0,
    "1": sdl2.SDL_SCANCODE_1,
    "2": sdl2.SDL_SCANCODE_2,
    "3": sdl2.SDL_SCANCODE_3,
    "4": sdl2.SDL_SCANCODE_4,
    "5": sdl2.SDL_SCANCODE_5,
    "6": sdl2.SDL_SCANCODE_6,
    "7": sdl2.SDL_SCANCODE_7,
    "8": sdl2.SDL_SCANCODE_8,
    "9": sdl2.SDL_SCANCODE_9,
    "up": sdl2.SDL_SCANCODE_UP,
    "down": sdl2.SDL_SCANCODE_DOWN,
    "left": sdl2.SDL_SCANCODE_LEFT,
    "right": sdl2.SDL_SCANCODE_RIGHT,
    "lctrl": sdl2.SDL_SCANCODE_LCTRL,
    "rctrl": sdl2.SDL_SCANCODE_RCTRL,
    "lalt": sdl2.SDL_SCANCODE_LALT,
    "ralt": sdl2.SDL_SCANCODE_RALT,
    "space": sdl2.SDL_SCANCODE_SPACE,
    "f1": sdl2.SDL_SCANCODE_F1,
    "f2": sdl2.SDL_SCANCODE_F2,
    "f3": sdl2.SDL_SCANCODE_F3,
    "f4": sdl2.SDL_SCANCODE_F4,
    "f5": sdl2.SDL_SCANCODE_F5,
    "f6": sdl2.SDL_SCANCODE_F6,
    "f7": sdl2.SDL_SCANCODE_F7,
    "f8": sdl2.SDL_SCANCODE_F8,
    "f9": sdl2.SDL_SCANCODE_F9,
    "f10": sdl2.SDL_SCANCODE_F10,
    "f11": sdl2.SDL_SCANCODE_F11,
    "f12": sdl2.SDL_SCANCODE_F12,
    "tab": sdl2.SDL_SCANCODE_TAB,
    "slash": sdl2.SDL_SCANCODE_SLASH,
    "backslash": sdl2.SDL_SCANCODE_BACKSLASH,
    "apostrophe": sdl2.SDL_SCANCODE_APOSTROPHE,
    "equals": sdl2.SDL_SCANCODE_EQUALS,
    "backspace": sdl2.SDL_SCANCODE_BACKSPACE,
    "home": sdl2.SDL_SCANCODE_HOME,
    "end": sdl2.SDL_SCANCODE_END,
    "pageup": sdl2.SDL_SCANCODE_PAGEUP,
    "pagedown": sdl2.SDL_SCANCODE_PAGEDOWN,
    "delete": sdl2.SDL_SCANCODE_DELETE,
    "comma": sdl2.SDL_SCANCODE_COMMA,
    "period": sdl2.SDL_SCANCODE_PERIOD,
    "lshift": sdl2.SDL_SCANCODE_LSHIFT,
    "rshift": sdl2.SDL_SCANCODE_RSHIFT,
    "semicolon": sdl2.SDL_SCANCODE_SEMICOLON,
    "enter": sdl2.SDL_SCANCODE_RETURN,
    "escape": sdl2.SDL_SCANCODE_ESCAPE,
    "pad0": sdl2.SDL_SCANCODE_KP_0,
    "pad1": sdl2.SDL_SCANCODE_KP_1,
    "pad2": sdl2.SDL_SCANCODE_KP_2,
    "pad3": sdl2.SDL_SCANCODE_KP_3,
    "pad4": sdl2.SDL_SCANCODE_KP_4,
    "pad5": sdl2.SDL_SCANCODE_KP_5,
    "pad6": sdl2.SDL_SCANCODE_KP_6,
    "pad7": sdl2.SDL_SCANCODE_KP_7,
    "pad8": sdl2.SDL_SCANCODE_KP_8,
    "pad9": sdl2.SDL_SCANCODE_KP_9,
    "padenter": sdl2.SDL_SCANCODE_KP_ENTER,






}
class window:
    def __init__(self,windowname):
        # sdl can open only one window at a time, so we will initialize and free it here
        sdl2.ext.init()
        self.window=sdl2.ext.Window(windowname,(800,600))
        self.window.show()
        self.keystates={}
    def close(self):
        self.window.close()
        sdl2.ext.quit()
    def held(self,key):
        try:
            return self.keystates[str(keys[key])]
        except Exception as e:
            return 0
    def loop(self):
        self.events=sdl2.ext.get_events()
        for event in self.events:
            if event.type==sdl2.SDL_KEYDOWN and event.key.repeat==0: self.keystates[str(event.key.keysym.sym)]=1
            if event.type==sdl2.SDL_KEYUP: self.keystates[str(event.key.keysym.sym)]=0
        gc.collect()
        return 1
    def pressed(self,key):
        for event  in self.events:
            if event.type==sdl2.SDL_KEYDOWN and event.key.repeat==0 and event.key.keysym.sym==keys[key]:
                return 1
        return 0
    def released(self,key):
        for event  in self.events:
            if event.type==sdl2.SDL_KEYUP and event.key.keysym.sym==keys[key]:
                return 1
        return 0
def newwindow(windowname):
    return window(windowname)
