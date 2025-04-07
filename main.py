import flet as ft
from producto import Producto
from pedido import Pedido

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
        {"name": "CAFÉ AMERICANO", "icon_name": ft.Icons.COFFEE_OUTLINED},
        {"name": "MALTEADA DE FRESA", "icon_name": ft.Icons.COFFEE_MAKER},
        {"name": "SMOOTHIE MORA AZUL", "icon_name": ft.Icons.BRUNCH_DINING_SHARP},
    ]
    
    pastel = Producto('pastel', 50, 0)
    flan = Producto('flan', 50, 0)
    galletas = Producto('galletas', 120, 0)
    brownie = Producto('brownie', 80, 0)
    coffe = Producto('café', 40, 0)
    malteada = Producto('malteada', 50, 0)
    smoothie = Producto('smoothie', 60, 0)
    carro = [pastel , flan, galletas, brownie, coffe, malteada, smoothie]
    
    def get_options() -> list:
        options = []
        for icon in icons:
            options.append(
                ft.DropdownOption(key=icon["name"], leading_icon=icon["icon_name"])
            )
        return options
    
    def addRow(e) -> None:
        
        cantidad = 0
        x = False
        if selector.value == "REBANADA DE PASTEL":
            cantidad = pastel.increment()
            pastel.id = len(Pedido.elementos)
            x = Pedido.addElement(pastel)
        elif selector.value == 'REBANADA DE FLAN':
            cantidad = flan.increment()
            flan.id = len(Pedido.elementos)
            x = Pedido.addElement(flan)
        elif selector.value == 'DOCENA DE GALLETAS':
            cantidad = galletas.increment()
            galletas.id = len(Pedido.elementos)
            x = Pedido.addElement(galletas)
        elif selector.value == 'BROWNIE':
            cantidad = brownie.increment()
            brownie.id = len(Pedido.elementos)
            x = Pedido.addElement(brownie)
        elif selector.value == 'CAFÉ AMERICANO':
            coffe.id = len(Pedido.elementos)
            cantidad = coffe.increment()
            x = Pedido.addElement(coffe)
        elif selector.value == 'MALTEADA DE FRESA':
            cantidad = malteada.increment()
            malteada.id = len(Pedido.elementos)
            x = Pedido.addElement(malteada)
        elif selector.value == 'SMOOTHIE MORA AZUL':
            smoothie.id = len(Pedido.elementos)
            cantidad = smoothie.increment()
            x = Pedido.addElement(smoothie)
        
        if selector.value is not None and x:
            tab.visible = True
            cuenta.visible = True
            tab.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(value=selector.value)),
                        ft.DataCell(ft.Text(value=str(cantidad)))
                    ]
                )
            )
        elif selector.value is not None:
            if selector.value == "REBANADA DE PASTEL":
                tab.rows[pastel.id-1].cells[1] = ft.DataCell(ft.Text(value=str(pastel.cantidad)))
            elif selector.value == 'REBANADA DE FLAN':
                tab.rows[flan.id-1].cells[1] = ft.DataCell(ft.Text(value=str(flan.cantidad)))
            elif selector.value == 'DOCENA DE GALLETAS':
                tab.rows[galletas.id-1].cells[1] = ft.DataCell(ft.Text(value=str(galletas.cantidad)))
            elif selector.value == 'BROWNIE':
                tab.rows[brownie.id-1].cells[1] = ft.DataCell(ft.Text(value=str(brownie.cantidad)))
            elif selector.value == 'CAFÉ AMERICANO':
                tab.rows[coffe.id-1].cells[1] = ft.DataCell(ft.Text(value=str(coffe.cantidad)))
            elif selector.value == 'MALTEADA DE FRESA':
                tab.rows[malteada.id-1].cells[1] = ft.DataCell(ft.Text(value=str(malteada.cantidad)))
            elif selector.value == 'SMOOTHIE MORA AZUL':
                tab.rows[smoothie.id-1].cells[1] = ft.DataCell(ft.Text(value=str(smoothie.cantidad)))
         
         
        cuenta.value = 'Total: ${}'.format( Pedido.calcularCarrito(carro))
        page.update()
    
    selector = ft.Dropdown(
        border=ft.InputBorder.UNDERLINE,
        enable_filter=True,
        editable=True,
        leading_icon=ft.Icons.SEARCH,
        options=get_options(),
        autofocus=True,
        width=270
    )
    
    tab = ft.DataTable(
        visible= False,
        heading_row_color=ft.Colors.GREY_100,
        columns=[
            ft.DataColumn(ft.Text(value='Producto')),
            ft.DataColumn(ft.Text(value='Cantidad'), numeric=True)
        ],
        rows=[]
    )
    
    cuenta = ft.Text(
                        value="TOTAL: {}".format(Pedido.calcularCarrito(carro)),
                        visible= False,
                        weight= ft.FontWeight.W_500
                    )
    
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
                                            ft.DataCell(ft.Text("$ 50")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("REBANADA DE FLAN")),
                                            ft.DataCell(ft.Text("NAPOLITANO")),
                                            ft.DataCell(ft.Text("$ 50")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("DOCENA DE GALLETAS")),
                                            ft.DataCell(ft.Text("ALMENDRAS")),
                                            ft.DataCell(ft.Text("$ 120")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("BROWNIE")),
                                            ft.DataCell(ft.Text("CHOCOLATE")),
                                            ft.DataCell(ft.Text("$ 80"))
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
                                            ft.DataCell(ft.Text("AMERICANO")),
                                            ft.DataCell(ft.Text("$ 40")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("MALTEADA")),
                                            ft.DataCell(ft.Text("FRESA")),
                                            ft.DataCell(ft.Text("$ 50")),
                                        ],
                                    ),
                                    ft.DataRow(
                                        cells=[
                                            ft.DataCell(ft.Text("SMOOTHIE")),
                                            ft.DataCell(ft.Text("MORA AZUL")),
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
                            ft.Text(value='AÑADA LOS ALIMENTOS DE SU AGRADO', weight=ft.FontWeight.W_500),
                            selector,
                            ft.ElevatedButton(text='AÑADIR AL CARRITO', on_click=addRow, width=270)
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START
                    ),
                    width=300,
                    height=500
                ),
                ft.Container(
                    content=ft.Column(
                        spacing=40,
                        controls=[
                            tab,
                            cuenta
                        ]
                    ),
                    width=270,
                    height=500
                )
            ]
        )
    )
    
    page.update()

ft.app(target=main)
