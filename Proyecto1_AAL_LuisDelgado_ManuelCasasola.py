from tkinter import *
from tkinter import messagebox
import random
import time

global sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora, intentos_fuerza, intentos_back, descartados_fuer, descartados_back
 
#Se crean las listas con todas las cartas
sospechosos = ["Mejor Amigo", "Novia", "Vecina", "Mensajero", "Extraño", "Hermanastro", "Colega"]
armas = ["Pistola", "Cuchillo", "Machete", "Pala", "Bate", "Botella", "Tubo", "Cuerda"]
motivos = ["Venganza", "Celos", "Dinero", "Accidente", "Drogas", "Robo"]
partes_cuerpo = ["Cabeza", "Pecho", "Abdomen", "Espalda", "Piernas", "Brazos"]
lugares = ["Sala", "Comedor", "Baño", "Terraza", "Cuarto", "Garage", "Patio", "Balcon", "Cocina"]
intentos_fuerza = []
intentos_back = []
descartados_fuer = []
descartados_back = []

#se calcula el largo de las listas
largo_sospechosos = len(sospechosos)
largo_armas = len(armas)
largo_motivos = len(motivos)
largo_partes_cuerpo = len(partes_cuerpo)
largo_lugares = len(lugares)


#se genera la combinación ganadora
combinacion_ganadora = [sospechosos[random.randint(0,largo_sospechosos-1)], armas[random.randint(0,largo_armas-1)], motivos[random.randint(0,largo_motivos-1)], partes_cuerpo[random.randint(0,largo_partes_cuerpo-1)], lugares[random.randint(0,largo_lugares-1)]]

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
    

    while True:

        print("===========================================")

        intento_sospechosos = sospechosos[random.randint(0,largo_sospechosos)]
        intento_armas = armas[random.randint(0,largo_armas)]
        intento_motivos = motivos[random.randint(0,largo_motivos)]
        intento_partes_cuerpo = partes_cuerpo[random.randint(0,largo_partes_cuerpo)]
        intento_lugares = lugares[random.randint(0,largo_lugares)]

        intento = [intento_sospechosos, intento_armas, intento_motivos, intento_partes_cuerpo, intento_lugares]

        intentos_fuerza.append(intento)

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
                #time.sleep(200)
                return print()

            if(intento == combinacion_ganadora):
                print()
                print("He resuelto el problema. La combinación ganadora es: ", combinacion_ganadora)
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
                            descartados_fuer.append(intento_sospechosos)
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
                            descartados_fuer.append(intento_armas)
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
                            descartados_fuer.append(intento_motivos)
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
                            descartados_fuer.append(intento_partes_cuerpo)
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
                            descartados_fuer.append(intento_lugares)
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

fuerza_bruta(sospechosos, armas, motivos, partes_cuerpo, lugares, combinacion_ganadora)

#Funcion para los botones de siguiente solucion -----------------------------------------------------

def siguiente_solucion(lis_intentos, lis_botones, bot_sig, lis_descartados, listbox):
    
    intento = lis_intentos[0]
    lis_botones[0].config(text= intento[0])
    lis_botones[1].config(text= intento[1])
    lis_botones[2].config(text= intento[2])
    lis_botones[3].config(text= intento[3])
    lis_botones[4].config(text= intento[4])
    listbox.insert(END, lis_descartados[0])

    lis_descartados.remove(lis_descartados[0])
    lis_intentos.remove(intento)

    if lis_intentos == []:
        bot_sig.config(state= DISABLED)
        

    return

#Ventana Pricipal-----------------------------------------------------------------------------------

def ven_prin(): # ventana principal
    #Ventana principal

    ven = Tk()
    ven.title("Crime Investigation - El Juego")
    ven.iconbitmap('lupa.ico')
    ven.geometry('1000x720+250+35')
    ven.resizable(width= False, height= False)

    titu = Label(ven, text= "Crime Investigation - El Juego", bg= "sienna3", fg= "white", font=("Times", 18), padx= 40)
    titu.place(x= 315, y= 20)

    #Cartas de la solucion------------------------------------------------------------------------------------------------------------
    solu_tex = Label(ven, text= "Cartas de la Solución", fg= "sienna3", font=("Times", 16))
    solu_tex.place(x= 412, y= 80)
    
    sos_gan = Button(ven, text= combinacion_ganadora[0], bg= "sienna3", fg= "white", font= ("Helvetica", 12), pady= 50, width= 10)
    arm_gan = Button(ven, text= combinacion_ganadora[1], bg= "sienna3", fg= "white", font= ("Helvetica", 12), pady= 50, width= 10)
    mot_gan = Button(ven, text= combinacion_ganadora[2], bg= "sienna3", fg= "white", font= ("Helvetica", 12), pady= 50, width= 10)
    par_gan = Button(ven, text= combinacion_ganadora[3], bg= "sienna3", fg= "white", font= ("Helvetica", 12), pady= 50, width= 10)
    lug_gan = Button(ven, text= combinacion_ganadora[4], bg= "sienna3", fg= "white", font= ("Helvetica", 12), pady= 50, width= 10)

    sos_gan.place(x= 200, y= 120)
    arm_gan.place(x= 325, y= 120)
    mot_gan.place(x= 450, y= 120)
    par_gan.place(x= 575, y= 120)
    lug_gan.place(x= 700, y= 120)

    #Cartas de los Algoritmos---------------------------------------------------------------------------------------------------------

    #Texto y Botones del algoritmo de fuerza bruta------------------------------------------------------------------------------------
    fuerza_tex = Label(ven, text= "Algoritmo de Fuerza Bruta", fg= "sienna3", font=("Times", 14))
    fuerza_tex.place(x= 400, y= 290)

    sos_fuer = Button(ven, text= intentos_fuerza[0][0], bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)
    arm_fuer = Button(ven, text= intentos_fuerza[0][1], bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)
    mot_fuer = Button(ven, text= intentos_fuerza[0][2], bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)
    par_fuer = Button(ven, text= intentos_fuerza[0][3], bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)
    lug_fuer = Button(ven, text= intentos_fuerza[0][4], bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)

    intentos_fuerza.remove(intentos_fuerza[0])

    sos_fuer.place(x= 210, y= 330)
    arm_fuer.place(x= 330, y= 330)
    mot_fuer.place(x= 455, y= 330)
    par_fuer.place(x= 580, y= 330)
    lug_fuer.place(x= 705, y= 330)

    #lista donde se mostraran las cartas que se van descartando

    desc_fuer = Label(ven, text= "Cartas Descartadas", fg= "sienna3", font=("Times", 11))
    desc_fuer.place(x= 42, y= 300)
    listbox_fuer = Listbox(ven, width= 14, height= 8, font = ("Helvetica",11))
    listbox_fuer.place(x= 45, y= 320)

    lis_bot_fuer = [sos_fuer, arm_fuer, mot_fuer, par_fuer, lug_fuer] #lista de los botones de las cartas de fuerza bruta

    #Texto y botones del algoritmo de backtracking------------------------------------------------------------------------------------
    backtra_tex = Label(ven, text= "Algoritmo de Backtracking", fg= "sienna3", font=("Times", 14))
    backtra_tex.place(x= 400, y= 500)

    sos_back = Button(ven, text= "Backtracking", bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)
    arm_back = Button(ven, text= "Backtracking", bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)
    mot_back = Button(ven, text= "Backtracking", bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)
    par_back = Button(ven, text= "Backtracking", bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)
    lug_back = Button(ven, text= "Backtracking", bg= "sienna3", fg= "white", font= ("Helvetica", 10), pady= 45, width= 10)

    sos_back.place(x= 210, y= 540)
    arm_back.place(x= 330, y= 540)
    mot_back.place(x= 455, y= 540)
    par_back.place(x= 580, y= 540)
    lug_back.place(x= 705, y= 540)

    lis_bot_back = [sos_back, arm_back, mot_back, par_back, lug_back] #lista de los botones de las cartas de backtracking

    #Botones de siguiente solución-----------------------------------------------------------------------------------------------------
    sig_fuer = Button(ven, text= "Siguiente Solucion", bg= "white", fg= "sienna3", font= ("Helvetica", 10), pady= 5, width= 15, relief= GROOVE, command= lambda: siguiente_solucion(intentos_fuerza, lis_bot_fuer, sig_fuer, descartados_fuer, listbox_fuer))
    sig_back = Button(ven, text= "Siguiente Solución", bg= "white", fg= "sienna3", font= ("Helvetica", 10), pady= 5, width= 15, relief= GROOVE)

    sig_fuer.place(x=830 ,y=375)
    sig_back.place(x=830 ,y=585)

    
    
    ven.mainloop()

ven_prin()