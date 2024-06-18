from tkinter import *
from tkinter import messagebox
from customtkinter import *
import json
import os

fila = []
jogando = []
histo = []
pontosDaPartida = 0
pontosJogador1 = 0
pontosJogador2 = 0
somaPontos1 = 0
somaPontos2 = 0

def setarPontos5():
    global pontosDaPartida
    pontosDaPartida = 5

def setarPontos7():
    global pontosDaPartida
    pontosDaPartida = 7

def setarPontos11():
    global pontosDaPartida
    pontosDaPartida = 11

def mudarJanela():
    global pontosDaPartida
    pegar = jogador1.get()
    pegar2 = jogador2.get()
    jogando.append(pegar)
    jogando.append(pegar2)
    if pontosDaPartida != 0 and pegar != '' and pegar2 != '':
        inicio.destroy()
    elif pegar == '':
        messagebox.showinfo("showinfo", "Insira o nome do jogador 1")
    elif pegar2 == '':
        messagebox.showinfo("showinfo", "Insira o nome do jogador 2") 
    elif pontosDaPartida == 0:
        messagebox.showinfo("showinfo", "Escolha a quantidade de pontos") 

def soma1():
    global pontosJogador1
    global pontosJogador2
    global pontosDaPartida
    global somaPontos1
    global somaPontos2
    rodada = []
    pontosJogador1 += 1
    somaPontos1 += 1
    pontos1 = Listbox(jogo, height=1, width=2)
    pontos1.insert(END, pontosJogador1)
    pontos1.place(x=60, y=50)
    if pontosJogador1 == pontosDaPartida - 1 and pontosJogador2 == pontosDaPartida - 1:
        pontosDaPartida = 2
        pontosJogador1 = 0
        pontosJogador2 = 0
        pontos1 = Listbox(jogo, height=1, width=2)
        pontos1.insert(END, 0)
        pontos1.place(x=60, y=50)
        pontos2 = Listbox(jogo, height=1, width=2)
        pontos2.insert(END, 0)
        pontos2.place(x=430, y=50)
    elif pontosJogador1 == pontosDaPartida:
        rodada.append(jogando[0])
        rodada.append(somaPontos1)
        rodada.append(jogando[1])
        rodada.append(somaPontos2)
        histo.append(rodada)
        somaPontos1 = 0
        somaPontos2 = 0
        pontos1 = Listbox(jogo, height=1, width=2)
        pontos1.insert(END, 0)
        pontos1.place(x=60, y=50)
        pontos2 = Listbox(jogo, height=1, width=2)
        pontos2.insert(END, 0)
        pontos2.place(x=430, y=50)
        pontosJogador1 = 0
        pontosJogador2 = 0
        fila.append(jogando[1])
        jogando[1] = fila[0]
        fila.pop(0)
        ordem = Listbox(jogo, height=15, width=20)
        for i in fila:
            ordem.insert(END, i)
        ordem.place(x=300, y=170)
        player1 = Listbox(jogo, height=1, width=20)
        for i in range(0, 1):
            player1.insert(END, jogando[i])
        player1.place(x=80, y=50)
        player2 = Listbox(jogo, height=1, width=20)
        for i in range(1, 2):
            player2.insert(END, jogando[i])
        player2.place(x=300, y=50)
        pontosDaPartida = save
        

def soma2():
    global pontosJogador2
    global pontosJogador1
    global pontosDaPartida
    global somaPontos2
    global somaPontos1
    rodada = []
    somaPontos2 += 1
    pontosJogador2 += 1
    pontos2 = Listbox(jogo, height=1, width=2)
    pontos2.insert(END, pontosJogador2)
    pontos2.place(x=430, y=50)
    if pontosJogador1 == pontosDaPartida - 1 and pontosJogador2 == pontosDaPartida - 1:
        pontos1 = Listbox(jogo, height=1, width=2)
        pontos1.insert(END, 0)
        pontos1.place(x=60, y=50)
        pontos2 = Listbox(jogo, height=1, width=2)
        pontos2.insert(END, 0)
        pontos2.place(x=430, y=50)
        pontosDaPartida = 2
        pontosJogador1 = 0
        pontosJogador2 = 0
    elif pontosJogador2 == pontosDaPartida:
        rodada.append(jogando[0])
        rodada.append(somaPontos1)
        rodada.append(jogando[1])
        rodada.append(somaPontos2)
        histo.append(rodada)
        somaPontos2 = 0
        somaPontos1 = 0
        pontos1 = Listbox(jogo, height=1, width=2)
        pontos1.insert(END, 0)
        pontos1.place(x=60, y=50)
        pontos2 = Listbox(jogo, height=1, width=2)
        pontos2.insert(END, 0)
        pontos2.place(x=430, y=50)
        pontosJogador1 = 0
        pontosJogador2 = 0
        fila.append(jogando[0])
        jogando[0] = fila[0]
        fila.pop(0)
        ordem = Listbox(jogo, height=15, width=20)
        for i in fila:
            ordem.insert(END, i)
        ordem.place(x=300, y=170)
        player1 = Listbox(jogo, height=1, width=20)
        for i in range(0, 1):
            player1.insert(END, jogando[i])
        player1.place(x=80, y=50)
        pontosDaPartida = save

def adicionarPessoa():
    pegar = jogador.get()
    if pegar != '':
        fila.append(pegar)
        ordem = Listbox(jogo, height=15, width=20)
        for i in fila:
            ordem.insert(END, i)
        ordem.place(x=300, y=170)

def removerPessoa():
    pegar = jogador.get()
    if pegar != '':
        fila.remove(pegar)
        ordem = Listbox(jogo, height=15, width=20)
        for i in fila:
            ordem.insert(END, i)
        ordem.place(x=300, y=170)

def historicos():
    historico = CTkToplevel()
    historico.title("Histórico")
    historico.geometry("300x500")
    CTkLabel(historico, text='Histórico de Partidas').place(x=90, y=10)
    hist = Listbox(historico, height=25, width=45)
    for partida in histo:
        hist.insert(END, partida)
        hist.insert(END, '\n')
    hist.place(x=10, y=40)

def salvar_historico():
    dados = {"historico": histo}
    with open('historico.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=2)

def carregar_historico():
    global histo
    if os.path.exists('historico.json'):
        with open('historico.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            histo = dados.get("historico", [])

def remover_historico():
    global histo
    histo = []
    if os.path.exists('historico.json'):
        os.remove('historico.json')

def quitar():
    salvar_historico()
    jogo.quit()

carregar_historico()

inicio = CTk()
inicio._set_appearance_mode("Dark")
inicio.title("Configurações")
inicio.geometry("500x500")

CTkLabel(inicio, text="Qual a quantidade de pontos para a vitória?").place(x=125, y=50)
pontos1 = CTkButton(inicio, width=80, height=52, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred', text='5', command=setarPontos5)
pontos1.place(x=100, y=100)
pontos2 = CTkButton(inicio, width=80, height=52, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',text='7', command=setarPontos7)
pontos2.place(x=200, y=100)
pontos3 = CTkButton(inicio, width=80, height=52, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',text='11', command=setarPontos11)
pontos3.place(x=300, y=100)

CTkLabel(inicio, text="Digite o nome do Jogador 1").place(x=165, y=200)
jogador1 = Entry(inicio, text='', width=30)
jogador1.place(x=147, y=230)
CTkLabel(inicio, text="Digite o nome do Jogador 2").place(x=165, y=300)
jogador2 = Entry(inicio, text='', width=30)
jogador2.place(x=147, y=330)

comeco = CTkButton(inicio, text="Começar", width=210, height=62, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',command=mudarJanela).place(x=135, y=400)

inicio.mainloop()

jogo = CTk()
jogo._set_appearance_mode("Dark")
jogo.title("Jogo")
jogo.geometry("500x500")

save = pontosDaPartida

player1 = Listbox(jogo, height=1, width=20)
for i in range(0, 1):
    player1.insert(END, jogando[i])
player1.place(x=80, y=50)
player2 = Listbox(jogo, height=1, width=20)
for i in range(1, 2):
    player2.insert(END, jogando[i])
player2.place(x=300, y=50)

pontos1 = Listbox(jogo, height=1, width=2)
pontos1.place(x=60, y=50)
pontos2 = Listbox(jogo, height=1, width=2)
pontos2.place(x=430, y=50)

pontoJogador1 = CTkButton(jogo, width=120, height=32, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',text='+1', command=soma1)
pontoJogador1.place(x=81, y=80)
pontoJogador2 = CTkButton(jogo, width=120, height=32, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',text='+1', command=soma2)
pontoJogador2.place(x=301, y=80)

CTkLabel(jogo, text="Opções").place(x=110, y=130)
CTkLabel(jogo, text="Nome do jogador:").place(x=85, y=160)
jogador = Entry(jogo, text='')
jogador.place(x=60, y=190, height=20, width=150)

adicionarJogador = CTkButton(jogo, width=210, height=42, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',text='Adicionar na Fila', command=adicionarPessoa)
adicionarJogador.place(x=30, y=230)
removerJogador = CTkButton(jogo, width=210, height=42, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',text='Remover da Fila', command=removerPessoa)
removerJogador.place(x=30, y=280)
botaoHistorico = CTkButton(jogo, width=210, height=42, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',text='Histórico', command=historicos)
botaoHistorico.place(x=30, y=330)
removerHistorico = CTkButton(jogo, width=210, height=42, border_width=0, corner_radius=8, fg_color='red', text_color='black', hover_color='darkred',text='Remover Histórico', command=remover_historico)
removerHistorico.place(x=30, y=380)
sair = CTkButton(jogo, width=210, height=42, border_width=0, corner_radius=8, fg_color='red', text_color='black', text='Sair', hover_color='darkred',command=quitar)
sair.place(x=30, y=430)

CTkLabel(jogo, text="Fila").place(x=350, y=140)
ordem = Listbox(jogo, height=15, width=20)
ordem.place(x=300, y=170)

jogo.mainloop()