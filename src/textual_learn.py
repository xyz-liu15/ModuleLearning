from textual.app import App,ComposeResult
from textual.widgets import Header,Footer,Static,Welcome
# from rich.traceback import install


# install(show_locals = True)

class MyApp(App):
    CSS_PATH = "../css_data/css_test.tcss"
    def compose(self) -> ComposeResult:
        """编排TUI界面"""
        yield Header(show_clock = True)
        yield Footer()
        
       

if __name__ == "__main__":
    app = MyApp()
    app.run()