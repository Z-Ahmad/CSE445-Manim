from manim import *

class CodeRate(Scene):
    def construct(self):
        title = Text("4. Code Rate (R)").scale(1.2)
        title.to_edge(UP)
        self.play(Write(title))

        explanation = Text("Ratio of information symbols to block length\nMeasures efficiency of a code", font_size=24, line_spacing=1.5)
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)

        rate_eqn = MathTex("R = \\frac{k}{n}").scale(1.2)
        rate_eqn.next_to(explanation, DOWN, buff=1)
        self.play(Write(rate_eqn))
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(rate_eqn),
        )
