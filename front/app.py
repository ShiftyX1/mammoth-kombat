import asyncio
import flet as ft

async def main(page: ft.Page) -> None:
    page.title = "Mammoth Kombat"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#141221"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"FulboArgenta": "fonts/FulboArgenta.ttf"}
    page.theme = ft.Theme(font_family="FulboArgenta")

    async def score_up(event: ft.ContainerTapEvent):
        global default_score
        score.data += 1
        score.value = str(score.data)
        image.scale = 0.85
        score_counter.opacity = 100
        score_counter.value = default_score
        score_counter.right = 0
        score_counter.left = tap_position[0]
        score_counter.top = tap_position[1]
        score_counter.bottom = 0
        progress_bar.value += (1 / 500)

        print(score.data, type(score.data))

        await page.update_async()
        await asyncio.sleep(0.1)
        score_counter.opacity = 0
        if score.data % 10 == 0:
            image.src = "mammoth_ceo.png"
            page.dialog = dlg
            dlg.open = True
            progress_bar.value = 0
        
        image.scale = 1
        await page.update_async()
    
    def on_tap_down(event: ft.ContainerTapEvent):
        global tap_position
        tap_position = (event.local_x, event.local_y)

    async def close_dlg(e):
        dlg.open = False
        await e.control.page.update_async()

    dlg = ft.AlertDialog(
        title=ft.Text("🐘 +500", text_align=ft.TextAlign.CENTER),
        content=ft.Column(
            [
                ft.Text("ГОЙДААА!")
            ],
            expand=False,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            height=300
        ),
        actions=[
            ft.TextButton("Да", on_click=close_dlg),
            ft.TextButton("ГОООООЛ!", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    score = ft.TextField(
        value=0, 
        data=0, 
        read_only=True, 
        border=ft.InputBorder.NONE, 
        text_align=ft.TextAlign.CENTER, 
        text_size=65, 
        dense=True,
    )
    # score = ft.Text(value=0, size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="mammoth_novice.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
        width=400,
        height=400
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color="#ff8b1f",
        bgcolor="#bf6524"
    )
    await page.add_async(
        ft.Row(
            [
                ft.Image(src="money_icon.png", width=100, height=100),
                score
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Container(
            content=ft.Stack(
                controls=[
                    image,
                    score_counter
                ]                
            ),
            on_click=score_up,
            on_tap_down=on_tap_down,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )

if __name__ == "__main__":
    tap_position = (0, 0)
    default_score = "+1"
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080)