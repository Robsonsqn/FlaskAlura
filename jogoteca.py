from flask import Flask, render_template
from domain.domains import Jogo
app = Flask(__name__)


def jogos_padrao():
    return [
        Jogo('Tetris', 'Arcade', 'Atari'),
        Jogo('Mario', 'Plataforma', 'SNES'),
        Jogo('Pokemon Lets Go', 'RPG', 'Switch')
    ]


@app.route('/home')
def home():
    lista_jogos = jogos_padrao()
    return render_template('lista.html', titulo='JOGOS', jogos=lista_jogos)


@app.route('/novo')
def novo():
    return render_template('cadastro.html', titulo='Novo Jogo'),


def main():
    app.run()


if __name__ == '__main__':
    main()

