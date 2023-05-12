from manim import *

class MinDistance(Scene):
    def construct(self):
        title = Text("3. Minimum distance (d_min)").scale(1.2)
        title.to_edge(UP)
        self.play(Write(title))

        explanation = Text("Minimum number of symbol differences\nbetween any pair of distinct codewords", font_size=24, line_spacing=1.5)
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(2)

        codeword_1 = Text("01100", font_size=24)
        codeword_1.next_to(explanation, DOWN, buff=1.5)
        self.play(Write(codeword_1))

        codeword_2 = Text("10101", font_size=24)
        codeword_2.next_to(codeword_1, DOWN, buff=1)
        self.play(Write(codeword_2))

        error_highlight = [BackgroundRectangle(codeword_1[i], buff=0.1, fill_opacity=0.5, fill_color=YELLOW) for i in range(len(codeword_1)) if codeword_1[i] != codeword_2[i]]
        self.play(*[Create(eh) for eh in error_highlight])
        self.wait(2)

        d_min_brace = Brace(VGroup(*error_highlight), RIGHT)
        d_min_label = d_min_brace.get_tex("d_{min}", buff=0.3)

        self.play(
            Create(d_min_brace),
            Write(d_min_label),
        )
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(codeword_1),
            FadeOut(codeword_2),
            *[FadeOut(eh) for eh in error_highlight],
            FadeOut(d_min_brace),
            FadeOut(d_min_label),
        )
