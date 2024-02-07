import flet
import requests


def main(page: flet.Page):
    page.title = "Weather Report App"
    page.theme_mode = "dark"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    user_data = flet.TextField(label='Enter the city', width=400)
    weather_data = flet.Text('', size=15)

    def get_info(event):
        temp = "The request is too short"
        if len(user_data.value) > 1:
            api = "openweatherapi"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={api}&units=metric"
            try:
                result = requests.get(url).json()
                temp = f"{result['main']['temp']} (feels like {result['main']['feels_like']}), {result['weather'][0]['description']}"
            except KeyError:
                temp = "City not found or weather data unavailable"
        weather_data.value = temp
        page.update()

    def change_theme(event):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

    page.add(
        flet.Row(
            [flet.IconButton(flet.icons.SUNNY_SNOWING, on_click=change_theme),
                flet.Text('Weather Report')
            ],
            alignment=flet.MainAxisAlignment.CENTER
        ),
        flet.Row(
            [user_data],
            alignment=flet.MainAxisAlignment.CENTER
        ),
        flet.Row(
            [weather_data],
            alignment=flet.MainAxisAlignment.CENTER
        ),
        flet.Row(
            [flet.OutlinedButton(text="Get", on_click=get_info)],
            alignment=flet.MainAxisAlignment.CENTER
        )
    )


flet.app(target=main)
