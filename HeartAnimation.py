from manim import *


class mt(ThreeDScene):
    def construct(self): 

        
        tdaxes = NumberPlane()

        a = ValueTracker(0.0)

        mathtext = MathTex(r'x^{2/3}+\sqrt{3.3-x^2}\cdot\sin({a} \pi x)').set_color(RED).to_edge(LEFT+UP,buff=1).shift(UP*0.5)
        mathtext_rec = Rectangle(height = mathtext.height*1.5, width=mathtext.width*1.1,fill_opacity=0.2,fill_color=GRAY,stroke_opacity=0).move_to(mathtext.get_center())

        text = always_redraw(lambda: Tex(f'{round(a.get_value(),ndigits=1)}').set_color(BLUE_C).shift(UP*2+LEFT*3).next_to(mathtext,RIGHT,buff=1.5))
        text_rec = Rectangle(height=mathtext.height*1.5,width=text.width*2,fill_opacity=0.2,fill_color=GRAY,stroke_opacity=0).move_to(text.get_center())
        a_text_in = mathtext[0][18].copy()
        
        
        a_text_in_rec = Rectangle(height=a_text_in.height*1.1,width=a_text_in.width*1.1,color=YELLOW).move_to(a_text_in.get_center())
    
        self.play(Create(tdaxes))
        self.play(Write(mathtext),Create(mathtext_rec))
        self.wait()

        self.play(Circumscribe(a_text_in),a_text_in.animate.set_color(BLUE_C),Circumscribe(text_rec),FadeIn(a_text_in_rec))
        mathtext[0][18].set_color(BLUE_C)
        self.play(FadeIn(text_rec))
        self.play(ReplacementTransform(VGroup(a_text_in,a_text_in_rec),text),run_time=2)


        graph = always_redraw(
            lambda: tdaxes.plot(lambda x: 
                                abs(x)**(2/3)+np.sqrt(3.3-x**2)*np.sin(a.get_value()*PI*x),
                                color=BLUE_C,
                                x_range=[-np.sqrt(3.3), np.sqrt(3.3)])
                        )

        self.play(Create(graph))

        self.play(a.animate.set_value(-6.8),run_time=4)
        self.play(a.animate.set_value(6.8),run_time=4)
        self.wait()

        heart = tdaxes.plot_implicit_curve(lambda x,y: (x**2+y**2-1)**3-x**2*y**3,fill_color=BLUE_C,fill_opacity=1).scale(1.5).shift(UP*0.6)
        tdgroup = VGroup(mathtext_rec,text,text_rec,a_text_in,a_text_in_rec)
        self.play(Unwrite(mathtext),FadeOut(tdgroup))
        self.play(ReplacementTransform(graph,heart))

        self.wait(3)
        







