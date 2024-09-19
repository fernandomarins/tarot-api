from flask import Flask, jsonify
app = Flask(__name__)

cards = [
    {
        "id": 0,
        "name": "O Louco",
        "major": True,
        "description": "Ousadia, liberdade, desprendimento, férias e lazer como tônica de tudo, viver cada momento. Representa a energia do espírito livre, da inocência e da espontaneidade. Ele não está preocupado com as convenções sociais, críticas alheias, ou com as expectativas dos outros. Ele quer viver o hoje, livre e seguindo sua intuição, se lançando ao desconhecido com coragem, Nos convida a encarar uma nova jornada sem medo, sem tabus, mesmo sem experiência. Na carta do Louco temos a representação de um menino, um jovem andando à beira do precipício, sendo corajoso, arriscando tudo para viver seus sonhos, levando apenas o necessário, porque para ele o que importa não é o destino final, e sim o que ele encontra na caminhada, no hoje, no percurso. Porém podendo não perceber muitas vezes que suas atitudes podem ser arriscadas e até irresponsáveis. Na carta também é retratado o cachorro, o sol e a flor branca em suas mãos, indicando pureza beirando a inocência. Pode representar a vontade de se libertar das restrições e das obrigações da vida cotidiana, buscando aventuras e experiências novas. No lado negativo pode trazer insensatez, excesso de dívidas, desorganização, ser leviano, inquieto, irresponsável e imaturo. Desordem energética.",
        "work": "Não é muito bem visto pelos colegas ou chefe, ou clientes, indisciplinado, não gosta de receber ordens, probabilidade de ser demitido. Falta de capacitação. Pode ser extremamente criativo, porém deseja trabalhar. Podendo gerar dificuldades de escolher um trabalho, não sabe o que quer.",
        "financial": "Está gastando demais, sendo impulsivo, extravagante, deslumbrado. Investimentos que dão prejuízos. Podendo acumular dívidas sem perceber. Necessita de mais cuidado no orçamento",
        "love": "Jovial, divertido, engraçado, despreocupado, ama, flerta, conversa sem compromisso. Pode indicar ir irresponsabilidade emocional.",
        "free_person": "Gosta pelo prazer de se divertir, mas não quer se preocupar, não faz planos para futuro, grande libido, curiosidade, futuro prazeroso mas sem compromisso.",
        "taken_person": "Inconstância nas atitudes, descompromisso, existe amor mas de um jeito agitado, tem tesão mas tem tendência a distanciamento ou separação, promessas que não são cumpridas, comportamento leviano, irresponsável, sem empatia ou consciência. Dificuldades.",
        "obstacle": "Imaturidade, imprudência, descuido, desordem, bagunça.",
        "advice": "Ser ousado, flexível, dinâmico, seguir a intuição, não é hora de ligar para a opinião dos outros."
    },
    {
        "id": 1,
        "name": "O Mago",
        "major": True,
        "description": "Inovação, sagacidade, destreza, esperteza, habilidade de agir, persuadir, criar, ter independência. Na carta do Mago encontramos todos os Naipes: copas, paus, espadas e ouros. Todos os elementos necessários para a magia acontecer. Com as mãos ele simboliza que como é no céu é na terra indicando seu poder de criação. É como se o Mago estivesse com a faca e o queijo na mão, só precisando agir para criar o que deseja: Dar vida aos seus pensamentos. O Mago tem o poder da Alquimia: transformar algo que não tinha valor nenhum em algo extremamente valioso. O mago é sempre um talvez, uma possibilidade, uma porta que se abre, mas nunca realmente uma efetivação ou realização. Necessita de esforço, é a força motriz da criação, mas para dar continuidade é necessário o empenho. Simboliza a capacidade de transformar ideias em ação e manifestar a realidade desejada. Ele representa o poder da vontade, da concentração e da habilidade de utilizar recursos disponíveis para alcançar objetivos. O Mago tem muita facilidade para persuadir, vender, convencer. É um símbolo de autonomia, criatividade e autoconfiança, nos lembrando de que somos os mestres de nossa própria jornada e que temos o poder de transformar nossa realidade.",
        "work": "Aumenta o ritmo de trabalho, bom relacionamento com colegas de trabalho. Pesquisa, investiga, busca. com momento para começar um projeto profissional, que exige esforço mas pode trazer bons resultados imediatos. Oportunidade de um novo trabalho ou fonte de renda.",
        "financial": "Ambição, esperteza, bons investimentos, grande oportunidade, nada é garantido, necessita perseverança e esforço. Tudo ainda é novo.",
        "love": "Tem interesse, deseja namorar ou se envolver com alguém, tem espontaneidade, busca por ser feliz, é naturalmente sedutor, sabe conquistar, gosta de conversar. Faz tudo para melhorar a relação.",
        "free_person": "Flerte, muita sedução, namoro passageiro, gosta mas não faz esforço, até quer algo mais sério, mas tudo depende o quão bom serão os momentos juntos.",
        "taken_person": "Melhoria no relacionamento, reconquista, quer buscar o tempo perdido, tem atitudes inovadoras, quer estar junto, está sempre pronto. Traz novos caminhos no relacionamento, faz planos para o futuro, como ter filhos, casamento, mudança de casa.",
        "obstacle": "Dificuldade em agir, em se posicionar. Dificuldade em tomar a frente, em ter atitude.",
        "advice": "É o momento de dialogar, não dá para esperar só as forças do destino agir. Precisa recriar, se mexer, buscar possibilidades para se alcançar aquilo que deseja."
    },
    {
        "id": 2,
        "name": "A Sacerdotisa",
        "major": True,
        "description": "Refletir, estudar, analisar. Intuição, privacidade, mistério. É reservada, passiva, enigmática e inteligente. A simbologia da carta traz o yin e o yang como um dos seus mistérios. A capacidade de ser feminina, intuitiva e ao mesmo tempo mais fria, mais racional, analítica. Arquétipo de uma grande sábia, que possui todo o conhecimento oculto universal, mas não deseja compartilhá-los com ninguém. A figura da Sacerdotisa é um símbolo da passividade ativa, então precisa sempre se atentar para agir mais, falar mais, buscar mais, sair da inércia, pois tem uma natureza mais lenta. Tem domínio, magnetismo, poder pessoal. Ela nos ensina que nem sempre precisamos agir ou buscar respostas externamente, mas que encontramos as respostas dentro de nós mesmos, por meio da escuta interior e da confiança em nossa intuição. Pode representar momentos onde guardamos um segredo, estamos mais quietos, com menos interação com o mundo e mais observadores. Situações no dia a dia que o processo acaba sendo mais lento.",
        "work": "Vida profissional segura, estável, mas rotineiro, sem novidades, sem possibilidades de promoção, sem emoção, sem expressão ou ação para mudar por enquanto.",
        "financial": "Orçamento apertado, pode não haver dívidas, mas também não há crescimento financeiro, tudo se mantém como está, sem muitas condições de mudar a situação atual. Burocracia, pode depender de terceiros para realizar algo. Contrato ou negociação em análise. Estagnação.",
        "love": "É conservador, pouco rígido, não fala exatamente o que está sentindo ou pensando, não gosta de ter iniciativa, espera sempre que o outro faça. Tudo permanece como está. Pode haver ressentimento antigo, carência afetiva.",
        "free_person": "Pensa em se relacionar mas não tomará nenhuma atitude. Se estiver solteiro, sem conversar com ninguém, continuará assim. Sente que é amado por outra pessoa. Falta autoestima. Muita conversa e pouca ação.",
        "taken_person": "Não fala o que pensa, não se expressa sexualmente, nada muda na relação, se estiverem bem, assim permanece. Se houver problemas conjugais, irá resultar em ressentimento.",
        "obstacle": "Segredo, silêncio, inércia, demora",
        "advice": "Analisar tudo com cuidado, não é o momento de falar o que pensa, não há nada de muito errado, mas precisa de calma e atenção. Melhor esperar."
    },
    {
        "id": 3,
        "name": "A Imperatriz",
        "major": True,
        "description": "Alegria, amor, prosperidade, fertilidade, cuidado, autocuidado, caminhos abertos, boas expectativas, bem-estar. (acompanhada com a carta 4 de paus, ás de paus, estrela, ficar atento à gravidez). Pode indicar mãe ou mulher com características maternas, pois na carta encontramos uma mulher grávida e o símbolo de Vênus, indicando feminilidade, atributos da energia yin. É romântica, esperançosa, gosta de ganhar atenção. É comunicativa, busca socializar. Simboliza a feminilidade, a sensualidade e a conexão com a natureza. Ela representa a capacidade de criar e nutrir a vida em todas as suas formas. Essa carta está associada à fertilidade, à maternidade, ao amor e à beleza. Representa a criatividade e a expressão artística, sugere um período fértil para o desenvolvimento de ideias, projetos e talentos criativos. Além disso, a carta da Imperatriz simboliza a abundância e a sofisticação. Também representa a capacidade de cuidar de nós mesmos e dos outros, proporcionando um ambiente seguro e acolhedor.",
        "work": "Realizações, promoção ou reclassificação profissional. É bem visto na profissão e entre os colegas, clientes. Continuar com as metas, não perder o foco. Chance de crescimento, criatividade, soluções e realizações.",
        "financial": "Prosperidade, lucro, pode indicar compras ou boas aplicações. Orçamento equilibrado.",
        "love": "Felicidade, romantismo, confiança, amor, sensualidade, prazer, desejo. Sabe o que quer, tem um objetivo afetivo. Não suporta mentiras ou enrolação. Nutre uma relação. Quer namorar, gosta de ser mimado, quer ser amado.",
        "free_person": "Deseja namorar, se sente seguro, tem muita atração.",
        "taken_person": "Melhoria no âmbito familiar, amor maduro e fiel com bons planos para o futuro a longo prazo, planos de formar família, ter filhos.",
        "obstacle": "Carência, falta de autoconfiança, falta de afeto. Podendo também retratar uma pessoa.",
        "advice": "Não perder tempo com pensamentos inúteis, não duvidar, seguir em frente, aproveitar as oportunidades. Dar atenção à beleza, feminilidade, sensualidade, cuidar de si. Nas relações, cuidar dos demais, ser educado e gentil."
    },
    {
        "id": 4,
        "name": "O Imperador",
        "major": True,
        "description": "Influência, autoritarismo, controle, organização, moralidade, figura masculina de poder (pai, chefe, marido). Está sentado no trono, delega funções, manda e desmanda, carrega uma coroa e um cetro que indica esta posição de poder. Tem capacidade de resolver seus problemas, administra e organiza. Não gosta de mudanças, só sairá do seu conforto em casos muito extremos. É competente, seguro, rígido, vence, realiza. Podendo ser inflexível, conservador, julgador, egoísta, ríspido ou possessivo. Simboliza a energia da força masculina, a liderança e o senso de ordem e disciplina. Representa o poder e a capacidade de assumir responsabilidades, estabelecer limites e criar estruturas sólidas. Está associada à autoridade e à habilidade de tomar decisões assertivas. Pode representar a figura de um governante ou líder que é respeitado e confiante em suas ações. Energia doméstica, estável, imutável no momento.",
        "work": "Segurança, estabilidade profissional, mas sem previsão de melhorias ou promoção, trabalha bem pois tem disciplina e experiência.",
        "financial": "Estabilidade momentânea, sem mais ganhos no momento. Tudo se mantém como está, consegue organizar suas finanças. Busca organizar a vida. Momento de guardar dinheiro, pagar dívidas e não exagerar.",
        "love": "Egoísmo, possessividade, deseja controlar e não aceita rejeição. Ora é apegado ora insensível. Indica relação duradoura, Pode indicar união por conveniência afetiva ou social. Avaliar o contexto do jogo para entender se existe amor realmente.",
        "free_person": "Não deseja namorar, só pensa no aqui e agora, coração fechado, não quer se entregar, sente atração porém individualista.",
        "taken_person": "Deseja um futuro longo juntos, protege, controla. Pode indicar falta de carinho e afeto. Futuro relacionamento conservador.",
        "obstacle": "Rigidez, controle, autoritarismo, inflexibilidade. Pode indicar uma pessoa.",
        "advice": "Não fraquejar, não se deixar levar por influências, manter sua autoridade, mandar e controlar."
    },
    {
        "id": 5,
        "name": "O Papa",
        "major": True,
        "description": "Tradicionalidade, conservadorismo, contratos, legalidade, acordos. É conservador, possui crenças enraizadas, virtude e moralidade. Tem disciplina, faz o que é correto, o combinado. Integridade. Bons costumes, valores, crenças espirituais, religião, estudo. Em suas mãos a representação de tudo o que há em cima há embaixo (princípio hermético). O papa traz um sinal de respeito, que exige uma moral e bom costume perante a sociedade. Podendo ser este também o motivo de uma pressão social. Ele sugere também a importância de seguir os princípios éticos e morais em nossas ações e decisões. Pode indicar estudos, busca por reconhecimento social. Representa autoridade espiritual, tradição, sabedoria e ensinamentos formais. Simboliza a busca por conhecimento espiritual, orientação de mentores. É um convite para buscar sabedoria e orientação espiritual, reconhecendo a importância da tradição e dos ensinamentos aprendidos. Em seu lado positivo faz conciliações, acordos, harmoniza, é flexível. No negativo é hipócrita faça o que eu digo mas não faça o que eu faço.",
        "work": "Estabilidade, forte influência social, admirado pelos colegas de trabalho/profissão, não indica promoção mas pode trazer melhorias futuras. Pode envolver acordos, contratos, questões burocráticas.",
        "financial": "Reorganização, sem gastar muito, precisando poupar um pouco, mas sem prejuízos. Acerto de dívidas depois de um período mais difícil. Atenção se precisar negociar algo.",
        "love": "Fidelidade, afeição, confiança, respeito, preservação. É tradicional, conservador, familiar, busca honrar o combinado, os acordos.",
        "free_person": "Quer namorar, mas tudo depende das atitudes do consulente, pode não ter atração sexual. Só irá virar namoro se ambos colaborarem nas ações, ao menor sinal de desrespeito, tudo acaba. Não deseja flertar por flertar.",
        "taken_person": "Fidelidade, carinho, atenção, promessas que são cumpridas, casamento. Sexo pode estar pouco atrativo, muito metódico, sem emoção. Relacionamento bem visto pela sociedade.",
        "obstacle": "Crenças, moralidade, influências sociais, burocracia.",
        "advice": "Não permitir que outras pessoas lhe digam o que fazer, tenha opinião. Agir dentro das regras, leis, cumprir os acordos. Ser fiel e honesto."
    },
    {
        "id": 6,
        "name": "Os Enamorados",
        "major": True,
        "description": "Escolhas diárias, possibilidades, dúvida entre duas opções, caminhos abertos, necessidade de socializar, livre-arbítrio. Simboliza a dualidade e a necessidade de fazer escolhas. Aqui os desejos começam a ser aflorados, as possibilidades são percebidas e por isso começa a gerar a dúvida. Na carta vemos a representação de Adão e Eva, sugerindo algo primitivamente puro, podendo haver uma benção do anjo acima, ou julgamento. Ela representa o momento em que nos deparamos com uma encruzilhada e somos confrontados com decisões que podem ter um impacto profundo em nossa vida emocional. A dualidade também pode se referir à escolha entre duas opções ou caminhos diferentes em outras áreas da vida, não apenas no amor. Pode representar a necessidade de decidir entre o coração e a razão, entre o que é seguro e familiar e o que é novo e desconhecido. Em seu lado positivo, traz opções, nada fica parado ou estagnado, podendo haver sociedades, desenvolvimento, romantismo. Já no lado negativo, dúvidas por influências externas, opiniões.",
        "work": "Melhoria profissional podendo haver uma novidade importante. Nova proposta de trabalho, freelancers, bons acordos. Trabalho que vem rápido, traz lucro, mas pode não ser fixo ou duradouro.",
        "financial": "Aumento de capital, tem recursos para saldar dívidas ou comprar algo importante. Aumento do poder de compra. Investimento que traz lucro.",
        "love": "Aumento de capital, tem recursos para saldar dívidas ou comprar algo importante. Aumento do poder de compra. Investimento que traz lucro.",
        "free_person": "Quer namorar, tende a virar amor, mas obstáculos podem aparecer para impedir. Sente uma atração física muito forte. Futuro incerto pois depende da conexão física e pode haver competição com outras pessoas, e até influência negativa familiar. Novidades chegando, podendo ser um novo relacionamento.",
        "taken_person": "Busca melhorias na relação, se questiona pensando em evoluir, ama e está muito feliz, busca casar, construir até uma família. Momento de felicidade na relação. (Se acompanhada com cartas de traição, pode indicar uma infidelidade por existir uma terceira pessoa, analisar o contexto do jogo).",
        "obstacle": "Dúvida, influência de terceiros.",
        "advice": "Buscar uma conciliação, ser gentil, socializar, não discutir, momento de agir de forma prática aceitando as diferenças."
    },
    {
        "id": 7,
        "name": "O Carro",
        "major": True,
        "description": "Autoconfiança, autoestima, poder pessoal, realização, caminho da vontade, do impulso, desenvolvimento, crescimento, popularidade, entusiasmo, emoções intensas podendo causar dúvidas. Viagem, distância física. Ir viajar ou precisar ir para uma outra região/cidade/estado. Suas vestimentas são luxuosas e traz consigo o poder de conduzir, dirigir. É necessário puxar as rédeas, não agir somente no impulso mas saber direcionar para onde se está indo. Para quem não sabe onde quer chegar, qualquer lugar serve, é necessário ter foco, para não se perder. A simbologia da Esfinge branca e preta (positivo e negativo) representam as forças opostas que precisam ser equilibradas e coordenadas para se alcançar o sucesso, caso não haja controle, acontecerá um desequilíbrio, o egocentrismo tomará conta. É uma carta que traz movimento, tudo é rápido. Pode representar viagem, distância física, deslocamento.",
        "work": "Se destaca, lidera. Pode haver promoção, desenvolvimento, possível indicação em nova função ou novo local de trabalho (cidade, região).",
        "financial": "Melhoria no orçamento, lucro, prosperidade. Cuidado com gastos excessivos, egocêntricos. Dívidas são resolvidas.",
        "love": "Entusiasmo, atração física, carinho, amor, impulsos do coração, diversão, desejos, popularidade, socialização.",
        "free_person": "Deseja namorar, mas também está atento a outras opções, sente muita atração física, está empolgado com a relação, vê tudo com muita intensidade. Pode começar uma nova relação, porém ficar com dúvida entre outro pretendente.",
        "taken_person": "Quer progredir na relação, busca sempre melhorar, tem muita atração física, se entrega totalmente, ama profundamente, quer casar, construir um futuro. Pode estar planejando/querendo alguma viagem.",
        "obstacle": "Excesso de autoconfiança, dificuldade de fazer escolhas (também podendo indicar viagem, algo distante).",
        "advice": "Agir imediatamente, seguir em frente, ter autoconfiança. Ser ágil, comunicativo, enérgico, sociável."
    },
    {
        "id": 8,
        "name": "A Força",
        "major": True,
        "description": "Controlar e dominar com paciência e tolerância, ter inteligência emocional. Argumentar com convicção, empatia, calma. Necessidade de autocontrole de sentimento e ações. Traz passividade, necessidade de refletir, agir com cautela e consciência. Se redimir, perdoar. Conexão espiritual que traz consciência e compaixão. Ela representa a capacidade de superar desafios e lidar com dificuldades por meio do equilíbrio e do controle emocional. A figura da mulher segurando o leão mostra a força gentil, que é capaz de domar e direcionar a energia bruta. A figura feminina na carta personifica a energia da compaixão, paciência e domínio de si mesma. Ela não utiliza a força bruta, mas sim a suavidade e a empatia para controlar o leão. Isso nos lembra que a verdadeira força vem de um lugar de amor e compreensão, em vez de agressividade. Tudo pode se resolver com inteligência emocional.",
        "work": "Bem visto e querido no ambiente de trabalho, estabilidade, administra bem o trabalho mas sem mudanças ou melhorias. Tudo permanece como está. Se precisa de novidades, pode demorar para chegar, necessita paciência.",
        "financial": "Organização, controle de gastos, economias e controle que fazem aumentar o capital a longo prazo.",
        "love": "Magnetismo, ama e quer estar próximo a seu amado, quer proteger, é feliz, sensível. Busca se redimir, perdoar e ser perdoado.",
        "free_person": "Pensa em namoro, é sincero, sente carinho e atração física. Pode indicar uma época sem muitas novidades para os solteiros.",
        "taken_person": "Satisfação, carinho, compreensão, paciência. Pode indicar desejo de fazer as pazes, se redimir e perdoar.",
        "obstacle": "Perdoar, compreender, aceitar, ter paciência.",
        "advice": "Ter coragem, não ter medo, não ouvir opiniões negativas, ter fé e acreditar. Agir com calma, empatia e paciência."
    },
    {
        "id": 9,
        "name": "O Eremita",
        "major": True,
        "description": "Sabedoria, iluminação, pesquisa, interiorização. Simboliza introspecção, sabedoria e busca interior, lentidão, autoconhecimento. Abrir mão de coisas e pessoas em prol de um futuro. Ele representa um período de retirada, reflexão e solidão voluntária, onde se procura a iluminação pessoal e o conhecimento interior. Ele representa um período em que é importante se afastar do mundo exterior para se conectar mais e buscar respostas profundas. A lanterna que o Eremita segura simboliza a luz da sabedoria que ele traz consigo e que guia seu caminho. O Eremita nos lembra da importância de reservar tempo para o autoconhecimento, de se afastar do barulho externo e da rotina da vida cotidiana, a fim de encontrar clareza e orientação espiritual. Pode trazer um período de individualidade, silêncio, isolamento, rompimentos, afastamentos. Necessidade de buscar a essência, para isso é necessário afastar-se. Eremita escolhe andar só em busca de sabedoria.",
        "work": "Segurança, rotina, cumpre bem suas obrigações, mas sem possibilidade de crescimento ou mudança, tudo fica do jeito que está (bate o ponto, cumpre com suas responsabilidades e vai embora sem muita vontade de continuar, sem expectativas).",
        "financial": "Orçamento limitado, necessidade de economia, não há prejuízos, mas também não há lucros.",
        "love": "Calma, conforto, respeito, mantém sua privacidade e tenta ter sabedoria para compreender os revezes da vida. Busca isolamento. Pode precisar de espaço.",
        "free_person": "Não nutre sentimentos, planeja ficar sozinho, pode indicar que será apenas amizade, podendo se afastar no futuro.",
        "taken_person": "Maturidade nas ações, fidelidade, busca ser honesto e compreensivo. Casal pode passar por um período de responsabilidades e pouco libido.",
        "obstacle": "Isolamento, exclusão, término, demora.",
        "advice": "Ter paciência, esperar, dar um tempo, se recolher, se afastar para refletir, buscar o equilíbrio interior."
    },
    {
        "id": 10,
        "name": "A Roda da Fortuna",
        "major": True,
        "description": "Mudanças, incertezas, instabilidade, reviravoltas, altos e baixos, mudanças repentinas na rotina, interferência de terceiros (trabalho, família…), problemas passageiros. Acompanhada de cartas positivas pode indicar golpe de boa sorte. Porém se acompanhada com cartas de desafios, indica que algo precisa ser 'revisto/refeito'. Simboliza a natureza cíclica da vida, as mudanças inevitáveis e as reviravoltas do destino. Ela nos lembra que tudo está em constante movimento e que os altos e baixos são uma parte essencial da existência humana. A Roda da Fortuna também está ligada à noção de karma, sugerindo que nossas ações passadas e presentes têm consequências e impactam nosso destino. Podendo trazer desde ciclos repetitivos, até mudanças inesperadas, mas seu objetivo é: lhe colocar de novo em frente a uma situação que não foi totalmente resolvida, como um karma que ainda não foi compreendido, não está consciente. É voltar e voltar nos mesmos problemas até que finalmente evolua.",
        "work": "Possibilidade de fofocas, desgaste na rotina. Mudança de local ou de rotina profissional, tudo muda de repente, mas não afeta o financeiro.",
        "financial": "Gastos além do orçamento por falta de limite pessoal, período instável. (Dependendo do arcano que acompanhar pode indicar compra, venda ou negociação, com lucros ou perdas). Mas nada se mantem estável por muito tempo.",
        "love": "Sentimentos inconstantes, podem gerar ansiedade, medo, nervosismo desnecessário. Novos interesses, mudança de pensamentos. Ciclos repetitivos.",
        "free_person": "Não sabe o que sente e o que deseja, inconstante e ansioso, tudo é incerto, possibilidade de surgir outras opções, novo pretendente.",
        "taken_person": "Ideias equivocadas, ansiedade, nervosismo, rixas afetivas. Podendo haver separação em função de alguma mudança no trabalho ou estudos.",
        "obstacle": "Ansiedade, reviravoltas, mudanças inesperadas, reviver situações passadas.",
        "advice": "Aceitar as mudanças, não ficar parado, não deixar estagnar, ser flexível, tomar cuidado com ansiedade e pensamentos dispersos."
    },
    {
        "id": 11,
        "name": "A Justiça",
        "major": True,
        "description": "Prudência, cautela, ordem, disciplina, direito, razão. Racionalidade, frieza, decisão, seriedade. Lei, jurídico, regras, legalidade, processos. Representa a necessidade de tomar decisões justas e éticas, levando em consideração todos os aspectos relevantes de uma situação. Necessidade de equilibrar diferentes perspectivas, considerar os prós e contras, e avaliar as consequências de nossas ações. Ação e reação, tudo terá uma consequência. A balança que a Justiça segura simboliza a ponderação, a análise e a consideração de todos os aspectos antes de tomar uma decisão. A espada representa a força e o poder da verdade, que podem ser usados para promover a justiça. Traz a importância da lei kármica da ação e reação, toda ação tem uma consequência. O preto no branco, bateu levou do Universo, fez o certo? Vai levar o certo! Fez o errado? Vai levar o errado.",
        "work": "Cuidado com a conduta, com a postura profissional, e até mesmo a aparência, está sendo observado/avaliado, evite estar em contato com fofocas. Período delicado.",
        "financial": "Pouco dinheiro circulando, precisando reavaliar os gastos, não fazer novas dívidas, não emprestar dinheiro nem pegar emprestado. Manter a ordem.",
        "love": "Frieza, muita racionalidade, isolamento. Sem atração física ou demonstração de afeto. Preocupa-se mais com o mundo material, não dando atenção ao emocional.",
        "free_person": "Não pensa em namorar, não nutre sentimentos nem desejos, podendo ser um pouco moralista, julgar o outro.",
        "taken_person": "Problemas na afinidade/comunicação, falta de carinho e atenção, distanciamento, necessário evitar conflitos para não gerar separação. Pode haver pressão na relação.",
        "obstacle": "Cobranças, exigências, frieza, indelicadeza (moralismo), questões judiciais.",
        "advice": "Agir corretamente, com ética, mantendo um bom comportamento. Atenção às consequências das atitudes e escolhas. Caso esteja passando por um período ruim, entender que pode ser frutos de escolhas passadas."
    },
    {
        "id": 12,
        "name": "O Enforcado",
        "major": True,
        "description": "Renúncias, sacrifícios, ilusões, utopia, vitimização, desânimo, estagnação, desconforto. Representa a necessidade de soltar, deixar ir e permitir que as coisas sigam seu curso natural. Virar do avesso, enxergar as coisas por um outro ângulo, fazer diferente do que se faz normalmente. Ele nos lembra que, às vezes, precisamos abrir a mão do controle, suspender nossas expectativas e permitir que a vida se desenrole de acordo com seu próprio ritmo. Ao pendurar-se de cabeça para baixo, o Enforcado nos convida a mudar nossa perspectiva e enxergar as coisas de maneira diferente. Ele nos desafia a questionar nossas crenças, padrões de pensamento e visão de mundo, a fim de obter uma compreensão mais profunda e ampla da vida. Quem está passando pela fase do Enforcado tem muita dificuldade de enxergar e aceitar seu estado atual, causando brigas, frustrações e desilusões por constantemente culpar o externo pelos episódios que vem vivenciando. Sendo assim, a única maneira de mudar seu estado atual é a mudança de visão, de perspectiva.",
        "work": "Dificuldades para executar tarefas, dificuldades para se expressar, bloqueio criativo, estagnação, não se sente apto ou não se sente feliz, porém sem riscos de demissão ou mudança no momento.",
        "financial": "Pouco dinheiro circulando, existem muitas ilusões com o dinheiro, a pessoa não consegue enxergar a realidade e cria fantasias arriscadas. Cuidado para não acumular dívidas.",
        "love": "Amargura, angústia, lamentação, falta de amor próprio, dependência afetiva, ressentimento, baixa autoestima.",
        "free_person": "Pensa ou sofre por outra pessoa, dificuldades com o passado, não sente atração física, não quer fazer dar certo.",
        "taken_person": "Problemas com o passado, não consegue superar uma situação, está triste, sem expectativas, ama mas está insatisfeito.",
        "obstacle": "Ilusão, ansiedade, negação, dificuldade de aceitar a realidade.",
        "advice": "Cuidado com a utopia, é necessário mudar o comportamento, o ideal é se manter calado, distante dos problemas, refletir mais e não tomar nenhuma decisão no momento."
    },
    {
        "id": 13,
        "name": "A Morte",
        "major": True,
        "description": "Encerramento, transformações, transmutação, mudanças drásticas de realidade. Mudanças físicas (casa, trabalho, cidade). Renascimento. Luto (não necessariamente por pessoas, mas por uma fase da vida que se foi). Transformação significativa e uma transição para um novo estágio na vida. Simboliza o ciclo natural da vida, onde o fim de algo abre caminho para o início de algo novo. Ela simboliza o fim de um ciclo, o encerramento de uma fase e a necessidade de deixar para trás o passado para dar lugar ao novo. A bandeira negra representa o luto, mas também a purificação e a renovação. O sol nos lembra que existe um novo renascer, um novo dia, que a transformação é essencial para o crescimento pessoal e espiritual. Assim como as estações do ano, a morte de uma fase permite que uma nova fase floresça. A carta da Morte não deve ser interpretada literalmente como morte física. Ela representa a morte de padrões, crenças, relacionamentos ou situações que já não nos servem mais. É um símbolo de fim e de renascimento, tanto internamente (pensamento e padrões de comportamento), quanto externamente (mudanças físicas como casa, trabalho…)",
        "work": "Reclassificação profissional, possível mudança de cargo, cidade, região. Melhoria, novas oportunidades.",
        "financial": "Reorganização financeira, investimento, poupança, lucros a médio e longo prazo. Pode indicar alguma mudança na forma de ganhar o dinheiro dependendo dos arcanos que o acompanham.",
        "love": "Mágoas, rancor, egoísmo, dificuldades com o passado, dificuldade de perdoar. Afastamento, términos.",
        "free_person": "Não deseja namorar, não nutre sentimentos, podendo ainda não ter superado o passado. Frieza, distância, indica que a pessoa futuramente pode encontrar um outro pretendente que interesse mais.",
        "taken_person": "Angústia, falta de carinho e atenção, tendência a brigas e afastamento, podendo haver separação temporária por fatores externos (viagem, trabalho, estudo, família).",
        "obstacle": "Encerramento de ciclo, término. Insensibilidade, dificuldade de deixar o passado.",
        "advice": "Mudar os pensamentos, não ter medo de fazer mudanças, de transformar-se, e se abrir a novos caminhos. Mudanças precisam acontecer."
    },
    {
        "id": 14,
        "name": "A Temperança",
        "major": True,
        "description": "Harmonia, equilíbrio, longevidade, paciência, autocontrole, adaptação, flexibilidade, nada se realiza a curto prazo, pois necessita calma, tempo e dedicação. A Temperança simboliza uma combinação harmoniosa de elementos opostos. Ela nos lembra da importância de encontrar um equilíbrio entre diferentes aspectos de nossa vida, como trabalho e lazer, razão e emoção, espiritualidade e materialidade. Simboliza a busca pelo equilíbrio e pela moderação em todas as áreas da vida. A importância de encontrar o ponto intermediário, de evitar extremos. Os vasos que o anjo segura representam uma necessidade de equilibrar as energias e emoções em nossa vida. A simbologia dos pés, um dentro d'água e o outro fora, representa o equilíbrio entre o emocional e o racional, como diz o ditado: \"Um pouco de droga e um pouco de salada\". A Temperança também carrega uma energia de renovação, depois da carta 13 da Morte, a Temperança vem como uma folha em branco, uma chance de adicionar coisas novas a uma nova energia. Também carrega a necessidade de ser flexível, moderado e cauteloso. No lado negativo pode trazer preguiça, enrolação, passividade.",
        "work": "Trabalho estável, sem mudanças à vista, cuidado em querer mudanças muito radicais no momento, tudo deve ser mantido como está, caso desejar mudanças, fazer isso aos poucos sem pressa, se planejando e se organizando.",
        "financial": "Orçamento equilibrado, podendo ficar um pouco apertada as finanças, o ideal seria não fazer investimentos, pensar a longo prazo.",
        "love": "Tranquilidade, carinho, amor, podendo haver tédio, preguiça de expressar sentimentos.",
        "free_person": "Não pensa em namorar, pode ficar na amizade, pois não tem atração física, desejo. Confia como amigo, mas não ama como amante.",
        "taken_person": "Tranquilidade, segurança, possui carinho e amor, planeja a longo prazo, mas pode se sentir entediado, os problemas são resolvidos com o tempo, sem muitas mudanças por enquanto. Necessita cuidado para não 'empurrar com a barriga' situações.",
        "obstacle": "Preguiça, demora, falta de atitude, passividade.",
        "advice": "Ter paciência, não discutir, buscar ser flexível e manter uma boa relação com os demais."
    },
    {
        "id": 15,
        "name": "O Diabo",
        "major": True,
        "description": "Vaidade, desejo, medo, nossas sombras, ansiedade, enfermidade, orgulho, ego, controle, mentiras, omissões, obsessão, ciúme. Representa os desejos materiais excessivos, as compulsões e os comportamentos autodestrutivos, tentação da influência negativa que podem surgir em nossas vidas, prendendo-nos em padrões. Está relacionada à sexualidade, à luxúria e aos desejos carnais. O Diabo representa as correntes que nos mantiveram presos a padrões de comportamento negativo, crenças limitantes e vícios que nos impedem de seguir em nossa jornada espiritual e pessoal. Ele nos alerta para a necessidade de confrontar nossos medos e enfrentar as partes fisiológicas de nós mesmos, a fim de nos libertarmos dessas amarras. Existem mecanismos do Ego que tentam nos controlar e acabam por ficarem inconscientes, aqui é o momento de trazê-los à tona. Ele pode representar a busca pelo prazer imediato, muitas vezes às custas de valores mais elevados ou responsabilidades pessoais. O diabo também pode representar uma situação de medo, ansiedade, onde a pessoa é tomada por pensamentos negativos. Deve-se estar atento à saúde do corpo físico, Diabo pode indicar algum problema de saúde.",
        "work": "Competitividade, ousadia, sagacidade, ambição, destaque entre colegas de trabalho, tendo um bom relacionamento. Podendo indicar também um período de medo e preocupações dependendo dos arcanos que lhe acompanharem.",
        "financial": "Boa quantia de dinheiro circulando, pagamento de dívidas, acerto de contas, porém não valoriza o que ganha. Risco de querer fazer dinheiro de forma ilícita.",
        "love": "Paixão, desejo, vontade, prazer, atração, impulsividade, posse, dependência, vaidade, quer muita atenção. Omissão, mentira.",
        "free_person": "Joguinho de sedução, deseja ter o controle da relação, gosta, quer se relacionar, mas com tendência a posse, controle e ciúmes. Pode indicar relação sendo construída, mas com tendência a brigas e desconfiança.",
        "taken_person": "Não confia no parceiro, por maiores que sejam as provas de fidelidade, forte paixão, mas com angústia por causa do medo de perder.",
        "obstacle": "Mentira, omissão, medo. Deve-se atentar também à saúde. (Pode indicar enfermidade).",
        "advice": "Ser egoísta, pensar apenas em si para chegar onde deseja, dar valor e atenção às suas próprias necessidades. Ter audacioso, ambicioso."
    },
    {
        "id": 16,
        "name": "A Torre",
        "major": True,
        "description": "Desconstrução, rompimento, mudança radical e inesperada de circunstâncias podendo causar dor da desilusão, do abandono, da rejeição, perda de status ou de controle. É um alerta de que nem sempre podemos evitar eventos disruptivos ou situações caóticas, e que às vezes é necessário passar por essas experiências para criar um novo começo. Pode indicar a necessidade de abandonar, desconstruir velhos padrões, crenças limitantes ou situações que já não nos servem mais. Se quebrar algo é hora de jogar fora e comprar outro, se brigar com alguém é hora de seguir em frente e não ficar lamentando o passado. Simboliza eventos inesperados, caóticos que fazem a pessoa \"perder o controle\". Embora possa ser um processo doloroso, nos lembra que a destruição pode abrir o caminho para a reconstrução e o crescimento pessoal. Se deu errado, quebrou ou desestabilizou, é porque algo não estava \"firme\". Através da destruição, podemos encontrar a oportunidade de reconstruir nossas vidas em bases mais sólidas e autônomas. A Torre pode simbolizar tanto eventos do dia a dia de forma externa, como experiências internas como: desconstruir a imagem que tinha sobre uma determinada pessoa ou relação.",
        "work": "Mudança indesejada, conflitos, rompimentos, contrato ou palavra não cumprida, podendo trazer atrasos ou prejuízos.",
        "financial": "Prejuízo ou perdas inesperadas, acúmulo de dívidas ou atraso em pagamentos, levar calote. Dificuldade de acertar as finanças.",
        "love": "Dificuldades, desacordos, brigas, rompimentos, situação caótica com muitos obstáculos trazendo desilusão, medo do futuro, rancor, decepção, orgulho ferido, vingança, sensação de abandono, sente-se traído.",
        "free_person": "Não pensa em se relacionar, desgosto, ama outra pessoa, pode ter algum trauma que afeta o sexual, tende a gerar traições, fazendo-se afastar, terminar.",
        "taken_person": "Pensa em separação, está decepcionado, sente-se rejeitado, desvalorizado. Pode gerar mágoas e desentendimentos na relação causando uma possível separação. Pode indicar um evento de traição.",
        "obstacle": "Rompimento inesperado, mudança de planos caótica.",
        "advice": "Mudar urgentemente as atitudes, a forma de pensar, perdoar e romper com aquilo que traz sofrimento, não ter medo do futuro ou de desagradar pessoas."
    },
    {
        "id": 17,
        "name": "A Estrela",
        "major": True,
        "description": "Inspiração, fé, boa esperança, serenidade, cura, libertação, realização, sonho realizado, conquistas, sucesso, revelação de boas notícias e período de evolução. Ela sugere a presença de energias positivas que nos ajudam a superar desafios e encontrar o equilíbrio emocional. As estrelas ao fundo simbolizam a conexão com o divino e com o plano espiritual muito mais aflorada. A simbologia dos jarros de água sendo derramados, representam a fase de libertação com as mágoas do passado, a água representa o emocional que vem sendo curado. O fato dela estar nua também reafirma a fase da libertação, da renovação, livre de qualquer influência do passado. Como a Fênix, ela ressurge das cinzas para reviver. A Estrela vem trazendo a confiança, a serenidade e a renovação da esperança. Ela representa a esperança que surge após períodos difíceis, trazendo consigo a promessa de um futuro melhor. Essa carta nos lembra que, mesmo nas situações mais externas, sempre há uma luz a ser encontrada.",
        "work": "Expansão, crescimento, realizações, possibilidade de promoção ou aprovação. Ótimo relacionamento com pessoas no trabalho.",
        "financial": "Equilíbrio, vive bem com o que possui, sente-se feliz e próspero, possibilidade de aumento de capital, bons investimentos a curto prazo, tudo acontece como planejado.",
        "love": "Tranquilidade, otimismo, autoconfiança, sensibilidade, empatia, carinho, respeito, fidelidade.",
        "free_person": "Deseja namorar, tem carinho, se identifica, podendo até nascer um amor verdadeiro. Está aberto a um futuro relacionamento com dedicação e cuidado.",
        "taken_person": "Ideias positivas e otimistas para a relação, se sente seguro, é fiel, tem amor e se sente naturalmente atraído fisicamente. Relacionamento feliz, com amor e reciprocidade.",
        "obstacle": "Excesso de expectativas, sonhar demais.",
        "advice": "Ter esperanças mesmo diante de situações difíceis, confiar no Universo, buscar amor próprio e autoconfiança."
    },
    {
        "id": 18,
        "name": "A Lua",
        "major": True,
        "description": "Inconsciente, mistérios da mente, imaginação, autoconhecimento, crise existencial, fantasias, ilusões, confusão entre o que é real e o que é imaginário. A carta da Lua simboliza a intuição, o subconsciente e as emoções profundas. Ela nos lembra que nem tudo é o que parece superficialmente e que existe um mundo interior complexo e rico dentro de nós. Nos convida a mergulhar em nossas emoções e explorar os mistérios de nossa psique. Nos alerta para a importância de prestar atenção às nossas emoções e de confiar em nossa intuição para nos guiar. Nos desafia a questionar as aparências e explorar as verdades ocultas. A lua é um astro iluminado pela luz do sol, enxergamos a lua no céu, como algo brilhante, mas na verdade é uma ilusão. A lua por si própria é somente escuridão. Portanto, no dia a dia, são episódios que se apresentam de uma forma, mas no fundo escondem uma outra versão. Podendo acontecer da pessoa não enxergar a realidade, por estar criando fantasias e expectativas irreais, causando ansiedade, medo, nervosismo, ciúmes e dependência emocional.",
        "work": "Melhoria profissional, podendo haver competição ou concorrer para um melhor cargo. Aumento da carga de trabalho mas com resultados positivos. Popularidade, muitas amizades, ajuda vinda de terceiros. Indicação de um amigo para uma vaga.",
        "financial": "Melhoria financeira, aumentando o fluxo de dinheiro, pagamentos, ganhos.",
        "love": "Paixão, ciúmes, medo de perder, deseja ser amado e reconhecido, romantismo beirando a dependência.",
        "free_person": "Falta de autoestima, sente muita atração, mas tem medo de amar, possíveis ilusões, com crises por ciúmes e fantasias.",
        "taken_person": "Confusão mental que atrapalha de enxergar a realidade, ama, quer estar perto porque tem medo de ficar sozinho, ser abandonado. Brigas familiares e ciúmes podem atrapalhar a relação.",
        "obstacle": "Omissão, mentira, segredo. Algo está oculto, podendo gerar apego emocional.",
        "advice": "Buscar o autoconhecimento, entender mais sobre si, seus medos e frustrações. Evitar conflitos pois não resolverá nada. Ter mais amor próprio."
    },
    {
        "id": 19,
        "name": "O Sol",
        "major": True,
        "description": "Realizações, prazer, alegria, gratidão, conquistas, nascimentos, podendo haver nascimento de criança próximo. Momentos de comemoração, caminhos abertos, sensibilidade, empatia, benevolência. O Sol representa a alegria, a diversão e a celebração da vida. Ela nos convida a desfrutar do presente e encontrar prazer nas pequenas coisas, aproveitar cada momento e encontrar a felicidade em nossa jornada. Frequentemente, há uma figura central, como uma criança ou um ser angelical, representando a pureza e a inocência. A simbologia do sol, a vitalidade, a iluminação e a consciência plena. Os girassóis são símbolos de abundância e prosperidade. A carta do Sol pode indicar tanto momentos felizes, que geram amor, até conquistas materiais, recompensas e realizações físicas.",
        "work": "Boas notícias, período de boas oportunidades, futuro promissor, bom relacionamento com pessoas ao redor.",
        "financial": "Bons fluxos financeiros, recebimento de dinheiro (de dívidas ou empréstimos), prosperidade, bons investimentos.",
        "love": "Alegria, generosidade, carinho, atração, entusiasmo, ama de uma forma pura, despretensiosa, quer encontrar a felicidade.",
        "free_person": "Quer namorar, está esperando o momento certo, sente-se alegre, quer amar, quer reciprocidade, grande possibilidade de nascer um amor verdadeiro.",
        "taken_person": "Planeja o amor para a relação, está feliz, satisfeito, período de felicidade e muita conexão.",
        "obstacle": "Excesso de confiança, de positivismo/otimismo.",
        "advice": "Aceitar ajuda dos outros, ser mais otimista, evitar se isolar, socializar."
    },
    {
    "id": 20,
        "name": "O Julgamento",
        "major": True,
        "description": "Refazer, curar, evoluir, transcender. Aceitação, libertação, acerto de contas, acerto com o passado, chance de renovação. Na carta do Julgamento, vemos figuras emergindo de caixões enquanto um anjo toca uma trombeta no céu. Isso representa a ideia de uma nova fase, um despertar para uma consciência mais elevada e a necessidade de avaliar nossas ações, escolhas e direcionamentos na vida. Os personagens estão despidos, trazendo a ideia da libertação, redenção. Simboliza a liberação de julgamentos e culpas, deixar de lado os ressentimentos e nos abrir para a cura e a transformação. O ideal é não se culpar e nem tentar achar um culpado, existem episódios que precisam acontecer por uma questão kármica de evolução. Essa carta representa a oportunidade de recomeçar, de se redimir e de buscar a evolução espiritual.",
        "work": "Mudança (podendo ser física, como o local de trabalho, cidade, estado) ou reclassificação profissional, melhoria na ocupação profissional, bom relacionamento com os demais no trabalho.",
        "financial": "Melhoria significativa nas finanças, aumento de salário com o passar dos meses, nova fonte de renda. Não é ideal fazer investimentos longos. (valorizar o que se tem hoje)",
        "love": "Renovação de afeto, perdão, novos pensamentos se reequilibrando, sentimentos positivos renascendo.",
        "free_person": "É atencioso, deseja se envolver, pode não dar certo uma relação por caminhos que são diferentes, mudança de casa, de trabalho ou em função de estudos. Em breve conhecerá alguém.",
        "taken_person": "Renovação de afeto, novos pensamentos mais positivos sobre a relação, novos caminhos se apresentando, deseja renovar a relação. Perdão.",
        "obstacle": "Questões de passado. Perdoar, mudar.",
        "advice": "Perdoar, seguir adiante, não se culpar. Reavaliar as próprias atitudes, não repetir o mesmo erro, usar o passado como exemplo."
    },
    {
        "id": 21,
        "name": "O Mundo",
        "major": True,
        "description": "Recomeços, realizações, um novo tempo, amadurecimento, momento de mudanças para o crescimento e evolução, conclusões positivas. Simboliza a integração e a harmonia de todas as áreas da vida. Na carta do Mundo, vemos uma figura central em uma mandala, associada ao Ouroboros (simbologia do ciclo da vida, do infinito, onde o início e o fim se conectam, da mudança, do tempo, da evolução) cercada por quatro figuras que representam os quatro elementos: fogo, água, ar e terra. A figura central está em equilíbrio, com uma fita em suas mãos, simbolizando a união e a conexão entre todos os aspectos da vida. Indica um momento da vida onde há um salto na sua evolução pessoal e espiritual. Ela representa a sensação de plenitude e de ter alcançado um estado de equilíbrio e maturidade. Simboliza também a conclusão de um ciclo e o início de um novo. Ela representa a culminação de nossos esforços e experiências, indicando um período de sucesso, reconhecimento e satisfação.",
        "work": "Melhoria profissional, conquista, mudança alcançada, tudo dentro do planejado. Questionamento sobre uma mudança de área para o futuro.",
        "financial": "Abundância, dificuldades resolvidas, busca de melhoria para aumentar o capital.",
        "love": "Felicidade, sinceridade, carinho, admiração. Amor próprio, autoconfiança. Nível mais alto de inteligência emocional e maturidade.",
        "free_person": "Deseja se relacionar mas sem compromissos ou responsabilidades, gosta, é carinhoso, podendo no futuro assumir uma relação.",
        "taken_person": "Questiona a relação para uma melhora, pensa em uma possível separação consensual, tem carinho, é sincero. Está muito confiante do que quer.",
        "obstacle": "Recomeçar, agir de forma madura, consciente.",
        "advice": "Ser independente, seja na vida amorosa, profissional ou financeira, focar mais em si mesmo, se importar mais com seus próprios objetivos."
    },
    {
        "id": 22,
        "name": "Ás de Paus",
        "major": False,
        "description": "Produtividade, oportunidades, propostas, fertilidade, vitalidade, união, bons acordos, reconciliação, inícios, criatividade, empolgação, planos que são colocados em prática que influenciam a longo prazo. Terreno fértil para novos projetos. O Ás de Paus indica uma oportunidade para canalizar sua criatividade, iniciar projetos aspirantes e buscar seus objetivos com entusiasmo renovado. Também pode ser interpretado como um sinal para aproveitar ao máximo suas habilidades e talentos únicos. É um momento para expressar-se autenticamente, confiar em sua intuição e seguir sua paixão. Essa carta sugere que você tem o poder criativo dentro de si para iniciar algo grandioso e impactante e está associado à coragem e à ação. Pode indicar convites, propostas, oportunidades.",
        "work": "Início de projetos, oportunidade de emprego, novidades, melhorias, busca por novas habilidades.",
        "financial": "Momentos favoráveis, de lucros e caminhos abertos para crescimento.",
        "love": "Alegria, amor, magnetismo, empolgação, felicidade em conversar, deseja começar uma relação. Convite para namorar. Início de relacionamento.",
        "obstacle": "Começar algo. Dialogar, Colocar suas ideias em prática.",
        "advice": "Seguir em frente com os projetos, buscar novidades. Apostar em um novo começo."
    }

]

@app.route('/', methods=['GET'])
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