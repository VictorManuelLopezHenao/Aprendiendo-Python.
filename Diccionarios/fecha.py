print("\nFormato de fecha (dd/mm/aa)")

fecha = input("Digite una fecha respecto al formato anterior: ")

meses = {
   "01": "enero",
    "02": "febrero",
    "03": "marzo",
    "04": "abril",
    "05": "mayo",
    "06": "junio",
    "07": "julio",
    "08": "agosto",
    "09": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}

dia, mes, año = fecha.split("/") 

print(f"{dia} de {meses[mes]} de {año}")