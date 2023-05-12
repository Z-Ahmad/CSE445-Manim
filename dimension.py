from manim import *

class Dimension(Scene):
    def construct(self):
        title = Text("2. Dimension (k)").scale(1.2)
        title.to_edge(UP)
        self.play(Write(title))

        explanation = Text("Number of information symbols in a codeword\nused to represent the original message", font_size=24, line_spacing=1.5)
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)

        message_box = RoundedRectangle(height=1.5, width=3, corner_radius=0.3)
        message_box.set_color(ORANGE)
        message_box.next_to(explanation, DOWN, buff=1)
        self.play(Create(message_box))

        message_symbols = [Text("M", font_size=24) for _ in range(4)]

        for i in range(len(message_symbols)):
            message_symbols[i].next_to(message_box.get_left(), RIGHT, buff=0.5 + i * 0.6)
            self.play(Write(message_symbols[i]))

        self.wait()

        k_brace = Brace(VGroup(*message_symbols), DOWN)
        k_label = k_brace.get_tex("k", buff=0.3)

        self.play(
            Create(k_brace),
            Write(k_label),
        )
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(message_box),
            *[FadeOut(symbol) for symbol in message_symbols],
            FadeOut(k_brace),
            FadeOut(k_label),
        )
