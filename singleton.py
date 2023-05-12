from manim import *

class SingletonBound(Scene):
    def construct(self):
        # Title
        title = Text("Singleton Bound").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Create axes for the graph
        axes = Axes(
            x_range=[0, 1.1, 0.1],
            y_range=[0, 1.1, 0.1],
            x_length=6,
            y_length=4,
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True}
        )

        axes.center().to_edge(DOWN)
        axes_labels = axes.get_axis_labels(x_label="\\frac{d_{min}}{n}", y_label="R")
        self.play(Create(axes), Write(axes_labels))

        # Graph of the Singleton Bound
        singleton_bound_graph = axes.plot(lambda x: 1 - x, x_range=[0, 1], color=YELLOW)
        singleton_bound_label = MathTex("R = 1 - \\frac{d_{min}}{n}", color=YELLOW)
        singleton_bound_label.next_to(singleton_bound_graph.get_end(), UP, buff=0.5).shift(2*UP)

        self.play(Create(singleton_bound_graph), Write(singleton_bound_label))
        self.wait(2)

        # Fade out all elements
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(singleton_bound_graph),
            FadeOut(singleton_bound_label),
        )
