from pygame import draw, Surface, SRCALPHA

from .tools import Tool


class Pencil(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        path = self.calculate_path(size)
        for position in path:
            draw.circle(canvas.get_surface, colour, position, 10)


class Marker(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        path = self.calculate_path(size)
        for position in path:
            marker_head = Surface((100, 100), SRCALPHA)
            position_x, position_y = position
            draw.rect(marker_head, (255, 0, 0, 255), (size, size, -size, -size))
            canvas.get_surface.blit(marker_head, (position_x, position_y))


class FountainPen(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):

        pen_size, pen_stroke = size, 0
        while pen_size != 0:
            pen_size -= 1
            pen_stroke += 1
            draw.line(canvas.get_surface, colour, (self.prev_mouse_x + pen_stroke, self.prev_mouse_y + pen_stroke),
                        (self.mouse_x + pen_stroke, self.mouse_y + pen_stroke))
