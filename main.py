import flet as ft
import string
import random

class App:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.bgcolor = ft.colors.BROWN_600
        self.page.window_min_width=600
        self.page.window_min_height=800
        self.page.window_maximizable = True
        self.page.padding = ft.padding.all(0)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.main()

    def main(self):

        avaivable_words = ['python', 'flet', 'programador', 'interface']
        choiced = random.choice(avaivable_words).upper() # Palavra a divinhar
        word_conj = set()

        def letter_to_guess(letter):
            return ft.Container(
                height = 30,
                width = 30,
                bgcolor = ft.colors.AMBER_500,
                border_radius = ft.border_radius.all(5),
                content = ft.Text(
                    value = letter,
                    color = ft.colors.WHITE,
                    size = 20,
                    text_align = ft.TextAlign.CENTER,
                    weight = ft.FontWeight.BOLD,
                ),
            )

        def validate_letter(e):
            e.control.disabled = True
            e.control.gradient = ft.LinearGradient(colors = [ft.colors.GREY])
            for pos, letter in enumerate(choiced):
                if e.control.content.value == letter:
                    word.controls[pos] = letter_to_guess(letter = letter)
                    word_conj.add(letter)  
                    if len(word_conj) == len(choiced):
                        self.page.dialog = ft.AlertDialog(
                            title = ft.Text(value = 'Você ganhou! :)'), 
                            open = True
                        )
                        word.controls = [letter_to_guess('_') for letter in choiced]
                        for letter in keyboard.content.controls:
                            letter.disabled = False
                            letter.gradient = ft.LinearGradient(
                                begin = ft.alignment.top_center,
                                end = ft.alignment.bottom_center,
                                colors = [ft.colors.AMBER, ft.colors.DEEP_ORANGE],
                            )
                        word_conj.clear()
           
            if e.control.content.value not in choiced:
                victim.data += 1
                errors = victim.data
                victim.src = f'images/hangman_{errors}.png'
                if errors > 7:
                    self.page.dialog = ft.AlertDialog(
                        title = ft.Text(value = 'Você perdeu! :('), 
                        open = True
                    )
                    victim.data = 0
                    errors = 0
                    word.controls = [letter_to_guess('_') for letter in choiced]
                    for letter in keyboard.content.controls:
                        letter.disabled = False
                        letter.gradient = ft.LinearGradient(
                            begin = ft.alignment.top_center,
                            end = ft.alignment.bottom_center,
                            colors = [ft.colors.AMBER, ft.colors.DEEP_ORANGE],
                        )
                    victim.src = f'images/hangman_{errors}.png'
                    word_conj.clear()

            self.page.update()    

        scene = ft.Image(col = 12, src = 'images/scene.png')

        victim = ft.Image(
            data=0,
            src='images/hangman_0.png', 
            repeat=ft.ImageRepeat.NO_REPEAT,
            height=200,
        )

        word = ft.Row(
            wrap = True,
            alignment = ft.MainAxisAlignment.CENTER,
            controls = [ 
                letter_to_guess('_') for letter in choiced
            ],
        )

        game = ft.Container(
            col={'xs': 12, 'lg': 6},
            padding=ft.padding.all(10),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[
                    victim,
                    word,
                ],
            ),
        )

        keyboard = ft.Container(
            col={'xs': 12, 'lg': 6},
            image_src='images/keyboard.png',
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            image_fit=ft.ImageFit.FILL,
            padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
            content=ft.Row(
                wrap=True,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=30,
                        width=30,
                        border_radius=ft.border_radius.all(5),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE],
                        ),
                        content=ft.Text(
                            value=letter,
                            color=ft.colors.WHITE,
                            size=20,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                        ),
                        disabled = False,
                        on_click=validate_letter,
                    ) for letter in string.ascii_uppercase
                ],   
            ),
        )

        layout = ft.ResponsiveRow(
            columns = 12,
            controls = [
                scene,
                game,
                keyboard,
                scene,
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
        )
        
        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target = App, assets_dir = 'assets')
