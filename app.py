from flask import Flask
app = Flask(__name__)

cards = [
    {
        "id": 0,
        "name": "O Louco",
        "description": "Ousadia, liberdade, desprendimento, férias e lazer como tônica de tudo, viver cada momento. Representa a energia do espírito livre, da inocência e da espontaneidade. Ele não está preocupado com as convenções sociais, críticas alheias, ou com as expectativas dos outros. Ele quer viver o hoje, livre e seguindo sua intuição, se lançando ao desconhecido com coragem, Nos convida a encarar uma nova jornada sem medo, sem tabus, mesmo sem experiência. Na carta do Louco temos a representação de um menino, um jovem andando à beira do precipício, sendo corajoso, arriscando tudo para viver seus sonhos, levando apenas o necessário, porque para ele o que importa não é o destino final, e sim o que ele encontra na caminhada, no hoje, no percurso. Porém podendo não perceber muitas vezes que suas atitudes podem ser arriscadas e até irresponsáveis. Na carta também é retratado o cachorro, o sol e a flor branca em suas mãos, indicando pureza beirando a inocência. Pode representar a vontade de se libertar das restrições e das obrigações da vida cotidiana, buscando aventuras e experiências novas. No lado negativo pode trazer insensatez, excesso de dívidas, desorganização, ser leviano, inquieto, irresponsável e imaturo. Desordem energética.",
        "work": "Não é muito bem visto pelos colegas ou chefe, ou clientes, indisciplinado, não gosta de receber ordens, probabilidade de ser demitido. Falta de capacitação. Pode ser extremamente criativo, porém deseja trabalhar. Podendo gerar dificuldades de escolher um trabalho, não sabe o que quer.",
        "financial": "Está gastando demais, sendo impulsivo, extravagante, deslumbrado. Investimentos que dão prejuízos. Podendo acumular dívidas sem perceber. Necessita de mais cuidado no orçamento",
        "love": "jovial, divertido, engraçado, despreocupado, ama, flerta, conversa sem compromisso. Pode indicar ir irresponsabilidade emocional.",
        "free_person": "Gosta pelo prazer de se divertir, mas não quer se preocupar, não faz planos para futuro, grande libido, curiosidade, futuro prazeroso mas sem compromisso.",
        "taken_person": "Inconstância nas atitudes, descompromisso, existe amor mas de um jeito agitado, tem tesão mas tem tendência a distanciamento ou separação, promessas que não são cumpridas, comportamento leviano, irresponsável, sem empatia ou consciência. Dificuldades.",
        "obstacle": "Imaturidade, imprudência, descuido, desordem, bagunça.",
        "advice": "Ser ousado, flexível, dinâmico, seguir a intuição, não é hora de ligar para a opinião dos outros."
    },
    {
        "id": 1,
        "name": "O Mago",
        "description": "Inovação, sagacidade, destreza, esperteza, habilidade de agir, persuadir, criar, ter independência. Na carta do Mago encontramos todos os Naipes: copas, paus, espadas e ouros. Todos os elementos necessários para a magia acontecer. Com as mãos ele simboliza que como é no céu é na terra indicando seu poder de criação. É como se o Mago estivesse com a faca e o queijo na mão, só precisando agir para criar o que deseja: Dar vida aos seus pensamentos. O Mago tem o poder da Alquimia: transformar algo que não tinha valor nenhum em algo extremamente valioso. O mago é sempre um talvez, uma possibilidade, uma porta que se abre, mas nunca realmente uma efetivação ou realização. Necessita de esforço, é a força motriz da criação, mas para dar continuidade é necessário o empenho. Simboliza a capacidade de transformar ideias em ação e manifestar a realidade desejada. Ele representa o poder da vontade, da concentração e da habilidade de utilizar recursos disponíveis para alcançar objetivos. O Mago tem muita facilidade para persuadir, vender, convencer. É um símbolo de autonomia, criatividade e autoconfiança, nos lembrando de que somos os mestres de nossa própria jornada e que temos o poder de transformar nossa realidade.",
        "work": "Aumenta o ritmo de trabalho, bom relacionamento com colegas de trabalho. Pesquisa, investiga, busca. com momento para começar um projeto profissional, que exige esforço mas pode trazer bons resultados imediatos. Oportunidade de um novo trabalho ou fonte de renda.",
        "financial": "Ambição, esperteza, bons investimentos, grande oportunidade, nada é garantido, necessita perseverança e esforço. Tudo ainda é novo.",
        "love": "Tem interesse, deseja namorar ou se envolver com alguém, tem espontaneidade, busca por ser feliz, é naturalmente sedutor, sabe conquistar, gosta de conversar. Faz tudo para melhorar a relação.",
        "free_person": "Flerte, muita sedução, namoro passageiro, gosta mas não faz esforço, até quer algo mais sério, mas tudo depende o quão bom serão os momentos juntos.",
        "taken_person": "Melhoria no relacionamento, reconquista, quer buscar o tempo perdido, tem atitudes inovadoras, quer estar junto, está sempre pronto. Traz novos caminhos no relacionamento, faz planos para o futuro, como ter filhos, casamento, mudança de casa.",
        "obstacle": "Dificuldade em agir, em se posicionar. Dificuldade em tomar a frente, em ter atitude.",
        "advice": "É o momento de dialogar, não dá para esperar só as forças do destino agir. Precisa recriar, se mexer, buscar possibilidades para se alcançar aquilo que deseja."
    }
]

@app.route('/get_cards', methods=['GET'])
def get_all_cards():
    return jsonify(cards)

@app.route('/get_card/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = next((c for c in cards if c["id"] == card_id), None)
    
    if card:
        return jsonify(card)
    else:
        return jsonify({"error": "Card not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)