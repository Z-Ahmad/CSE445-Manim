from manim import *

class RSCodeMinDistance(Scene):
    def construct(self):
        # Reed-Solomon code definition
        rs_code_definition = MathTex("\\text{RS}(n, k)").scale(1.2)
        rs_code_definition.to_edge(UP)

        # Define the minimum distance
        min_distance = MathTex("d_{min}", "= n - k + 1").scale(1.2)

        # Position the minimum distance below the definition
        min_distance.next_to(rs_code_definition, DOWN, buff=1)

        # Display the animations
        self.play(Write(rs_code_definition))
        self.wait(1)
        self.play(Write(min_distance))
        self.wait(2)

        # Clean up the scene
        self.play(
            FadeOut(rs_code_definition),
            FadeOut(min_distance)
        )
