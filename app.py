from flask import Flask, render_template

app = Flask ('Portfolio Acadêmico')


projetos = [
    {
        "nome": "PP1",
        "descricao": "Primeiro projeto prático da faculdade.",
        "link": "https://github.com/kenay-7/PP1"
    },
    {
        "nome": "PP2",
        "descricao": "Segundo projeto prático da faculdade.",
        "link": "https://github.com/kenay-7/PP2"
    },
    {
        "nome": "PP3",
        "descricao": "Terceiro projeto prático da faculdade.",
        "link": "https://github.com/kenay-7/PP3"
    },
    {
        "nome": "PP4",
        "descricao": "Quarto projeto prático da faculdade.",
        "link": "https://github.com/kenay-7/PP4"
    },
    {
        "nome": "PP5",
        "descricao": "Quinto projeto prático da faculdade.",
        "link": "https://github.com/kenay-7/PP5"
    },
    {
        "nome": "PP6",
        "descricao": "Sexto projeto prático da faculdade.",
        "link": "https://github.com/kenay-7/PP6"
    }
]

@app.route("/")
def home():
    return render_template("index.html", projetos=projetos)


if __name__ == "__main__":
    app.run(debug=True)