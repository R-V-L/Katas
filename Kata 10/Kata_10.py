def agua_restante(astronautas, agua_restante, dias_restantes):
    for argumento in [astronautas, agua_restante, dias_restantes]:
        try:
            argumento / 10
        except TypeError:
            raise TypeError(f"Todos los argumentos deben ser de tipo entero, en cambio se recibio: '{argumento}' del tipo {type(argumento)}")
    uso_diario = astronautas * 11
    uso_total = uso_diario * dias_restantes
    agua_total_restante = agua_restante - uso_total
    if agua_total_restante < 0:
        raise RuntimeError(f"No hay agua suficiente para {astronautas} astronautas despues de {dias_restantes} dias")
    return f"La cantidad de agua restante despues {dias_restantes} dias es: {agua_total_restante} litros"

print(agua_restante(5, 100, None))