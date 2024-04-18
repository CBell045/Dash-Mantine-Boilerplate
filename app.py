import dash
from dash import Dash
import dash_mantine_components as dmc
from components.footer import footer
from components.header import header

dash._dash_renderer._set_react_version('18.2.0')

app = Dash(use_pages=True)

app.layout = dmc.MantineProvider(
    theme={
        "fontFamily": "'Inter', sans-serif",
        },
    children=dmc.AppShell(
        children=[
            header,
            dmc.AppShellNavbar("Navbar"),
            # dmc.AppShellAside("Aside"),
            dmc.AppShellMain([
                dash.page_container,
            ]),
            footer,
            ],
        header={"height": 70},
        padding="xl",
        zIndex=1400,
        navbar={
            "width": 300,
            "breakpoint": "sm",
            "collapsed": {"mobile": True},
        },
        aside={
            "width": 300,
            "breakpoint": "xl",
            "collapsed": {"desktop": False, "mobile": True},
        },
        footer={"height": 50},
    ),
)

if __name__ == "__main__":
    app.run(debug=True)