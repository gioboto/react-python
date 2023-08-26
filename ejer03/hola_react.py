useState = React.useState
el = React.createElement

def App():
    val, setVal = useState("")

    def di_hola():
        setVal("Hola React!")

    def limpiar():
        setVal("")

    return [
        el('button', {'onClick': di_hola}, "Click aqui!"),
        el('button', {'onClick': limpiar}, "Limpiar"),
        el('div', None, val)
    ]

def render():
    ReactDOM.render(
        el(App, None),
        document.getElementById('root')
    )

document.addEventListener('DOMContentLoaded', render)

