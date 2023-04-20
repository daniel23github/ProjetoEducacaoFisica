from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import json


def minuto(s):
    if int(s) // 60 < 60:
        if int(s) % 60 < 10:
            r = f'{int(s) // 60}:0{int(s) % 60}'
        else:
            r = f'{int(s) // 60}:{int(s) % 60}'
    else:
        if (int(s) // 60) % 60 < 10:
            if int(s) % 60 < 10:
                r = f'{(int(s) // 60) // 60}:0{(int(s) // 60) % 60}:0{int(s) % 60}'
            else:
                r = f'{(int(s) // 60) // 60}:0{(int(s) // 60) % 60}:{int(s) % 60}'
        else:
            if int(s) % 60 < 10:
                r = f'{(int(s) // 60) // 60}:{(int(s) // 60) % 60}:0{int(s) % 60}'
            else:
                r = f'{(int(s) // 60) // 60}:{(int(s) // 60) % 60}:{int(s) % 60}'
    return str(r)

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)

    def definir(self):
       App.get_running_app().root.get_screen('comecar').s = App.get_running_app().root.get_screen('configuracoes').s

    def menu(self):
        App.get_running_app().root.get_screen('comecar').parar()
        self.definir()
        App.get_running_app().root.current = 'comecar'
        App.get_running_app().root.get_screen('comecar').n = 1
        App.get_running_app().root.get_screen('comecar').contar()

    def confirmacao(self, *args, **kwargs):
        box = BoxLayout(orientation='vertical', padding=10, spacing=20)
        botoes = BoxLayout(spacing=20, padding=10)

        pop = Popup(title='Quer sair?', content=box, size_hint=(None, None),
                    size=(400, 400))

        sim = Button(text='Sim', on_release=App.get_running_app().stop)
        nao = Button(text='Não', on_release=pop.dismiss)

        atencao = Image(source='atencao.png')

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        box.add_widget(atencao)
        box.add_widget(botoes)
        anima = Animation(size=(500, 400), duration=0.2, t='out_back')
        anima.start(pop)
        pop.open()
        return True

    def configuracoes(self, *args):
        App.get_running_app().root.get_screen('configuracoes').loadData()
        App.get_running_app().root.current = 'configuracoes'


class Configuracoes(Screen):
    s = NumericProperty()
    s2 = NumericProperty()
    m = StringProperty()
    m2 = StringProperty()
    tempos = []
    path = ''
    def adicionar(self):
        self.s += 60
        App.get_running_app().root.get_screen('configuracoes').ids.label3.text = minuto(self.s)
        self.saveData()
    def diminuir(self):
        if self.s > 0:
            self.s -= 60
            App.get_running_app().root.get_screen('configuracoes').ids.label3.text = minuto(self.s)
            self.saveData()
    def adicionar2(self):
        self.s2 += 10
        App.get_running_app().root.get_screen('configuracoes').ids.label2.text = minuto(self.s2)
        self.saveData()
    def diminuir2(self):
        if self.s2 > 0:
            self.s2 -= 10
            App.get_running_app().root.get_screen('configuracoes').ids.label2.text = minuto(self.s2)
            self.saveData()

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def loadData(self, *args):
        try:
            with open(self.path+'data.json', 'r') as data:
                self.tempos = json.load(data)
                self.s = self.tempos[0]
                self.s2 = self.tempos[1]
                self.m = minuto(self.s)
                self.m2 = minuto(self.s2)
        except FileNotFoundError:
            with open(self.path+'data.json', 'w') as data:
                self.tempos = [300, 60]
                self.saveData()
                self.loadData()

    def saveData(self, *args):
        with open(self.path+'data.json', 'w') as data:
            self.tempos[0] = self.s
            self.tempos[1] = self.s2
            json.dump(self.tempos, data)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)
        self.path = App.get_running_app().user_data_dir + '/'
        self.loadData()

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

class Votacao(Screen):
    co = 0
    def votacao(self):
        if App.get_running_app().root.get_screen('comecar').s > 0:
            App.get_running_app().root.current = 'comecar'
            App.get_running_app().root.get_screen('comecar').contar()

        else:
            App.get_running_app().root.get_screen('resultado').definir()
            App.get_running_app().root.current = 'resultado'

    def b1(self):
        self.co += 1
        self.votacao()


    def b2(self):
        self.co += 2
        self.votacao()


    def b3(self):
        self.co += 3
        self.votacao()


    def b4(self):
        self.co += 4
        self.votacao()


    def b5(self):
        self.co += 5
        self.votacao()


    def b6(self):
        self.co += 6
        self.votacao()


    def b7(self):
        self.co += 7
        self.votacao()


    def b8(self):
        self.co += 8
        self.votacao()


    def b9(self):
        self.co += 9
        self.votacao()


    def b10(self):
        self.co += 10
        self.votacao()


class Comecar(Screen):
    s = 0
    co = 0
    n = 1
    co2 = 0

    def contar(self, *args):
        Clock.unschedule(self.contar)
        if self.co == App.get_running_app().root.get_screen('configuracoes').s2 or self.s == 0:
            self.co = 0
            self.co2 += 1
            App.get_running_app().root.current = 'votacao'

        elif self.confirmar(self.n) == True:
            self.contarV()

        if self.s == 0:
            self.n = 2

    def contarV(self, *args):
        App.get_running_app().root.get_screen('comecar').ids.label.text = minuto(self.s)
        self.s -= 1
        self.co += 1
        Clock.schedule_once(self.contar, 1)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'configuracoes'
            self.parar()
            return True

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)


    def confirmar(self, n):
        if n == 1:
            return True
        else:
            return False
    def parar(self):
        self.n = 2
        self.co2 = 0
        self.co = 0
        App.get_running_app().root.get_screen('votacao').co = 0

    def comecar(self):
        App.get_running_app().root.current = 'configuracoes'
        self.parar()

class Resultado(Screen):
    media = NumericProperty()
    def definir(self):
        self.media = App.get_running_app().root.get_screen('votacao').co / App.get_running_app().root.get_screen('comecar').co2


class test(App):
    def build(self):
        return Gerenciador()

test().run()
