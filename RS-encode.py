from manim import *

class ReedSolomonGeneration(Scene):
    def construct(self):
        # Original data and encoded data placeholders
        original_data = Text("Original Data: A B C").scale(0.8)
        encoded_data = Text("Encoded Data: A B C ? ? ?").scale(0.8)

        # Position the text elements
        original_data.to_edge(UP)
        encoded_data.to_edge(DOWN)

        # Arrows and labels for encoding
        arrow = Arrow(original_data.get_bottom(), encoded_data.get_top(), buff=0.5)
        encoding_label = Text("Encoding").scale(0.6).next_to(arrow, RIGHT)

        # Display the original data
        self.play(Write(original_data))
        self.wait(1)

        # Show the encoding process
        self.play(GrowArrow(arrow), Write(encoding_label))
        self.wait(1)

        # Reveal the encoded data with redundancy symbols
        self.play(Transform(original_data, encoded_data))
        self.wait(2)

        # Clean up the scene
        self.play(FadeOut(arrow), FadeOut(encoding_label), FadeOut(encoded_data))
