from manim import *
# y = mx + b
class VaryingM(Scene):
    def construct(self):
        m_tracker = ValueTracker(0.25) # Slope tracker value
        b_tracker = ValueTracker(0) # y-intercept tracker value
        # Axes
        ax = Axes([0, 10], [0, 10], axis_config={"include_tip": False})
        labels = ax.get_axis_labels(x_label="x", y_label="y")        
        # Slope and y-intercept labels
        m_label = Tex(f"m = ").move_to(ax.c2p(1, 9))
        b_label = Tex(f"b = ").next_to(m_label, DOWN)
        m_num_text = DecimalNumber(m_tracker.get_value()).next_to(m_label, RIGHT).align_to(m_label, DOWN)
        b_num_text = DecimalNumber(b_tracker.get_value()).next_to(b_label, RIGHT).align_to(b_label, DOWN)
        # Graph
        def get_y(x): return m_tracker.get_value() * x + b_tracker.get_value() # Graph function
        graph = ax.plot(lambda x : m_tracker.get_value() * x + b_tracker.get_value(), color=RED)
        # Add everything to the scene
        self.add(m_label, b_label, m_num_text, b_num_text)
        self.play(Create(ax), Create(graph), Write(labels))
        # Add updaters
        graph.add_updater(lambda g: g.become(ax.plot(get_y, color=RED)))
        m_num_text.add_updater(lambda m: m.set_value(m_tracker.get_value()).next_to(m_label, RIGHT).align_to(m_label, DOWN))
        b_num_text.add_updater(lambda b: b.set_value(b_tracker.get_value()).next_to(b_label, RIGHT).align_to(b_label, DOWN))
        self.wait()
        self.play(m_tracker.animate.set_value(3), b_tracker.animate.set_value(5), run_time=2)