from pygame import display

class Renderer():
    _pool = []

    _screen = None
    _screen_size = (0,0)

    _clear_color = (0,0,0)

    @staticmethod
    def create_viewport(height, width, background_color = (0,0,0)):
        Renderer._screen_size = (height, width)
        Renderer._clear_color = background_color
        Renderer._screen = display.set_mode(Renderer._screen_size)

    @staticmethod
    def get_viewport_size():
        return Renderer._screen_size

    @staticmethod
    def get_viewport_width():
        return Renderer._screen_size[1]

    @staticmethod
    def get_viewport_height():
        return Renderer._screen_size[0]

    @staticmethod
    def add_drawable(drawable):
        #TODO check if object has function draw
        Renderer._pool.append(drawable)

    @staticmethod
    def render_pool():
        Renderer._screen.fill(Renderer._clear_color)
        [item.draw(Renderer._screen) for item in Renderer._pool]
        display.flip()
