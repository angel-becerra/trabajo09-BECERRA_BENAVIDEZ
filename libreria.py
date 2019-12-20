#ejercisio01
def calor(masa,temperatura,calor_especifio):
    calor=(masa*temperatura*calor_especifio)
    return calor
#fin calor


#ejercisio02
def volumen(lado01,lado02,lado03):
    volumen=(lado01*lado02*lado03)
    return volumen
#fin_volumen

#ejercisio03
def promedio(nota01,nota02,nota03):
    if promedio != 10:
        return "aprobado"
    else:
        return "desaprobado"
#fin_promedio


#ejercisio04
def cantidad_total(nro_producto1,nro_producto2,nro_producto3):
    cantidad_total=(nro_producto1+nro_producto2+nro_producto3)
    return cantidad_total

#fin_cantidad_total


#ejercisio05
def nombre_completo(nombre,primer_apellido,segundo_apellido):
    nombre_completo=(nombre+" " +primer_apellido +" "+segundo_apellido)
    return nombre_completo
#fin_nombre_completo



#ejercisio06
def mayor(x,y):
    if (x < y):
        return x
    if (y < x):
        return y


#fin_menor


#ejercisio07
def mayor(a,b):
    if (a > b):
        return a
    if (b > a):
        return b


#fin_mayor


#ejercisio08
def m(JUAN,ANGEL):
    if (JUAN < ANGEL):
        return JUAN
    if ( JUAN < ANGEL):

        return ANGEL
#fin_mayor

#ejercisio09
def total_de_postulantes(ingenierias,biomedicas,letras):
    total_de_postulantes=(ingenierias+biomedicas+letras)
    return total_de_postulantes
#fin_total_de_postulantes

#ejercisio10
def nota_final(nota_de_trabajos,nota_de_examenes,nota_de_exposiciones):
    if nota_final != 10:
        return "paso de año"
    else:
        return "reprobado"
#fin_nota_final

#jercisio11
def empuje(densidad_del_liquido,volumen_sumergido,gravedad):
    empuje=(densidad_del_liquido*volumen_sumergido*gravedad)
    return empuje
#fin_empuje


#ejercisio12
def voltaje(intensidad_electrica,resistencia_electronica):
    voltaje=(intensidad_electrica*resistencia_electronica)
    return voltaje
#fin_voltaje


#ejercisio13
def fuerza(masa,aceleracion):
    fuerza=(masa*aceleracion)

    return fuerza
#fin_fuerza


#ejercisio14
def longitud_de_arco(angulo_en_sexagesimales,radio):
    longitud_de_arco=(angulo_en_sexagesimales*radio)
    return longitud_de_arco
#fin_longitud_de_arco

#ejercisio15
def total_ingresos(costo_por_examen,total_de_postulantes):
    total_ingresos=(costo_por_examen*total_de_postulantes)
    return total_ingresos
#fin_total_ingresos

#ejercisio16
def datos_personales(nombre,edad,dni):
    datos_personales=( nombre+" "+  "tiene"+"  "  + str(edad)+   "y su dni es" +" "  +str(dni))
    return datos_personales
#fin_datos_personales

#ejercisio17
def menor(angel,santiago):
    if (angel > santiago):
        return angel
    else:
        return santiago
#fin_menor

#ejercisio18
def area_rectangulo(base,altura):
    area_rectangulo=(base*altura)
    return area_rectangulo
#fin_area_rectangulo


#ejercisio19
def gasto_total(gasto_por_habitante,numero_de_habitantes,alquiler_de_vivienda):
    gasto_total=(gasto_por_habitante*numero_de_habitantes+alquiler_de_vivienda)
    return gasto_total
#fin_gasto_total

#ejercisio20
def energia_cinetica(masa,gravedad,haltura):
    energia_cinetica=(masa*gravedad*haltura)
    return energia_cinetica
#fin_energia_cinetica

#ejercisio21
def mayor(tatiana,roberto):
    if (tatiana > roberto):
        return  tatiana
    else:
        return roberto
#fin_mayor

#ejercisio22
def gasto_de_estudiante(pasajes,comida,vivienda):
    gasto_de_estudiante=(pasajes*comida*vivienda)
    return gasto_de_estudiante
#fin_gasto_de_estudiante

#ejercisio23
def numero_dni(numero):
    numero_invalido= (len(numero) !=8 or numero.isdigit() == False)
    while (numero_invalido == True):
        numero = input("ingrese numero de dn1 valido:")
        numero_invalido = (len(numero) !=8 or numero.isdigit() == False)
    return (numero)
#fin_numero_dni



#ejercisio24
def numero_telefono(numero):
    numero_invalido= (len(numero) !=9 or numero.isdigit() == False)
    while (numero_invalido == True):
        numero = input("ingrese numero de telefono valido:")
        numero_invalido = (len(numero) !=9 or numero.isdigit() == False)
    return (numero)
#fin_numero_dni

#ejercisio25
def resta_positiva(a,b):
    if(a>b):
     return (a-b)
    if(b>a):
     return (b-a)
#fin_resta_positiva



















