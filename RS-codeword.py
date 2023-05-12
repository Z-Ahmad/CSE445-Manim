from manim import *

class RSCodeword(Scene):
    def construct(self):
        # Original Data Symbols
        data_symbols = Text("Original Data Symbols: [D1, D2, D3, D4, D5, D6, D7, D8]").scale(0.6)
        data_symbols.to_edge(UP)
        self.play(Write(data_symbols))
        self.wait(2)

        # Error-Correcting Symbols
        error_symbols = Text("Error-Correcting Symbols: [E1, E2]").scale(0.6)
        error_symbols.next_to(data_symbols, DOWN, buff=0.5)
        self.play(Write(error_symbols))
        self.wait(2)

        # Codeword
        codeword = Text("Codeword: [D1, D2, D3, D4, D5, D6, D7, D8, E1, E2]").scale(0.6)
        codeword.next_to(error_symbols, DOWN, buff=0.5)
        self.play(Write(codeword))
        self.wait(2)

        # Fade out all text elements
        self.play(
            FadeOut(data_symbols),
            FadeOut(error_symbols),
            FadeOut(codeword),
        )
