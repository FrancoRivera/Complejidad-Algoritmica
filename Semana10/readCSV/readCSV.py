import csv
import datetime
import json

class Trabajador():
    def __str__(self):
        return self.nombre + " minutos: " +str(self.minutos_retraso) + " dias: " +str(self.contador_dias)


    def __init__(self, nombre):
        self.nombre = nombre
        self.activo = False
        self.cant_dias = 0
        self.cant_marcaciones = 0
        self.dias_trabajados =0
        self.minutos_retraso = 0
        self.lista_marcaciones = list()
        self.lista_fechas = list()
        self.lista_horas = list()
        self.lista_tardanzas = list()
        self.dict_marcaciones = {}
        self.contador_dias = 0

    def ingresarMarcacion(self, marcacion):
        self.cant_marcaciones +=1
        marcacion = str(marcacion).replace(".", "")
        dt = datetime.datetime.strptime(marcacion, "%d/%m/%Y %I:%M:%S %p")
        self.lista_marcaciones.append(dt)
        fecha = str(dt.year) + "-" +(str(dt.month) if len(str(dt.month))>1 else "0" +str(dt.month)) + "-" + (str(dt.day) if len(str(dt.day))>1 else "0" +str(dt.day))
        if fecha not in self.lista_fechas:
            self.lista_fechas.append(fecha)

    def getDiferencia(self, date1, date2):
        return 0

    def get_marcacion_fecha(self, fecha):
        return self.dict_marcaciones.get(str(fecha))

    def get_marcaciones(self):
        return self.lista_marcaciones

    def dentroRango(self, fecha_ini, fecha_fin, date):
        fecha_ini =  datetime.datetime.strptime(fecha_ini, "%Y-%m-%d")
        fecha_fin = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")

        if date > fecha_ini and date < fecha_fin:
            return True
        return False

    def contarMinutos(self, fecha_ini="2015-01-01", fecha_fin="2020-01-01", mostrar=False):
        contador = 0
        fecha = datetime.datetime.now()
        almuerzo = False
        hora_almuerzo = ""
        salida = False
        self.contador_dias = 0
        self.lista_marcaciones.sort()
        for dt in self.lista_marcaciones:
            if not self.dentroRango(fecha_ini, fecha_fin, dt): #si no esta dentro del rango
                continue #skippear
            if fecha.day == dt.day and fecha.month == dt.month  and fecha.year == dt.year:
                if almuerzo:
                    self.getDiferencia(hora_almuerzo, dt)
                    almuerzo =False
                    salida = True
                else:
                    if salida:
                        salida = False
                        continue
                    hora_almuerzo = dt
                    almuerzo = True

                pass
            else:
                if dt.hour >= 8:
                    dif_horas = dt.hour - 8
                    suma = int(dif_horas*60) + int(dt.minute)
                    if suma > 200:
                        continue
                    self.lista_tardanzas.append(str(dt) + " " +  str(suma))
                    self.contador_dias += 1
                    self.minutos_retraso += suma

                fecha = str(dt.year) + "-" +(str(dt.month) if len(str(dt.month))>1 else "0" +str(dt.month)) + "-" + (str(dt.day) if len(str(dt.day))>1 else "0" +str(dt.day))
                self.dict_marcaciones[str(fecha)] = (str(dt.hour) if len(str(dt.hour))>1 else "0" +str(dt.hour))+":"+(str(dt.minute) if len(str(dt.minute))>1 else "0" +str(dt.minute))

            fecha = dt
        if mostrar:
            self.imprimirTardanzas()

    def imprimirTardanzas(self):
        for i in self.lista_tardanzas:
            print(i)

    def imprimirMarcaciones(self):
        for i in self.lista_marcaciones:
            print(i)

    def getJson(self):
        dic = '{ "nombre": "'+ str(self.nombre)+'"'
        dic += ', "color": "' + str("green") + '"'
        dic += ', "marcaciones": ['
        for i in range(0, len(self.lista_marcaciones)-1):
            dic += '"' +str(self.lista_marcaciones[i]) + '", '
        dic += '"'+ str(self.lista_marcaciones[-1]) + '"'
        dic += "]}"
        return dic



class Asistencia():
    def __init__(self, fecha_ini, fecha_fin):
        self.dict_usuarios ={1:Trabajador("Isabel Melchor"),
                3:Trabajador("Liliana Ordoñez"),
                4:Trabajador("Jose Valdivia"),
                5: Trabajador("Jennifer Huaman"),
                7: Trabajador("Isabel Rosas"),
                10: Trabajador("Franco Rivera"),
                11: Trabajador("Makarena Flores"),
                13: Trabajador("Claudia Adonayre"),
                14: Trabajador("Noelia Herrera"),
                15: Trabajador("Rayza Joaquin"),
                16: Trabajador("Wendy Luque"),
                17: Trabajador("Lilian Salazar"),
                18: Trabajador("Mayra Sanchez"),
                19: Trabajador("Rossmery Salcedo")
                }
        self.fecha_ini = fecha_ini
        self.dt_ini = datetime.datetime.strptime(fecha_ini, "%Y-%m-%d")
        self.dt_fin =datetime.datetime.strptime(fecha_fin, "%Y-%m-%d")
        self.fecha_fin = fecha_fin

        self.dict_fechas = {}

    def get_lista_fechas(self):
        lista_fechas = list()
        fecha_ini = self.dt_ini.date()
        fecha_fin = self.dt_fin.date()
        delta = fecha_fin - fecha_ini

        for i in range(delta.days + 1):
            fecha = str(fecha_ini + datetime.timedelta(days=i))
            lista_fechas.append(fecha)
        return lista_fechas

    def get_info(self):
        with open('CHECKINOUT.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                if self.dict_usuarios.get(int(row[0])) != None:
                    self.dict_usuarios.get(int(row[0])).ingresarMarcacion(row[1])

        print(datetime.datetime.now() - past)
        trabajadores = list()

        for i in self.dict_usuarios:
            trabajadores.append(self.dict_usuarios[i])
            self.dict_usuarios[i].contarMinutos(fecha_ini=self.fecha_ini, mostrar=False)

        lista_fechas = self.get_lista_fechas()

        print(datetime.datetime.now() - past)

        for i in trabajadores:
            self.dict_fechas[str(i.nombre)] = []
            for fecha in lista_fechas:
                this_fecha = i.get_marcacion_fecha(fecha)
                this_fecha = this_fecha if this_fecha is not None else "0"
                self.dict_fechas[str(i.nombre)].append(this_fecha)

        return self.dict_fechas

    def imprimirInfo(self):
        for i in self.dict_fechas:
            print(i)
            print(self.dict_fechas[i])

    def exportar(self, nombre="export"):
        with open( nombre + '.csv', 'r') as csvfile:
            csvfile.write()




ae = Asistencia("2017-10-01", "2017-10-30")

past = datetime.datetime.now()
ae.get_info()

for i in ae.dict_usuarios:

    ae.dict_usuarios.get(i).contarMinutos(fecha_ini="2017-08-01",fecha_fin="2017-10-31", mostrar=False)
    print(ae.dict_usuarios.get(i))
    #ae.dict_usuarios.get(i).contarMinutos(fecha_ini="2017-08-01", fecha_fin="2017-10-31", mostrar=True)

print(datetime.datetime.now() - past)