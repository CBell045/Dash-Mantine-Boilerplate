from dash import dash
import dash_mantine_components as dmc

dash._dash_renderer._set_react_version('18.2.0')

app = dash.Dash()

app.layout = dmc.MantineProvider([
    dmc.AppShell([
        dmc.AppShellMain(dmc.Title("Home Page")),
    ])
])

if __name__ == "__main__":
    app.run(debug=True)