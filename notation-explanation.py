from manim import *

class NotationExplanation(Scene):
    def construct(self):
        # Define the main variables and their descriptions
        variables = VGroup(
            Text("n: Block length"),
            Text("k: Dimension"),
            Text("d_min: Minimum distance")
        ).arrange(DOWN, aligned_edge=LEFT)

        # Position the variables on the left side
        variables.to_edge(LEFT)

        # Define the Reed-Solomon code representation
        rs_code = Text("RS(n, k, d_min)")

        # Position the Reed-Solomon code on the right side
        rs_code.to_edge(RIGHT)

        # Create arrows connecting the variables to the Reed-Solomon code
        arrows = VGroup(
            Arrow(variables[0].get_right(), rs_code.get_left(), buff=0.2),
            Arrow(variables[1].get_right(), rs_code.get_left(), buff=0.2),
            Arrow(variables[2].get_right(), rs_code.get_left(), buff=0.2)
        )

        # Display the animation
        self.play(Write(variables), Write(rs_code), *[Create(arrow) for arrow in arrows])
        self.wait(2)
        self.play(FadeOut(variables), FadeOut(rs_code), FadeOut(arrows))
