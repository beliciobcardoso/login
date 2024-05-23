import os
import dotenv
import time

import flet as ft

dotenv.load_dotenv(dotenv.find_dotenv())

user_login = os.getenv("USER_LOGIN")
password_login = os.getenv("PASSWORD_LOGIN")

def main(pagina):
    pagina.scroll = "adaptive"
    pagina.padding = 20
    
    
    def close_dlg(e):
        tela_login.open = False
        tela_cadastro.open = False
        pagina.update()
    
    button_cancel = ft.ElevatedButton("Cancelar", on_click=close_dlg)
    
 
    table = ft.DataTable(
        sort_column_index=0,
        sort_ascending=False,
        columns=[
            ft.DataColumn(ft.Text("First name"), on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
            ft.DataColumn(ft.Text("Last name")),
            ft.DataColumn(ft.Text("Age"), numeric=True),
            ft.DataColumn(ft.Text("Email"))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("Smith")),
                    ft.DataCell(ft.Text("43")),
                    ft.DataCell(ft.Text("john.smith" + "@email.com")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Jack")),
                    ft.DataCell(ft.Text("Brown")),
                    ft.DataCell(ft.Text("19")),
                    ft.DataCell(ft.Text("jack.brown" + "@email.com")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Emma")),
                    ft.DataCell(ft.Text("Johnson")),
                    ft.DataCell(ft.Text("32")),
                    ft.DataCell(ft.Text("emma.johnson" + "@email.com")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Michael")),
                    ft.DataCell(ft.Text("Williams")),
                    ft.DataCell(ft.Text("24")),
                    ft.DataCell(ft.Text("michael.williams" + "@email.com")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Sophia")),
                    ft.DataCell(ft.Text("Jones")),
                    ft.DataCell(ft.Text("29")),
                    ft.DataCell(ft.Text("sophia.jones" + "@email.com")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("William")),
                    ft.DataCell(ft.Text("Taylor")),
                    ft.DataCell(ft.Text("35")),
                    ft.DataCell(ft.Text("william.taylor" + "@email.com")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Alice")),
                    ft.DataCell(ft.Text("Wong")),
                    ft.DataCell(ft.Text("25")),
                    ft.DataCell(ft.Text("alice.wong" + "@email.com")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("James")),
                    ft.DataCell(ft.Text("Brown")),
                    ft.DataCell(ft.Text("21")),
                    ft.DataCell(ft.Text("james.brown" + "@email.com")),
                ],
            ),
        ],
    )
    
    def register_users(event):
        first_name = input_first_name.value
        last_name = input_last_name.value
        age = input_age.value
        email = input_email.value
        
        table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(first_name)),
                    ft.DataCell(ft.Text(last_name)),
                    ft.DataCell(ft.Text(age)),
                    ft.DataCell(ft.Text(email)),
                ],
            )
        )
        
        input_first_name.value = ""
        input_last_name.value = ""
        input_age.value = ""
        input_email.value = ""
        
        tela_cadastro.open = False
        pagina.update()
    
    button_cadastro_user = ft.ElevatedButton("Cadastrar", on_click=register_users)
    
           
    input_first_name = ft.TextField(label="First name")
    input_last_name = ft.TextField(label="Last name")
    input_age = ft.TextField(label="Age")
    input_email = ft.TextField(label="Email")
    
    input_column = ft.Column([input_first_name, input_last_name, input_age, input_email])
    
    container_input_cadastro = ft.Container(
        content=input_column, 
        alignment=ft.alignment.center, 
        width=600, 
        height=300
        )
    
    tela_cadastro = ft.AlertDialog(
        modal=True,
        title=ft.Text("Cadastro"), 
        content=container_input_cadastro,
        actions=[button_cadastro_user, button_cancel], 
        actions_alignment=ft.MainAxisAlignment.END
        )

    
    def cadastro_page(event):
        pagina.dialog = tela_cadastro
        tela_cadastro.open = True
        pagina.update()
    
    button_criar = ft.ElevatedButton("Criar usuário", on_click=cadastro_page, color="blue")    
    row_controls = ft.Row([button_criar])
    
    container_control = ft.Container(content=row_controls, alignment=ft.alignment.top_center, padding=20)
        
    def login(event):
        user = input_user.value
        password = input_password.value
        
        if user == user_login and password == password_login:
            pagina.remove(container_main)
            tela_login.open = False
            input_user.value = ""
            input_password.value = ""
            pagina.snack_bar = ft.SnackBar(ft.Text("Login efetuado com sucesso", size=30, color="white"), bgcolor="green")
            pagina.snack_bar.open = True
            pagina.add(container_control)
            pagina.add(container_main)
            pagina.update()
            time.sleep(60)
            pagina.remove(container_control)
            pagina.snack_bar.open = False
            pagina.update()
        else:
            pagina.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha inválidos", size=30, color="white"), bgcolor="red")
            pagina.snack_bar.open = True
            input_user.value = ""
            input_password.value = ""
            pagina.update()
        
        
    input_user = ft.TextField(label="Usuário")
    input_password = ft.TextField(label="Senha", password=True)
    button_login = ft.ElevatedButton("Login", on_click=login)
    
    input_column = ft.Column([input_user, input_password])
    
    container_input = ft.Container(
        content=input_column, 
        alignment=ft.alignment.center, 
        width=300, 
        height=150
        )
    
    tela_login = ft.AlertDialog(
        modal=True,
        title=ft.Text("Login"), 
        content=container_input,
        actions=[button_login, button_cancel], 
        actions_alignment=ft.MainAxisAlignment.END
        )
        
    def login_page(event):
        pagina.dialog = tela_login
        tela_login.open = True
        pagina.update()
        
    
    pagina.appbar = ft.AppBar(
            leading=ft.Icon(name=ft.icons.SETTINGS_OUTLINED, color="blue", size=50),
            leading_width=40,
            title=ft.Text("App Flet", size=30, color="white"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Configurações"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="login", checked=False, on_click=login_page
                        ),
                    ]
                ),
            ],

    )
    
    container_main = ft.Container(content=table, alignment=ft.alignment.center)
    
    # pagina.add(container_control)
    
    pagina.add(container_main)
  

    
ft.app(main, view=ft.WEB_BROWSER, port=8080)