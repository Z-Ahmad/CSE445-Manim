from manim import *

class BlockLength(Scene):
    def construct(self):
        title = Text("1. Block Length (n)").scale(1.2)
        title.to_edge(UP)
        self.play(Write(title))

        explanation = Text("Total number of symbols in a codeword\nincluding information and redundancy symbols", font_size=24, line_spacing=1.5)
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)

        codeword_box = RoundedRectangle(height=2, width=6, corner_radius=0.3)
        codeword_box.set_color(YELLOW)
        codeword_box.next_to(explanation, DOWN, buff=1)
        self.play(Create(codeword_box))

        info_symbols = [Text("I", font_size=24) for _ in range(4)]
        redundancy_symbols = [Text("R", font_size=24) for _ in range(2)]

        symbols = info_symbols + redundancy_symbols
        for i in range(len(symbols)):
            symbols[i].next_to(codeword_box.get_left(), RIGHT, buff=0.5 + i * 0.8)
            self.play(Write(symbols[i]))

        self.wait()

        info_brace = Brace(VGroup(*info_symbols), DOWN)
        redundancy_brace = Brace(VGroup(*redundancy_symbols), DOWN)

        info_label = info_brace.get_tex("k", buff=0.3)
        redundancy_label = redundancy_brace.get_tex("n - k", buff=0.3)

        self.play(
            Create(info_brace),
            Write(info_label),
            Create(redundancy_brace),
            Write(redundancy_label),
        )
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(codeword_box),
            *[FadeOut(symbol) for symbol in symbols],
            FadeOut(info_brace),
            FadeOut(redundancy_brace),
            FadeOut(info_label),
            FadeOut(redundancy_label),
        )
