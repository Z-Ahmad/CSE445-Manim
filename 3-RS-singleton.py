from manim import *

class RSCodeSingletonBound(Scene):
    def construct(self):
        # Define the rate of Reed-Solomon codes
        rs_rate = MathTex("R", "=", "\\frac{k}{n}").scale(1.2)
        rs_rate.to_edge(UP)

        # Singleton bound formula
        singleton_bound = MathTex("R", "\\leq", "1 -", "\\frac{d_{min}}{n}").scale(1.2)

        # Position the Singleton bound below the rate
        singleton_bound.next_to(rs_rate, DOWN, buff=1)

        # Show the relationship between the rate and the bound
        relationship = MathTex("\\frac{k}{n}", "\\leq", "1 -", "\\frac{n - k + 1}{n}").scale(1.2)

        # Position the relationship below the Singleton bound
        relationship.next_to(singleton_bound, DOWN, buff=1)

        # Display the animations
        self.play(Write(rs_rate))
        self.wait(1)
        self.play(Write(singleton_bound))
        self.wait(2)
        self.play(Write(relationship))
        self.wait(2)

        # Clean up the scene
        self.play(
            FadeOut(rs_rate),
            FadeOut(singleton_bound),
            FadeOut(relationship)
        )
