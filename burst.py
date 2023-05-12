from manim import *
import random

class BurstErrors(Scene):
    def construct(self):
        message_length = 16
        error_length = 5
        error_start = 6

        # Create a random binary message
        original_message = [random.choice(["0", "1"]) for _ in range(message_length)]
        corrupted_message = original_message.copy()

        # Introduce burst errors
        for i in range(error_start, error_start + error_length):
            corrupted_message[i] = "1" if corrupted_message[i] == "0" else "0"

        # Display original message
        original_text = Text("Original Message: ", t2c={"Original Message: ": BLUE}).scale(0.8)
        original_text.shift(2 * UP)
        self.play(Write(original_text))

        original_message_text = MathTex(*original_message).scale(0.8)
        original_message_text.next_to(original_text, RIGHT, buff=0.3)
        self.play(Write(original_message_text))
        self.wait(2)

        # Display corrupted message
        corrupted_text = Text("Corrupted Message: ", t2c={"Corrupted Message: ": RED}).scale(0.8)
        corrupted_text.shift(2 * DOWN)
        self.play(Write(corrupted_text))

        corrupted_message_text = MathTex(*corrupted_message).scale(0.8)
        corrupted_message_text.next_to(corrupted_text, RIGHT, buff=0.3)
        self.play(Write(corrupted_message_text))
        self.wait(2)

        # Highlight burst errors
        error_rectangles = []
        for i in range(error_start, error_start + error_length):
            error_rectangle = Rectangle(height=0.7, width=0.7, fill_color=YELLOW, fill_opacity=0.5)
            error_rectangle.move_to(corrupted_message_text[i].get_center())
            error_rectangles.append(error_rectangle)

        self.play(*[Create(rect) for rect in error_rectangles])
        self.wait(2)

        # Fade out
        self.play(
            FadeOut(original_text),
            FadeOut(original_message_text),
            FadeOut(corrupted_text),
            FadeOut(corrupted_message_text),
            *[FadeOut(rect) for rect in error_rectangles],
        )
