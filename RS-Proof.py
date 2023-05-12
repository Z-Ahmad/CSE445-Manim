from manim import *

class RSProofSingleton(Scene):
    def construct(self):
        # Parameters of RS codes
        params_text = Text("RS Codes Parameters (n, k, d_min)").scale(0.8).set_color(BLUE)
        params_text.to_edge(UP)
        self.play(Write(params_text))
        self.wait(2)

        # Relationship between parameters
        relationship = MathTex("d_{min} = n - k + 1").scale(0.8).set_color(BLUE)
        relationship.next_to(params_text, DOWN, buff=0.5)
        self.play(Write(relationship))
        self.wait(2)

        # Rate of the code
        rate = MathTex("R = \\frac{k}{n}").scale(0.8).set_color(BLUE)
        rate.next_to(relationship, DOWN, buff=0.5)
        self.play(Write(rate))
        self.wait(2)

        # Singleton Bound
        singleton_bound = MathTex("R \\leq 1 - \\frac{d_{min}}{n}").scale(0.8).set_color(GREEN)
        singleton_bound.next_to(rate, DOWN, buff=0.5)
        self.play(Write(singleton_bound))
        self.wait(2)

        # Substituting d_min
        substitution = MathTex("R = \\frac{k}{n} \\leq 1 - \\frac{n - k + 1}{n}").scale(0.8)
        substitution.next_to(singleton_bound, DOWN, buff=0.5)
        self.play(Write(substitution))
        self.wait(2)

        # Multiply both sides by n
        multiply = MathTex("k \\leq n - (n - k + 1)").scale(0.8)
        multiply.next_to(substitution, DOWN, buff=0.5)
        self.play(Write(multiply))
        self.wait(2)

        # Simplify inequality
        simplify = MathTex("k \\leq k - 1").scale(0.8)
        simplify.next_to(multiply, DOWN, buff=0.5)
        self.play(Write(simplify))
        self.wait(2)

        # Fade out all text elements except the simplified inequality
        self.play(
            FadeOut(params_text),
            FadeOut(relationship),
            FadeOut(rate),
            FadeOut(singleton_bound),
            FadeOut(substitution),
            FadeOut(multiply),
        )

        # Move the simplified inequality to the top
        self.play(simplify.animate.next_to(params_text, DOWN, buff=0.25))
        self.wait(2)

        # Conclusion
        conclusion = Text("RS codes meet the Singleton Bound").scale(0.8)
        conclusion.next_to(simplify, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(2)

        # Fade out the remaining text elements
        self.play(
            FadeOut(simplify),
        )
        
        # Singleton Bound visualization

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

        # Point representing RS codes meeting the Singleton Bound
        rs_point = Dot(axes.c2p(0.5, 0.5), color=BLUE)
        rs_label = MathTex("RS").scale(0.8).set_color(BLUE)
        rs_label.next_to(rs_point, DOWN, buff=0.2)

        self.play(Create(rs_point), Write(rs_label))
        self.wait(2)

        # Fade out all elements
        self.play(
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(singleton_bound_graph),
            FadeOut(singleton_bound_label),
            FadeOut(rs_point),
            FadeOut(rs_label),
            FadeOut(conclusion)
        )
