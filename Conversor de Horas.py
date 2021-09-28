segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horas = segundos // 3600
segundos_rest = horas % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")

