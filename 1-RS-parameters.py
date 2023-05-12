from manim import *

class RSCodeParameters(Scene):
    def construct(self):
        # Reed-Solomon code definition
        rs_code_definition = MathTex("\\text{RS}(n, k)").scale(1.2)
        rs_code_definition.to_edge(UP)

        # Define the parameters
        parameters = VGroup(
            MathTex("n", ": \\text{ Block length}"),
            MathTex("k", ": \\text{ Dimension}")
        ).arrange(DOWN, aligned_edge=LEFT)

        # Position the parameters below the definition
        parameters.next_to(rs_code_definition, DOWN, buff=1)

        # Singleton bound formula
        singleton_bound = MathTex("R", "\\leq", "1 -", "\\frac{d_{min}}{n}").scale(1.2)

        # Position the Singleton bound below the parameters
        singleton_bound.next_to(parameters, DOWN, buff=1)

        # Display the animations
        self.play(Write(rs_code_definition))
        self.wait(1)
        self.play(Write(parameters))
        self.wait(2)
        self.play(Write(singleton_bound))
        self.wait(2)

        # Clean up the scene
        self.play(
            FadeOut(rs_code_definition),
            FadeOut(parameters),
            FadeOut(singleton_bound)
        )
