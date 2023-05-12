from manim import *

class NoisyChannel(Scene):
    def construct(self):
        # Original, encoded, and corrupted data
        original_data = Text("Data Stream: A B C D E F").scale(0.8)
        encoded_data = Text("Encoded Data: A B C D E F X Y Z").scale(0.8)
        corrupted_data = Text("Corrupted Data: A B X D E Y X Y Z").scale(0.8)

        # Position the text elements
        original_data.to_edge(UP)
        encoded_data.next_to(original_data, DOWN, buff=1.5)
        corrupted_data.next_to(encoded_data, DOWN, buff=1.5)

        # Reed-Solomon corrected data
        corrected_data = Text("Corrected Data: A B C D E F X Y Z").scale(0.8)
        corrected_data.next_to(corrupted_data, DOWN, buff=1.5)

        # Arrows for data transmission
        arrow1 = Arrow(original_data.get_bottom(), encoded_data.get_top(), buff=0.1)
        arrow2 = Arrow(encoded_data.get_bottom(), corrupted_data.get_top(), buff=0.1)
        arrow3 = Arrow(corrupted_data.get_bottom(), corrected_data.get_top(), buff=0.1)

        # Display the original and encoded data with arrow
        self.play(Write(original_data), Write(encoded_data), Write(arrow1))
        self.wait(1)

        # Simulate the noisy channel by transforming the encoded data to corrupted data with arrow
        self.play(TransformMatchingShapes(encoded_data, corrupted_data), Write(arrow2))
        self.wait(1)

        # Highlight the corrupted symbols
        corrupted_symbols = VGroup(corrupted_data[16], corrupted_data[19])
        self.play(corrupted_symbols.animate.set_color(RED))
        self.wait(1)

        # Show the Reed-Solomon correction with arrow
        self.play(Write(corrected_data), Write(arrow3))
        self.wait(1)

        # Highlight the corrected symbols
        corrected_symbols = VGroup(corrected_data[16], corrected_data[19])
        self.play(corrected_symbols.animate.set_color(GREEN))
        self.wait(1)

        # Clean up the scene
        self.play(
            FadeOut(original_data),
            FadeOut(corrupted_data),
            FadeOut(corrected_data),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
        )
