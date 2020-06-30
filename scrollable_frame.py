from tkinter import Scrollbar, Frame, Canvas


class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = Canvas(self, *args, **kwargs)
        scrollbar = Scrollbar(
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
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        container.bind("<MouseWheel>", lambda event: self._on_mousewheel(event))

        
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-event.delta/120),"units")

        