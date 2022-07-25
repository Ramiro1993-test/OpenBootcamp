import tkinter as tk
from tkinter import ttk
from turtle import width
import os

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title('')
        self.labelframe1=ttk.LabelFrame(self.ventana1, text='Aplicacion')
        self.labelframe1.grid(column=0, row=0, padx=5,pady=5)
        self.aplicacion()
        self.labelframe2=ttk.LabelFrame(self.ventana1, text='Operaciones')
        self.labelframe2.grid(column=0, row=5, padx=5,pady=5) 
        self.operaciones() 
        self.laberlframe3=ttk.LabelFrame(self.ventana1, text='Resultado') 
        self.labelframe1.grid(column=0, row=7, padx=20,pady=20)
        self.resultado()
        self.ventana1.mainloop()
       
    def aplicacion(self): 
      self.label1=ttk.Label(self.labelframe1, text='Codigo articulo: ')
      self.label1.grid(column=0, row=1, padx=5,pady=5)
      self.cod_art=tk.StringVar()
      self.entry=ttk.Entry(self.labelframe1, width=10, textvariable=self.cod_art)
      self.entry.grid(column=1,row=1)
      self.label2=ttk.Label(self.labelframe1, text='Producto: ')
      self.label2.grid(column=0, row=2, padx=5,pady=5)
      self.pro=tk.StringVar()
      self.entry2=ttk.Entry(self.labelframe1, width=10, textvariable=self.pro)
      self.entry2.grid(column=1,row=2)
      self.label3=ttk.Label(self.labelframe1, text='Precio: ')
      self.label3.grid(column=0, row=3, padx=5,pady=5)
      self.pre=tk.StringVar()
      self.entry3=ttk.Entry(self.labelframe1, width=10, textvariable=self.pre)
      self.entry3.grid(column=1,row=3)

    def operaciones(self):
       self.boton1=ttk.Button(self.labelframe2, text='Registrar', command=self.registrar)
       self.boton1.grid(column=0,row=6, padx=5,pady=5)  
       self.boton2=ttk.Button(self.labelframe2, text='Mostrar', command=self.mostrar)
       self.boton2.grid(column=1,row=6, padx=5,pady=5)
       self.boton3=ttk.Button(self.labelframe2, text='Limpiar',command=self.limpiar)
       self.boton3.grid(column=2,row=6, padx=5,pady=5)
       self.boton4=ttk.Button(self.labelframe2, text='Consultar',command=self.consultar)
       self.boton4.grid(column=3,row=6, padx=5,pady=5) 

    def registrar(self):
      self.productos={}
      self.productos[self.cod_art.get()]=(self.pro.get(),self.pre.get())
      self.label4.config(text='Registrado')

    def mostrar(self):
      self.label4.config(text=self.productos)  

    def resultado(self):   
      self.label4=ttk.Label(self.ventana1, text='resultado')
      self.label4.grid(column=0, row=8)

    def limpiar(self):
      self.entry.delete(0,"end") 
      self.entry2.delete(0,"end")
      self.entry3.delete(0,"end")

    def consultar(self):
        self.label4.config(text=self.productos) 

    
      

      

        
aplicacion1=Aplicacion()
