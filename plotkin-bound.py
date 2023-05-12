from manim import *

class PlotkinBound(Scene):
    def construct(self):
        # Define the Plotkin Bound description
        plotkin_description = Text("M <= 2n/d for d <= n/2").scale(0.8)

        # Position the description at the top of the scene
        plotkin_description.to_edge(UP)

        # Create axes for the graphical representation
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 20, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
        )
        axes.shift(1.5 * DOWN)
        axes_labels = axes.get_axis_labels(x_label="d", y_label="M")

        # Create a line representing the Plotkin Bound
        plotkin_line = axes.get_line_from_axis_to_point(
            axes.coords_to_point(0, 20), axes.coords_to_point(5, 10)
        ).set_color(YELLOW)

        # Define the RS code point
        rs_code_point = axes.get_point_from_coords(3, 9)
        rs_code_label = (
            Text("RS(3, 9)").scale(0.6).next_to(rs_code_point, RIGHT)
        )

        # Display the Plotkin Bound description
        self.play(Write(plotkin_description))
        self.wait(1)

        # Show the graphical representation
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(plotkin_line), run_time=2)
        self.wait(1)

        # Show the RS code meeting the Plotkin Bound
        self.play(FadeIn(rs_code_point), Write(rs_code_label))
        self.wait(1)

        # Clean up the scene
        self.play(
            FadeOut(plotkin_description),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(plotkin_line),
            FadeOut(rs_code_point),
            FadeOut(rs_code_label),
        )
