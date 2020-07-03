from tkinter import Scrollbar, Frame, Canvas

'''
 the ScrollableFrame is a frame with a scrollbar toghether

 @container => where the ScrolableFrame will be drawn
'''
class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.numberOfChilds = 0
        self._on_end = lambda: None
        self.canvas = Canvas(self, *args, **kwargs)
        self.scrollbar = Scrollbar(
            self,
            orient="vertical",
            command=self.canvas.yview
        )
        self.scrollable_frame = Frame(self.canvas, *args, **kwargs)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        container.bind("<MouseWheel>", lambda event: self._on_mousewheel(event))

    '''
        setOnEnd => this method sets the event OnEnd, it recives a lambda _on_end and by default is None

        @_on_end => is the lambda funcion for when the mouseWheel turn to 95%
    '''
    def setOnEnd(self, _on_end):
        self._on_end = _on_end

    '''
        _on_mousewheel => this method is an event reciver for when mouseWheel changes
    '''
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-event.delta/120),"units")
        if self.scrollbar.get()[1] > 0.95:
            self._on_end()
