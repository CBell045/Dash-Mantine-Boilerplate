import dash
import dash_mantine_components as dmc

dash.register_page(__name__, path="/")


layout = [
    dmc.Title("Home Page"),
    dmc.Text("Welcome to the home page!"),
]
