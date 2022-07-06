from datetime import datetime , timedelta

nacimiento = datetime(2005, 8, 22, 8, 30)

edad = datetime.now() - nacimiento



anios = (edad.days / 365)

print(anios)

print(((edad.days / 365)- anios)*12)
time = timedelta(anios)
print(time)