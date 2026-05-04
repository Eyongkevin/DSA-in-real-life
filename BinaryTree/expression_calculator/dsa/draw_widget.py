from kivy.uix.widget import Widget
from kivy.graphics import Line, Ellipse, Color
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Rectangle

from dsa.evaluator import is_number


class TreeWidget(Widget):

    def draw_tree(self, root):
        self.canvas.clear()

        if not root:
            return

        width = self.width
        height = self.height

        depth = self.get_depth(root)

        # vertical spacing between levels
        level_height = height / (depth + 1)

        # start from center top
        self._draw_node(
            node=root,
            x=width / 2,
            y=height - level_height,
            dx=width / 4,
            level_height=level_height
        )

    def _draw_node(self, node, x, y, dx, level_height):
        if not node:
            return

        # Draw circle
        with self.canvas:
            Color(0.2, 0.6, 1, 1)
            Ellipse(pos=(x - 40, y - 40), size=(80, 80))

        # Draw text
        label = CoreLabel(text=str(node.data), font_size=30 if is_number(node.data) else 50)
        label.refresh()
        texture = label.texture

        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(texture=texture, pos=(x - texture.size[0]/2, y - texture.size[1]/2), size=texture.size)

        # Left child
        if node.left_child:
            child_x = x - dx
            child_y = y - level_height

            with self.canvas:
                Line(points=[x, y, child_x, child_y], width=1.2)

            self._draw_node(node.left_child, child_x, child_y, dx / 2, level_height)

        # Right child
        if node.right_child:
            child_x = x + dx
            child_y = y - level_height

            with self.canvas:
                Line(points=[x, y, child_x, child_y], width=1.2)

            self._draw_node(node.right_child, child_x, child_y, dx / 2, level_height)

    def get_depth(self, node):
        if not node:
            return 0
        return 1 + max(self.get_depth(node.left_child), self.get_depth(node.right_child))
