#Proyecto 01 Manuel Casasola Luis Diego 

import tkinter
import random
import time

def clue():

    #Se crean las listas con todas las cartas
    sospechosos = ["mejor_amigo", "novia", "vecina", "mensajero", "extraño", "hermanastro", "colega"]
    armas = ["pistola", "cuchillo", "machete", "pala", "bate", "botella", "tubo", "cuerda"]
    motivos = ["venganza", "celos", "dinero", "accidente", "drogas", "robo"]
    partes_cuerpo = ["cabeza", "pecho", "abdomen", "espalda", "piernas", "brazos"]
    lugares = ["sala", "comedor", "baño", "terraza", "cuarto", "garage", "patio", "balcon", "cocina"]

    print("===========================================")
    print()
    print("Sospechosos: ", sospechosos)
    print("Armas: ", armas)
    print("Motivos: ", motivos)
    print("Partes del cuerpo: ", partes_cuerpo)
    print("Lugares: ", lugares)
    print()
    print("===========================================")

    #se calcula el largo de las listas
    largo_sospechosos = len(sospechosos)
    largo_armas = len(armas)
    largo_motivos = len(motivos)
    largo_partes_cuerpo = len(partes_cuerpo)
    largo_lugares = len(lugares)


    #se genera la combinación ganadora
    combinacion_ganadora = [sospechosos[random.randint(0,largo_sospechosos-1)], armas[random.randint(0,largo_armas-1)], motivos[random.randint(0,largo_motivos-1)], partes_cuerpo[random.randint(0,largo_partes_cuerpo-1)], lugares[random.randint(0,largo_lugares-1)]]
    print()
    print("Combinación ganadora: ", combinacion_ganadora)
    print()
    print("===========================================")

    
    fuerza_bruta(sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora)
    backtracking(sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora, 1000)
    



def fuerza_bruta(lista_sospechosos, lista_armas, lista_motivos, lista_partes_cuerpo, lista_lugares, lista_combinacion_ganadora):

    sospechosos = lista_sospechosos
    armas = lista_armas
    motivos = lista_motivos
    partes_cuerpo = lista_partes_cuerpo
    lugares = lista_lugares

    combinacion_ganadora = lista_combinacion_ganadora

    largo_sospechosos = len(sospechosos)-1
    largo_armas = len(armas)-1
    largo_motivos = len(motivos)-1
    largo_partes_cuerpo = len(partes_cuerpo)-1
    largo_lugares = len(lugares)-1

    sospechosos_descartados = []
    armas_descartadas = []
    motivos_descartados = []
    partes_cuerpo_descartadas = []
    lugares_descartados = []

    print()
    print("Algoritmo de Fuerza Bruta")
    print()
    
    cantidad = 0
    while True:

        print("===========================================")

        intento_sospechosos = sospechosos[random.randint(0,largo_sospechosos)]
        intento_armas = armas[random.randint(0,largo_armas)]
        intento_motivos = motivos[random.randint(0,largo_motivos)]
        intento_partes_cuerpo = partes_cuerpo[random.randint(0,largo_partes_cuerpo)]
        intento_lugares = lugares[random.randint(0,largo_lugares)]

        intento = [intento_sospechosos, intento_armas, intento_motivos, intento_partes_cuerpo, intento_lugares]
        cantidad += 1


        print()
        print("Intento: ", intento)
        print("Combinación ganadora: ", combinacion_ganadora)
        print()

        print("Sospechosos descartados: ", sospechosos_descartados)
        print("Armas descartadas: ", armas_descartadas)
        print("Motivos descartados: ", motivos_descartados)
        print("Partes de cuerpo descartadas: ", partes_cuerpo_descartadas)
        print("Lugares descartados: ", lugares_descartados)

        print()

        

        dado = random.randint(1,5)
        #dado = 1

        while True:

            #print("Dado: ", dado)

            if((len(sospechosos_descartados) == 6) and (len(armas_descartadas) == 7) and (len(motivos_descartados) == 5) and (len(partes_cuerpo_descartadas) == 5) and (len(lugares_descartados) == 8)):
                print()
                print("He resuelto el problema (descarte). La combinación ganadora es: ", combinacion_ganadora)
                print("La cantidad de intentos ha sido: ", cantidad)
                #time.sleep(200)
                return print()

            if(intento == combinacion_ganadora):
                print()
                print("He resuelto el problema. La combinación ganadora es: ", combinacion_ganadora)
                print("La cantidad de intentos ha sido: ", cantidad)
                #time.sleep(200)
                return print()

            if(dado == 1):

                if(intento_sospechosos != combinacion_ganadora[0]):


                    i = 0
                    while i <= largo_sospechosos:

                        if(intento_sospechosos == sospechosos[i]):
                            sospechosos = sospechosos[:i] + sospechosos[i+1:]
                            largo_sospechosos = len(sospechosos)-1
                            sospechosos_descartados = sospechosos_descartados + [intento_sospechosos]
                            print("Carta descartada: ", intento_sospechosos)
                            break
                        else:
                            i += 1
                            continue
                    break

                elif(intento_sospechosos == combinacion_ganadora[0]):
                    dado = random.randint(1,5)
                    continue


            if(dado == 2):

                if(intento_armas != combinacion_ganadora[1]):

                    i = 0
                    while i <= largo_armas:

                        if(intento_armas == armas[i]):
                            armas = armas[:i]+ armas[i+1:]
                            largo_armas = len(armas)-1
                            armas_descartadas = armas_descartadas + [intento_armas]
                            print("Carta descartada: ", intento_armas)
                            break
                        else:
                            i += 1
                            continue
                    break

                elif(intento_armas == combinacion_ganadora[1]):
                    dado = random.randint(1,5)
                    continue

            if(dado == 3):

                if(intento_motivos != combinacion_ganadora[2]):

                    i = 0
                    while i <= largo_motivos:

                        if(intento_motivos == motivos[i]):
                            motivos = motivos[:i] + motivos[i+1:]
                            largo_motivos = len(motivos)-1
                            motivos_descartados = motivos_descartados + [intento_motivos]
                            print("Carta descartada: ", intento_motivos)
                            break
                        else:
                            i += 1
                            continue
                    break

                elif(intento_motivos == combinacion_ganadora[2]):
                    dado = random.randint(1,5)
                    continue

            if(dado == 4):

                if(intento_partes_cuerpo != combinacion_ganadora[3]):

                    i = 0
                    while i <= largo_partes_cuerpo:
                        
                        if(intento_partes_cuerpo == partes_cuerpo[i]):
                            partes_cuerpo = partes_cuerpo[:i] + partes_cuerpo[i+1:]
                            largo_partes_cuerpo = len(partes_cuerpo)-1
                            partes_cuerpo_descartadas = partes_cuerpo_descartadas + [intento_partes_cuerpo]
                            print("Carta descartada: ", intento_partes_cuerpo)
                            break
                        else:
                            i += 1
                            continue
                    break
                elif(intento_partes_cuerpo == combinacion_ganadora[3]):
                    dado = random.randint(1,5)
                    continue

            
            if(dado == 5):

                if(intento_lugares != combinacion_ganadora[4]):

                    i = 0
                    while i <= largo_lugares:

                        if(intento_lugares == lugares[i]):
                            lugares = lugares[:i] + lugares[i+1:]
                            largo_lugares = len(lugares)-1
                            lugares_descartados = lugares_descartados + [intento_lugares]
                            print("Carta descartada: ", intento_lugares)
                            break
                        else:
                            i += 1
                            continue
                    break
                elif(intento_lugares == combinacion_ganadora[4]):
                    dado = random.randint(1,5)
                    continue

            else:
                print("No debería entra aquí!!!")

def backtracking(lista_sospechosos, lista_armas, lista_motivos, lista_partes_cuerpo, lista_lugares, lista_combinacion_ganadora, cantidad_restricciones):

    sospechosos = lista_sospechosos
    armas = lista_armas
    motivos = lista_motivos
    partes_cuerpo = lista_partes_cuerpo
    lugares = lista_lugares

    combinacion_ganadora = lista_combinacion_ganadora

    largo_sospechosos = len(sospechosos)-1
    largo_armas = len(armas)-1
    largo_motivos = len(motivos)-1
    largo_partes_cuerpo = len(partes_cuerpo)-1
    largo_lugares = len(lugares)-1

    descartes = []

    cant_restricciones = cantidad_restricciones
    intentos_inteligentes = []

    cantidad = 0
    cantidad_intentos = 0

    print("===========================================")
    print()
    print("Algoritmo de Backtracking")
    print()
    print("===========================================")

    #creación de las listas SIN la combinación ganadora (restantes)
    sospechosos_restantes = []
    armas_restantes = []
    motivos_restantes = []
    partes_cuerpo_restantes = []
    lugares_restantes = []

    #sospechosos restantes
    i = 0 #contador
    while i <= largo_sospechosos:

        if(sospechosos[i] == combinacion_ganadora[0]):
            i += 1

        else:
            sospechosos_restantes = sospechosos_restantes + [sospechosos[i]]
            i += 1

    #armas restantes
    i = 0 #contador
    while i <= largo_armas:

        if(armas[i] == combinacion_ganadora[1]):
            i += 1

        else: 
            armas_restantes = armas_restantes + [armas[i]]
            i += 1
    
    #motivos restantes
    i = 0 #contador
    while i <= largo_motivos:

        if(motivos[i] == combinacion_ganadora[2]):
            i += 1

        else: 
            motivos_restantes = motivos_restantes + [motivos[i]]
            i += 1
    
    #partes de cuerpo restantes
    i = 0 #contador
    while i <= largo_partes_cuerpo:

        if(partes_cuerpo[i] == combinacion_ganadora[3]):
            i += 1

        else: 
            partes_cuerpo_restantes = partes_cuerpo_restantes + [partes_cuerpo[i]]
            i += 1

    #lugares restantes
    i = 0 #contador
    while i <= largo_lugares:

        if(lugares[i] == combinacion_ganadora[4]):
            i += 1

        else: 
            lugares_restantes = lugares_restantes + [lugares[i]]
            i += 1

    
    print()
    print("Sospechosos restantes: ", sospechosos_restantes)
    print("Armas restantes: ", armas_restantes)
    print("Motivos restantes: ", motivos_restantes)
    print("Partes del cuerpo restantes: ", partes_cuerpo_restantes)
    print("Lugares restantes: ", lugares_restantes)
    print()

    print()
    print("Combinación ganadora: ", combinacion_ganadora)
    print()

    print("===========================================")

    #Creación de restricciones 
    i = 0

    restricciones = []

    cantidad_act = 0
    while i < cant_restricciones:

        while True:
            categoria_1 = random.randint(1,5)

            if(categoria_1 == 1):
                carta_seleccionada = random.randint(0,5)
                carta_1 = sospechosos_restantes[carta_seleccionada]
                break

            elif(categoria_1 == 2):
                carta_seleccionada = random.randint(0,6)
                carta_1 = armas_restantes[carta_seleccionada]
                break

            elif(categoria_1 == 3):
                carta_seleccionada = random.randint(0,4)
                carta_1 = motivos_restantes[carta_seleccionada]
                break

            elif(categoria_1 == 4):
                carta_seleccionada = random.randint(0,4)
                carta_1 = partes_cuerpo_restantes[carta_seleccionada]
                break

            elif(categoria_1 == 5):
                carta_seleccionada = random.randint(0,7)
                carta_1 = lugares_restantes[carta_seleccionada]
                break
            else: 
                print("No debería entrar a aquí")

        while True:
            categoria_2 = random.randint(1,5)

            if(categoria_2 == 1):
                carta_seleccionada = random.randint(0,5)
                carta_2 = sospechosos_restantes[carta_seleccionada]
                break

            elif(categoria_2 == 2):
                carta_seleccionada = random.randint(0,6)
                carta_2 = armas_restantes[carta_seleccionada]
                break

            elif(categoria_2 == 3):
                carta_seleccionada = random.randint(0,4)
                carta_2 = motivos_restantes[carta_seleccionada]
                break

            elif(categoria_2 == 4):
                carta_seleccionada = random.randint(0,4)
                carta_2 = partes_cuerpo_restantes[carta_seleccionada]
                break

            elif(categoria_2 == 5):
                carta_seleccionada = random.randint(0,7)
                carta_2 = lugares_restantes[carta_seleccionada]
                break
            else: 
                print("No debería entrar a aquí")
        

        if(categoria_1 == categoria_2):
            continue

        if(carta_1 == carta_2):
            continue
        
        restriccion_act = [carta_1, carta_2]
        flag = True
        for x in range(0,len(restricciones)):
            if(restriccion_act == restricciones[x]):
                flag = False
                cantidad_act += 1
                break

        if(cantidad_act == 1000000):
            print("Ya no se pueden hacer más restricciones: ")
            break

        if(flag == False):
            continue

        restricciones = restricciones + [restriccion_act]

        i += 1

    print()
    print("Restricciones: ", restricciones)
    print()

    while True:

        intento_sospechosos = sospechosos[random.randint(0,largo_sospechosos)]
        intento_armas = armas[random.randint(0,largo_armas)]
        intento_motivos = motivos[random.randint(0,largo_motivos)]
        intento_partes_cuerpo = partes_cuerpo[random.randint(0,largo_partes_cuerpo)]
        intento_lugares = lugares[random.randint(0,largo_lugares)]


        intento = [intento_sospechosos, intento_armas, intento_motivos, intento_partes_cuerpo, intento_lugares]

        i = 0
        flag = True
        while i < len(restricciones):

            restriccion_actual = restricciones[i]

            carta_1 = restricciones[i][0]
            carta_2 = restricciones[i][1]

            m = 0

            while m < 4:

                if(carta_1 == intento[m]):
                    
                    n = 0
                    while n < 4:

                        if(carta_2 == intento[n]):
                            flag = False
                            break
                        
                        n += 1
                    break
                    
                
                m += 1
            
            if(flag == False):
                break

            i += 1

        if(flag == False):
            continue
        
        if(flag == True):
            break
    
    backtracking_aux(lista_sospechosos, lista_armas, lista_motivos, lista_partes_cuerpo, lista_lugares, lista_combinacion_ganadora, restricciones, intentos_inteligentes, descartes, cantidad_intentos, intento)

def backtracking_aux(lista_sospechosos, lista_armas, lista_motivos, lista_partes_cuerpo, lista_lugares, lista_combinacion_ganadoras, restricciones, intentos_inteligentes, lista_descartes, cantidad_intentos, intento):

    print("===========================================")

    combinacion_ganadora = lista_combinacion_ganadoras
    descartes = lista_descartes
    sospechosos = lista_sospechosos
    armas = lista_armas
    motivos = lista_motivos
    partes_cuerpo = lista_partes_cuerpo
    lugares = lista_lugares

    largo_sospechosos = len(lista_sospechosos)-1
    largo_armas = len(lista_armas)-1
    largo_motivos = len(lista_motivos)-1
    largo_partes_cuerpo = len(lista_partes_cuerpo)-1
    largo_lugares = len(lista_lugares)-1

    cantidad = cantidad_intentos

    intento = intento

    cantidad += 1

    print()
    print("Intento: ", intento)
    intentos_inteligentes = intentos_inteligentes + [intento]
    print("Combinación ganadora: ", combinacion_ganadora)
    print()

    """
    print("Sospechosos descartados: ", sospechosos_descartados)
    print("Armas descartadas: ", armas_descartadas)
    print("Motivos descartados: ", motivos_descartados)
    print("Partes de cuerpo descartadas: ", partes_cuerpo_descartadas)
    print("Lugares descartados: ", lugares_descartados)
    """
    print()

    

    dado = random.randint(1,5)
    #dado = 1

    

    #print("Dado: ", dado)
    """
    if((len(sospechosos_descartados) == 6) and (len(armas_descartadas) == 7) and (len(motivos_descartados) == 5) and (len(partes_cuerpo_descartadas) == 5) and (len(lugares_descartados) == 8)):
        print()
        print("He resuelto el problema (descarte). La combinación ganadora es: ", combinacion_ganadora)
        print("Intentos hechos: ")
        for x in range(0,len(intentos_inteligentes)):

            print(intentos_inteligentes[x])


        print("Restricciones: ", restricciones)
        print()
        print("La cantidad de intentos ha sido: ", cantidad)
        #time.sleep(200)
        return print()
    """

    if(intento == combinacion_ganadora):
        print()
        print("He resuelto el problema. La combinación ganadora es: ", combinacion_ganadora) 
        print("Intentos hechos: ")
        for x in range(0,len(intentos_inteligentes)):

            print(intentos_inteligentes[x])


        print("Restricciones: ", restricciones)
        print()
        print("La cantidad de intentos ha sido: ", cantidad)
        print("La cantidad de restricciones ha sido: ", len(restricciones))
        print()
        print("Cartas descartadas: ", descartes)
        #time.sleep(200)
        return print()

    while True:

        #print("Dado 2.0: ", dado)
        if(dado == 1):

            if(intento[0] != combinacion_ganadora[0]):


                i = 0
                while i <= largo_sospechosos:

                    if(intento[0] == sospechosos[i]):
                        sospechosos = sospechosos[:i] + sospechosos[i+1:]
                        largo_sospechosos = len(sospechosos)-1
                        descartes = descartes + [intento[0]]
                        print("Carta descartada: ", intento[0])

                        contador_max = 0
                        while True:
                            contador_max += 1
                            cambio = sospechosos[random.randint(0,largo_sospechosos)]
                            intento = [cambio, intento[1], intento[2], intento[3], intento[4]]
                            i = 0
                            flag = True
                            while i < len(restricciones):

                                restriccion_actual = restricciones[i]

                                carta_1 = restricciones[i][0]
                                carta_2 = restricciones[i][1]

                                m = 0

                                while m < 4:

                                    if(carta_1 == intento[m]):
                                        
                                        n = 0
                                        while n < 4:

                                            if(carta_2 == intento[n]):
                                                flag = False
                                                break
                                            
                                            n += 1
                                        break
                                        
                                    
                                    m += 1
                                
                                if(flag == False):
                                    break

                                i += 1

                            if(flag == False):
                                if(contador_max == 10000):
                                    dado(dado = random.randint(1,5))
                                    break
                                continue
                            
                            if(flag == True):
                                backtracking_aux(sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora, restricciones, intentos_inteligentes, descartes, cantidad, intento)
                                x = False
                                break

                        if(x == False):
                            break
                        
                    else:
                        i += 1
                        continue

                if(x == False):
                     break   

                continue
                

            elif(intento[0] == combinacion_ganadora[0]):
                dado = random.randint(1,5)
                continue


        if(dado == 2):

            if(intento[1] != combinacion_ganadora[1]):


                i = 0
                while i <= largo_armas:

                    if(intento[1] == armas[i]):
                        armas = armas[:i] + armas[i+1:]
                        largo_armas = len(armas)-1
                        descartes = descartes + [intento[1]]
                        print("Carta descartada: ", intento[1])

                        contador_max = 0
                        while True:
                            contador_max += 1
                            cambio = armas[random.randint(0,largo_armas)]
                            intento = [intento[0], cambio, intento[2], intento[3], intento[4]]
                            i = 0
                            flag = True
                            while i < len(restricciones):

                                restriccion_actual = restricciones[i]

                                carta_1 = restricciones[i][0]
                                carta_2 = restricciones[i][1]

                                m = 0

                                while m < 4:

                                    if(carta_1 == intento[m]):
                                        
                                        n = 0
                                        while n < 4:

                                            if(carta_2 == intento[n]):
                                                flag = False
                                                break
                                            
                                            n += 1
                                        break
                                        
                                    
                                    m += 1
                                
                                if(flag == False):
                                    break

                                i += 1

                            if(flag == False):
                                if(contador_max == 10000):
                                    dado(dado = random.randint(1,5))
                                    break
                                continue
                            
                            if(flag == True):
                                backtracking_aux(sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora, restricciones, intentos_inteligentes, descartes, cantidad, intento)
                                x = False
                                break

                        if(x == False):
                            break

                    else:
                        i += 1
                        continue
                    
                if(x == False):
                     break   

                continue
                

            elif(intento[1] == combinacion_ganadora[1]):
                dado = random.randint(1,5)
                continue

        if(dado == 3):

            if(intento[2] != combinacion_ganadora[2]):


                i = 0
                while i <= largo_motivos:

                    if(intento[2] == motivos[i]):
                        motivos = motivos[:i] + motivos[i+1:]
                        largo_motivos = len(motivos)-1
                        descartes = descartes + [intento[2]]
                        print("Carta descartada: ", intento[2])

                        contador_max = 0
                        while True:
                            contador_max += 1
                            cambio = motivos[random.randint(0,largo_motivos)]
                            intento = [intento[0], intento[1], cambio, intento[3], intento[4]]
                            i = 0
                            flag = True
                            while i < len(restricciones):

                                restriccion_actual = restricciones[i]

                                carta_1 = restricciones[i][0]
                                carta_2 = restricciones[i][1]

                                m = 0

                                while m < 4:

                                    if(carta_1 == intento[m]):
                                        
                                        n = 0
                                        while n < 4:

                                            if(carta_2 == intento[n]):
                                                flag = False
                                                break
                                            
                                            n += 1
                                        break
                                        
                                    
                                    m += 1
                                
                                if(flag == False):
                                    break

                                i += 1

                            if(flag == False):
                                if(contador_max == 10000):
                                    dado(dado = random.randint(1,5))
                                    break
                                continue
                            
                            if(flag == True):
                                backtracking_aux(sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora, restricciones, intentos_inteligentes, descartes, cantidad, intento)
                                x = False
                                break
                        if(x == False):
                            break

                    else:
                        i += 1
                        continue
                    
                if(x == False):
                     break   

                continue
                

            elif(intento[2] == combinacion_ganadora[2]):
                dado = random.randint(1,5)
                continue

        if(dado == 4):

            if(intento[3] != combinacion_ganadora[3]):

                i = 0
                while i <= largo_partes_cuerpo:

                    if(intento[3] == partes_cuerpo[i]):
                        partes_cuerpo = partes_cuerpo[:i] + partes_cuerpo[i+1:]
                        largo_partes_cuerpo = len(partes_cuerpo)-1
                        descartes = descartes + [intento[3]]
                        print("Carta descartada: ", intento[3])

                        contador_max = 0
                        while True:
                            contador_max += 1
                            cambio = partes_cuerpo[random.randint(0,largo_partes_cuerpo)]
                            intento = [intento[0], intento[1], intento[2], cambio, intento[4]]
                            i = 0
                            flag = True
                            while i < len(restricciones):

                                restriccion_actual = restricciones[i]

                                carta_1 = restricciones[i][0]
                                carta_2 = restricciones[i][1]

                                m = 0

                                while m < 4:

                                    if(carta_1 == intento[m]):
                                        
                                        n = 0
                                        while n < 4:

                                            if(carta_2 == intento[n]):
                                                flag = False
                                                break
                                            
                                            n += 1
                                        break
                                        
                                    
                                    m += 1
                                
                                if(flag == False):
                                    break

                                i += 1

                            if(flag == False):
                                if(contador_max == 10000):
                                    dado(dado = random.randint(1,5))
                                    break
                                continue
                            
                            if(flag == True):
                                backtracking_aux(sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora, restricciones, intentos_inteligentes, descartes, cantidad, intento)
                                x = False
                                break

                        if(x == False):
                            break

                    else:
                        i += 1
                        continue
                    
                if(x == False):
                     break   

                continue
                

            elif(intento[3] == combinacion_ganadora[3]):
                dado = random.randint(1,5)
                continue

        
        if(dado == 5):

            if(intento[4] != combinacion_ganadora[4]):

                i = 0
                while i <= largo_lugares:

                    if(intento[4] == lugares[i]):
                        lugares = lugares[:i] + lugares[i+1:]
                        largo_lugares = len(lugares)-1
                        descartes = descartes + [intento[4]]
                        print("Carta descartada: ", intento[4])

                        contador_max = 0
                        while True:
                            contador_max += 1
                            cambio = lugares[random.randint(0,largo_lugares)]
                            intento = [intento[0], intento[1], intento[2], intento[3], cambio]
                            i = 0
                            flag = True
                            while i < len(restricciones):

                                restriccion_actual = restricciones[i]

                                carta_1 = restricciones[i][0]
                                carta_2 = restricciones[i][1]

                                m = 0

                                while m < 4:

                                    if(carta_1 == intento[m]):
                                        
                                        n = 0
                                        while n < 4:

                                            if(carta_2 == intento[n]):
                                                flag = False
                                                break
                                            
                                            n += 1
                                        break
                                        
                                    
                                    m += 1
                                
                                if(flag == False):
                                    break

                                i += 1

                            if(flag == False):
                                if(contador_max == 10000):
                                    dado(dado = random.randint(1,5))
                                    break
                                continue
                            
                            if(flag == True):
                                backtracking_aux(sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora, restricciones, intentos_inteligentes, descartes, cantidad, intento)
                                x = False
                                break

                        if(x == False):
                            break

                    else:
                        i += 1
                        continue
                    
                if(x == False):
                     break   

                continue
                

            elif(intento[4] == combinacion_ganadora[4]):
                dado = random.randint(1,5)
                continue

        else:
            print("No debería entra aquí!!!")
    


clue()