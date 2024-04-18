import dash_mantine_components as dmc
from dash_iconify import DashIconify

footer = dmc.AppShellFooter(
    dmc.Group(
        p='sm',
        justify='space-between',
        children=[
            dmc.Group([
                dmc.Text("By Chad Bell"),
            ]),
            dmc.Group([
                dmc.Anchor(
                    h=28,
                    href="https://www.linkedin.com/in/chadbell045/",
                    children=DashIconify(icon="mdi:linkedin", width=28, color="black")
                ),
                dmc.Anchor(
                    h=28,
                    href="https://github.com/CBell045/dash-polars-pandas",
                    children=DashIconify(icon="mdi:github", width=28, color="black")
                ),
                dmc.Anchor(
                    h=28,
                    href="mailto:chadbell045@gmail.com",
                    children=DashIconify(icon="heroicons:envelope-16-solid", width=28, color="black")
                ),
            ])
        ]
    )
)