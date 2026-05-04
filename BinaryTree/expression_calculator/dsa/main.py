from kivy.lang import Builder
from kivymd.app import MDApp

from dsa.evaluator import evaluate_expression
from draw_widget import TreeWidget

class EvalTreeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("main.kv")

    def solve_expression(self, expression):
        # Temporary logic (we'll replace in Episode 1)
        try:
            result, root_node = evaluate_expression(expression)
            self.root.ids.result_label.text = f"Answer: {str(round(result, 2))}"
            self.display_tree(root_node)
        except Exception as ex:
            print(ex)
            self.root.ids.result_label.text = "Invalid Expression"

    def clear_input(self):
        self.root.ids.expression_input.text = ""
        self.root.ids.result_label.text = "Answer:"

    def display_tree(self, root):
        tree_widget = self.root.ids.tree_area
        tree_widget.draw_tree(root)

    def clear_tree(self):
        tree_widget = self.root.ids.tree_area
        tree_widget.canvas.clear()

if __name__ == "__main__":
    EvalTreeApp().run()