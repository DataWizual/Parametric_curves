from manim import *
import numpy as np
import itertools
from threading import Thread


class Param(Scene):
    def construct(self):

        def parametric_function(t, a, b, c):
            x = np.cos(a*t) + np.cos(b*t)/2 + np.sin(c*t)/3
            y = np.sin(a*t) + np.sin(b*t)/2 + np.cos(c*t)/3
            return np.array([x, y, 0])

        parametric_curve = ParametricFunction(
            lambda t: parametric_function(t, 1, 1, 0), t_range=[0, 2 * PI], color=BLUE)
        parametric_curve.set_x(-2).set_y(2.5)

        formula_text = MathTex(r"cos(at) + \frac{cos(bt)}{2} + \frac{sin(ct)}{3}\\"
                               r"sin(at) + \frac{sin(bt)}{2} + \frac{cos(ct)}{3}",
                               font_size=34)
        formula_text.set_x(4).set_y(2.5)
        formula_text[0][4].set_color(PURE_RED)
        formula_text[0][31].set_color(PURE_RED)
        formula_text[0][12].set_color(PURE_BLUE)
        formula_text[0][39].set_color(PURE_BLUE)
        formula_text[0][22].set_color(PURE_GREEN)
        formula_text[0][49].set_color(PURE_GREEN)

        self.play(Write(formula_text), run_time=2)

        a = Tex(r"a", r" = ", font_size=32)
        a[0].set_color(PURE_RED)
        a[1].set_color(WHITE)
        a.next_to(formula_text, DOWN, buff=0.5)

        b = Tex(r"b", r" = ", font_size=32)
        b[0].set_color(PURE_BLUE)
        b[1].set_color(WHITE)
        b.next_to(a, DOWN, buff=0.5)

        c = Tex(r"c", r" = ", font_size=32)
        c[0].set_color(PURE_GREEN)
        c[1].set_color(WHITE)
        c.next_to(b, DOWN, buff=0.5)

        a_text = DecimalNumber(1, num_decimal_places=1,
                               font_size=24).next_to(a[1], RIGHT, buff=0.2)
        b_text = DecimalNumber(1, num_decimal_places=1,
                               font_size=24).next_to(b[1], RIGHT, buff=0.2)
        c_text = DecimalNumber(1, num_decimal_places=1,
                               font_size=24).next_to(c[1], RIGHT, buff=0.2)

        self.add(a, a_text, b, b_text, c, c_text)

        a_tracker = ValueTracker(1)
        b_tracker = ValueTracker(1)
        c_tracker = ValueTracker(0)

        c_1_curve = self.c(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 1)
        b_1_curve = self.b(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 0)
        a_1_curve = self.a(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 0)

        c_4_curve = self.c(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 15, 1)
        b_4_curve = self.b(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 15, 0)
        a_4_curve = self.a(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 15, 0)

        c_5_curve = self.c(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 30, 1)
        b_5_curve = self.b(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 30, 0)
        a_5_curve = self.a(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 30, 0)

        c_8_curve = self.c(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 15)
        b_8_curve = self.b(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 15)
        a_8_curve = self.a(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 15)

        c_9_curve = self.c(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 30)
        b_9_curve = self.b(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 30)
        a_9_curve = self.a(a_tracker, b_tracker, c_tracker,
                           parametric_curve, parametric_function, a_text, b_text, c_text, 1, 30)

        c_1_start = Thread(target=c_1_curve)
        c_4_start = Thread(target=c_4_curve)
        c_5_start = Thread(target=c_5_curve)
        c_8_start = Thread(target=c_8_curve)
        c_9_start = Thread(target=c_9_curve)
        b_1_start = Thread(target=b_1_curve)
        b_4_start = Thread(target=b_4_curve)
        b_5_start = Thread(target=b_5_curve)
        b_8_start = Thread(target=b_8_curve)
        b_9_start = Thread(target=b_9_curve)
        a_1_start = Thread(target=a_1_curve)
        a_4_start = Thread(target=a_4_curve)
        a_5_start = Thread(target=a_5_curve)
        a_8_start = Thread(target=a_8_curve)
        a_9_start = Thread(target=a_9_curve)

        c_1_start.start()
        b_1_start.start()
        a_1_start.start()
        c_4_start.start()
        b_4_start.start()
        a_4_start.start()
        c_5_start.start()
        b_5_start.start()
        a_5_start.start()
        c_8_start.start()
        b_8_start.start()
        a_8_start.start()
        c_9_start.start()
        b_9_start.start()
        a_9_start.start()

    def a(self, a_tracker, b_tracker, c_tracker, parametric_curve, parametric_function, a_text, b_text, c_text, b, c):
        colors = [PURE_BLUE, YELLOW, PURE_RED]
        forward_range = range(1, 10)
        backward_range = range(10, 0, -1)
        combined_range = itertools.chain(forward_range, backward_range)
        for i in combined_range:
            color_start = colors[i % len(colors)]
            color_end = colors[(i + 1) % len(colors)]
            self.play(
                a_tracker.animate.set_value(i),
                b_tracker.animate.set_value(b),
                c_tracker.animate.set_value(c),
                UpdateFromFunc(
                    parametric_curve,
                    lambda curve: curve.become(
                        ParametricFunction(
                            lambda t: parametric_function(t, a_tracker.get_value(),
                                                          b_tracker.get_value(),
                                                          c_tracker.get_value()),
                            t_range=[0, 2 * PI],
                            color=interpolate_color(
                                color_start, color_end, 0.5)
                        )
                    ),
                ),
                UpdateFromFunc(a_text, lambda mob: mob.set_value(
                    a_tracker.get_value())),
                UpdateFromFunc(b_text, lambda mob: mob.set_value(
                    b_tracker.get_value())),
                UpdateFromFunc(c_text, lambda mob: mob.set_value(
                    c_tracker.get_value())),
                rate_func=linear,
                # run_time=1,
            )

    def b(self, a_tracker, b_tracker, c_tracker, parametric_curve, parametric_function, a_text, b_text, c_text, a, c):
        forward_range = range(1, 10)
        backward_range = range(10, 0, -1)
        combined_range = itertools.chain(forward_range, backward_range)
        colors = [PURE_BLUE, YELLOW, PURE_RED]
        for i in combined_range:
            color_start = colors[i % len(colors)]
            color_end = colors[(i + 1) % len(colors)]
            self.play(
                a_tracker.animate.set_value(a),
                b_tracker.animate.set_value(i),
                c_tracker.animate.set_value(c),
                UpdateFromFunc(
                    parametric_curve,
                    lambda curve: curve.become(
                        ParametricFunction(
                            lambda t: parametric_function(t, a_tracker.get_value(),
                                                          b_tracker.get_value(),
                                                          c_tracker.get_value()),
                            t_range=[0, 2 * PI],
                            color=interpolate_color(
                                color_start, color_end, 0.5)
                        )
                    ),
                ),
                UpdateFromFunc(a_text, lambda mob: mob.set_value(
                    a_tracker.get_value())),
                UpdateFromFunc(b_text, lambda mob: mob.set_value(
                    b_tracker.get_value())),
                UpdateFromFunc(c_text, lambda mob: mob.set_value(
                    c_tracker.get_value())),
                rate_func=linear,
                # run_time=1,
            )

    def c(self, a_tracker, b_tracker, c_tracker, parametric_curve, parametric_function, a_text, b_text, c_text, a, b):
        forward_range = range(0, 10)
        backward_range = range(10, -1, -1)
        combined_range = itertools.chain(forward_range, backward_range)
        colors = [PURE_BLUE, YELLOW, PURE_RED]
        for i in combined_range:
            color_start = colors[i % len(colors)]
            color_end = colors[(i + 1) % len(colors)]
            self.play(
                a_tracker.animate.set_value(a),
                b_tracker.animate.set_value(b),
                c_tracker.animate.set_value(i),
                UpdateFromFunc(
                    parametric_curve,
                    lambda curve: curve.become(
                        ParametricFunction(
                            lambda t: parametric_function(t, a_tracker.get_value(),
                                                          b_tracker.get_value(),
                                                          c_tracker.get_value()),
                            t_range=[0, 2 * PI],
                            color=interpolate_color(
                                color_start, color_end, 0.5)
                        )
                    ),
                ),
                UpdateFromFunc(a_text, lambda mob: mob.set_value(
                    a_tracker.get_value())),
                UpdateFromFunc(b_text, lambda mob: mob.set_value(
                    b_tracker.get_value())),
                UpdateFromFunc(c_text, lambda mob: mob.set_value(
                    c_tracker.get_value())),
                rate_func=linear,
                # run_time=1,
            )
