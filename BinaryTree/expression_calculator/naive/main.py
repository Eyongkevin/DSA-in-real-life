from kivy.lang import Builder
from kivymd.app import MDApp

from dsa.evaluator import evaluate_expressioin


class EvalTreeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("main.kv")

    def solve_expression(self, expression):
        try:
            result = round(evaluate_expressioin(expression), 2)
            self.root.ids.result_label.text = f"Answer: {str(result)}"
        except Exception as ex:
            self.root.ids.result_label.text = "Invalid Expression"

    def clear_input(self):
        self.root.ids.expression_input.text = ""
        self.root.ids.result_label.text = "Answer:"

if __name__ == "__main__":
    EvalTreeApp().run()