import flet as ft
from producto import Producto

def main(page: ft.Page) -> None:
    # General settings of the window
    page.title = 'Main Window'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Elements of the GUI
    administrador = ft.ElevatedButton(
        text='ADMINISTRADOR', color=ft.Colors.BLACK, bgcolor=ft.Colors.BLUE_100, height=100, width=200
    )
    consumidor = ft.ElevatedButton(
        text='CONSUMIDOR', color=ft.Colors.BLACK, bgcolor=ft.Colors.GREEN_100, height=100, width=200, on_click=lambda e: ConsumidorView(page)
    )
    
    page.add(administrador, consumidor)

def ConsumidorView(page: ft.Page) -> None:
    page.title = 'Creación de pedido'
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Clear the page before adding new content
    page.controls.clear()
    
    page.add(ft.Text(
        value='GENERANDO MI PEDIDO',
        size=40,
        weight=ft.FontWeight.W_300
    ))
    
    # List with the main icons
    icons = [
        {"name": "REBANADA DE PASTEL", "icon_name": ft.Icons.CAKE_OUTLINED},
        {"name": "REBANADA DE FLAN", "icon_name": ft.Icons.CAKE_OUTLINED},
        {"name": "DOCENA DE GALLETAS", "icon_name": ft.Icons.COOKIE_OUTLINED},
        {"name": "BROWNIE", "icon_name": ft.Icons.BREAKFAST_DINING},
        {"name": "CAFÉ CAPPUCCINO", "icon_name": ft.Icons.COFFEE_OUTLINED},
        {"name": "CAFÉ AMERICANO", "icon_name": ft.Icons.COFFEE_OUTLINED},
        {"name": "MALTEADA DE FRESA", "icon_name": ft.Icons.COFFEE_MAKER},
        {"name": "MALTEADA DE CHOCOLATE", "icon_name": ft.Icons.COFFEE_MAKER},
        {"name": "SMOOTHIE DE MANZANA", "icon_name": ft.Icons.BRUNCH_DINING_SHARP},
        {"name": "SMOOTHIE DE MORA AZUL", "icon_name": ft.Icons.BRUNCH_DINING_SHARP}
    ]
    
    def get_options():
        options = []
        for icon in icons:
            options.append(
                ft.DropdownOption(key=icon["name"], leading_icon=icon["icon_name"])
            )
        return options
    
    def addRow(e) -> None:
        tab.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(selector.value)),
                    ft.DataCell(ft.Text("1"))
                ]
            )
        )
        page.update()
    
    selector = ft.Dropdown(
        border=ft.InputBorder.UNDERLINE,
        enable_filter=True,
        editable=True,
        leading_icon=ft.Icons.SEARCH,
        options=get_options(),
        autofocus=True,
        width=260
    )
    
    tab = ft.DataTable(
        heading_row_color=ft.Colors.GREY_100,
        columns=[
            ft.DataColumn(ft.Text(value='Producto')),
            ft.DataColumn(ft.Text(value='Cantidad'), numeric=True)
        ]
    )
    
    texto = ft.Text(value='')
    
    # Menu de postres y bebidas
    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    padding=40,
                    content=ft.Column(
                        spacing=40,
                        controls=[
                            ft.DataTable(
                                heading_row_height=70,
                                data_row_min_height=50.0,
                                heading_row_color=ft.Colors.GREY_100,
                                columns=[
                                    ft.DataColumn(ft.Text("POSTRE")),
                                    ft.DataColumn(ft.Text("SABORES")),
                                    ft.DataColumn(ft.Text("PRECIO"), numeric=True),
                                ],
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("REBANADA DE PASTEL")),
                                            ft.DataCell(ft.Text("TRES LECHES")),
                                            ft.DataCell(ft.Text("$ 35")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("REBANADA DE FLAN")),
                                            ft.DataCell(ft.Text("NAPOLITANO")),
                                            ft.DataCell(ft.Text("$ 35")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("DOCENA DE GALLETAS")),
                                            ft.DataCell(ft.Text("ALMENDRAS")),
                                            ft.DataCell(ft.Text("$ 100")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("BROWNIE")),
                                            ft.DataCell(ft.Text("CHOCOLATE")),
                                            ft.DataCell(ft.Text("$ 60"))
                                        ]
                                    )
                                ],
                            ),
                            ft.DataTable(
                                heading_row_height=70,
                                heading_row_color=ft.Colors.GREY_100,
                                columns=[
                                    ft.DataColumn(ft.Text("BEBIDA")),
                                    ft.DataColumn(ft.Text("SABORES")),
                                    ft.DataColumn(ft.Text("PRECIO"), numeric=True),
                                ],
                                rows=[
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("CAFÉ")),
                                            ft.DataCell(ft.Text("CAPPUCCINO, AMERICANO")),
                                            ft.DataCell(ft.Text("$ 40")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("MALTEADA")),
                                            ft.DataCell(ft.Text("CHOCOLATE, FRESA")),
                                            ft.DataCell(ft.Text("$ 50")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("SMOOTHIE")),
                                            ft.DataCell(ft.Text("MANZANA, MORA AZUL")),
                                            ft.DataCell(ft.Text("$ 60")),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    width=600,
                ),
                ft.Container(
                    content=ft.Column(
                        spacing=40,
                        controls=[
                            ft.Text(value='AÑADA LOS ALIMENTOS DE SU AGRADO', weight=ft.FontWeight.W_400),
                            selector,
                            ft.ElevatedButton(text='AÑADIR AL CARRITO', on_click=addRow, width=300)
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START
                    ),
                    width=300,
                    height=500
                ),
                ft.Container(
                    content=ft.Column(
                        spacing=20,
                        controls=[
                            tab
                        ]
                    ),
                    width=260,
                    height=500
                )
            ]
        )
    )
    
    page.update()

ft.app(target=main)
