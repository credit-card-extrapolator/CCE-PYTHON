'''
CCE(Credit Card Extrapolator) codigo pyhon

Requisitos:

- Python 3 en adelante.
- La libreria de tkinter que ya viene por defecto.
- Importar os sys si no los tienes instalalos.

Version 1.0.
Fecha de creacion: 19/06/2020
Fecha de publicacion en el repositorio GitHub: 27/11/2020
Autor: Anderson H.
Telegram: @Rene010
Grupo-telegram: @sobrehacking

PD: Este codigo lo cree mientras aprendia a programar con python, 
por eso repito demasiado codigo, pero en un futuro lo mejorare. :)'''


from tkinter import *
import webbrowser as wb
import os, sys

""" Puse esto aqui porque si lo pongo debajo de las configuracion de las ventanas me da error porque
no encuentra la funcion"""

""" Esta funcion es para que al empaquetarlo con Pyinstaller busque los archivo en la carperta principal"""
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

ventana =Tk()
ventana.geometry("700x500+0+0")
ventana.resizable(0,0)
ventana.title("Credit Card Extrapolator")
ventana.configure(bg="#1d1e21")
ventana.iconbitmap(resolver_ruta("./logo.ico"))



frame2 = Frame(ventana,bg="#1d1e21")
frame2.place(y=120, width=700, height=300)

#-----------------FUNCIONES----------------

""" Esta funcion lo que hace es limpiar el frame2 para que asi salga un metodo"""
def limpiador_de_frames():
        for i in frame2.winfo_children():
            i.destroy()

""" Estas funciones son solo links al precionar el boton los lleva a estas url"""
def boton_youtube():
        wb.open_new(r"https://www.youtube.com/channel/UCfzu-cvx2iPLjc95PdbVlbw?view_as=subscriber")

def boton_telegram():
        wb.open_new(r"https://t.me/sobrehacking")

def boton_pagina():
        wb.open_new(r"https://credit-card-extrapolator.github.io/CCE/index.html")
def boton_informacion():
        wb.open_new(r"https://credit-card-extrapolator.github.io/CCE/metodos.html")


""" Esta es para limitar la cantidad de caracteres de las cajas de text en 16 digitos"""
def limitar_caracteres(c):
    if len(c) > 16:
        return False
    return True




        
    
#-----------------METODO BASICO--------------------

def abrir_basico():

#Esta funcion lo que hace es que al precionar el boton del metodo basi se ponga en SUNKEN y ponga en FLAT los demas botones.
       
    limpiador_de_frames()
    met1.config(relief=SUNKEN,background ="red3", fg="white" )
    met2.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met3.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met4.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met5.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met6.config(relief=FLAT,background ="white", fg="#1d1e21" )

#Funcion que se ejecuta al dar click en extrapolar en el metodo Basico
    def extrapolar_basico():
            c1 = caja.get()
            c2_c1 = c1[6:len(c1)]
            c3 = c1[0:6]
            for i in range(len(c2_c1)):
                    c3 += 'x'
            caja2.delete(0, END)
            caja2.insert(0, c3)

            """ Funcion para copiar lo que hay en la caja donde se imprime el resultado"""
    def copiar_al_portapapeles():
            caja2.select_range(0,len(caja2.get()))
            ventana.clipboard_clear()
            ventana.clipboard_append(caja2.get())
            
    vcmd = frame2.register(func=limitar_caracteres)
    
  
    
    #OBJETOS------------------------
    
    caja = Entry(frame2, validate="key", validatecommand=(vcmd, '%P'))
    caja2= Entry(frame2,)

    generar =Button(frame2,text="Extrapolar",command=extrapolar_basico )
    copiar = Button(frame2, text="Copiar", command=copiar_al_portapapeles)

    tex2 = Label(frame2, text="Coloca la CC")
    tex3= Label(frame2, text= "La cc debe tener 16 digitos sin puntos")
    tex4= Label(frame2, text= "Resultado")
    tex5= Label(frame2, text= "Ej_resultado: 123456xxxxxxxxx")

    
    #-----------------------CONFIGURACIONES------------------------

    caja.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f")
    caja.place(x= 235, y=27, width=200, height=26)

    caja2.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f", )
    caja2.place(x= 235, y=122,width=200, height=26)


    generar.config(fg= "white", bg="red3", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="red4",cursor="hand2", overrelief=RAISED, activeforeground="white")
    generar.place(x= 455, y=25, height=30,width=119)

    copiar.config(fg= "white", bg="red3", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="red4",cursor="hand2", overrelief=RAISED, activeforeground="white")
    copiar.place(x= 455, y=120, height=30, width=119)


    tex2.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex2.place(x= 80, y=20)
    
    tex3.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex3.place(x= 250, y=60)

    tex4.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex4.place(x= 80, y=115)

    tex5.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex5.place(x= 265, y=155)

    



#-----------------------METODO ACTIVACION --------------------------

def abrir_activacion():
    

    limpiador_de_frames()
    met1.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met2.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met3.config(relief=SUNKEN,background ="green4", fg="white" )
    met4.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met5.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met6.config(relief=FLAT,background ="white", fg="#1d1e21" )
    
    
    def extrapolar_activacion():
            c1 = caja_activacion.get()
            c2_c1 = c1[10:len(c1)]
            c3 = c1[:10]
            for i in range(len(c2_c1)):
                    c3 += 'x'
            caja_activacion2.delete(0, END)
            caja_activacion2.insert(0, c3)
    def copiar_al_portapapeles():
            caja_activacion2.select_range(0,len(caja_activacion2.get()))
            ventana.clipboard_clear()
            ventana.clipboard_append(caja_activacion2.get())

    vcmd = frame2.register(func=limitar_caracteres)
    
 

#-----------------------OBJETOS------------------------
    
    caja_activacion = Entry(frame2, validate="key", validatecommand=(vcmd, '%P'))
    caja_activacion2= Entry(frame2)

    generar_activacion =Button(frame2,text="Extrapolar",command=extrapolar_activacion )
    copiar_activacion = Button(frame2, text="Copiar", command=copiar_al_portapapeles)

    tex2_activacion= Label(frame2, text="Coloca la CC")
    tex3_activacion= Label(frame2, text= "La cc debe tener 16 digitos sin puntos")
    tex4_activacion= Label(frame2, text= "Resultado")
    tex5_activacion= Label(frame2, text= "Ej_resultado: 1234567891xxxxxx")

    
    #-----------------------CONFIGURACIONES------------------------

    caja_activacion.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f")
    caja_activacion.place(x= 235, y=27, width=200, height=26)

    caja_activacion2.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f", )
    caja_activacion2.place(x= 235, y=122,width=200, height=26)


    generar_activacion.config(fg= "white", bg="green4", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="green3",cursor="hand2", overrelief=RAISED, activeforeground="white")
    generar_activacion.place(x= 455, y=25, height=30,width=119)

    copiar_activacion.config(fg= "white", bg="green4", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="green3",cursor="hand2", overrelief=RAISED, activeforeground="white")
    copiar_activacion.place(x= 455, y=120, height=30, width=119)


    tex2_activacion.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex2_activacion.place(x= 80, y=20)
    
    tex3_activacion.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex3_activacion.place(x= 250, y=60)

    tex4_activacion.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex4_activacion.place(x= 80, y=115)

    tex5_activacion.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex5_activacion.place(x= 265, y=155)



#-----------------------METODO SIMILITUD --------------------------

def abrir_similitud():
    

    limpiador_de_frames()
    met1.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met2.config(relief=SUNKEN,background ="deepskyblue3", fg="white" )
    met3.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met4.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met5.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met6.config(relief=FLAT,background ="white", fg="#1d1e21" )
    
    def extrapolar_similitud():
            c1 = caja_similitud.get()
            c2 = caja_similitud2.get()
            temp_c1 = c1[6:len(c1)]
            temp_c2=c2[6:len(c2)]
            c3 = c1[0:6]
            for i in range(len(temp_c1)):
                if temp_c1[i] == temp_c2[i]:
                    c3 += temp_c1[i]
                else:
                    c3 += 'x'
            caja_similitud3.delete(0, END)
            caja_similitud3.insert(0, c3)

    def copiar_al_portapapeles():
            caja_similitud3.select_range(0,len(caja_similitud3.get()))
            ventana.clipboard_clear()
            ventana.clipboard_append(caja_similitud3.get())
            
    vcmd = frame2.register(func=limitar_caracteres)
    
    


 

#-----------------------OBJETOS------------------------
    
    caja_similitud = Entry(frame2, validate="key", validatecommand=(vcmd, '%P'))
    caja_similitud2= Entry(frame2, validate="key", validatecommand=(vcmd, '%P'))
    caja_similitud3= Entry(frame2)

    generar_similitud =Button(frame2,text="Extrapolar",command=extrapolar_similitud )
    copiar_similitud = Button(frame2, text="Copiar", command=copiar_al_portapapeles)

    tex2_similitud= Label(frame2, text="Coloca  la  CC1")
    tex2_2_similitud= Label(frame2, text= "Coloca  la  CC2")
    tex3_similitud= Label(frame2, text= "La dos cc deben tener 16 digitos sin puntos")
    tex4_similitud= Label(frame2, text= "Resultado")
    tex5_similitud= Label(frame2, text= "Ej_resultado: 123456789x49xx64")

    
    #-----------------------CONFIGURACIONES------------------------

    caja_similitud.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f")
    caja_similitud.place(x= 235, y=27, width=200, height=26)
    
    caja_similitud2.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f")
    caja_similitud2.place(x= 235, y=65, width=200, height=26)

    caja_similitud3.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f", )
    caja_similitud3.place(x= 235, y=135,width=200, height=26)

    


    generar_similitud.config(fg= "white", bg="deepskyblue3", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="deepskyblue1",cursor="hand2", overrelief=RAISED, activeforeground="white")
    generar_similitud.place(x= 455, y=26, height=30,width=119)

    copiar_similitud.config(fg= "white", bg="deepskyblue3", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="deepskyblue1",cursor="hand2", overrelief=RAISED, activeforeground="white")
    copiar_similitud.place(x= 455, y=134, height=30, width=119)


    tex2_similitud.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex2_similitud.place(x= 60, y=20)
    
    tex2_2_similitud.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex2_2_similitud.place(x= 60, y=60)

    tex3_similitud.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex3_similitud.place(x= 240, y=95)

    tex4_similitud.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex4_similitud.place(x= 60, y=130)

    tex5_similitud.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex5_similitud.place(x= 265, y=165)


#-----------------------METODO IDENTACION --------------------------

def abrir_identacion():
    

    limpiador_de_frames()
    met1.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met2.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met3.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met4.config(relief=SUNKEN,background ="green4", fg="white" )
    met5.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met6.config(relief=FLAT,background ="white", fg="#1d1e21" )
    
    def extrapolar_identacion():
            cadena=caja_identacion.get()
            resultado   = cadena[:7] + "x" + cadena[8:10] + "xx" + cadena[12:14] + "x" + cadena[-1]
            caja_identacion2.delete(0,END)
            caja_identacion2.insert(0,resultado)
    

    def copiar_al_portapapeles():
            caja_identacion2.select_range(0,len(caja_identacion2.get()))
            ventana.clipboard_clear()
            ventana.clipboard_append(caja_identacion2.get())
            
    vcmd = frame2.register(func=limitar_caracteres)
    


 

#-----------------------OBJETOS------------------------
    
    caja_identacion = Entry(frame2, validate="key", validatecommand=(vcmd, '%P'))
    caja_identacion2= Entry(frame2)

    generar_identacion =Button(frame2,text="Extrapolar",command=extrapolar_identacion )
    copiar_identacion = Button(frame2, text="Copiar", command=copiar_al_portapapeles)

    tex2_identacion= Label(frame2, text="Coloca la CC")
    tex3_identacion= Label(frame2, text= "La cc debe tener 16 digitos sin puntos")
    tex4_identacion= Label(frame2, text= "Resultado")
    tex5_identacion= Label(frame2, text= "Ej_resultado: 3014587x56xx58x9")

    
    #-----------------------CONFIGURACIONES------------------------

    caja_identacion.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f")
    caja_identacion.place(x= 235, y=27, width=200, height=26)

    caja_identacion2.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f", )
    caja_identacion2.place(x= 235, y=122,width=200, height=26)


    generar_identacion.config(fg= "white", bg="green4", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="green3",cursor="hand2", overrelief=RAISED, activeforeground="white")
    generar_identacion.place(x= 455, y=25, height=30,width=119)

    copiar_identacion.config(fg= "white", bg="green4", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="green3",cursor="hand2", overrelief=RAISED, activeforeground="white")
    copiar_identacion.place(x= 455, y=120, height=30, width=119)


    tex2_identacion.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex2_identacion.place(x= 80, y=20)
    
    tex3_identacion.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex3_identacion.place(x= 250, y=60)

    tex4_identacion.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex4_identacion.place(x= 80, y=115)

    tex5_identacion.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex5_identacion.place(x= 265, y=155)





#-----------------------NUMERO DIGITOS --------------------------

def abrir_digitos():
    

    limpiador_de_frames()
    met1.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met2.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met3.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met4.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met5.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met6.config(relief=SUNKEN,background ="red3", fg="white" )
    

    def copiar_al_portapapeles():
            caja_identacion2.select_range(0,len(caja_identacion2.get()))
            ventana.clipboard_clear()
            ventana.clipboard_append(caja_identacion2.get())

    def num_digitos():
            c1=caja_identacion.get()
            c1 = str(c1)
    
            texto = StringVar()
            texto2 = StringVar()
            texto3 = StringVar()
            texto4 = StringVar()
            texto5 = StringVar()

            text1= Label(frame2, bg="WHITE", fg="red")
            text1.config(justify="center",  font="Bebas 12 normal")
            text1.place(x=380, y=90, height= 30, width=60)
            
            text2= Label(frame2, bg="#1d1e21", fg="white")
            text2.config(justify="center", font="Bebas 12 normal")
            text2.place(x=180, y=90, height= 30, width=160)
    
            text3= Label(frame2, bg="#1d1e21", fg="white")
            text3.config(justify="center", font="Bebas 12 normal")
            text3.place(x=180, y=140, height= 30, width=160)

            text4= Label(frame2, bg="white", fg="white")
            text4.config(justify="center", width=len(c1), font="Bebas 12 normal")
            text4.place(x=380, y=140, height= 30, )

            text5= Label(frame2, bg="#1d1e21", fg="white")
            text5.config(justify="center", font="Ubuntu 10 bold")
            text5.place(x=200, y=200, height= 30, width=280)

    
            if len(c1) == 16:
                
                texto.set(len(c1))
                text1.config(textvariable=texto,  fg= "green4")
                
                texto2.set("Numero  de  digitos")
                text2.config(textvariable=texto2, bg= "green4")


                texto3.set("CC")
                text3.config(textvariable=texto3, bg= "green4" )

                texto4.set(c1)
                text4.config(textvariable=texto4, fg= "green4")

                texto5.set("TU CC TIENE LA LONGITUD CORRECTA")
                text5.config(textvariable=texto5, bg="green4")

        
            else:
                texto.set(len(c1))
                text1.config(textvariable=texto, fg= "red3")
                
                texto2.set("Numero  de  digitos")
                text2.config(textvariable=texto2, bg= "red3",  )

                texto3.set("CC")
                text3.config(textvariable=texto3, bg= "red3")

                texto4.set(c1)
                text4.config(textvariable=texto4,  fg= "red3")
        
                texto5.set("TU CC NO TIENE LA LONGITUD CORRECTA")
                text5.config(textvariable=texto5, bg="red3")


#-----------------------OBJETOS------------------------
    
    caja_identacion = Entry(frame2,)

    generar_identacion =Button(frame2,text="Comprobar" , command= num_digitos)


    tex2_identacion= Label(frame2, text="Coloca la CC")
    tex3_identacion= Label(frame2, text= "Comprueba cuantos digitos tiene tu cc")


    
    #-----------------------CONFIGURACIONES------------------------

    caja_identacion.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f")
    caja_identacion.place(x= 235, y=27, width=200, height=26)


    generar_identacion.config(fg= "white", bg="red2", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="red3",cursor="hand2", overrelief=RAISED, activeforeground="white")
    generar_identacion.place(x= 455, y=25, height=30,width=119)


    tex2_identacion.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex2_identacion.place(x= 80, y=20)
    
    tex3_identacion.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex3_identacion.place(x= 250, y=60)



#-----------------------METODO SOFIA --------------------------

def abrir_sofia():
    

    limpiador_de_frames()
    met1.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met2.config(relief=FLAT,background = "white", fg="#1d1e21")
    met3.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met4.config(relief=FLAT,background ="white", fg="#1d1e21" )
    met5.config(relief=SUNKEN,background ="deepskyblue3", fg="white" )
    met6.config(relief=FLAT,background ="white", fg="#1d1e21" )
    
    def extrapolar_sofia():
        C1= caja_sofia.get()

        C2= caja_sofia2.get()

        C11 = C1[0:8]

        C21 = C2[0:8]
        C22 = C2[8:16]

        C2 =C11+ ''.join(str(int(C21[i]) * int(C22[i])) for i in range(8))[0:8]

        C2 = C2[0:8] + ''.join(C2[i] if C1[i] == C2[i] else "1" if i == 15 else 'x' for i in range(8, 16))

        caja_sofia3.delete(0,END)
        caja_sofia3.insert(0,C2)


    def copiar_al_portapapeles():
            caja_sofia3.select_range(0,len(caja_sofia3.get()))
            ventana.clipboard_clear()
            ventana.clipboard_append(caja_sofia3.get())
            
    vcmd = frame2.register(func=limitar_caracteres)
    
    


 

#-----------------------OBJETOS------------------------
    
    caja_sofia = Entry(frame2, validate="key", validatecommand=(vcmd, '%P'))
    caja_sofia2= Entry(frame2, validate="key", validatecommand=(vcmd, '%P'))
    caja_sofia3= Entry(frame2)

    generar_sofia =Button(frame2,text="Extrapolar",command=extrapolar_sofia )
    copiar_sofia = Button(frame2, text="Copiar", command=copiar_al_portapapeles)

    tex2_sofia= Label(frame2, text="Coloca  la  CC1")
    tex2_2_sofia= Label(frame2, text= "Coloca  la  CC2")
    tex3_sofia= Label(frame2, text= "La dos cc deben tener 16 digitos sin puntos")
    tex4_sofia= Label(frame2, text= "Resultado")
    tex5_sofia= Label(frame2, text= "Ej_resultado: 45689791xxxxxxx1")

    
    #-----------------------CONFIGURACIONES------------------------

    caja_sofia.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f")
    caja_sofia.place(x= 235, y=27, width=200, height=26)
    
    caja_sofia2.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f")
    caja_sofia2.place(x= 235, y=65, width=200, height=26)

    caja_sofia3.config(relief=FLAT, width= 25, font=("Ubuntu 10 bold"), justify="center",
                                    cursor="xterm", bg= "white", fg="#282a2f", )
    caja_sofia3.place(x= 235, y=135,width=200, height=26)

    


    generar_sofia.config(fg= "white", bg="deepskyblue3", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="deepskyblue1",cursor="hand2", overrelief=RAISED, activeforeground="white")
    generar_sofia.place(x= 455, y=26, height=30, width=119)

    copiar_sofia.config(fg= "white", bg="deepskyblue3", font=("Bebas 14 normal"), relief=FLAT,
            activebackground ="deepskyblue1",cursor="hand2", overrelief=RAISED, activeforeground="white")
    copiar_sofia.place(x= 455, y=134, height=30, width=119)


    tex2_sofia.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex2_sofia.place(x= 60, y=20)
    
    tex2_2_sofia.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex2_2_sofia.place(x= 60, y=60)

    tex3_sofia.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex3_sofia.place(x= 240, y=95)

    tex4_sofia.config(fg="white", bg= "#1d1e21", font="Bebas 17 normal")
    tex4_sofia.place(x= 60, y=130)

    tex5_sofia.config(fg="white", bg="#1d1e21", font="Ubuntu 7 italic")
    tex5_sofia.place(x= 265, y=165)


"""Codigo de la ventana principal"""


#-----------------------VENTANA PRINCIPAL-----------------------------    

#-----------------------IMAGENES---------------------------
imagen = PhotoImage(file=resolver_ruta('./logogrey.png' ))
imaglebel = Label(ventana,image=imagen, bg="#1d1e21")
imaglebel.place(x= 20, y=6)

pagina1= PhotoImage(file=resolver_ruta('./pagina.png'))
im = PhotoImage(file=resolver_ruta('./i.png'))

youtubei = PhotoImage(file=resolver_ruta('./youtube.png'))
tl = PhotoImage(file=resolver_ruta('./logte.png'))


#-----------------------OBJETOS---------------------------
bienvenida = Label(frame2,text="ESCOGE  EL  METODO  QUE  DESEAS  UTILIZAR")
bienvenida2 = Button(frame2,text=" MAS INFORMACIÓN", command=boton_informacion)
titulo = Label(text="CREDIT  CARD  EXTRAPOLATOR")
version= Label(text="v1.0")

met1 = Button(ventana, text="BASICO" ,command=abrir_basico )
met2 = Button(ventana, text="SIMILITUD", command=abrir_similitud)
met3 = Button(ventana, text="ACTIVACION", command=abrir_activacion)
met4 = Button(ventana, text="IDENTACION", command= abrir_identacion)
met5 = Button(ventana, text="SOFIA", command=abrir_sofia)
met6 = Button(ventana, text="N.DIGITOS", command= abrir_digitos)
inf = Button(ventana, image=im, command=boton_informacion)
pag = Button(ventana, image=pagina1, command=boton_pagina)
youtube = Button(ventana, image=youtubei,command=boton_youtube ) 
telegram = Button(ventana, image=tl, command=boton_telegram)




#-----------------------CONFIGURACIONES---------------------------
bienvenida.place(x=0, y=60, width=700)
bienvenida.config(fg="white", bg= "#1d1e21", font="Bebas 18 normal", justify="center")
                    
bienvenida2.place(x=260, y=95)
bienvenida2.config(fg="white", bg= "#1d1e21", font="Ubuntu 13 bold", justify="center",
                   relief=FLAT,activebackground ="#1d1e21", cursor="hand2", overrelief=RAISED , activeforeground="white")

version.place(y=10,x=620)
version.config(bg="#1d1e21", fg="white", cursor="hand2", font="bebas 15 normal" , width=6)

titulo.place(y=35,x=170)
titulo.config(bg="#1d1e21", fg="white", font="Bebas 23 normal" , width=26)



met1.config(fg= "#1d1e21", bg="white", font=("Bebas 21 normal"), relief=FLAT,
            activebackground ="red3", cursor="hand2", overrelief=RAISED , activeforeground="white")
met1.place(x= 100, y=370,width = 160, height =40)

met2.config(fg= "#1d1e21", bg="white", font=("Bebas 20 normal"), relief=FLAT,
            activebackground ="deepskyblue3", cursor="hand2" , overrelief=RAISED,activeforeground="white")
met2.place(x= 100, y=440,width = 160, height =40)

met3.config(fg= "#1d1e21", bg="white", font=("Bebas 20 normal"), relief=FLAT,
            activebackground ="green4",cursor="hand2", overrelief=RAISED, activeforeground="white")
met3.place(x= 270, y=370,width = 170, height =40)

met4.config(fg= "#1d1e21", bg="white", font=("Bebas 20 normal"), relief=FLAT,
            activebackground ="green4", cursor="hand2", overrelief=RAISED , activeforeground="white")
met4.place(x= 270, y=440,width = 170, height =40)

met5.config(fg= "#1d1e21", bg="white", font=("Bebas 20 normal"), relief=FLAT,
            activebackground ="deepskyblue3", cursor="hand2" , overrelief=RAISED, activeforeground="white")
met5.place(x= 450, y=370,width = 160, height =40)

met6.config(fg= "#1d1e21", bg="white", font=("Bebas 21 normal"), relief=FLAT,
            activebackground ="red3",cursor="hand2", overrelief=RAISED, activeforeground="white")
met6.place(x= 450, y=440,width = 160, height =40)



inf.config( bg="white",activebackground="red3", cursor="hand2", relief=FLAT, overrelief=RAISED)
inf.place(x= 620, y=440,width = 55, height =40)

pag.config( activebackground="green3", cursor="hand2", relief=FLAT, overrelief=RAISED, bg="white")
pag.place(x= 620, y=370,width = 55, height =40)

telegram.place(x= 30, y=370, width = 55, height =40)
telegram.config( activebackground="deepskyblue3", cursor="hand2", relief=FLAT, overrelief=RAISED, bg="white")

youtube.place(x=30,y=440,width = 55, height =40)
youtube.config( activebackground="red2", cursor="hand2", relief=FLAT, overrelief=RAISED, bg="white")    

ventana.mainloop()
