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
        "suit": "clubs",
        "description": "Produtividade, oportunidades, propostas, fertilidade, vitalidade, união, bons acordos, reconciliação, inícios, criatividade, empolgação, planos que são colocados em prática que influenciam a longo prazo. Terreno fértil para novos projetos. O Ás de Paus indica uma oportunidade para canalizar sua criatividade, iniciar projetos aspirantes e buscar seus objetivos com entusiasmo renovado. Também pode ser interpretado como um sinal para aproveitar ao máximo suas habilidades e talentos únicos. É um momento para expressar-se autenticamente, confiar em sua intuição e seguir sua paixão. Essa carta sugere que você tem o poder criativo dentro de si para iniciar algo grandioso e impactante e está associado à coragem e à ação. Pode indicar convites, propostas, oportunidades.",
        "work": "Início de projetos, oportunidade de emprego, novidades, melhorias, busca por novas habilidades.",
        "financial": "Momentos favoráveis, de lucros e caminhos abertos para crescimento.",
        "love": "Alegria, amor, magnetismo, empolgação, felicidade em conversar, deseja começar uma relação. Convite para namorar. Início de relacionamento.",
        "obstacle": "Começar algo. Dialogar, Colocar suas ideias em prática.",
        "advice": "Seguir em frente com os projetos, buscar novidades. Apostar em um novo começo."
    },
    {
        "id": 23,
        "name": "Dois de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Reflexão, adiamento, atraso, imprevistos, empecilhos, necessidade de melhor avaliação ou julgamento. Projetos, planos. Atraso, suspensão causadas por terceiros, não depende apenas do consulente. Tudo é superável. Promessa não cumprida, acordos desfeitos. Planos feitos, programados para futuro. É um símbolo da energia empreendedora e da exploração de novos horizontes. Ele representa a fase inicial de um projeto, onde você está avaliando suas opções e considerando os caminhos possíveis. Podendo necessitar a participação de terceiros (sejam coisas, empresas, ou pessoas). É uma carta que reflete a necessidade de planejar com sabedoria e tomar decisões estratégicas para alcançar seus objetivos, representa o poder da escolha. Na carta observamos o personagem com o 'mundo' nas mãos e buscando o horizonte, indicando que há possibilidades futuras, mas necessitam de tempo e de esforço.",
        "work": "Imprevistos, atrasos, não apenas pelas atitudes do consulente, mas sim por fatores externos de força maior. Pode representar também um projeto em mente que necessita de empenho e tempo.",
        "financial": "Obstáculos, demora, impasse, mas sem trazer grandes prejuízos. Planos para futuro.",
        "love": "Demora para dar uma resposta, necessidade de buscar apoio de outras pessoas, dualidade, espera.",
        "obstacle": "Demora, atraso, adiamento.",
        "advice": "Analisar melhor antes de agir, repensar os próprios desejos e atitudes."
    },
    {
        "id": 24,
        "name": "Três de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Negociação, parceria, união, compreensão, cooperação, permuta, contrato, aliança, empreendimento bem sucedido, caminhos abertos, ajuda de terceiros, expansão, crescimento. Essa carta indica que você está estabelecendo bases sólidas para o futuro e que está tomando as medidas necessárias para garantir o sucesso a longo prazo. O Três de Paus também está relacionado à colaboração e à parceria. O que está ao redor neste momento (podendo ser uma pessoa, ou um trabalho, algo que o consulente se associa) pode servir como alicerce, trazendo segurança para dar os próximos passos. Pode indicar a necessidade de trabalhar em conjunto com outras pessoas para alcançar um objetivo comum. Essa carta representa a importância de compartilhar ideias, recursos e perspectivas para obter sucesso. Na carta observamos o personagem no alto da colina, indicando que já percorreu um bom caminho, e deseja conquistar mais terras. Os bastões simbolizam o apoio externo.",
        "work": "Evolução, crescimento, sucesso, soluções, parcerias.",
        "financial": "Influência de terceiros de forma positiva para uma melhoria.",
        "love": "Parceria, reciprocidade, perdão, dedicação, solução dos obstáculos. Relacionamento podendo ajudar em outras áreas da vida.",
        "obstacle": "Receber apoio, entrar em acordo.",
        "advice": "Se organizar e cooperar com o meio social, usar o que se tem ao redor ao seu favor."
    },
    {
        "id": 25,
        "name": "Quatro de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Festa, casamento, reunião, celebração, união, aliança, descanso, férias, contratos, trocas, reciprocidade, uma boa associação, segurança, boa administração, estabilidade, conquistas, lealdade, confiança. É uma representação de eventos comemorativos, como casamentos, aniversários. Essa carta indica que você alcançou um marco importante em sua jornada e que é hora de comemorar seu progresso, isso lhe dará um maior gás para continuar a jornada. Também representa estabilidade e segurança. Ela sugere que você criou uma base sólida em sua vida e que está desfrutando de um período de harmonia e paz. Junto com cartas de fertilidade (Às de Paus, Imperatriz) pode indicar gravidez.",
        "work": "Aprovação, conquista, resultado positivo, férias.",
        "financial": "Segurança, administra bem o que possui. Sem grandes mudanças. Pode haver um episódio de conquista.",
        "love": "Confiança, sorte, superação, dar um próximo passo no relacionamento, podendo juntar as escovas de dentes. Casamento, contrato.",
        "obstacle": "Acordo, relacionamento/casamento.",
        "advice": "Ter paciência e ser compreensivo. Ser leal e agir corretamente."
    },
    {
        "id": 26,
        "name": "Cinco de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Conflitos, discussões, brigas (que acabam por serem construtivas), divergências de opiniões e ideologias. Obstáculos causados por desentendimentos ou desgaste. Trabalho árduo, esforço, chances, reorganização. Tudo é superável. Simboliza uma situação em que diferentes perspectivas, ideias ou interesses se entrelaçam em conflito. Pode representar discordância, competição ou uma luta pelo poder. Essa carta indica que você pode encontrar resistência ou obstáculos no caminho enquanto busca alcançar seus objetivos. Pode sugerir a necessidade de se afirmar e defender suas opiniões ou posições diante de outros. Também pode representar conflitos internos, quando se deseja fazer algo, mas pelas circunstâncias é necessário fazer algo diferente, gerando resistência. Observamos na carta um ambiente onde cada personagem defende sua ideia, assim causando conflito com os demais. Existem momentos onde não adianta apenas falar, é necessário demonstrar em atitudes aquilo que é defendido.",
        "work": "Brigas, competições, necessidade de empenho, esforço, precisar se posicionar.",
        "financial": "Reorganização. Desentendimento com terceiros.",
        "love": "Conflitos, diferenças, opiniões divergentes, rivalidade.",
        "obstacle": "Brigas, conflitos, esforço.",
        "advice": "Entrar em um consenso, ter disposição, se posicionar, expor sua opinião mas evitando discussões."
    },
    {
        "id": 27,
        "name": "Seis de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Conquista, orgulho, benefício, aprovação, destaque, reconhecimento, promoção, segurança, disciplina, recompensa pelo empenho, sucesso. O tempo de peleja acabou, já pode desfrutar o mel da vitória. Simboliza um período de triunfo e conquista. Indica que você superou desafios e obteve sucesso em seus empreendimentos. Traz uma sensação de orgulho, de reconhecimento, otimismo e está associada à autoconfiança e à liderança. Ela indica que seus esforços e talentos estão sendo reconhecidos e valorizados pelos outros, onde você alcançou um alto nível de competência e habilidade em sua carreira. Pode indicar no lado negativo dificuldade de reconhecer os próprios erros, de dar o braço a torcer, gerando orgulho ou arrogância.",
        "work": "Conquista, reconhecimento, aplausos, liderança, promoção, aprovação.",
        "financial": "Recompensa, melhoria financeira através do esforço do passado, conquista.",
        "love": "Quer ser reconhecido, está confiante. Orgulho, no sentido de não querer dar o braço a torcer. Pode acontecer de se sentir realizado por ter conquistado algo na vida amorosa (uma relação, uma pessoa).",
        "obstacle": "Orgulho, rigidez, arrogância.",
        "advice": "Se manter confiante, analisar melhor seus objetivos. Elogiar, dar crédito."
    },
    {
        "id": 28,
        "name": "Sete de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Perseverança, luta, determinação, pressão vinda de terceiros, recuperação, chances, adversidades, desafios, concorrência, competição. O Sete de Paus simboliza a necessidade de defender suas posições, ideias ou princípios diante de oposição ou desafios. Essa carta indica que você está enfrentando obstáculos ou resistência em seu caminho, mas está disposto a lutar por aquilo em que acredita. Também está relacionada à coragem e à perseverança. Ela representa a força interior necessária para enfrentar os desafios e resistir às pressões externas. Sugere que você estabeleça limites saudáveis e mantenha-se fiel a si mesmo, mesmo que isso signifique se afastar de certas pessoas ou situações. Na carta observamos o personagem lutando, de defendendo as interferências externas, assim como no dia a dia lutamos contra os obstáculos (trânsito, chuva, uma terceira pessoa, uma competição profissional).",
        "work": "Provas e desafios com resultados positivos. Esforço, pressão, competição, concorrência.",
        "financial": "Obstáculos e dificuldades que serão superados.",
        "love": "Adversidades, dificuldades que podem vir do externo ou de terceiros. Pode significar concorrência amorosa. Pode também retratar esforço, perseverança por um objetivo.",
        "obstacle": "Dificuldades, pressão, concorrência.",
        "advice": "Persistir nos objetivos, não perder tempo, ter determinação."
    },
    {
        "id": 29,
        "name": "Oito de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Mudança, conclusão, sucesso, imprevistos por meios diferentes e inusitados. Mudança na rotina trazendo renovação, vantagens, caminhos se abrem e tudo que estava travado flui, progride. Simboliza uma fase de mudança e transformação rápida em sua vida. Essa carta indica que você está experimentando um fluxo de energia intenso e que as coisas estão se movendo rapidamente ao seu redor. Pode representar novas oportunidades surgindo de repente, eventos emocionantes ou avanço significativo em seus projetos e objetivos. O Oito de Paus vem como um removedor de obstáculos. Podendo trazer também mudanças de planos rápidas, surgindo uma nova solução. Pode retratar uma conversa para resolver algo, ou uma mudança de planos que traz melhorias, até uma mudança física (casa, viagem, trabalho), sempre para renovar, melhorar.",
        "work": "Mudanças repentinas com resultados positivos, soluções, boa comunicação.",
        "financial": "Necessidade de economia para usar nos próximos meses.",
        "love": "Conciliação, finalização em consenso, diálogo para trazer mudanças na relação, renovação. Novas oportunidades.",
        "obstacle": "Mudanças repentinas.",
        "advice": "Buscar a renovação, novos caminhos, novas soluções."
    },
    {
        "id": 30,
        "name": "Nove de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Obstáculos, burocracia, atrasos, dúvidas, pendências, hesitação, decepção (com situações, não com pessoas). Prorrogação causada por força maior (como causas naturais). Defensiva, pressão, opressão. Essa carta indica que você passou por situações difíceis e provações, mas conseguiu se manter firme e continuar avançando. Guardando ainda muita bagagem de experiências passadas, onde não deseja reviver. Além disso, o Nove de Paus representa a necessidade de descanso e recuperação após um período de luta. Ele lembra que é importante cuidar de si mesmo, tanto fisicamente quanto emocionalmente, para restaurar suas energias e fortalecer-se para os desafios futuros. Essa carta sugere que você reserve um tempo para descansar, recarregar e se preparar para a próxima etapa de sua jornada.",
        "work": "Desafios causados por coisas ou pessoas, pendências, demora, opressão, derrota, dificuldades passageiras.",
        "financial": "Desengano, problemas financeiros passageiros que precisam ser enfrentados.",
        "love": "Opressão, medo de se entregar por causa de experiências passadas que foram negativas.",
        "obstacle": "Demora, prorrogação, desafios.",
        "advice": "Ter responsabilidade nas atitudes, agir com maturidade."
    },
    {
        "id": 31,
        "name": "Dez de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Sobrecarga, esgotamento, pressão externa (família, trabalho), luta em prol de um objetivo, finalização dos problemas trazendo progresso, dedicação que gera recompensa. O Dez de Paus simboliza a sensação de estar sobrecarregado com múltiplas responsabilidades e obrigações. Essa carta indica que você pode estar carregando um fardo pesado em sua vida, seja físico, emocional ou mental. Pode representar uma fase em que você se sente esgotado e sobrecarregado com tarefas, expectativas ou problemas. Pode indicar a importância de estabelecer limites saudáveis e aprender a dizer 'não' quando necessário. Essa carta lembra que você não precisa assumir todas as responsabilidades e encargos que lhe são impostos. Pode representar um período de finalização de um tempo difícil, cansativo, um período de renovação.",
        "work": "Sobrecarga por assumir responsabilidades alheias. Reorganização para solucionar problemas.",
        "financial": "Dívidas que se encerram. Melhorias por causa de uma nova fase. Problemas financeiros que podem ser resolvidos, embora cause desgaste.",
        "love": "Pressão, necessidade de impor limites. Recomeçar, reestruturar o amor, necessidade de inovar. Independência.",
        "obstacle": "Finalizar, superar. Situação que pesa, limita, sobrecarrega.",
        "advice": "Permanecer firme, impor limites."
    },
    {
        "id": 32,
        "name": "Valete de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Impulso, empolgação, sinceridade, prenúncio de notícias, mensagem, ligação, conversa, chamado. O Valete de Paus representa juventude, entusiasmo, criatividade e potencial. Simboliza o início de uma jornada ou empreendimento criativo. Ele representa um período de energia juvenil, paixão por um novo projeto ou empreendimento. Ele representa a fase de descoberta, aprendizado e crescimento, onde você está experimentando novas ideias e buscando expressar sua criatividade com autoconfiança e autoestima. Esse Valete é o mais sincero e fiel, pode indicar sentimentos puros e verdadeiros. Como arquétipo, pode indicar uma pessoa mais jovem.",
        "work": "Notícias, propostas, projetos, criatividade, boas ideias, boa comunicação.",
        "financial": "Início de projetos, novidades, boa perspectiva de ganhos (através de esforço e dedicação).",
        "love": "Conversas, lealdade, dedicação, sinceridade, empolgação, atração física, persistência, início de projetos, convites.",
        "obstacle": "Conversar, ser sincero. Iniciar algo.",
        "advice": "Ajudar, participar, falar. Colocar em práticas projetos, ter iniciativa."
    },
    {
        "id": 33,
        "name": "Cavaleiro de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Impulso, ousadia, sagacidade, diversão, sensualidade, desejo, renovação, novidade, ganhos inesperados (não apenas no financeiro), capacidade de superar qualquer obstáculo. Pode representar mudança de residência ou viagem (mais longa que precise de avião). O Cavaleiro de Paus representa a busca por aventura, ação e progresso. Ele personifica a energia ardente do fogo, trazendo consigo um senso de entusiasmo e motivação. Essa carta representa um espírito corajoso e empreendedor, chama atenção por onde passa, disposto a enfrentar desafios e buscar novas oportunidades. Ele é ousado, audacioso e não teme correr riscos em busca de suas ambições. Não gosta de ser controlado, gosta de ser livre. Tem dificuldades para assumir compromissos. Gosta da farra. Esta carta indica também popularidade e socialização.",
        "work": "Destaque, sagacidade, mudanças positivas, soluções, força de vontade, criatividade, novas ideias.",
        "financial": "Boa sorte nos empreendimentos, ganhos.",
        "love": "Atração física, vontade, persistência, autoconfiança (cuidado com o excesso de autoconfiança), diversão, sensualidade.",
        "obstacle": "Mudar, agir. Se divertir. (Pode representar uma pessoa com as características deste Cavaleiro).",
        "advice": "Se abrir para o novo, não ter medo de nada. Arriscar, socializar, se divertir."
    },
    {
        "id": 34,
        "name": "Rainha de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Poder pessoal, beleza, autoestima, confiança, empolgação, acordo, troca, sucesso, lucros, amizade, união. Conclusão com sucesso. A Rainha de Paus representa liderança, paixão, criatividade, poder e autoconfiança. Representa a capacidade de manifestar sua visão criativa no mundo. Ela é inspirada, comunicativa, vibrante, gosta de chamar atenção, é percebida por onde passa. É engraçada e gosta de manter o bom humor, mesmo em dias mais tristes. É visionária e encoraja a expressar sua essência. Muito comunicativa e alto astral. Essa carta sugere que você confie em suas habilidades e assuma um papel de liderança. Indica um bom momento para cuidar da auto-estima, mudar aparência física, investir em novidades, inovar.",
        "work": "Liderança natural, inteligência, boas ideias, êxito, conclusão, conquista.",
        "financial": "Caminhos abertos, bom fluxo financeiro.",
        "love": "Paixão, atração física, união feliz e conexão. Autoestima. Visibilidade.",
        "obstacle": "Autoestima, autoconfiança. Arquétipo (pessoa) com as características desta Rainha.",
        "advice": "Ser sincero, manter a palavra, não perder o foco. Socializar. Inovar. Cuidar da autoestima. Agir com poder."
    },
    {
        "id": 35,
        "name": "Rei de Paus",
        "major": False,
        "suit": "clubs",
        "description": "Prosperidade, liderança, acordos, contrato, compromisso, negócios, determinação, autoconfiança, sucesso, nobreza, beleza, autoestima, produtividade, poder. O Rei de Paus personifica a figura do líder carismático e influente. Ele é um indivíduo confiante, corajoso e capaz de tomar decisões firmes. Sua presença é magnética e inspiradora, e ele é apreciado por aqueles ao seu redor. Gosta de chamar atenção e ser elogiado. Está associado à energia do fogo, simbolizando a paixão, a criatividade e a ação. É uma carta que simboliza a confiança em si mesmo, a capacidade de liderar com sabedoria e a habilidade de transformar ideias em realidade. Está associado também a fazer acordos, entrar em consenso com algo ou alguém. Assumir uma responsabilidade, firmar um compromisso.",
        "work": "Acordos e contratos positivos, liderança, produção, avanço, desenvolvimento, crescimento.",
        "financial": "Prosperidade, caminhos abertos através de bons negócios.",
        "love": "Lealdade, amor, assumir compromissos, ideias para futuro, reconciliação, desejo. Desejo por poder e controle.",
        "obstacle": "Assumir uma responsabilidade, entrar em acordo. Falta de autoconfiança. Pode indicar uma pessoa com as características deste Rei.",
        "advice": "Seguir em frente, acreditar em si mesmo, nos próprios projetos, ser flexível."
    },
    {
        "id": 36,
        "name": "Ás da Copas",
        "major": False,
        "suit": "hearts",
        "description": "Realizações, recomeços, surpresas, felicidade, êxtase, amor, compreensão, perdão, intuição, fertilidade. Emocional sendo expandido, indica um novo começo emocional, uma oportunidade de amor, afeto e conexões profundas. Pode representar a evolução de um novo relacionamento, uma renovação em um relacionamento existente ou uma manifestação de sentimentos intensos e positivos em geral. Geralmente é retratada uma mão emergindo de uma nuvem ou de uma fonte, segurando um cálice ou um copo com uma flor ou um símbolo de amor. Essa representação visual transmite a energia de uma nova oportunidade emocional que surge em nossa vida e nos faz transbordar. Proporcionando bons momentos, podendo ser uma surpresa que faz o emocional feliz. Mesmo podendo ser uma conquista física/material, faz bem ao coração.",
        "work": "Surpresa feliz, realizações, conquistas, início promissor.",
        "financial": "Boas notícias, realizações.",
        "love": "Início ou recomeço de relacionamento. Sentimentos de amor, dedicação, felicidade e romantismo.",
        "obstacle": "Recomeçar, perdoar, amar.",
        "advice": "Abrir o coração, agradecer e buscar uma convivência com harmonia."
    },
    {
        "id": 37,
        "name": "Dois de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Namoro, amor, parceria, sociedade, reciprocidade, encontro, contrato, reconciliação, amizade, conexão, carinho, promessas cumpridas. É o amor romântico, uma amizade profunda ou qualquer tipo de parceria significativa. Representa o equilíbrio emocional e a harmonia nos relacionamentos. Ela nos lembra da importância de manter uma abertura e honestidade, de expressar nossos sentimentos de forma clara e comunicação e ouvir atentamente o outro. É comum ver a representação de duas pessoas que se encontram frente a frente, segurando cada uma um cálice ou copo. Essa imagem simboliza a igualdade, a reciprocidade e a troca de emoções entre essas duas pessoas que se encaixam. Pode indicar uma união não por apenas desejos carnais, mas sim por conexões sentimentais, pessoas parecidas, com os mesmos desejos, mesmas intenções, mesmos gostos, que se encaixam quando juntos.",
        "work": "Parceria, sociedade, amizade, um bom relacionamento. Apoio.",
        "financial": "Ajuda/envolvimento do parceiro, amigo ou sócio.",
        "love": "Namoro, relação com conexão além do sexual, amor, harmonia.",
        "obstacle": "Lidar com uma relação, amizade ou sociedade.",
        "advice": "Ser honesto, sincero e colaborar, agir em parceria. Valorizar a união, uma aliança."
    },
    {
        "id": 38,
        "name": "Três de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Felicidade, comemoração, conquistas, namoro, início de uma nova fase bem sucedida, casamento, venda, promoção, aprovação, gravidez, amizades, círculo social, festa, celebrações (aniversário, chá de bebê). Boas notícias, simboliza encontros sociais, festividades e celebrações em grupo. Ele representa a alegria e a felicidade que são compartilhadas com amigos, familiares ou pessoas queridas. É comum ver três pessoas reunidas, geralmente brincando ou dançando juntas. Essa representação visual transmite energia de alegria por uma nova fase, começo de um novo estilo de vida, com amizades ou através de uma união.",
        "work": "Realização, resolução, promoção, acordo, bom relacionamento com colegas.",
        "financial": "Boas notícias, sorte, prosperidade, investimento que deu certo.",
        "love": "Carinho, cumplicidade, prazer, alegria, namoro, casamento, união feliz.",
        "obstacle": "Amizades, pessoas ao redor, sentimentos.",
        "advice": "Aceitar as oportunidades, ser otimista. Socializar."
    },
    {
        "id": 39,
        "name": "Quatro de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Insatisfação, desânimo, reclamação, ingratidão, amargura, desapontamento, falta de energia para reagir. Está descrente do futuro, mesmo não havendo muitos obstáculos. Também pode representar uma sensação de tédio ou estagnação emocional. Pode ser um sinal de que estamos nos sentindo presos ou entediados em certas áreas de nossas vidas emocionais e precisamos buscar novas perspectivas e experiências. É comum ver uma pessoa sentada, com os braços cruzados e uma expressão de desinteresse ou insatisfação, mesmo possuindo 3 copas e tendo a oportunidade de ganhar mais uma. Essa representação visual transmite a sensação de alguém que está mergulhado em seus próprios pensamentos e emoções, desconectado do mundo exterior, não reconhecendo as oportunidades e episódios positivos que acontecem à sua volta. Mesmo tendo todo apoio e oportunidades, insiste em reclamar.",
        "work": "Sensação que outras pessoas são mais valorizadas que você. Descrença, desânimo.",
        "financial": "Reclamações, mesmo não havendo nada errado. Não enxerga um futuro melhor e o medo de perder tira a alegria de ganhar.",
        "love": "Desesperança, aborrecimento, desconfiança (não exatamente por sinais de infidelidade, mas por estar com muitos sentimentos negativos).",
        "obstacle": "Reclamação, desânimo.",
        "advice": "Parar e refletir o que deseja da vida, se as atitudes condizem com o que espera que aconteça."
    },
    {
        "id": 40,
        "name": "Cinco de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Separação, perdas, frustrações, arrependimento, distanciamento, decepção, remorso, tristeza. Indica um momento de descontentamento emocional, onde nos sentimos tristes e desapontados em relação a uma situação ou a um relacionamento. Pode representar a sensação de ter perdido algo importante ou de ter sido traído de alguma forma, levando a uma sensação de tristeza, decepção e remorso. É importante observar que, mesmo no Cinco de Copas, nem tudo está perdido. Na carta, ainda restam duas copas em pé, representando a esperança e a possibilidade de encontrar um caminho para superar a tristeza e a decepção. Podemos estar como o personagem da carta, chorando a perda de 3 copas, mas sem perceber que ainda restam duas copas em pé, necessitando de atenção. Mesmo diante de momentos difíceis, temos compromissos e situações que precisam de atenção.",
        "work": "Possível afastamento, perda, reprovação, demissão. Em breve terá novas chances.",
        "financial": "Frustração, não acontece o que foi desejado/planejado, podendo não haver perda financeira, mas sim decepção ou quebra de expectativas emocionais.",
        "love": "Separação (temporária ou definitiva), afastamento, desilusão, arrependimento, revolta ou reclamações (sem muito sentido).",
        "obstacle": "Perda, separação, decepção.",
        "advice": "Momento de se afastar dos problemas e manter a calma. Não agir no impulso."
    },
    {
        "id": 41,
        "name": "Seis de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Carinho, presentes, inocência, energia de criança, criança interior, nostalgia, recordações, saudades, deve-se tomar cuidado com o lado negativo de viver apenas para alimentar lembranças, lamentações, lembrando 'do tempo que era bom'. Pode indicar um encontro significativo com pessoas do passado, seja um amigo de infância, um antigo amor ou um familiar distante. Essa carta também pode representar a busca por conforto emocional e a necessidade de encontrar segurança e felicidade em nossas memórias e experiências passadas. É comum ver duas crianças, uma delas oferecendo uma flor à outra. Essa representação visual transmite a ideia de um encontro doce e inocente, onde a troca de sentimentos e a reconexão com o passado. Pode representar um momento onde se é carinhoso e está presenteando alguém. Pode representar também uma amizade.",
        "work": "Bom relacionamento, amigos queridos, apego às pessoas do ambiente de trabalho.",
        "financial": "Incertezas, não seria o melhor momento para investir. Precisa se atentar às relações. Pode ter ligação afetiva nas finanças, ajuda de amigo ou parceiro amoroso.",
        "love": "Carinho, boas lembranças, saudades, presentes, podendo existir irresponsabilidades por falta de maturidade e comparações com o passado. Pessoa do passado retornando.",
        "obstacle": "Pessoa do passado, amizade, inocência, saudade.",
        "advice": "Avançar, seguir em frente. Resolver todas as pendências. Presentear alguém, dar carinho, atenção. Valorizar o passado, as boas lembranças."
    },
    {
        "id": 42,
        "name": "Sete de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Dúvidas, fantasias, devaneios, expectativas irreais, capricho, soberba, sentimentos superficiais por vaidade. É comum ver sete taças flutuando no ar, cada uma delas contendo um símbolo diferente. Esses símbolos podem representar diferentes desejos, sonhos ou ilusões que capturam a atenção do observador. Essa representação visual sugere a ideia de um cenário de escolhas e opções ilusórias, onde é necessário fazer uma escolha consciente e discernir o que é real e possível. Nos lembra da importância de manter os pés no chão e de avaliar cuidadosamente as opções disponíveis. Ele nos alerta para o perigo das ilusões e da dispersão de energia em busca de desejos impossíveis ou pouco realistas. Pode representar um momento de muitas dúvidas, por causa de um emocional aflorado, que cria expectativas em um futuro, se esquecendo de viver o aqui e agora.",
        "work": "Dúvidas por ilusões, criando-se muitas ideias e possibilidades na mente, podendo nem ao menos serem reais.",
        "financial": "Ilusão podendo trazer prejuízos, ambição, desejos por vaidade. O ideal seria não fazer nenhum investimento nesse momento.",
        "love": "Paixão podendo gerar ilusões, deixando a pessoa cega, tomada pelos desejos, expectativas e dúvidas.",
        "obstacle": "Dúvida, expectativas, desejos irreais.",
        "advice": "Buscar a melhor das opções, ter ambição."
    },
    {
        "id": 43,
        "name": "Oito de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Perdas, equívoco, momentos de crise, decepções, escândalo, frustrações, doença, prejuízos, demissão, divórcio, tudo influenciado pelas atitudes do consulente. É comum ver uma figura solitária andando em um terreno de lama em direção a um horizonte distante, deixando para trás oito copas. Essa representação visual transmite a ideia de uma jornada solitária, difícil de sair, em busca de algo mais significativo, abandonando o que considerava seguro. Deixar no passado, mudar a direção, andar para um novo caminho. Traz uma bagagem emocional de passado, lembranças que desequilibram o emocional. É necessário buscar novas opções. Indica um momento de desapego emocional, onde é necessário deixar para trás relacionamentos, situações ou padrões de vida que não nos servem mais.",
        "work": "Perda, desilusão, rompimento, erro na conduta.",
        "financial": "Perdas, maus investimentos, desperdício, prejuízos (causados pelas escolhas do próprio consulente).",
        "love": "Perdas emocionais, desilusão, egoísmo, decepção, despedida, afastamento, possibilidade de separação, cansaço emocional por momentos de crise.",
        "obstacle": "Perda, desilusão, decepções passadas.",
        "advice": "Falar a verdade, mesmo que traga algum prejuízo. Fazer o que é correto. Se afastar, mudar, procurar uma outra opção. Não investir."
    },
    {
        "id": 44,
        "name": "Nove de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Alegria, prazer, vantagem, desejo realizado, bem-estar, realização podendo ser material mas com valor sentimental, união, acordo, noivado, novos caminhos positivos. É comum ver uma figura sentada ou em pé, rodeada por nove copas espontâneas. Essa representação visual transmite uma sensação de tranquilidade e abundância, como se o personagem estivesse muito satisfeito com suas conquistas, seus desejos foram realizados, ele está expondo sua felicidade a todos. As copas estão cheias e transbordantes, simbolizando a realização e a plenitude emocional. Ele indica um período de harmonia e contentamento interior, onde nossos desejos e expectativas são realizados. É uma carta de celebração, onde podemos desfrutar das recompensas de nossos esforços e sentir gratidão pelas bênçãos que sentimos. Deve-se somente ter atenção no seu lado negativo, podendo sugerir exageros, como excesso de comida/bebida, excesso de prazer, querer viver apenas no gozo da vida.",
        "work": "Realização, conquistar aquilo que deseja.",
        "financial": "Realizações, conquistas, compra de algo com valor sentimental, boas notícias.",
        "love": "Felicidade, prazer, atração física, união, acordo, namoro, noivado.",
        "obstacle": "Desejos, prazer, exageros.",
        "advice": "Realizar suas vontades. Cumprir com suas promessas a si mesmo. Aproveitar a vida."
    },
    {
        "id": 45,
        "name": "Dez de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Plenitude, virtudes, honra, família, amor, recomeços, soluções positivas, resolução de problemas, equilíbrio, união, festa. É comum ver uma cena de uma família feliz, muitas vezes em um ambiente idílico, como um jardim ou uma paisagem tranquila. A família está reunida, sorrindo e compartilhando momentos de alegria. Essa representação transmite uma sensação de união, conexão e felicidade em um contexto familiar. Brilha um arco-íris ao fundo, simbolizando um momento de alívio depois de dias difíceis. Simboliza realizações de relacionamentos harmoniosos. É uma carta que reflete o amor e a aceitação mútua entre as pessoas, a criação de um ambiente emocionalmente seguro e aconchegante. Representa também a celebração das conquistas familiares e a expressão de afeto e gratidão uns pelos outros. Traz a sensação de dever cumprido, podendo passar para uma nova fase da vida, recomeçar.",
        "work": "Bom relacionamento, conquista, tranquilidade, soluções.",
        "financial": "Abundância, pagamento, honrar com os compromissos.",
        "love": "Amor, carinho, atenção, energia de família. Namoro, casamento, associação positiva. Encontrar soluções com calma e amor.",
        "obstacle": "Família, encontrar a paz nas relações. Recomeçar.",
        "advice": "Ter equilíbrio, buscar um bom relacionamento com o meio onde vive. Ser paciente e buscar a felicidade e o otimismo."
    },
    {
        "id": 46,
        "name": "Valete de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Notícias, conversas que envolvem amor, carinho, atenção, convite, promessa, amizade, namoro, sinceridade, confiança. É comum ver um jovem segurando uma taça ou cálice com atenção e cuidado. Ele geralmente está em um ambiente sereno, próximo a um corpo d'água, como um rio ou lago. A água representa as emoções e a intuição, ressaltando a conexão do Valete de Copas com o mundo emocional. É um jovem carinhoso, sonhador, que deseja amar, ser querido e aceito pelas pessoas ao seu redor. Gosta de criar expectativas, imaginar, sonhar. É um transportador do amor e das emoções. Ele traz consigo uma energia de compaixão, empatia e sensibilidade. Sugere um estado de romantismo e busca pelo amor verdadeiro. Pode indicar desde uma conversa em prol de um relacionamento amoroso, amizades sinceras, até sentimentos de carinho, romantismo, inocência e expectativas em algo ou alguém.",
        "work": "Boas notícias, amizade, bom relacionamento, convite, oportunidade.",
        "financial": "Renovação, expectativas de melhorias. Deve tomar cuidado em gerar muitas expectativas financeiras.",
        "love": "Carinho, atenção, conversa, sinceridade, romantismo, pessoa meiga, querida.",
        "obstacle": "Excesso de expectativas, sonhos inocentes.",
        "advice": "Ser sincero, honesto e solicito. Puxar assunto, falar, expressar sentimentos."
    },
    {
        "id": 47,
        "name": "Cavaleiro de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Sedução, convites, desejos, atração, encanto, paixão, podendo ser fantasiosa, promessas feitas no calor das emoções e não cumpridas, ilusão. O Cavaleiro de Copas é alguém que é apaixonado, educado, romântico e gentil. Ele é um buscador de emoções profundas e verdadeiras. É o tipo de pessoa que compra presentes, entrega flores, demonstra o seu amor. Ele se deixa levar pela intuição e pelas emoções, seguindo seu coração e buscando a satisfação emocional e pode indicar uma tendência a se envolver em fantasias românticas ou a se deixar levar por emoções excessivas. Pode indicar um convite, como um encontro romântico, uma proposta. Pode indicar que o emocional esteja aflorado, fazendo com que enxergue tudo de forma mais intensa.",
        "work": "Busca por melhorias, por reconhecimento. Promessas não cumpridas por terceiros.",
        "financial": "Instabilidade, cuidado com ilusões, possibilidades que não são reais. Contrato enganoso, enrolação.",
        "love": "Paixão, desejo, sedução, atração, quer amar e ser amado, está embriagado de desejos, mas não será sempre assim. Emocional aflorado causando ilusões, fantasias.",
        "obstacle": "Desejos. Pessoa com as características deste Cavaleiro.",
        "advice": "Se entregar aos desejos, realizar as fantasias e vontades. Viver intensamente."
    },
    {
        "id": 48,
        "name": "Rainha de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Dedicação, generosidade, inércia, estagnação, tempo, segredos, sentimentos ocultos. A Rainha de Copas personifica a energia emocional, intuitiva e compassiva do naipe de Copas. Ela é um símbolo de amor incondicional, empatia, intuição e nutrição emocional. É uma figura maternal e acolhedora. Ela está sempre pronta para oferecer apoio emocional, compreensão e cuidado aos outros. Ela é uma ouvinte atenta e gentil, capaz de compreender e aceitar as emoções dos outros sem julgamento. Também pode representar a importância de cuidar de si mesmo emocionalmente. Ela nos lembra que devemos nos permitir sentir nossas emoções, nutrir nosso próprio bem-estar emocional e estabelecer limites saudáveis nos relacionamentos. Pode representar momentos onde o emocional está aflorado, porém com dificuldades para expressar essas emoções. Momento de passividade.",
        "work": "Suspensão, demora, dedicação, cuidado, bom relacionamento.",
        "financial": "Atrasos, demora, nada muda, tudo permanece como está.",
        "love": "Amor, afeto, carinho, cuidado, mas não revela tudo que sente ou pensa.",
        "obstacle": "Passividade. Pessoa com as características desta Rainha.",
        "advice": "Ser paciente, não falar nem fazer nada no momento."
    },
    {
        "id": 49,
        "name": "Rei de Copas",
        "major": False,
        "suit": "hearts",
        "description": "Progresso, conquista em meio às dificuldades, dons, dedicação, aperfeiçoamento. Idealiza, sonha, busca alegria e prazer mesmo sem poder, quer ser reconhecido, quer agradar. O Rei de Copas é capaz de sintonizar-se com as necessidades e os sentimentos dos outros, oferecendo apoio emocional e orientação. Ele é alguém que se importa profundamente com o bem-estar dos outros e está disposto a oferecer ajuda e suporte quando necessário. Também representa o equilíbrio entre a mente e o coração. Ele integra a sabedoria da razão com a sabedoria das emoções, tomando decisões com base na lógica e na compaixão. Porém pode indicar vaidade, onde o desejo é maior que o senso de realidade. Podemos observar na carta que o trono do Rei de Copas está solto sob a água, indicando comportamentos que não passam confiança, são contraditórios. Falar uma coisa e fazer outra.",
        "work": "Conquista, adaptação, autoconfiança, determinação.",
        "financial": "Satisfação, realizações financeiras, bons resultados.",
        "love": "Desejo, quer fazer dar certo, se dedica, quer mais fazer pelos outros do que para si mesmo.",
        "obstacle": "Exageros emocionais. Pessoa com características deste Rei.",
        "advice": "Ter mais amor-próprio, cuidar de si, se manter confiante."
    },
    {
        "id": 50,
        "name": "Ás de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Início de um caminho promissor, abundância, ganhos, dinheiro, recompensa, valor, riqueza, prosperidade, realização, confiança, melhorias materiais, compras importantes, investimento, vantagem. Representa a energia do elemento Terra e está associada a questões materiais, financeiras, externas e tangíveis. É um símbolo de potencial e oportunidade. Ela indica um novo começo ou um novo empreendimento que pode trazer benefícios materiais ou financeiros. Representa a possibilidade de crescimento, estabilidade e segurança material. Pode representar dinheiro inesperado, um ganho, um investimento. Período de prosperidade.",
        "work": "Bons resultados, início de projeto, investimento financeiro. Aumento de salário, melhorias.",
        "financial": "Prosperidade, ganhos, resultados, segurança, investimento.",
        "love": "Valor, melhorias afetivas, confiança, segurança (pode indicar relação com envolvimento também na vida financeira).",
        "obstacle": "Dinheiro, recebimento.",
        "advice": "Agir com autoconfiança, buscar ser leal. Investir financeiramente, juntar dinheiro, dar atenção às finanças."
    },
    {
        "id": 51,
        "name": "Dois de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Equilíbrio, espera, impasse, divisão, conclusão demorada, prorrogação, dificuldades causadas por terceiros, medo de perder. Representa equilíbrio, adaptação e malabarismo de áreas múltiplas da vida. A necessidade de encontrar um equilíbrio entre diferentes aspectos da vida, como trabalho e lazer, diversão, responsabilidades, finanças, trabalho e relacionamentos. Dar conta de várias coisas ao mesmo tempo. Podendo surgir dúvidas sobre o que precisa de mais atenção na vida no momento, fazendo com que acumule tarefas e obrigações e não consiga fazer o que é realmente importante. O desejo de 'não deixar a peteca cair'. Porém necessita de mais tempo para se preparar. Muitas vezes não é possível fazer tudo ao mesmo tempo.",
        "work": "Ter que dividir algo, escolher, esperar ou ter rivalidade. Obstáculos e atrasos.",
        "financial": "Pouco dinheiro, necessidade de esperar, não fazer investimento longo (evitar parcelamento e dívidas que possam se arrastar).",
        "love": "Impasse, obstáculos, preocupações desnecessárias, ter que se dividir para dar conta.",
        "obstacle": "Dúvida, demora.",
        "advice": "Ser flexível, se manter paciente. Esperar."
    },
    {
        "id": 52,
        "name": "Três de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Crescimento, trabalho em equipe, acordos, compromisso, bons resultados, união, contrato, regras, confiança, boa habilidade para se relacionar, seja no amor seja no profissional. Problemas resolvidos. Representa colaboração, habilidades e realizações através do trabalho em equipe. Essa carta é um motivador de que, ao unir forças e aproveitar as habilidades complementares dos outros, é possível alcançar resultados muito melhores do que se estivéssemos trabalhando sozinhos. É um alerta para a rotina, as responsabilidades do dia a dia, como horários, hábitos, compromissos. É necessário agir com responsabilidade, consigo mesmo e com os demais.",
        "work": "Bom acordo, contrato. Trabalho em equipe, parcerias, bons negócios. Destaque.",
        "financial": "Abundância, resultados rápidos. Podendo ser também através de uma relação ou parceria.",
        "love": "Confiança, compromisso, período de crescimento, evolução.",
        "obstacle": "Trabalho, compromissos, equipe.",
        "advice": "Aceitar propostas, fazer parcerias, ser amigável, se manter aberto a acordos."
    },
    {
        "id": 53,
        "name": "Quatro de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Controle, apego, teimosia, possessividade, medo de perder e de ficar sem o que controla, avareza, mesquinharia, falta de generosidade, insatisfação, estagnação, uma resistência a mudanças ou uma aversão a correr riscos. Pode indicar a importância de liberar o medo de perda ou economia e permitir um fluxo mais livre de energia e recursos em sua vida. Perde tempo se preocupando em acumular e pode acabar gerando estagnação, escassez. Pode indicar dificuldades por responsabilidade do próprio consulente. 'O medo de perder tira o brilho de ganhar', ficar constantemente preocupado em querer ter o controle tira a naturalidade da vida.",
        "work": "Rigidez, teimosia, controle, dificuldade em dividir.",
        "financial": "Escassez, avareza, ganância, controle. Medo de ficar sem dinheiro. Problemas financeiros. Pouco dinheiro circulando.",
        "love": "Apego, medo de perder, possessividade nas atitudes.",
        "obstacle": "Apego, controle.",
        "advice": "Se manter no controle, administrar e organizar seus projetos e desejos."
    },
    {
        "id": 54,
        "name": "Cinco de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Escassez, prejuízos, sensação de falta, crises, dificuldades, insegurança, impotência, desgaste, tanto financeiro quanto emocional. Essa carta simboliza momentos de dificuldades financeiras ou emocionais, ou a sensação de estar excluído ou desamparado. Ela representa um período de escassez de material, perda ou falta de recursos. Pode indicar preocupações financeiras, dificuldades de trabalho, saúde precária ou uma sensação de isolamento social. O pensamento de escassez limita o comportamento, trazendo medo, insegurança, se sentir inútil. Deve-se atentar às formas de sair deste estado, não alimentar ainda mais a escassez, a insuficiência.",
        "work": "Sensação de perda, perda de recursos, insegurança, dificuldades.",
        "financial": "Pouco dinheiro circulando, prejuízos, gastos inesperados.",
        "love": "Sensação de incapacidade, sente-se reprovado, abandonado, inseguro, impotente.",
        "obstacle": "Insegurança, problemas financeiros, problemas de saúde.",
        "advice": "Não investir, esperar, focar na realidade da situação e aguardar."
    },
    {
        "id": 55,
        "name": "Seis de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Doação, ajuda, caridade, generosidade, dúvidas, opções, aperfeiçoamento, pode ter a necessidade de adiar um projeto para focar em outro. O Seis de Ouros pode indicar a presença de algo/alguém em sua vida que está disposta a oferecer ajuda, orientação ou recursos. Pode representar a necessidade de compartilhar seus próprios recursos, seja financeiro, emocional ou intelectual, de uma maneira equilibrada e harmoniosa. Pode representar comércio, negociação, troca. O Seis de Ouros quando traz dúvidas, acaba sendo por uma boa causa, com intuito de ajudar, de ser generoso com alguém, querendo abdicar algo em sua vida pessoal em prol de alguém.",
        "work": "Ajuda, proposta, melhoria profissional. Momentos de lentidão.",
        "financial": "Receber ou ajudar financeiramente.",
        "love": "Quer ajudar, estar próximo. Ajudar financeiramente. Dúvidas pois busca por melhorias.",
        "obstacle": "Receber apoio. Dúvida.",
        "advice": "Pensar melhor antes de agir, realizar. Se possível ajudar algo ou alguém, fazer filantropia, caridade."
    },
    {
        "id": 56,
        "name": "Sete de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Dúvida (trocar certo pelo duvidoso), crescimento, melhoria, saúde, progresso, vantagens, colheita. Essa carta simboliza um período de espera e avaliação. Ela representa o momento em que você planta as sementes do seu trabalho e agora precisa esperar pacientemente pelo crescimento e desenvolvimento. Com isso pode trazer dúvida, se investe ou não, se arrisca ou não. É um momento de avaliar o progresso feito até agora e considerar as opções disponíveis para o futuro. Os caminhos se encontram abertos para ter ganhos, resultados futuros. O Sete de Ouros também destaca a importância de investir tempo e energia em um projeto ou objetivo e ter paciência para permitir que ele amadureça e se desenvolva.",
        "work": "Expansão, resultados, lucros, segurança, dúvida para algo positivo.",
        "financial": "Melhorias, ganhos, riquezas, lucro.",
        "love": "Pode haver dúvida entre opções de pretendentes, mas sente-se seguro, sabe que tem boas opções e um caminho feliz.",
        "obstacle": "Dúvida.",
        "advice": "Insistir nos objetivos, seguir em frente, perseverar."
    },
    {
        "id": 57,
        "name": "Oito de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Estudo, dedicação, reforma, descoberta, aprendizado, esforço com resultados a longo prazo, aumento das habilidades profissionais ou acadêmicas. Investir tempo, dinheiro em algo para o futuro. O Oito de Ouros também pode sugerir um período de um ritmo mais intenso de aprendizado e crescimento profissional. Pode indicar a importância de aperfeiçoamento, lapidar seus conhecimentos, estudar algo novo, ter novas habilidades, ou treinamento específico para seguir em sua carreira ou em um projeto em particular. Tudo com resultados mais distantes. O Oito de Ouros traz a energia da reforma, da melhoria, da lapidação, seja internamente ou externamente, como reformar uma casa, consertar algo que está danificado ou precisa de um \"trato\".",
        "work": "Dedicação, aprender novas habilidades, intensa atividade profissional, fazer um curso, lapidar seus conhecimentos para ter resultados no futuro.",
        "financial": "Melhoria financeira, juntando dinheiro ou pensando em um sucesso para o futuro.",
        "love": "Descoberta, aprendizagem, fazer uma renovação, reciclar, pensa no futuro e busca melhorias.",
        "obstacle": "Estudar, consertar, se dedicar a um trabalho.",
        "advice": "Deixar as mudanças acontecerem, se abrir para o novo, pensar no que deseja a longo prazo."
    },
    {
        "id": 58,
        "name": "Nove de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Realização, dinheiro inesperado, recompensa, reconhecimento, felicidade, autoconfiança, orgulho, autoestima, resultados prósperos e satisfatórios, segurança, poder pessoal, bem-estar. O Nove de Ouros pode indicar um período próspero, momentos de estabilidade e conclusão pessoal. Pode representar um período em que você está colhendo os frutos do seu trabalho árduo e desfrutando das recompensas. Essa carta sugere que você alcançou um nível de segurança e proteção que lhe permite aproveitar a vida em seu próprio ritmo, sem a necessidade de depender dos outros. Podemos observar na carta que a personagem está com uma mão no ouro e outra na águia, símbolo de inteligência e sabedoria, indicando a necessidade de saber fazer bons investimentos e ter maturidade financeira para aproveitar o que se ganha.",
        "work": "Recompensa, reconhecimento, promoção, aumento de salário.",
        "financial": "Dinheiro inesperado (podendo ser também resultado de um trabalho/esforço), melhoria, ganhos, recompensa, herança.",
        "love": "Sente-se seguro, com a autoestima elevada, mantém sua independência.",
        "obstacle": "Excesso de confiança.",
        "advice": "Dar valor às suas conquistas, agir com educação e paciência, se mantendo autoconfiante."
    },
    {
        "id": 59,
        "name": "Dez de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Prosperidade, abundância, família, honra, virtudes, regras, segurança, status, crenças, ancestralidade, costumes que podem ir passando de geração em geração. Boa administração, boa organização que mantém a harmonia. O Dez de Ouros também destaca a importância das conexões familiares e da tradição. Ele representa uma herança familiar forte, tanto material quanto cultural, que fornece uma base sólida para o sucesso e a continuidade. É um sinal de prosperidade, abundância e estabilidade em vários aspectos da vida, incluindo finanças, relacionamentos e harmonia familiar. Pode indicar crenças e valores fortes, a habilidade de administrar, controlar uma situação, com autoridade e experiência. Agir de forma correta, fazer tudo 'conforme manda o figurino'.",
        "work": "Conquistas, segurança e estabilidade, bons resultados.",
        "financial": "Prosperidade e abundância, boa relação com dinheiro, podendo em alguns casos ter influência da família.",
        "love": "Sentimentos conservadores, familiar, estável, confia e deseja continuar.",
        "obstacle": "Família, valores.",
        "advice": "Continuar, seguir com os projetos, agir corretamente, dentro das leis ou regras sociais."
    },
    {
        "id": 60,
        "name": "Valete de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Proativo, dedicado, ambicioso, trabalhador, gosta de aprender coisas novas, é focado, confiante e responsável. Início de projeto ou acordo. Pode indicar melhoria salarial, uma promoção profissional ou uma reconciliação afetiva depois de um período separados ou conturbados. Essa carta simboliza o potencial de crescimento, aprendizado e novas oportunidades no campo material. O Valete de Ouros representa uma energia jovem e curiosa, pronta para explorar o mundo e aprender habilidades práticas. Ele é dedicado, focado e determinado em alcançar seus objetivos financeiros e materiais. Essa carta também pode indicar o início de um novo empreendimento ou projeto relacionado ao trabalho, finanças ou estudos, sempre com muita dedicação e ambição em crescimento e resultados.",
        "work": "Promoção, assumir novas responsabilidades, oportunidade de crescimento para melhorar sua experiência profissional.",
        "financial": "Aumento no fluxo financeiro, aumento de salário, boas oportunidades de compra ou investimentos.",
        "love": "Dedicação, responsabilidade, reconciliação. É confiante e transparece isso, quer fazer o melhor pelo ser amado.",
        "obstacle": "Recomeçar, agir, estudar.",
        "advice": "Colocar em prática suas ideias, projetos, desejos. Agir imediatamente."
    },
    {
        "id": 61,
        "name": "Cavaleiro de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Confiança, busca pela estabilidade e pelo controle, sistemático, organizado, esforçado, persistente, possessivo, controlador, quer conduzir, mandar. Cumpre com suas obrigações e promessas. Assume responsabilidades. Essa carta simboliza a inteligência e o comprometimento em alcançar o sucesso e a segurança financeira. O Cavaleiro de Ouros representa uma energia persistente e focada, que está disposto a trabalhar arduamente e tomar medidas concretas para alcançar suas metas materiais. O Cavaleiro de Ouros pode indicar um período de estabilidade e progresso lento, mas seguro. Pode sugerir a necessidade de abordar suas metas de forma prática e estratégica, estabelecendo bases sólidas para o sucesso a longo prazo. O tipo de pessoa que é 'pau para toda obra', mas não espere atitudes românticas, ou iniciativa dele.",
        "work": "Assumir responsabilidades (mesmo sem recompensa financeira), controlar, administrar, ser cauteloso e dedicado.",
        "financial": "Organizar as finanças, não gastar mais que o necessário, se organizar, poupar, economizar pensando no futuro a longo prazo.",
        "love": "Se esforça para ter o que deseja, mas sem criatividade ou romantismo, cumpre o que promete mas com o intuito de manter tudo estável.",
        "obstacle": "Controle, responsabilidades. Pessoa com as características deste Cavaleiro.",
        "advice": "Seguir em frente com suas ideias, organizando todas as áreas da vida, sendo sistemático e cuidadoso."
    },
    {
        "id": 62,
        "name": "Rainha de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Dedicação, prosperidade, abundância, bem-estar, conforto, cuidado, organização, segurança, constância, elegância, refinamento, capacidade de gerar lucro, riquezas, de controlar e administrar. Personalidade de 'mãe', mesmo se não for mãe ainda. Se dedica, quer ser útil. Essa carta simboliza a conexão com a terra, a natureza e os aspectos práticos da vida. A Rainha de Ouros representa a força e a segurança financeira, bem como a abundância e a capacidade de cuidar dos outros. Ela é uma figura materna e protetora, que valoriza a estabilidade e o conforto em todos os aspectos da vida. Ela é prática, confiável e tem um senso de responsabilidade bem desenvolvido. Não gosta de correr riscos, colocar a mão onde não alcança, gosta de conforto, segurança, em todos os aspectos da vida. Deve-se atentar ao lado negativo do controle, querer controlar depois coisas e pessoas.",
        "work": "Confiança, estabilidade, valorização, constância nos projetos, rotina.",
        "financial": "Abundância, segurança material, chance de ter ainda mais melhorias, consegue se controlar e se organizar.",
        "love": "Fidelidade, dedicação, família, segurança, controle. Sente-se confortável.",
        "obstacle": "Controle. Pessoa com as características desta Rainha.",
        "advice": "Se manter autoconfiante, manter uma rotina, a vida organizada, preservando a segurança e o conforto."
    },
    {
        "id": 63,
        "name": "Rei de Ouros",
        "major": False,
        "suit": "diamonds",
        "description": "Poder, estabilidade, realização, conquistas materiais, progresso e crescimento. É rígido, pensa apenas no que pode trazer uma vantagem, é sagaz porém inflexível, gosta de controlar. Gosta de conforto (quer qualidade, e não quantidade). Essa carta simboliza a autoridade, o sucesso material e a realização financeira. O Rei de Ouros é um líder confiante, que alcançou um alto nível de segurança e estabilidade em sua vida. Ele possui uma abordagem prática e realista para lidar com questões materiais e é conhecido por sua habilidade em administrar recursos e tomar decisões sábias em relação a negócios e finanças. Como podemos observar na imagem da carta, o Rei de Ouros está de costas para o seu castelo, indicando comportamento egoísta, pensando apenas no que é benéfico para si.",
        "work": "Segurança, destaque, poder, realização de seus desejos e ambições.",
        "financial": "Estabilidade, conquistas, força para gerar ainda mais prosperidade, para prover.",
        "love": "Pode indicar fidelidade, porém com sentimento de controle e possessividade, tende a querer se sentir seguro e confortável, usando do seu poder para isso.",
        "obstacle": "Rigidez, inflexibilidade, controle. Pessoa com características deste Rei.",
        "advice": "Se manter autoconfiante, não fraquejar, continuar os esforços para obter sucesso. Agir de forma muito correta e seguro de si. Controlar, organizar."
    },
    {
        "id": 64,
        "name": "Ás de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Poder, ação, persuasão, autoridade, recomeços, inícios difíceis que exigem racionalidade, responsabilidade e poderá influenciar a longo prazo. Força mental, intelectual, habilidade de pensar, se posicionar de forma segura, autoconfiante, corajosa e saber administrar a realidade. Essa carta simboliza o poder do pensamento e da mente. Ela representa a clareza mental, a intuição aguçada e a capacidade de tomar decisões lógicas e assertivas. O Ás de Espadas indica um momento de insight e compreensão, onde a verdade é revelada e as ilusões são dissipadas. O Ás de Espadas é geralmente considerado um sinal positivo para a vida. Ele indica um novo começo, a oportunidade de alcançar a vitória através do poder da mente. Pode representar uma nova ideia, um plano estratégico.",
        "work": "Capacidade intelectual de iniciar um novo projeto ou persuadir, convencer, tem autoridade, tem conquistas.",
        "financial": "Conclusões positivas, soluções, recomeço de projeto.",
        "love": "Seriedade, recomeços mesmo diante de tempos difíceis, determinação, racionalidade.",
        "obstacle": "Decisão, atitude, persuasão. Recomeço.",
        "advice": "Ter garra e confiar em si mesmo para atingir seus objetivos."
    },
    {
        "id": 65,
        "name": "Dois de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Dúvida, desconfiança, discórdia, rivalidade, empate, egoísmo, momentos tensos onde o racional fala mais alto, a intuição acaba sendo ignorada, a comunicação é falha e se houver interferência de terceiros será através de mentiras ou omissões, causando desconfiança e orgulho. Essa carta representa a tomada de decisões e o dilema interno. A figura com os olhos vendados indica que uma pessoa está passando por uma situação em que precisa usar sua mente e intuição para resolver um conflito. Ela pode estar enfrentando uma escolha difícil, onde há dois caminhos ou opções que parecem igualmente válidas. Ela simboliza a necessidade de equilibrar diferentes aspectos, opiniões ou perspectivas em uma situação. Pode representar um momento de impasse, onde é necessário encontrar um ponto de equilíbrio entre duas forças opostas. Uma figura segurando as espadas mostra a importância de encontrar um meio-termo e evitar extremos. Ao mesmo tempo as espadas (símbolo do racional) fecham o coração, dificultando o sentir, a intuição.",
        "work": "Discórdia, desentendimento com colegas, egoísmo, oposição, nada no momento se resolve, podendo gerar inimizades.",
        "financial": "Dúvidas, momentos de tensão e preocupação, podendo causar dívidas por causa de conflitos e dificuldade de fazer acordos.",
        "love": "Discórdia, desconfiança, falsidade, omite algo, egoísmo, dúvida. Fica na defensiva.",
        "obstacle": "Dúvida, rivalidade, desconfiança.",
        "advice": "Insistir, lutar pelo que acredita."
    },
    {
        "id": 66,
        "name": "Três de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Decepção, separação, perda emocional, tristeza, lágrimas, traição, ferimento, sofrimento, dor, desilusão porque as expectativas não foram supridas. A imagem da carta evoca uma sensação de angústia e desolação. O coração partido simboliza a dor profunda e a sensação de desamparo diante de uma situação dolorosa. As espadas representam a mente e o intelecto, sugerindo que a dor pode ser resultado de uma percepção dolorosa ou de uma verdade difícil de encarar. Essa carta sugere que é importante lidar com a situação de forma honesta e enfrentar a realidade, mesmo que isso envolva enfrentar a dor e o desconforto. No dia a dia pode representar uma separação, um rompimento, enquanto no emocional, uma decepção, sofrer por algo. Necessidade de cuidado especial quando o assunto for saúde e gravidez, podendo gerar perdas, dores e até aborto.",
        "work": "Perdas, rompimento, impossibilidade, incapacidade, traição, decepção causada por terceiros. Rompimento de sociedade.",
        "financial": "Desilusão, demora, perda, erro, tristeza.",
        "love": "Sente-se traído, desiludido, impossibilidade de retorno ou reconciliação. Está triste e desapontado.",
        "obstacle": "Separação, traição, sofrimento.",
        "advice": "Se afastar de tudo que o deixa preocupado ou triste, é o momento de buscar algo novo, seguir em frente, renovar."
    },
    {
        "id": 67,
        "name": "Quatro de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Repouso, recuperação, lentidão, introspecção, isolamento, silêncio, estagnação, adiamento consciente, férias, preguiça. Dificuldade de receber auxílio de terceiros, podendo se sentir sozinho, distante ou ignorado. O Quatro de Espadas representa um período de descanso, recuperação e rejuvenescimento. É um momento em que é necessário reservar um tempo para si mesmo, afastar-se das preocupações e obrigações externas e encontrar um espaço de paz e quietude para recarregar as energias. Pode indicar uma necessidade de se afastar do estresse e das pressões da vida cotidiana para recuperar a energia e restaurar o equilíbrio interno. Em situações do dia a dia, pode indicar dar um tempo, não fazer nada, esperar. Pode indicar um tempo de recuperação de saúde, física ou mental.",
        "work": "Afastamento, atestado médico, férias, preguiça, incapacidade.",
        "financial": "Atrasos, demora, sem ganhos e sem crescimento no momento, necessita poupar.",
        "love": "Afastamento, pouca comunicação, sente-se abandonado, sozinho, necessita se recuperar mentalmente.",
        "obstacle": "Afastamento, repouso, silêncio.",
        "advice": "Esperar, não forçar, deixar o tempo parar, tirar uns dias para repousar."
    },
    {
        "id": 68,
        "name": "Cinco de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Insensibilidade, frieza, vaidade, inveja, fofoca, intriga, soberba, mentiras, omissões, plágio, falsidade. A carta Cinco de Espadas retrata uma cena de conflito e competição. Na imagem, várias figuras estão em posição de confronto, enquanto outras derrotadas parecem ou desanimadas. Essa carta representa desentendimentos, competição desleal, intrigas, fofocas, situações de falsidade, omissões, joguinhos por poder ou até mesmo ações manipuladoras que visam obter vantagem pessoal em cima dos outros. Essa carta sugere a necessidade de cautela, equilíbrio e evitar participar de jogos de poder negativo. Pode representar insensibilidade, ter interesse apenas pelos próprios assuntos e não ter empatia com os demais.",
        "work": "Inveja, fofoca, mentiras, plágio, conflitos, competição por poder.",
        "financial": "Perigo nos investimentos, perdas, problemas burocráticos, acordos não cumpridos, atrasados, o ideal seria não investir no momento. Gastos por egocentrismo. Pode haver brigas por dinheiro, disputas legais e cobranças.",
        "love": "Egoísmo, insensibilidade, preocupa-se apenas consigo mesmo, não tendo sensibilidade com os demais. Podendo omitir informações.",
        "obstacle": "Insensibilidade, fofoca, intrigas.",
        "advice": "Não é o momento de expressar opiniões, melhor se manter calado e distante, deixando o tempo passar."
    },
    {
        "id": 69,
        "name": "Seis de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Mudança de perspectiva, desistência, suspensão, incapacidade, imprevistos, desordem, negligência, falta de auto estima, pensamentos passados influenciam negativamente, vazio emocional, falta de fé ou estímulos. Pode indicar a superação de desafios, a busca por soluções e a decisão de seguir em frente, deixando para trás situações negativas ou emocionalmente pesadas. A carta Seis de Espadas retrata uma figura em um barco, navegando para longe, deixando para trás uma paisagem turbulenta. Essa carta simboliza uma jornada de transição, de deixar para trás dificuldades e buscar uma nova perspectiva ou um lugar de paz e estabilidade. Podendo indicar viagens, não a passeio, mas sim para resolver algo importante, indicando distância física, ou viagem a trabalho.",
        "work": "Viagem a trabalho. Mudança de planos, desistência, sem criatividade, falta de planejamento, necessidade de mudar algo.",
        "financial": "Instabilidade, sem retorno, necessidade de buscar novas opções. Viagem.",
        "love": "Instabilidade emocional, sente-se sem expectativas. Afastamento, necessidade de abandonar o passado e buscar novos caminhos.",
        "obstacle": "Viagem, distância. Desistência.",
        "advice": "Férias forçadas, precisa relaxar, descansar a mente e o corpo."
    },
    {
        "id": 70,
        "name": "Sete de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Trapaça, malandragem, esperteza, malícia, sagacidade, perspicácia, deve-se manter atento, ser inteligente e agir com cautela. Podendo ser vítima de um roubo, furto ou golpe, como também ter a necessidade de ser sagaz, ligeiro e ter astúcia. A atmosfera é de disfarce, estratégia e possíveis intenções ocultas. Essa carta representa situações em que a astúcia, a dissimulação e a manipulação podem estar presentes. Essa carta também pode indicar a necessidade de adotar uma abordagem estratégica em suas ações. Ela sugere que você avalie cuidadosamente suas opções e tome medidas inesperadas para alcançar seus objetivos. Pode ser necessário usar táticas inteligentes ou se afastar de situações desfavoráveis. No entanto, é importante lembrar que ações controladas na manipulação ou na desonestidade podem ter consequências negativas a longo prazo. Deve-se atentar com saúde do corpo físico, podendo haver algum prejuízo por causa de saúde.",
        "work": "Cuidado com fofocas, pode haver competição. Novos planos, esforço e empenho para ter um resultado futuro. Situações perigosas que exigem astúcia e destreza para com o social.",
        "financial": "Cuidado com bens materiais, furtos, roubos, golpes, propostas duvidosas.",
        "love": "Manipulação, malandragem, quer tirar alguma vantagem, sente-se espertinho e tem esperança de conseguir aquilo que deseja.",
        "obstacle": "Manipulação, esperteza, golpe.",
        "advice": "Cuidado com a forma que fala ou age com os demais, necessidade de ser esperto, sagaz. Melhor ficar calado."
    },
    {
        "id": 71,
        "name": "Oito de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Procrastinação, deslealdade, inconsciência, pensamentos acelerados, cegueira, desespero, omissão, reprovação, condenação, críticas que desestabilizam o psicológico. Vitimização, o consulente reclama e sofre por tal situação, que ele mesmo causou. É a sensação de estar preso em uma situação ou padrão de pensamento negativo. Pode representar a maneira como nos colocamos em restrições autoimpostas, criando obstáculos e limitações em nossa vida. A venda nos olhos indica uma falta de clareza ou percepção em relação à situação em que nos encontramos. As Espadas representam suas próprias crenças limitantes, medos ou padrões de pensamento. Pode estar se sentindo preso, se sabotando.",
        "work": "Sente-se inapto, cria problemas e limitações, podendo ter consequências negativas por causa de suas próprias ações.",
        "financial": "Pode representar uma sensação de impotência ou falta de liberdade em relação às finanças. Sente-se preso em uma situação financeira difícil, incapaz de encontrar uma solução ou uma saída. Podendo haver prejuízos.",
        "love": "Sente-se traído, reclama da relação, sente-se limitado, inseguro, não enxergando suas próprias atitudes.",
        "obstacle": "Ansiedade, procrastinação, pensamentos acelerados, erros causados pelo próprio consulente.",
        "advice": "Falar a verdade, fazer o correto, não alimentar o erro. Necessidade de pedir ajuda (ajuda médica se sentir algo na saúde e ajuda terapêutica para a saúde mental)."
    },
    {
        "id": 72,
        "name": "Nove de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Vitimização, ansiedade, insônia, desespero, arrependimento, remorso, angústia, aflição, sofrimento, imaturidade emocional causando pensamentos negativos. Necessidade de cuidar da saúde, fazer exames médicos ou fazer cirurgia. Nove de Espadas retrata uma figura solitária sentada na cama, com expressão de angústia e as mãos no rosto. Acima dela, no céu, há nove espadas suspensas, representando preocupações, ansiedades e medos. Essa carta simboliza a inquietação mental, a angústia emocional e a preocupação excessiva, causando remorso, pensar depois em passado e o que poderia ter feito diferente. Indica uma mente sobrecarregada por pensamentos negativos, medos e preocupações excessivas. Essas preocupações podem ser reais ou imaginárias, mas independentemente disso, elas estão causando um grande impacto emocional e mental.",
        "work": "Ansiedade, culpa, nervosismo, preocupações que perturbam a mente e causam medo. Afastamento em função da saúde.",
        "financial": "Preocupações com dinheiro ou dívidas, inquietação e estresse por falta de segurança. Gastos com saúde.",
        "love": "Medo por causa do passado, culpa, remorso, nervosismo, sente-se sozinho mesmo estando próximo de outras pessoas. Culpa-se por tudo.",
        "obstacle": "Ansiedade. Saúde.",
        "advice": "Necessidade de se afastar dos problemas para refletir seus erros."
    },
    {
        "id": 73,
        "name": "Dez de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Dor, sofrimento, apunhalada nas costas, traição, karma (no sentido de evoluir), última dor podendo ter uma renovação logo em seguida. Mártir, culpa. A carta Dez de Espadas é frequentemente interpretada como um símbolo de angústia, sofrimento e dor intensa. Ela sugere o fim de um ciclo ou situação difícil, representando um momento de colapso, esgotamento e desespero. Pode ser um indicativo de que uma situação ou problema se tornou insustentável e está chegando ao seu ponto mais baixo. Pode simbolizar traição, decepção ou uma crise profunda. Também pode representar a sensação de ser oprimido pelas circunstâncias, onde todos os esforços parecem inúteis. O aprendizado seria uma oportunidade para crescer, traz uma ideia de karma, aprender com os erros e se reconstruir após uma crise. Pode indicar também desistir de algo, mudar a opção.",
        "work": "Encerramento, decepção, traição, decisão, perdas.",
        "financial": "Perdas, finalizações dolorosas, perdas.",
        "love": "Decepção, dor com o passado gerando mágoas, ansiedade, discórdia, necessidade de terminar um episódio e começar uma nova etapa da vida.",
        "obstacle": "Término, dor passada.",
        "advice": "Necessidade de mudar o comportamento e pensamentos."
    },
    {
        "id": 74,
        "name": "Pajem de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Mentiras, omissão, fofoca, intriga, falsidade. Ficar na defensiva, atacando e tentando se defender do mundo, mesmo sem estar em perigo. Espionagem, stalker, se esconde para observar. Manipulador, tenta persuadir para que suas vontades sejam feitas. Momentos estressantes com pessoas perigosas. Sabe persuadir, tem pensamento rápido, ágil, sagaz, inteligente. Essa carta também pode representar a energia de tomar decisões lógicas e racionais, lidar com problemas de forma objetiva e utilizar a mente de forma estratégica. Também pode ter uma conotação negativa em algumas circunstâncias, e pode representar uma pessoa jovem que é fria ou insensível emocionalmente. Também pode indicar uma mentalidade cínica ou uma tendência a manipular os outros através das palavras. Deve-se atentar a saúde dos filhos.",
        "work": "Cuidado com fofocas, mentiras, ou pessoas espertinhas.",
        "financial": "Sagacidade para resolver problemas e encontrar soluções rápidas, porém pode passar por um período estressante. Cuidado com propostas duvidosas.",
        "love": "Quer manipular para ter razão, é esperto, frio e sabe usar as palavras ao seu favor.",
        "obstacle": "Omissão, falsidade, fofoca.",
        "advice": "Pondere as palavras, cuidado ao se relacionar, nem tudo precisa ser dito, seja perspicaz."
    },
    {
        "id": 75,
        "name": "Cavaleiro de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Rapidez, agilidade, empenho, esforço mental e intelectual, determinação, disposição, ousadia para enfrentar os obstáculos e alcançar seus objetivos, sempre de uma forma direta, racional e sem medo. O Cavaleiro de Espadas representa energia e ação direcionada para a mente e o intelecto. Ele simboliza a coragem, a força e a busca pela verdade e pelo conhecimento. Essa carta é associada a alguém que é lógico, ágil, analítico e tem habilidades estratégicas. Pode ter uma tendência a ser demasiadamente racional, frio ou distante emocionalmente, ser impaciente e agir de forma impulsiva, sem considerar completamente as consequências de suas ações.",
        "work": "Esforço, empenho, busca crescer, alcançar algo. Impulsividade, rebeldia, quer seguir sua verdade.",
        "financial": "Possibilidade de melhoria através da sua disposição. Apenas deve-se tomar cuidado com gastos por impulso ou atitudes que podem gerar maus resultados.",
        "love": "Se esforça, quer conquistar, é rápido, ágil, não espera. Pode ser um pouco mais frio, não demonstrando tanto romantismo.",
        "obstacle": "Ter agilidade. Pessoa com as características deste Cavaleiro.",
        "advice": "Siga em frente com seus planos, não espere. Momento de agir."
    },
    {
        "id": 76,
        "name": "Rainha de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Prática, direta, racional, impaciente, insensível. Intolerância, rancor, frieza, distanciamento, desentendimento, constrangimento, soberba, dificuldade em ter paz ou sentir amor ou perdoar. A Rainha de Espadas simboliza características como inteligência, racionalidade, perspicácia e poder de análise. Ela é uma mulher de mente aguçada, capaz de pensar de forma lógica e objetiva. A Rainha de Espadas é conhecida por sua habilidade em lidar com situações com clareza, tomar decisões determinadas na razão e na verdade, e comunicar-se de forma direta e precisa. Rainha de Espadas também pode ter uma tendência a ser crítica demais, distante emocionalmente ou dominadora. Ela pode respeitar a lógica e a razão acima das emoções, o que leva a uma falta de empatia em certas situações.",
        "work": "Cumpre com as obrigações, mesmo se não estiver satisfeito, faz o que deve ser feito. Sem muitas novidades.",
        "financial": "Problemas que precisam ser solucionados, buscando alternativas diferentes.",
        "love": "Frieza, separação, distância física, insensibilidade, raiva, obsessão, não consegue perdoar.",
        "obstacle": "Frieza, distância. Pessoa com as características desta Rainha.",
        "advice": "Seguir em frente com seus objetivos a qualquer custo."
    },
    {
        "id": 77,
        "name": "Rei de Espadas",
        "major": False,
        "suit": "spades",
        "description": "Racional, direto, frio, insensível, prefere não falar, não se expressar, tenta se manter no mesmo lugar, sem alterações. Demora, atraso, distância. Força, estratégia, inteligência, praticidade, autocontrole. O Rei de Espadas é conhecido por sua natureza lógica, racional e intelectual, tem habilidades de análise e resolução de problemas. Ele toma decisões na lógica, na razão e em princípios éticos. Sua mente afiada e clara permite que ele veja além das aparências e compreenda a verdade subjacente em qualquer situação. Sempre leva em consideração a razão, e nunca a emoção, podendo demonstrar frieza e insensibilidade. É severo e inflexível consigo mesmo. Pode demonstrar indiferença, desinteresse.",
        "work": "Poder de tomar decisões. Ritmo de trabalho lento, sem novidades porém seguro.",
        "financial": "Segurança, estabilidade. Sem mudanças ou surpresas financeiras.",
        "love": "É frio, distante, fechado, egoísta, insensível. Não deseja se relacionar no momento. Distanciamento, separação momentânea.",
        "obstacle": "Frieza, afastamento, demora. Pessoa com as características deste Rei.",
        "advice": "Ter foco, faça chuva ou faça sol, insista nos seus objetivos."
    }
]

runes = [
    {
        "id": 0,
        "name": "Fehu",
        "power": "Posses, riquezas, propriedades, conquistas. Início de ciclos, alta capacidade criativa e de constância, pois tudo aquilo que é conquistado, precisa continuar, sem perder o ritmo. Por ser fogo, proporciona a abertura de caminhos junto com a força impulsionadora do fogo, ampliando e também gerando transformações. Amplia o que já existe, tornando ainda mais próspero e nutrindo o foco. força e movimento. também é destruição, pois tudo que inicia, acaba.",
        "magic": "Reforça os poderes psíquicos; serve como canal de transferência ou projeção de poder; captação dos poderes dos astros para a esfera pessoal; promove a evolução pessoal social e o aumento dos bens.",
        "tree": "Sabugueiro",
        "rock": "Cornalina (boa sorte e fertilidade); Turmalina Verde (transferência de energia para a esfera pessoal); Âmbar (vitalidade)",
        "color": "Vermelho-claro"
    },
    {
        "id": 1,
        "name": "Uruz",
        "power": "Força, persistência, adaptabilidade, mesmo sofrendo ou estando em uma posição não favorável, me mantenho firme e forte. Ligada, também, à saúde física e psíquica, estimulando persistência, coragem, agressividade com sabedoria e discernimento, na hora certa, inteligência e controle da impulsividade/fúria. Ao lidar com alguém indeciso, a Uruz faz com que a pessoa tenha um poder maior de decisão, impulsionando-a a agir e sair da lentidão. Trabalha com a ideia de correr risco para ter mudança. Tira do medo e leva até a sabedoria. Na saúde, trabalha músculos, força, vigor, energia e movimentação geral.",
        "magic": "Serve para formar e moldar circunstâncias criativamente através da vontade e da inspiração; cura e manutenção da boa saúde física e mental; proporciona situações afortunadas (muito usada como talismã); indução das correntes magnéticas da Terra (as 'Veias do Dragão'); realização da causalidade; conhecimento e compreensão do Self.",
        "tree": "Bétula",
        "rock": "Olho-de-Tigre (traz coragem, confiança e força)",
        "color": "Verde-escuro"
    },
    {
        "id": 2,
        "name": "Thurisaz",
        "power": "Representa os conflitos, adversidades voltadas à natureza agressiva, problemas internos, psicológicos. Ótima para problemas 'reativos', como ídolo, esquizofrenia, pois possui uma força que retira do interno para o externo, expurgando. É vista como uma runa defesa-ataque, como um contra-feitiço. Lembra um porco-espinho, que seu maior ataque é sua própria defesa. Rompe todas as barreiras, todas as defesas e limpa o crescimento, como um renascimento. Abre o caminho para a pessoa, como uma fênix. Limpa excessos. A mente se submete, se abre e permite a entrada da sua intenção e ação, do consciente ao subconsciente.",
        "magic": "Defesa ativa; destruição dos inimigos; maldição; o despertar da vontade de agir; preparo para a geração em todos os sentidos; magia para o amor; conhecimento da divisão e da unidade de todas as coisas.",
        "tree": "Carvalho",
        "rock": "Ágata (proteção); Hematita (força e coragem para o combate)",
        "color": "Vermelho-forte"
    },
    {
        "id": 3,
        "name": "Ansuz",
        "power": "Significando boca, representa a comunicação inteligente, efetiva e com qualidade, regida por Mercúrio. Traz a mensagem com mais entonação, mais força e capta a atenção dos ouvintes, prestando atenção. Passa confiança de alguém com autoridade, gerando entrosamento e embasamento no que é dito, com ótima oratória, inteligência, congruência e poder. Ótimo uso para líderes, comunicadores, influenciadores e vendedores. Trabalha a espontaneidade.",
        "magic": "Aumento dos poderes mágicos ativos e passivos; desenvolvimento das habilidades clarividentes, do dom da palavra magnética e convincente, do poder de sugestão e hipnose; aquisição de conhecimento criativo; inspiração e êxtase; comunicação divina; afastamento da morte e do temor através do conhecimento de Óðinn.",
        "tree": "Freixo",
        "rock": "Lápis-lázuli (estabelece uma ponte entre o humano e o Divino)",
        "color": "Azul-escuro"
    },
    {
        "id": 4,
        "name": "Raidho",
        "power": "Representa a roda, o movimento, o correto equilíbrio entre a linha tênue do respeito e até onde podemos ir por alguém, ou seja, sinalizando os limites. A ideia da Raido é termos pleno controle da direção da nossa vida, e não o contrário. É estar no comando e de acordo com nossa vontade. Eu movimento meu destino! Ajuda muito na viagem astral, pois nos impulsiona até o destino. Raido fala sobre movimentação, deslocamento e irmos atrás, sobre o real desejo de atingirmos nossos objetivos através das nossas próprias ações, tendo constância.",
        "magic": "Fortalece as habilidades rituais e sua experiência; acesso ao aviso interior; aumenta a consciência de processos naturais; atua na combinação de ritmos pessoais (internos) e exteriores; obtenção de justiça de acordo com o direito.",
        "tree": "Carvalho",
        "rock": "Turquesa (indica o melhor caminho rumo a um objetivo); Jacinto (assegura bons relacionamentos sociais/cooperação)",
        "color": "Vermelho-claro forte"
    },
    {
        "id": 5,
        "name": "Kenaz",
        "power": "Significa saber. Vinculada ao processo de ensino e aprendizado. Se refere à aproximação, união de membros de uma mesma equipe e mesmo fim. Ajuda também na conexão. Trás congruência e autoridade caso eu a utilize com o intuito de convencer, trás exclusividade e valor, como algo precioso. Também trás clareza, por ser fogo, trás energia, entusiasmo, êxtase, gera emoção e conexão, sendo vista como a melhor opção. Boa também para fascinação. O fogo abre o caminho, queimando obstáculos, ajuda na regeneração do corpo e na resiliência. No campo sexual, traz excitação, tesão e energia alta, liberando os hormônios com maior força (vasodilatação).",
        "magic": "Reforço das habilidades em todos os campos; inspiração criativa; maior polarização como instrumento de operações mágicas; operações de regeneração e cura; trabalho para o amor (principalmente sexual).",
        "tree": "Pinheiro",
        "rock": "Ágata de Fogo (ligação com as energias criativas da Terra); Quartzo Fumê (estimula e purifica o chacra base ou raiz)",
        "color": "Vermelho-claro"
    },
    {
        "id": 6,
        "name": "Gebo",
        "power": "Representa troca, relações harmoniosas e recíprocas, gera conexão verdadeira, empatia e amplia o foco no momento agora, gerando presença e atenção plena. Por ter a energia da reciprocidade, é considerada uma runa de 'pagar o preço', pois eu preciso entregar algo para também receber. Ao ser utilizada em outra pessoa, gera uma boa impressão e interesse, podendo fortalecer o laço já existente ou dando início a um possível relacionamento, não necessariamente amoroso.",
        "magic": "Magia sexual; iniciação mágica sexual; união mística; aumento dos poderes mágicos; harmonia entre irmãos e amantes; influência mágica nos mundos humano e Divino; aquisição de sabedoria.",
        "tree": "Freixo ou Olmo",
        "rock": "Esmeralda (equilíbrio dos aspectos físico, mental e emocional); Jade (pureza e serenidade; desenvolve a capacidade de amar)",
        "color": "Azul-profundo"
    },
    {
        "id": 7,
        "name": "Wunjo",
        "power": "Representa o ar, catavento. A ideia de buscar a perfeição, buscar a completude das coisas. Trabalha no sentido da realização, buscando até mesmo, se intencionado, gerar desejos nas pessoas. Sucesso nos planos e metas. Também age no sentido de fazer as coisas acontecerem. Triunfo, vitória, celebração, tranquilidade, alívio e fluidez. Transformação. Na saúde, trabalha a respiração.",
        "magic": "Reforça laços e coesões; invocação de amizade e harmonia; afasta a alienação; felicidade e bem-estar, relacionamento de laços e multiplicidade de relacionamentos de todos os tipos; 'acabamento' em rituais que envolvem runas de significado específico, reforçando-os.",
        "tree": "Freixo",
        "rock": "Topázio (traz alegria); Quartzo Rosa (abre o coração)",
        "color": "Amarelo"
    },
    {
        "id": 8,
        "name": "Hagalaz",
        "power": "Representa as forças do passado. Lições que não foram bem finalizadas e aprendidas. Experiências de vida das quais não aprendemos a mensagem, problemas e memórias mal resolvidos e pendentes. Problemas familiares, amorosos e de qualquer teor, que de alguma forma seguem ainda presos em nós, comprometendo nossa realidade atual, como crenças, comportamentos e situações que se repetem, gerando caos e 'distúrbios'. É aquela destruição que temos que enfrentar para 'nascermos' novamente, renovados e amadurecidos. Ela trás uma nova consciência, limpando o passado e nos tirando da dor e paralisia. Na saúde: sangue, cortes, ferimentos, pois ameniza a dor. É como, também, uma tocha que ilumina o local, iluminando as sombras.",
        "magic": "Integração e balanço (= equilíbrio) de poder; experiência e sabedoria mística; proteção.",
        "tree": "Teixo ou Freixo",
        "rock": "Ponta de Quartzo Transparente (concentra a energia em um único ponto; ajuda a focalizar o melhor caminho para romper velhos hábitos ou estabelecer novos)",
        "color": "Azul-claro"
    },
    {
        "id": 9,
        "name": "Nautiz",
        "power": "Necessidade de autoperdão em relação a alguma experiência que gerou culpa, que hoje nos paralisa, como se fosse uma pendência a se resolver, travando um pouco de dar o passo adiante. Nos mostra que somente com trabalho duro conquistaremos nossos objetivos, fazendo com que valorizemos nossos esforços honestos. Ela remove limitações, desbloqueia e ajuda a desvincular com os erros do passado. Auxilia a nos colocar na frequência gamma, relacionada a clareza mental, insights, ideias e visões de soluções, mas não só em meio a problemas, ela ajuda também a como trabalharmos nossos objetivos, descobrindo novos meios. Relacionada a braços, estresse, obsessões, vícios, questões compulsivas e bloqueios mentais.",
        "magic": "Superação da angústia; desenvolvimento da vontade mágica; desenvolvimento de poderes espirituais; uso da força da resistência sobre a vontade com propósitos mágicos; inspiração; elimina o ódio e as disputas; ajuda a criar uma necessidade de ordem; proteção; adivinhação.",
        "tree": "Faia",
        "rock": "Obsidiana (mostra ao Ego de modo rude e muitas vezes grosseiro o seu devido lugar e o que precisa para mudar e avançar para o próximo passo de desenvolvimento evolutivo)",
        "color": "Preto"
    },
    {
        "id": 10,
        "name": "Isa",
        "power": "Gelo, congela, acalma. Representa a paralisação, a pausa, cristalização. Tem a ideia de quebrar a resistência para que possamos mudar. É uma runa estática, faz com que algo seja paralisado e concentrado. Ótima para ser usada em bindrunes. Ajuda no foco, concentração e atenção. Ela, utilizada sozinha, nos deixa lerdos. Ajuda a mudar o padrão de comportamento, como por exemplo os pensamentos repetitivos destrutivos que temos no dia a dia, pois os mesmos ficam retornando a todo momento, nos atordoando e estressando. Ajuda na saúde em úlceras, gastrites, ansiedades, crises, nervosismos. Exemplo de combinação: Isa + Inguz = Prende a energia sexual, mantendo-a ativa.",
        "magic": "Desenvolvimento da concentração e da vontade; contração/redução/parada das forças dinâmicas não desejadas; integração do Ego com o sistema multiversal equilibrado; poder de controle sobre outras criaturas.",
        "tree": "Amieiro",
        "rock": "Gema de Sílica ou Diamante Herkimer (liberam tensões emocionais ou áreas congestionadas)",
        "color": "Preto"
    },
    {
        "id": 11,
        "name": "Jera",
        "power": "Plantio e colheita. Justiça, recompensa pelos feitos. Indica que tudo são ciclos, fluxos e etapas, movimentos. Ligada à fertilidade da colheita, relacionada ao que fiz pela vida, recebendo meu 'karma' pelas minhas ações. Lembra que minhas ações possuem consequências e ninguém foge disso. Ótimo uso para quando precisamos que a justiça seja feita e com mais velocidade, precisão. Também é finalizações de etapas e ciclos, mas ao mesmo tempo, abre uma nova etapa para o '2° round'.",
        "magic": "Fertilidade; criatividade; paz e harmonia; iluminação; realização da natureza cíclica do Multiverso; realização do mistério da circunferência onipresente (= a totalidade de um ciclo); trazer outros conceitos a uma realização material.",
        "tree": "Carvalho",
        "rock": "Ágata Musgosa (sintoniza quem a usa com as forças da natureza, ajudando o metódico a entrar em contato com seu lado intuitivo e o criativo a canalizar suas energias de modo mais prático).",
        "color": "Azul-claro"
    },
    {
        "id": 12,
        "name": "Eihwaz",
        "power": "Indica uma necessidade de pausa em prol de um conflito emocional que precisa ser resolvido. Nos faz entender que devemos correr o risco, nos posicionarmos assertivamente sem ficarmos mornos, paralisados na dúvida, em cima do muro. Além disso, ótimo símbolo para que resolvamos uma situação complicada estagnada. Proporciona sabedoria, clareza e reconhecer o caminho certo, sem ilusões e distrações. De volta ao centro.",
        "magic": "Proteção; defesa; comunicação mística ou religiosa com seres não-humanos; comunicação com outros mundos (principalmente Asgarðr) e as fontes Cósmicas de Urðr, Minir e Hvergelmir; fortalecimento de hamingia (= sorte) e da força vital.",
        "tree": "Teixo",
        "rock": "Turmalina Negra (proteção)",
        "color": "Ouro"
    },
    {
        "id": 13,
        "name": "Sowilo",
        "power": "Símbolo do Sol, da energia. Fala sobre a luz, a verdade, o divino, o sucesso. Intenção elevada, poder, reconhecimento do eu interior no processo de evolução. Ilumina muito em momentos de busca do desenvolvimento pessoal. Passa insights, orientações, clarezas. Vigor, saúde e disposição. Empodera nossas qualidades e personalidade, mas também ilumina o oculto, logo, nossos problemas e sombras. Tira fora toda dúvida, sombra, mentiras, enganações e autosabotagem.",
        "magic": "Fortalecimento dos centros psíquicos; aumento da vontade espiritual; orientação pelo caminho; iluminação; vitória e sucesso através da vontade própria.",
        "tree": "Zimbro ou Junípero",
        "rock": "Diamante (amplifica a presença da Luz)",
        "color": "Branco ou Prata"
    },
    {
        "id": 14,
        "name": "Tiwaz",
        "power": "Runa do Guerreiro. Usada muito pelos vikings nas espadas e em suas guerras para conquistar uma vitória justa, honesta e merecida. Ela fala muito sobre uma atitude, uma força mais impulsiva, 'obrigando' a sair da energia da inércia e passividade. Coragem, determinação, correr riscos e enfrentar seus maiores medos. 'Sem dúvida, terei minha vitória! Botarei a cara à tapa'. Faz ir além, mesmo cansado, sem forças, dando 101% de esforço. Como é de essência espiritual, nos faz ir além do material. A 'guerra' tem que ser grandiosa e não superficial. A Tiwaz pode ser vista como um anjo espiritual, fortalecendo e evitando a queda dos seus protegidos. No comportamento, passa a imagem de alguém imponente, com poder, respeito e até certo temor. Autoridade, hierarquia, importância. Alfa. Saúde: mãos, dedos, articulações, ossos, força no passe magnético e energia.",
        "magic": "A obtenção da justa vitória e sucesso; desenvolvimento da vontade espiritual; desenvolvimento do poder de auto-sacrifício positivo; desenvolvimento da fé em magia e religião.",
        "tree": "Carvalho",
        "rock": "Rubi (fornece suprimento extra de energia quando o desânimo ameaça o domínio de uma situação); Bloodstone ou Heliotrópio (aumenta a coragem)",
        "color": "Vermelho Vibrante"
    },
    {
        "id": 15,
        "name": "Berkana",
        "power": "Energia feminina, emotiva, sensitiva, acolhedora e introspectiva. Nutre, zela, abraça e acolhe, lembrando muito uma mãe. Possui a energia da fertilidade, sendo ótima para projetos, manter a constância, gerar novas ideias e levar adiante, dando atenção aos detalhes. Diminui preocupações, ansiedades, ajuda na sensibilidade, traz acolhimento, emotividade e influencia muito no início e fim de ciclos, pois entende a hora certa de tudo. Na saúde, ótima em uso geral.",
        "magic": "Renascimento espiritual; fortalecimento dos poderes do segredo; trabalho de encobrimento e proteção; contenção e manutenção de outros poderes; realização da unidade, da harmonia do momento como mãe de todas as coisas; traz idéias à tona no processo criativo.",
        "tree": "Bétula",
        "rock": "Jet ou Azeviche (grande poder de absorção da energia negativa)",
        "color": "Verde-escuro"
    },
    {
        "id": 16,
        "name": "Ehwaz",
        "power": "Cavalo de asas de Odin. Potência, velocidade e astúcia. Representa a força da inspiração para ir além, ultrapassando a dificuldade de uma maneira de cima, pelas asas representando a consciência elevada divina. Mais do que tudo, é movimento, então nos ajuda em todos os sentidos. O cavalo é transporte e o único animal capaz de nos fazer alcançar todos os planos, logo, ótima para viagem astral. Muito usada para visitar o passado e limpar aquilo que está pendente, nos paralisando aqui no hoje. Na saúde, ótima para costas e pernas.",
        "magic": "Simplificação da viagem da alma através dos mundos e projeção da alma em Midgarðr; realização da unidade fundamental do complexo psicossomático; concede fé e lealdade; fonte de conhecimento profético; projeção do poder mágico; rapidez e velocidade em todos os aspectos.",
        "tree": "Carvalho ou Freixo",
        "rock": "Turquesa ou Sardonix (estimula a autoconfiança)",
        "color": "Branco"
    },
    {
        "id": 17,
        "name": "Mannaz",
        "power": "Humanidade. Empatia, compaixão, conexão verdadeira, persuasão e humildade. Corta o ego, a arrogância e a mentira da superioridade. Traz a humildade e simplicidade de volta, olhando 'reto' para as pessoas. Equilibra a empatia, nos amadurece e ajuda nas curas e desenvolvimento pessoal. Por ser uma runa voltada ao convívio social, à humanidade, ela é ótima para o verdadeiro rapport, gerando uma ótima impressão e aumentando nosso valor social, tendo mais influência, presença e persuasão.",
        "magic": "Realização da Estrutura Divina na humanidade; aumento da inteligência, da memória e dos poderes da mente; equilíbrio dos pólos da personalidade; liberação do hugauge – a terceira visão.",
        "tree": "Azevinho",
        "rock": "Ametista (realiza a integração do Eu Inferior com o Eu Superior propiciando a individuação)",
        "color": "Vermelho-Escuro"
    },
    {
        "id": 18,
        "name": "Laguz",
        "power": "Água, emoção, abertura e vulnerabilidade. Purificação, limpeza, sensibilidade e ampliação de magnetismo e intuição, ajudando a 'digerir' as situações dolorosas que paralisam. Comunica a ideia de movimentação, ir a algum lugar, fazendo com que as coisas fluam para estarem onde devem. Também é símbolo de flexibilidade, pois a água se adapta a qualquer ambiente. Está conectada, também, à lua, que a mesma é água, nos ajudando a passar por todas as fases da vida, inclusive nossa parte sombria, acessando nossos sentimentos e emoções, soltando tudo que é tóxico.",
        "magic": "Orientação em testes iniciatórios difíceis; aumento de vitalidade e força de vida; coleta e reunião de poder mágico amorfo para a formação e estruturação pela vontade; aumento de magnetismo; desenvolvimento da segunda visão.",
        "tree": "Salgueiro",
        "rock": "Malaquita (canaliza as forças superiores para finalidades humanitárias. Para os que se encontram em processo de purificação, age como expurgador e espelho para o subconsciente, refletindo na mente consciente o que requer depuração).",
        "color": "Verde-Profundo"
    },
    {
        "id": 19,
        "name": "Ingwaz",
        "power": "Energia masculina da fertilidade, voltada ao masculino. Ajuda com impulsionamento das coisas, dando mais força, potência e velocidade, ajudando a fazer acontecer através da energia sexual. Tesão, excitação, libido, vontade, auto confiança, poder dominante, fogo, expansão e iniciar. Gera muito movimento e é excelente também para o campo sexual/amoro.",
        "magic": "Armazenamento e contenção de poder para uso ritual; ritos de fertilidade; meditação passiva; centralização da energia e do pensamento; súbita liberação de energia.",
        "tree": "Macieira",
        "rock": "Marfim (afeta a maneira pela qual o indivíduo examina a sua existência, ajudando na concentração, na introspecção e na análise. Devido a sua origem animal, deve ser usado com muito critério – somente se for realmente necessário – ou sua energia se volta contra o mago).",
        "color": "Amarelo"
    },
    {
        "id": 20,
        "name": "Dagaz",
        "power": "Representa o novo dia, o amanhecer, a renovação e a transição para o novo início. Associada ao elemento Ar, trás ideias e insights, organizando nosso mental para termos clareza. Tudo aquilo que precisa ser finalizado, será; a Dagaz trás a força que não temos, o impulso que precisamos para passar por uma dificuldade que nos paralisa. Representa a luz do fim do túnel, a mudança drástica e nos devolve o controle da própria vida. Fim do negativo para o positivo tomar conta.",
        "magic": "Atingir o momento místico através da penetração do segredo do Paradoxo Odínico; recepção da inspiração mística.",
        "tree": "Abeto Vermelho",
        "rock": "Fluorita (sintoniza a mente com o espírito, desenvolvendo a compreensão intelectual da verdade, dos conceitos cósmicos da realidade e das leis que regem o universo).",
        "color": "Azul-Claro"
    },
    {
        "id": 21,
        "name": "Othala",
        "power": "Busca contato direto com a ancestralidade, como padrões de herança, com o intuito de fazer a mudança nas pessoas. Trabalha muito com os traços genéticos e familiares, ajudando a reconhecer o que de fato é nosso e o que herdamos da linhagem ancestral, como padrões e sistemas, nos dando consciência, discernimento e libertação para vivermos nossa individualidade no hoje. Autenticidade, personalidade, consciência, ressignificação, lembranças e memórias. Conexão com o tempo passado. Muitas vezes, essa ruptura precisa acontecer, mesmo que de forma drástica. A morte (renovação) vem e o novo toma espaço. Sacrifícios. Ótima, também, para resgatarmos traços positivos de herança emocional familiar, conhecendo mais sobre nossa família e aperfeiçoando o autoconhecimento, nos proporcionando maturidade e evolução.",
        "magic": "Manter a ordem entre companheiros; concentração em interesses comuns em casa, na família e na sociedade; passagem de egocentricidade para clanocentricidade (relativo ao clã); recepção de Poder Divino e sabedoria de gerações passadas; aquisição de riqueza e prosperidade.",
        "tree": "Espinheiro",
        "rock": "Madeira Petrificada (traz memórias e talentos de vidas passadas que servirão para despertar o dragão ancestral do poder)",
        "color": "Amarelo-Escuro"
    },
    {
        "id": 22,
        "name": "Perth",
        "power": "Vista como a boca do lobo e também como 'útero cósmico', onde surge tudo que desejamos, sendo a força da vida. É onde podemos buscar as respostas da vida e não permanecermos na dúvida, indecisão. Faz com que tudo se revele dentro de nós. A sombra se ilumina, o segredo é desvendado e a verdade vem à tona. Conseguimos usar dons ocultos que temos e não tínhamos consciência. Pertinente, ajuda a eliminarmos as dúvidas e ver o lado 'correto', pois a mentira não existe com essa runa em ação. Mudanças mais drásticas, liberações e renovações. Ajuda também a encontrarmos pertences perdidos. Saúde: peitos e vagina, pois é 'nascimento'."
    },
    {
        "id": 23,
        "name": "Algiz",
        "power": "Pelo seu expansivo formato de abertura, representa a canalização dos deuses para os homens, e vice-versa. Falando muito sobre a proteção divina, ela nos remete à bravura de um alce, o guerreiro com os braços para cima, destemido e pronto para o combate. Sensação de autoridade, valor, bravura, coragem e poder pessoal. Como estabelece uma conexão com o divino, nos auxilia trabalhando nossa premonição, diretamente pela intuição, fazendo com que tenhamos mais atenção e que recebamos insights, protegendo-nos do perigo. Ela estabelece as ondas gamma, facilitando a consciência de estar atenta. Ótima para utilizar no magnetismo à distância, pois evita que interferências negativas se conectem na união. Na saúde, trabalha com a sanidade mental, pois é onde o todo trabalha."
    }

]

daemons = [
    {
        "id": 0,
        "name": "Baal",
        "enn": "Ayer Secore On Ca Ba al",
        "description": "O Primeiro Espírito Principal é um Rei que governa no Oriente, chamado Bael no Ars Goetia, mas aqui usaremos o nome real dele: Baal. Ele é o representante na Terra do Senhor Enki, e o primeiro entre os deuses antigos. Comanda um exército de 66 legiões de espíritos. Sendo poderoso, porém extremamente discreto, Baal pode usar diferentes formas para se comunicar com aqueles que o procuram. Essas aparências podem variar, estando entre elas a de um gato, um sapo ou, a mais clássica: um homem jovem, com características felinas. Quando se comunica, sua voz é grave e rouca.\n\nSegundo o Ars Goetia, a ele é atribuída a capacidade de tornar indivíduos invisíveis. \"Ficar invisível\" pode ter diferentes significados dependendo do contexto em que é utilizado. Por exemplo, na esfera espiritual ou sobrenatural, \"ficar invisível\" pode se referir à capacidade de Bael de fazer com que um indivíduo se torne imperceptível aos olhos dos outros seres, sejam eles humanos ou espíritos. Isto pode ser algo bem útil, porque a pessoa pode se camuflar ou se esconder fisicamente, tornando-se difícil de ser localizada. Assim a pessoa pode, por exemplo, transitar por lugares onde a sua presença não está permitida, sem chamar a atenção. Ou pode andar em meio a outras pessoas, sem ser percebida, mas vendo e ouvindo tudo, já que, como ninguém vai notar a sua presença, as pessoas vão falar livremente na sua frente.\n\nBaal era conhecido como o Senhor da Fertilidade e das Tormentas. Sendo assim, outra capacidade dele está referida ao bem-estar sexual e à fertilidade, e assim ele pode ser chamado para ajudar, em situações em que esses quesitos estejam com problemas.\n\nFinalmente, a capacidade dele de “controlar o clima” pode ser usada para “criar tormentas” e \"calmarias\" na vida das pessoas. Baal é capaz de criar verdadeiro caos na vida de alguém, fazendo com que essa pessoa se sinta dentro de uma tormenta. Ou pode acalmar a realidade de uma pessoa. Isso é um poder e tanto, já que podemos conturbar a vida de alguém, fazendo-o perder o foco, ou podemos criar passividade, fazendo com que a pessoa perca a “garra” competitiva.\n\nBaal trabalha muito bem com outros Senhores Antigos, mas tem um vínculo especial com dois deles, Agares e Vassago, dos quais falaremos a continuação.",
        "planet": "Sol",
        "direction": "Sul",
        "pathworking": "O deserto\nO interior de um templo antigo\nUma fonte de água fresca\nA sensação de Segurança"
    },
    {
        "id": 1,
        "name": "Agares",
        "enn": "Rean ganen ayar da Agares",
        "description": "O Duque Agreas, também conhecido como Agares, é o Segundo Espírito e está subordinado ao poder do Oriente. Quando se manifesta, assume a forma de um homem de meia-idade, atraente, montado em um dragão e segurando um açor em sua mão, apesar do qual, a sua aparência é tranquila.\n\nAgares é descrito como tendo a habilidade de dar um impulso poderoso àqueles que estão estagnados ou parados, concedendo-lhes a energia necessária para que possam avançar em suas metas e objetivos. Sua influência também se estende àqueles que fugiram, permitindo que ele possa ajudar no retorno de indivíduos que, por algum motivo, tenham ido embora.\n\nAlém de sua capacidade de motivar e encorajar, Agares possui outra habilidade surpreendente: ele é capaz de facilitar o aprendizado de qualquer língua ou idioma existente. Isso não está limitado só a parte do aprendizado de idiomas, já que com sua vasta compreensão das linguagens e do mundo, Agares é capaz de conceder aos indivíduos a capacidade de se comunicar e se entender com pessoas de outras culturas e nacionalidades, que poderiam ter sido inacessíveis de outra forma. Essa habilidade é valiosa para aqueles que viajam para o exterior, estudantes de línguas ou profissionais que precisam se comunicar e entender a cultura de pessoas de outras nacionalidades.\n\nAqueles que invocam Agares também podem contar com seu poder para destruir dignidades espirituais e temporais e até mesmo causar destruição (o que no texto é chamado de “terremotos”). No entanto, essa influência pode ser perigosa e deve ser utilizada com cuidado e responsabilidade, pelos possíveis retornos que pode ter.\n\nAnteriormente, fazia parte da Ordem das Virtudes. Agora governa 31 legiões de espíritos, o que o torna um líder poderoso e influente dentro da hierarquia dos senhores antigos, tanto pelo número de subordinados quanto pela sua origem angelical.",
        "planet": "Vênus",
        "direction": "Norte",
        "pathworking": "Um cavalo correndo\nUm raio caindo\nUma caverna com diamantes nas paredes\nA sensação de Segurança"
    },
    {
        "id": 2,
        "name": "Vassago",
        "enn": "Keyan vefa jedan tasa Vassago",
        "description": "O Terceiro Espírito, chamado Vassago, é descrito como uma Princesa poderosa que compartilha da mesma natureza de Agares, ou seja, ela também responde ao Senhor do Oriente. Sua personalidade é gentil e benevolente, e sua habilidade é declarar tanto as coisas passadas quanto as futuras, além de ser capaz de descobrir todas as coisas ocultas ou perdidas. Vassago é mencionada no Livro do Ofício dos Espíritos como Usagoo, aparecendo como um anjo, \"justo e verdadeiro em tudo o que faz\".\n\nVassago é conhecida por sua capacidade de desvendar segredos e mistérios, e muitos invocam sua ajuda para encontrar objetos perdidos, descobrir a verdade por trás de uma situação ou mesmo para prever o futuro. Seus poderes são particularmente úteis para aqueles que desejam explorar a sabedoria antiga ou investigar questões ocultas e esotéricas.\n\nPorém, temos que lembrar que, além de suas habilidades divinatórias e sua forma gentil, Vassago é uma líder forte e governa 26 legiões de espíritos. Aqueles que procuram sua ajuda devem fazê-lo com respeito.\n\nVassago é considerada um espírito extremamente útil para tanto para aqueles que desejam se aprofundar nos mistérios da vida e do universo, como para os que buscam respostas para questões específicas. Seus poderes divinatórios e sua habilidade para descobrir coisas ocultas ou perdidas podem ajudar a esclarecer muitos mistérios e oferecer respostas valiosas para aqueles que a invocam com sinceridade e respeito.",
        "planet": "Júpiter",
        "direction": "Oeste",
        "pathworking": "A beira de um mar calmo, sem ondas\nUm cavalo negro observando\nA noite estrelada\nA sensação de estar sendo avaliado/observado"
    },
    {
        "id": 3,
        "name": "Samigina",
        "enn": "Esta ta et tasa Gamigin",
        "description": "Samigina é o Quarto Espírito, um Grande Marquês. Ele é conhecido por aparecer em duas formas: inicialmente, como um pequeno cavalo ou asno, e, em seguida, transformando-se em uma forma humana, a pedido do invocador. Sua voz é rouca e imponente.\n\nSamigina governa mais de 30 legiões de inferiores, sendo um líder forte e poderoso. Seu poder é especialmente útil para aqueles que desejam explorar as artes liberais e as ciências. Como um espírito experiente e sábio, ele tem a capacidade de ensinar todas as ciências liberais, tornando-se um guia valioso para aqueles que procuram aprender.\n\nAlém disso, Samigina tem a capacidade de lidar com as almas das pessoas que morreram em pecado, uma habilidade única e poderosa que pode trazer alívio para aqueles que sofrem pela perda de um ente querido. Sua capacidade de ajudar as almas a encontrar a paz e a redenção é altamente valorizada entre aqueles que o invocam.\n\nEmbora seja um espírito poderoso, Samigina também é gentil e benevolente, buscando sempre ajudar aqueles que o invocam com sinceridade e respeito. Aqueles que desejam invocar Samigina devem fazê-lo com a mente clara e a intenção pura, para que possam receber suas bênçãos e orientação em seu caminho.\n\nEm resumo, Samigina é capaz de ensinar todas as ciências liberais e lidar com as almas das pessoas que morreram em pecado. Sua presença pode trazer conforto e orientação para aqueles que buscam sua ajuda, tornando-se um valioso guia em suas jornadas.",
        "planet": "Lua",
        "direction": "Oeste",
        "pathworking": "Um lago sob a luz do luar\nUma casa, com as janelas iluminadas por luz amarela\nUma lareira acesa, com duas cadeiras frente a ela\nUma sensação de tranquilidade"
    },
    {
        "id": 4,
        "name": "Marbas",
        "enn": "Renach tasa uberace biasa icar Marbas",
        "description": "Marbas é o quinto Espírito, um Grande Presidente. Quando invocado, ele aparece inicialmente na forma de um grande leão, mas, a pedido do invocador, pode assumir uma forma humana. Sua aparência é majestosa e intimidadora, refletindo seu poder e autoridade.\n\nMarbas é conhecido por sua habilidade em responder a questões sobre coisas ocultas ou secretas, revelando informações que muitas vezes são desconhecidas. Além disso, ele tem a habilidade de causar doenças e, paradoxalmente, também tem a capacidade de curá-las, sendo um espírito ambivalente que pode ser tanto benéfico quanto maléfico.\n\nAlém disso, Marbas é um espírito altamente habilidoso nas artes mecânicas, dando aos seus invocadores um grande conhecimento e sabedoria em tais áreas. Ele pode ensinar técnicas avançadas e habilidades que podem ajudar a aprimorar a engenharia e outras áreas técnicas.\n\nUma habilidade única de Marbas é a capacidade de transformar homens em outras formas, uma capacidade poderosa que pode ser usada para uma variedade de fins. Ele pode conceder a habilidade de se transformar em outras criaturas, ou mesmo em objetos, abrindo uma ampla gama de possibilidades para seus invocadores. Temos que entender aqui que Marbas não vai mudar o corpo físico da pessoa que o invoca, mas a forma como os outros a veem. Ele pode fazer com que uma pessoa tímida projete a energia de um tigre, e assim seja sentida por aqueles que a rodeiam, impondo medo e respeito. De igual forma pode fazer com que uma pessoa perigosa pareça inofensiva e pacífica.\n\nMarbas governa 36 legiões de espíritos, o que o torna um líder poderoso. Ele é altamente respeitado e sua presença pode trazer grande proteção e orientação para aqueles que o invocam.",
        "planet": "Mercúrio",
        "direction": "Leste",
        "pathworking": "As ruínas de uma cidade no deserto\nPalmeiras que se agitam com o vento\nUm obelisco de pedra dourada, numa praça abandonada\nA sensação de estar alerta"
    },
    {
        "id": 5,
        "name": "Valefor",
        "enn": "Keyman vefa tasa Valefor",
        "description": "O sexto Espírito é Valefor, um Duque Grande e Poderoso que aparece como uma mistura de um leão com um burro. Ele é de natureza alegre e bondosa, e tem a habilidade de incitar paixões e desejos, especialmente em relação ao amor e à luxúria. Ele é capaz de fazer com que as pessoas se apaixonem, mesmo que isso pareça impossível, e é especialmente hábil em influenciar aqueles que estão distantes.\n\nValefar é um espírito altamente habilidoso em todas as formas de arte, incluindo música, dança e poesia, e pode ensinar a seus invocadores as técnicas avançadas nessas áreas. Ele também tem a habilidade de criar músicas e poemas em tempo real, trazendo à vida performances únicas e impressionantes.\n\nAlém disso, Valefar é um espírito muito versátil, capaz de ajudar em muitas tarefas diferentes. Ele é um mestre em lidar com o comércio, e pode ajudar em assuntos relacionados a finanças e negócios. Ele também tem conhecimento em artes mágicas, como a invocação de espíritos e a criação de amuletos e talismãs.\n\nValefar governa 10 legiões de espíritos, o que o torna um líder influente na hierarquia demoníaca. Sua personalidade alegre e habilidades versáteis fazem dele um espírito altamente valorizado por aqueles que o invocam.",
        "planet": "Vênus",
        "direction": "Norte",
        "pathworking": "Uma praia no entardecer\nUma bela mulher passa caminhando e se perde na distância\nAs ondas rompem suavemente na areia dourada\nUma sensação de alegria"
    },
    {
        "id": 6,
        "name": "Amon",
        "enn": "Avage Secore Amon ninan",
        "description": "O Sétimo Espírito é conhecido como Amon, um Marquês poderoso e extremamente severo. Sua aparição é aterrorizante, na forma de um lobo com cauda de serpente, cuja boca é capaz de exalar chamas ardentes. No entanto, sob o comando do Mago, ele pode assumir outras formas, como a de um Homem com grandes e afiados dentes de cão, ou simplesmente um homem com cabeça de corvo.\n\nAmon é capaz de revelar todas as coisas passadas e futuras, fornecendo informações precisas e detalhadas sobre qualquer questão. Ele é especialista em solucionar desentendimentos e reconciliar amizades rompidas.\n\nAmon governa sobre 40 legiões de espíritos, demonstrando sua liderança forte e habilidades para organizar e comandar outras entidades espirituais.\n\nAmon pode ser um aliado extremamente poderoso, tanto pelo seu conhecimento profundo sobre o passado, presente e futuro, assim como pela sua capacidade de resolver conflitos interpessoais.",
        "planet": "Lua",
        "direction": "Oeste",
        "pathworking": "Uma espada com empunhadura brilhante\nUm castelo antigo, de pedra cinza\nUm salão com armaduras nas paredes e uma mesa no centro\nUma sensação de calma"
    },
    {
        "id": 7,
        "name": "Barbatos",
        "enn": "Eveta fubin Barbatos",
        "description": "O Oitavo Espírito é Barbatos, um Grande Duque poderoso e sábio. Ele chega acompanhado por quatro Reis, que realçam seu poder.\n\nEle conhece todos os segredos da natureza e é capaz de conceder poder sobre os animais, fazendo com que eles obedeçam ao comando do invocador. Ele pode ensinar a arte da caça e revelar tesouros escondidos.\n\nBarbatos é também capaz de prever o futuro e revelar as coisas ocultas e secretas. Ele é capaz de reconciliar amigos e inimigos e pode proteger aqueles que o invocam de seus inimigos.\n\nEle é da ordem das Virtudes, e ainda mantém poder sobre uma parte dela. Governa 30 legiões de espíritos. Com sua grande sabedoria e poder, Barbatos é um espírito altamente respeitado e pode ser um aliado muito útil.",
        "planet": "Vênus",
        "direction": "Sul",
        "pathworking": "Uma mesa coberta de planos antigos e uma grande bússola\nPelas janelas abertas entra a luz do sol e dá para ver os telhados\nUma jarra de água fresca com dois copos de vidro\nUma sensação de calma"
    },
    {
        "id": 8,
        "name": "Paimon",
        "enn": "Linan tasa jedan Paimon",
        "description": "O Nono Espírito na hierarquia é Paimon, um Grande Rei. Quando invocado, ele aparece sentado em um dromedário com uma coroa gloriosa em sua cabeça. Acompanhando-o, há uma multidão de espíritos. No primeiro encontro Paimon pode ter uma voz poderosa e ressonante, e a comunicação pode ser difícil. O mago deve então pedir para ele se expressar de forma clara. Ele é realmente um anjo e, antes da queda, seu nome era Umbriel.\n\nPaimon é capaz de ensinar todas as Artes e Ciências, bem como outras coisas secretas e misteriosas. Ele tem o poder de revelar a verdade sobre o mundo material (a Terra), sobre o mundo de emoções que a sustenta e define o mundo anterior (as Águas), bem como muitas coisas sobre o mundo mental (os Ventos). Ele pode também responder qualquer outra coisa que você deseje saber.\n\nPaimon também tem a habilidade de conceder Dignidade e confirmá-la. Ele pode amarrar ou tornar qualquer homem sujeito ao mago, se este assim o desejar.\n\nEle pode dar bons familiares que possuem o conhecimento de todas as artes.\n\nPaimon é da Ordem das Potências e governa sobre 200 legiões de espíritos, sendo alguns deles da Ordem dos Anjos e a outra parte das Potências. No entanto, segundo o Ars Goetia, os espíritos subordinados nem sempre estão presentes, a menos que o mago os chame.",
        "planet": "Sol/Saturno",
        "direction": "Leste",
        "pathworking": "Uma caverna iluminada com tochas\nUm tesouro cheio de ouro e pedras preciosas\nUm lago coberto por uma cúpula com diamantes\nUma sensação de força"
    },
    {
        "id": 9,
        "name": "Buer",
        "enn": "Erato on ca Buer anon",
        "description": "O Nono Espírito na hierarquia é Paimon, um Grande Rei. Quando invocado, ele aparece sentado em um dromedário com uma coroa gloriosa em sua cabeça. Acompanhando-o, há uma multidão de espíritos. No primeiro encontro Paimon pode ter uma voz poderosa e ressonante, e a comunicação pode ser difícil. O mago deve então pedir para ele se expressar de forma clara. Ele é realmente um anjo e, antes da queda, seu nome era Umbriel.\n\nPaimon é capaz de ensinar todas as Artes e Ciências, bem como outras coisas secretas e misteriosas. Ele tem o poder de revelar a verdade sobre o mundo material (a Terra), sobre o mundo de emoções que a sustenta e define o mundo anterior (as Águas), bem como muitas coisas sobre o mundo mental (os Ventos). Ele pode também responder qualquer outra coisa que você deseje saber.\n\nPaimon também tem a habilidade de conceder Dignidade e confirmá-la. Ele pode amarrar ou tornar qualquer homem sujeito ao mago, se este assim o desejar.\n\nEle pode dar bons familiares que possuem o conhecimento de todas as artes.\n\nPaimon é da Ordem das Potências e governa sobre 200 legiões de espíritos, sendo alguns deles da Ordem dos Anjos e a outra parte das Potências. No entanto, segundo o Ars Goetia, os espíritos subordinados nem sempre estão presentes, a menos que o mago os chame.",
        "planet": "Mercúrio",
        "direction": "Sul",
        "pathworking": "Um jardim cheio de plantas e flores\nUma fonte de água cristalina\nUm gazebo de madeira, com trepadeiras, no centro do jardim\nUma sensação de expectativa"
    },
    {
        "id": 10,
        "name": "Gusion",
        "enn": "Secore vesa anet Gusion",
        "description": "O Décimo Primeiro Espírito em ordem é Gusion, um Duque poderoso e forte. Quando se manifesta, assume a forma de um Xenopilus, uma criatura estranha e mística, parte homem, parte lobo.\n\nEste espírito é conhecido por sua habilidade em contar todas as coisas, sejam elas passadas, presentes ou futuras.\n\nAlém disso, ele é capaz de fornecer o significado e a resolução para todas as perguntas que o mago possa ter.\n\nGusion tem uma habilidade única de conciliar e reconciliar amizades que foram abaladas. Ele é muito respeitado por sua capacidade de trazer paz e harmonia onde antes havia conflito. Além disso, ele é capaz de conceder honra e dignidade àqueles que merecem.\n\nEste poderoso Duque governa sobre mais de 40 legiões de espíritos, o que o torna muito influente no mundo espiritual. Aqueles que desejam convocá-lo devem estar preparados para enfrentar sua imponente presença, ao mesmo tempo majestosa e intimidadora.",
        "planet": "Mercúrio",
        "direction": "Sul",
        "pathworking": "Um cetro de ouro\nUm chicote de couro preto\nUma balança sobre uma mesa\nUma sensação de força"
    },
    {
        "id": 11,
        "name": "Sitri",
        "enn": "Lirach Alora vefa Sitri",
        "description": "O Décimo Segundo Espírito na ordem é Sitri, um Grande Príncipe com habilidades intrigantes. Ele aparece inicialmente com uma cabeça de Leopardo e asas de um Grifo, mas após receber o comando do Mago, assume a forma humana, sendo muito bonito.\n\nEste Espírito tem o poder de inflamar o amor nos homens e mulheres, despertando paixões intensas e desejo sexual. Se o Mago assim o desejar, Sitri pode fazer com que homens e mulheres se mostrem nus, sendo capaz de influenciar tanto a mente quanto o corpo.\n\nSua capacidade de inspirar a luxúria tem sido frequentemente mencionada, e ele é considerado um especialista em assuntos relacionados ao amor. Ele pode fazer as pessoas sentirem-se atraídas uma pela outra, aumentar a sensualidade e desencadear desejos sexuais.\n\nSitri exerce seu comando sobre 60 legiões de espíritos, sendo um aliado valioso para aqueles que desejam alcançar o sucesso em assuntos amorosos e sensuais. Com a ajuda deste Príncipe, o Mago pode encontrar novos amores ou reacender a chama do relacionamento atual.",
        "planet": "Júpiter",
        "direction": "Norte",
        "pathworking": "Uma espada com cabo de ouro e rubis\nUma cama coberta com uma colcha vermelha e dourada\nUm jardim cheio de flores exuberantes\nUma sensação de alegria"
    },
    {
        "id": 12,
        "name": "Beleth",
        "enn": "Lirach tasa vefa wehl Beleth",
        "description": "O Décimo Terceiro Espírito, conhecido como Beleth (também referido como Bileth ou Bilet), é um rei poderoso e temido na hierarquia dos espíritos. Segundo o Ars Goetia, ele é frequentemente descrito como cavalgando em um cavalo de cor clara, acompanhado por trombetas e outros instrumentos musicais, que ecoam em sua presença.\n\nA primeira aparição de Beleth pode ser intimidante e desconcertante, pois sua fúria é perceptível. O Mago, porém, deve permanecer firme na sua intenção, até ele ficar calmo. No entanto, mesmo mostrando seu poder pessoal, o Mago não pode nunca esquecer que Beleth é um Grande Rei e deve ser tratado com cortesia e respeito, como qualquer outro rei ou príncipe que merece homenagens.\n\nA importância deste Senhor Antigo fica clara quando consideramos que, segundo o Pseudomonarchia Daemonum, já citado antes, o filho de Noé, Ham, foi o primeiro a invocá-lo após o dilúvio e, com a ajuda dele, escreveu um livro sobre matemática. Isto já nos indica que ele pode nos ajudar tanto no estudo de ciências exatas quanto no pensamento lógico.\n\nMas o poder principal de Beleth é o de influenciar e manipular o amor entre homens e mulheres, podendo fazer com que eles se apaixonem profundamente. Ele pode conceder os desejos dos magos e magas que o invocam, trazendo assim, felicidade e satisfação aos seus corações.\n\nDe acordo com a tradição, Beleth pertence à Ordem das Potências e tem o controle de 85 legiões de espíritos, o que indica seu status e grandeza na hierarquia espiritual.",
        "planet": "Sol",
        "direction": "Norte",
        "pathworking": "Um cavalo branco\nUm campo verde, com flores vermelhas\nUm círculo de pedras\nUma sensação de firmeza"
    },
        {
        "id": 13,
        "name": "Beleth",
        "enn": "Caymen vefa Leraje",
        "description": "Leraje, também conhecido como Leraie, é o décimo quarto Espírito da Goétia. Leraje é um Marquês Grande em Poder, que se apresenta como um Arqueiro vestido de verde, carregando um arco e uma aljava. A imagem do arqueiro simboliza sua habilidade em atingir seus objetivos, assim como sua natureza competitiva e guerreira.\n\nLeraje é conhecido por sua capacidade de causar grandes batalhas e competições, sendo um espírito que pode ser invocado para ajudar em disputas e conflitos. Além disso, ele também é capaz de causar feridas profundas que podem se tornar infectadas, uma habilidade que é considerada perigosa e pode ser usada como arma em uma batalha.\n\nAssociado ao signo de Sagitário, Leraje é considerado um espírito de fogo, o que significa que ele é impetuoso, apaixonado e enérgico. Sua energia é considerada dinâmica e transformadora, e pode ser invocada para trazer mudanças rápidas e intensas.\n\nLeraje governa trinta legiões de espíritos, o que significa que ele tem um grande poder e influência sobre outros espíritos e demônios. Seu domínio sobre essas legiões o torna um espírito poderoso e temido, mas também pode ser invocado para ajudar em questões relacionadas à liderança e organização.\n\nGuerreiro, competitivo e impetuoso, Leraje é capaz de causar conflitos e feridas profundas nos alvos determinados pelo mago. Seu domínio sobre trinta legiões de espíritos o torna uma figura poderosa e influente no mundo espiritual, e pode ser invocado para ajudar em disputas, batalhas e questões relacionadas à liderança.",
        "planet": "Lua",
        "direction": "Sul",
        "pathworking": "Uma mão empunhando uma faca\nUma mesa com pão e vinho\nUm cômodo fresco, num dia de sol insuportável\nUma sensação de descanso"
    },
    {
        "id": 14,
        "name": "Eligos",
        "enn": "Jedan on ca Eligos inan",
        "description": "Eligos é o décimo quinto Espírito da Goétia. Ele é um Grande Duque que aparece na forma de um belo cavaleiro, carregando uma lança, uma insígnia e uma serpente. Sua imagem simboliza sua habilidade em desvendar coisas ocultas e conhecer eventos futuros, assim como sua natureza guerreira e protetora.\n\nEligos é conhecido por sua habilidade em descobrir segredos ocultos e prever eventos futuros, especialmente relacionados a guerras e conflitos. Ele é capaz de fornecer informações sobre como as batalhas serão travadas, o que as pessoas podem esperar encontrar e como elas podem se preparar para a vitória. Seu conhecimento das artes da guerra o torna um espírito valioso para aqueles que buscam a vitória em disputas militares.\n\nAlém disso, Eligos é capaz de inspirar o amor e o aprecio dos senhores e das grandes personalidades, uma habilidade que pode ser usada para conquistar a simpatia e a benevolência dos poderosos. Seu domínio sobre o amor o torna um espírito capaz de trazer harmonia e equilíbrio às relações pessoais e interpessoais.\n\nEligos governa sessenta legiões de espíritos, o que significa que ele tem um grande poder e influência sobre outros espíritos e demônios. Seu domínio sobre essas legiões o torna uma figura poderosa e temida no mundo espiritual, mas também pode ser invocado para ajudar em questões relacionadas à liderança e organização.\n\nGuerreiro e protetor, Eligos é capaz de fornecer informações precisas sobre eventos futuros e ajudar na preparação para a vitória em batalhas. Sua habilidade em inspirar o amor dos poderosos o torna um espírito valioso em questões políticas e pessoais. Seu domínio sobre sessenta legiões de espíritos o torna uma figura poderosa e influente no mundo espiritual, capaz de ajudar em questões de liderança e organização.",
        "planet": "Vênus",
        "direction": "Oeste",
        "pathworking": "Uma serpente se arrasta pelo chão\nUm guerreiro observa com atenção\nUma mesa com duas jarras de cerveja\nUma sensação de força"
    },
    {
        "id": 15,
        "name": "Zepar",
        "enn": "Lyan Ramec catya Zep",
        "description": "Zepar é o décimo sexto espírito da Goetia, listado como um Grande Duque. Ele é descrito como um soldado com roupas e armaduras vermelhas. O seu ofício é fazer com que as mulheres se apaixonem pelos homens e, assim, uni-los no amor. Além disso, ele é conhecido por torná-las estéreis.\n\nSegundo a tradição ocultista, Zepar é invocado pelos magos para ajudá-los a conquistar o amor de uma mulher desejada. Ele pode ser solicitado para ajudar a fortalecer um relacionamento amoroso existente ou para atrair um novo amor.\n\nAlém disso, é importante destacar que Zepar governa 26 legiões de espíritos inferiores. Esses espíritos podem ser convocados pelos magos para ajudá-los em diferentes tarefas, desde a proteção pessoal até a obtenção de riqueza.",
        "planet": "Vênus",
        "direction": "Norte",
        "pathworking": "Um cavalo negro esperando o cavaleiro\nUm caminho beirado por árvores\nUma mesa com cadeiras, pão e vinho, sob uma grande árvore\nA sensação de ser sedutor"
    },
    {
        "id": 16,
        "name": "Botis",
        "enn": "Jedan hoesta noc ra Botis",
        "description": "O décimo sétimo espírito da Goetia é Botis, um grande presidente e conde que tem uma aparência um tanto quanto assustadora. Quando se manifesta pela primeira vez, ele assume a forma de uma víbora. No entanto, sob o comando do mago que o invocou, ele pode assumir uma forma humana, com grandes dentes e dois chifres. Em suas mãos, ele carrega uma espada brilhante e afiada, pronta para usar em defesa de seu invocador.\n\nBotis é um espírito muito poderoso e é conhecido por ter o dom de contar todas as coisas passadas e futuras. Ele é um grande aliado para aqueles que buscam orientação sobre o que está por vir, e também para aqueles que desejam entender melhor seu passado.\n\nAlém desse poder, Botis tem uma habilidade única para reconciliar amigos e inimigos, tornando-o um aliado valioso para aqueles que desejam resolver conflitos e curar relacionamentos quebrados.\n\nÉ interessante notar que Botis governa mais de 60 legiões de espíritos, o que indica que ele é um espírito muito respeitado e temido entre seus pares. As habilidades e o poder de proteção de Botis são muito valorizados e sua influência é considerada extremamente poderosa.",
        "planet": "Mercúrio/Marte",
        "direction": "Oeste",
        "pathworking": "Um guerreiro, com armadura, portando uma espada na mão\nUma cidade antiga, com casas brancas\nUm lugar com sombra, sob as palmeiras\nUma sensação de alegria"
    },
    {
        "id": 17,
        "name": "Bathin",
        "enn": "Dyen Pretore on ca Bathin",
        "description": "Bathin é o décimo oitavo espírito da hierarquia do Ars Goetia e é conhecido como um duque poderoso e forte. Sua aparência é descrita como a de um homem forte, com uma cauda de serpente e montado em um cavalo pálido. Essa imagem é impressionante e muitas vezes evoca medo e respeito em quem o invoca.\n\nEntre suas habilidades e poderes, Bathin é reconhecido por sua extensa compreensão das virtudes das ervas e das pedras preciosas.\n\nSegundo o Ars Goetia, ele tem o poder de transportar repentinamente homens de um país para outro. Mesmo que isso não aconteça fisicamente, essa habilidade o torna um espírito extremamente útil para aqueles que precisam viajar longas distâncias, com rapidez. Ele pode fazer com que a viagem aconteça de forma suave e rápida. Também é muito útil para quem quer refinar a arte da viagem astral.\n\nBathin é também um governante, com o controle de mais de 30 legiões de espíritos. Seus poderes de comando são considerados altamente eficazes e muitas vezes são temidos por aqueles que o servem. No entanto, para aqueles que o invocam com respeito e devoção, Bathin pode oferecer proteção, sabedoria e orientação em seu caminho espiritual.\n\nEmbora não seja tão conhecido, Bathin é um espírito poderoso e respeitado, com habilidades e poderes que são altamente valorizados pelos que buscam seu auxílio. Seu conhecimento das virtudes das ervas e das pedras preciosas e seu poder de transporte o tornam um espírito muito procurado, enquanto sua posição de governante o torna uma figura de autoridade e comando no mundo dos espíritos.",
        "planet": "Vênus",
        "direction": "Norte",
        "pathworking": "Uma bússola antiga\nA ponte de um barco, com a roda do leme de madeira\nO deck do barco, durante o dia, com o mar agitado\nUma sensação de tensão"
    },
    {
        "id": 18,
        "name": "Sallos",
        "enn": "Serena Alora Sallos Aken",
        "description": "O décimo nono espírito da lista de espíritos descritos no Ars Goetia é conhecido como Sallos (ou Saleos). Descrito como um Grande e Poderoso Duque, Sallos é um ser espiritual que tem o poder de influenciar os desejos amorosos das pessoas. Ele é capaz de conceder o amor das mulheres aos homens e dos homens às mulheres, sendo considerado um especialista em assuntos do coração.\n\nQuando evocado, Sallos se manifesta na forma de um galante soldado montado em um crocodilo, usando uma coroa ducal na cabeça, mas de maneira pacífica. A sua aparência exótica e impressionante, bem como o seu ar imponente, demonstra o seu poder e autoridade como um dos grandes duques do inferno.\n\nDe acordo com os grimórios antigos, Sallos governa trinta legiões de espíritos e é um dos mais importantes comandantes entre os Shedim. A sua influência é capaz de moldar as emoções e os desejos das pessoas, tornando-o uma entidade muito procurada por aqueles que buscam ajuda nos assuntos amorosos.\n\nSallos é um espírito extremamente poderoso e respeitado, conhecido por governar legiões de outros seres espirituais e ter a capacidade de conceder o amor e influenciar os desejos amorosos das pessoas.",
        "planet": "Vênus",
        "direction": "Norte",
        "pathworking": "Uma grande catedral, com bancos de madeira escura\nUm enorme órgão, com tubos de metal brilhante\nUm jardim do lado de fora, com bancos de pedra\nA sensação de justiça"
    },
    {
        "id": 19,
        "name": "Purson",
        "enn": "Ana jecore on ca Purson",
        "description": "O vigésimo espírito da lista de espíritos descritos no 'Ars Goetia' é Purson, um Grande Rei cuja aparência é imponente e majestosa. Ele é descrito como um homem com rosto de leão e carregando uma víbora cruel em sua mão. À medida que ele avança, o som de muitas trombetas pode ser ouvido ao seu redor, anunciando a sua chegada.\n\nPurson é conhecido por possuir grande conhecimento e sabedoria, sendo capaz de descobrir tesouros ocultos e revelar informações sobre o passado, presente e futuro. Ele pode assumir uma forma humana ou etérea e tem a habilidade de responder com veracidade a todas as questões terrenas, secretas e divinas, incluindo aquelas sobre a criação do mundo.\n\nDe acordo com a tradição goética, Purson é capaz de gerar bons espíritos familiares, que são seres espirituais que ajudam os humanos em suas tarefas e objetivos pessoais. Sob seu governo, há vinte e duas legiões de espíritos, que são parte da ordem das Virtudes e parte da ordem dos Tronos.\n\nPurson é um espírito extremamente poderoso e respeitado na tradição ocultista, sendo considerado um dos grandes entre os Shedim. Sua aparência majestosa e sua habilidade de revelar informações ocultas fazem dele uma entidade muito procurada por aqueles que buscam sabedoria e conhecimento em assuntos espirituais e ocultos.",
        "planet": "Sol",
        "direction": "Norte",
        "pathworking": "Um cavaleiro em armadura, sobre um cavalo branco\nUma grande mansão\nUm cômodo com poltronas de madeira frente a uma lareira acesa\nUma sensação de força"
    },
    {
        "id": 20,
        "name": "Marax",
        "enn": "Kaymen Vefa Marax",
        "description": "O vigésimo primeiro espírito da lista de espíritos descritos no 'Ars Goetia' é Marax, um Grande Conde e Presidente. Ele é descrito como um grande touro com rosto humano, e é um Shedim que se especializa em trazer sabedoria aos homens.\n\nMarax pode ajudar aqueles que buscam conhecimento em astronomia e outras ciências liberais. Ele é capaz de compartilhar conhecimentos e segredos ocultos sobre o universo e suas leis. Além disso, ele pode conceder a seus invocadores a habilidade de entender os segredos da natureza, incluindo as virtudes das ervas e pedras preciosas.\n\nSegundo a tradição goética, Marax é capaz de gerar bons familiares, que são seres espirituais que ajudam os humanos em seus esforços e projetos pessoais. Esses familiares podem ajudar seus mestres a se tornarem sábios e conhecedores das artes ocultas, incluindo a magia, a alquimia, a astrologia e outras áreas de estudo espiritual.\n\nSob seu governo, Marax tem 30 legiões de espíritos, que são seres que trabalham sob seu comando para realizar suas tarefas e obedecer às suas ordens. Esses espíritos são habilidosos em ajudar a trazer sabedoria e conhecimento aos humanos, tornando-os mestres em várias ciências e artes.",
        "planet": "Mercúrio/Marte",
        "direction": "Norte",
        "pathworking": "Uma mesa com instrumentos de alquimia\nUma lareira acesa, com um fogo azul\nUm cômodo na penumbra, aconchegante\nUma sensação de curiosidade"
    },
    {
        "id": 21,
        "name": "Ipos",
        "enn": "Desa an Ipos Ayer",
        "description": "O vigésimo segundo espírito é Ipos, uma poderosa Condessa e Princesa. Segundo o Ars Goetia, ela é descrita como um anjo com cabeça de leão, pés de ganso e rabo de lebre, mas Johann Weyer dá uma descrição mais interessante: ele disse que Ipos aparece como um anjo ou como um leão malvado e astuto. Eu diria que uma mistura das duas coisas se aproxima mais à realidade desta Shedim.\n\nEla é conhecida por sua grande sabedoria e conhecimento do passado, presente e futuro. De acordo com a tradição goética, Ipos é um espírito capaz de conceder inteligência e coragem aos homens. Ela é habilidosa em ajudar aqueles que buscam conhecimento, tornando-os mais sábios e astutos em suas decisões. Ela também é capaz de ajudar a desenvolver a coragem necessária para enfrentar os desafios da vida com bravura e determinação.\n\nIpos governa 36 legiões de espíritos, que trabalham sob sua supervisão para realizar suas tarefas e obedecer às suas ordens. Esses espíritos são capazes de auxiliar seus invocadores em uma ampla variedade de tarefas, incluindo a obtenção de conhecimento e sabedoria, a realização de tarefas difíceis e a superação de obstáculos.\n\nAlém disso, Ipos é capaz de ajudar a prever o futuro, permitindo que seus invocadores antecipem os desafios que enfrentarão e se preparem adequadamente para enfrentá-los. Ela é considerada um dos espíritos mais sábios e poderosos do reino espiritual, capaz de conceder habilidades e conhecimentos valiosos para aqueles que o invocam.",
        "planet": "Marte",
        "direction": "Oeste",
        "pathworking": "Uma tormenta no deserto\nUma caverna escura, que protege da tempestade\nUm lago de água fresca dentro da caverna\nUma sensação de poder"
    },
    {
        "id": 22,
        "name": "Aim",
        "enn": "Ayer avage secore Aim",
        "description": "O Vigésimo Terceiro Espírito é Aim (ou Haborym), um Duque poderoso e imponente que se apresenta na forma de um homem belo, mas com três cabeças distintas. A primeira é de uma serpente, a segunda é de um homem com duas estrelas na testa, e a terceira é a de um bezerro. Ele cavalga em uma serpente, enquanto segura um tição em sua mão, que tem o poder de incendiar cidades, castelos e grandes lugares. Já esta característica dele o faz ideal para ajudar quando estamos querendo causar confusão num grupo de pessoas. Pode ser desde gerar mal-estar até fazer com que 'o circo pegue fogo' mesmo.\n\nAim tem a capacidade de tornar uma pessoa espirituosa, inteligente e comunicativa, de todas as formas possíveis. Com a sua ajuda, podemos nos transformar no centro das atenções em qualquer lugar. Além disso, ele tem a capacidade de dar respostas verdadeiras a perguntas específicas. Ele é um ser extremamente inteligente e sabe muito sobre os mistérios do mundo. Sua natureza ardente e poderosa torna-o útil em situações em que força e coragem são necessárias.\n\nEste duque governa 26 legiões de espíritos inferiores que estão à sua disposição para realizar suas tarefas.",
        "planet": "Vênus",
        "direction": "Sul",
        "pathworking": "Uma grande fogueira, com chamas laranjas e amarelas\nUm castelo, iluminado pelas labaredas\nA sala de armas do castelo, com uma lareira onde arde um fogo azul\nUma sensação de agitação"
    },
    {
        "id": 23,
        "name": "Naberius",
        "enn": "Eyan tasa volocur Naberius",
        "description": "O Vigésimo Quarto Espírito é Naberius, um Marquês extremamente valente. Ele costuma se manifestar na forma de uma garça negra, e quando fala, sua voz é rouca. Ele tem um talento especial para tornar os homens astutos em todas as artes e ciências, principalmente na arte da retórica. Isto faz com que a pessoa que o chama termine desenvolvendo astúcia e perspicácia, sabendo como usar o conhecimento ao seu favor, e ganhando a capacidade de persuadir e influenciar aqueles ao seu redor.\n\nAlém disso, Naberius é capaz de restaurar dignidades e honras que foram perdidas, trazendo de volta a reputação e prestígio que uma pessoa possa ter perdido ao longo do tempo. Seu conhecimento é vasto e sua sabedoria é profunda, permitindo que ele forneça informações precisas e úteis sobre diversos assuntos.\n\nNaberius governa 19 legiões de espíritos, cada um sob seu comando. Esses espíritos são poderosos e são capazes de realizar tarefas incríveis, desde a realização de feitiços até a execução de ordens específicas. Eles são leais a Naberius e trabalham incansavelmente para cumprir seus desejos.",
        "planet": "Lua",
        "direction": "Leste",
        "pathworking": "A vista desde o alto de uma montanha\nUm céu azul claro, com uma águia voando\nUm lugar com grama para sentar-se e observar a paisagem\nUma sensação de dignidade"
    },
    {
        "id": 24,
        "name": "Glasya-Labolas",
        "enn": "Elan tepar secore on ca Glasya-Lobolas",
        "description": "O Vigésimo Quinto Espírito é conhecido como Glasya-Labolas, e é considerado um dos mais poderosos Presidentes e Condes dentre todos os espíritos no Ars Goetia. Sua aparência é descrita como sendo a de um cão com asas de grifo, o que lhe confere uma presença intimidadora e imponente.\n\nEste espírito é conhecido por sua habilidade excepcional em facilitar o aprendizado de todas as artes e ciências com grande rapidez, o que o torna um guia valioso para aqueles que buscam conhecimento e sabedoria. Entretanto, é importante destacar que ele também é conhecido por incitar à violência, ao derramamento de sangue e ser o instigador de todos os assassinatos.\n\nAlém disso, Glasya-Labolas é capaz de ensinar coisas passadas, presentes e futuras, o que o torna um aliado poderoso para aqueles que buscam respostas sobre o passado, o presente ou o futuro. Se desejado, ele também pode causar amor entre amigos e inimigos, e conceder invisibilidade (um poder semelhante ao de Baal).\n\nEle exerce o controle sobre 36 legiões de espíritos. É importante ter em conta que Glasya-Labolas é um dos demônios goéticos mais perigosos, e seu poder só deve ser invocado com extrema cautela e respeito. Sua natureza violenta e suas habilidades únicas o tornam um espírito temido, mas também muito respeitado.",
        "planet": "Mercúrio/Marte",
        "direction": "Sul",
        "pathworking": "A noite escura, com estrelas\nUma árvore enorme, com galhos frondosos na altura da cabeça de um homem\nUma lâmpada acesa, iluminando sob a árvore\nUma sensação de agressividade"
    },
    {
        "id": 25,
        "name": "Bune",
        "enn": "Wehl melan avage Bune Tasa",
        "description": "O vigésimo sexto espírito da demonologia é Bune, também conhecido como Bim. Este Duque é considerado forte, grande e poderoso, e sua aparência é descrita, no Ars Goetia, como a de um dragão com três cabeças. Sua voz é alta e graciosa, o que produz respeito e admiração.\n\nMas segundo o ocultista Carroll Runyon, o nome Bune está associado à cidade de Buto, que estava dedicada ao culto da deusa Wadget. Ela costumava ser representada, entre outras formas, por uma cobra com asas, uma bela mulher usando uma toca de serpente com asas, ou uraeus (o que daria a impressão de ser uma serpente com 3 cabeças), ou uma mulher com cabeça de serpente. Pela sua capacidade metamórfica, aqui a representamos como uma princesa com um dragão nas suas costas.\n\nBune tem comando sobre os espíritos dos mortos, fazendo com que esses espíritos se reúnam em seus sepulcros ou se desloquem até o lugar que ela indicar, o que a transforma numa aliada espetacular para magos e magas que trabalhem com necromancia. Além disso, ela tem o poder de conceder riquezas a um homem ou mulher, e de torná-lo sábio e eloquente. Se invocada corretamente, Bune é capaz de fornecer respostas verdadeiras às demandas e perguntas de seus invocadores.\n\nBune governa 30 legiões de espíritos, o que significa que ela tem um grande exército sob seu comando e pode ser uma poderosa aliada para aqueles que buscam sua ajuda. Em resumo, Bune é uma Duquesa muito respeitada, principalmente pelas suas capacidades necromânticas, e é capaz de conceder muitos benefícios para aqueles que buscam sua ajuda. No entanto, é importante lembrar que sua natureza é feroz e seu poder é inigualável, pois tem a força de um dragão.",
        "planet": "Vênus",
        "direction": "Terra",
        "pathworking": "Um cetro de ouro com esmeraldas\nUm chicote de couro\nUm cômodo antigo, com poltronas na beira de uma piscina\nUma sensação de realeza e altivez"
    },
    {
        "id": 26,
        "name": "Ronove",
        "enn": "Wehl melan avage Bune Tasa",
        "description": "Ronove é o vigésimo sétimo espírito do Ars Goetia, e é considerado um Marquês e Grande Conde. Sua aparência é descrita como a de um monstro, mas não se deixe enganar pela sua aparência aterrorizante, Ronove é um espírito que pode ser extremamente útil para aqueles que o invocam.\n\nUma das habilidades de Ronove é o seu conhecimento da Arte da Retórica, que ele ensina de forma excepcional. Ou seja, pode fazer com que quem o invoca termine tendo uma habilidade muito grande de convencer outras pessoas. Além disso, ele tem o poder de conceder bons servidores aos seus invocadores, o que pode ser muito útil para aqueles que precisam de assistência em suas tarefas diárias.\n\nRonove também é capaz de facilitar o aprendizado de línguas, tornando-o uma escolha popular entre aqueles que procuram se comunicar melhor com pessoas de outras culturas. Além disso, ele tem a habilidade de conseguir favores com amigos ou inimigos, o que pode ser extremamente útil em situações políticas ou comerciais.\n\nEste Marquês tem sob seu comando 19 legiões de espíritos, o que significa que ele tem uma grande quantidade de poder sob seu controle. Ronove é um espírito com muitas habilidades e pode ser útil em uma variedade de situações. Sua capacidade de ensinar a Arte da retórica, conceder bons servidores e facilitar o aprendizado de línguas, bem como conseguir favores com amigos ou inimigos, faz dele uma escolha popular entre aqueles que buscam seus poderes.",
        "planet": "Vênus",
        "direction": "Terra",
        "pathworking": "Uma grande biblioteca, com prateleiras de madeira escura\nUma mesa com uma bússola\nVárias cadeiras de madeira com assento de veludo vermelho\nUma sensação de sabedoria"
    },
    {
        "id": 27,
        "name": "Berith",
        "enn": "Hoath redar ganabal Berith",
        "description": "O Vigésimo Oitavo Espírito em Ordem é Berith, um Duque poderoso, grande e terrível. Berith, ou Baal Berith, o 'Senhor da Aliança' como era conhecido antigamente, foi o Elohim de Sechem, no reino de Canaã. Quando aparece, ele assume a forma de um soldado vestindo roupas vermelhas, montado em um cavalo vermelho e usando uma coroa de ouro em sua cabeça.\n\nSua voz é clara e sutil, e ele é capaz de dar respostas verdadeiras sobre o Passado, Presente e Futuro. Ou seja, ele pode nos dar informação sobre o que aconteceu, para entender por que estamos na situação atual, pode analisar essa situação atual e pode nos indicar os possíveis futuros a partir do presente.\n\nBerith é um especialista em finanças e é capaz de ensinar como ter sucesso em qualquer empreendimento financeiro. Ele é conhecido por ter o 'toque de Midas', o que significa que ele pode transformar tudo em ouro. Se alguém estiver procurando por sucesso financeiro, Berith é o espírito a invocar.\n\nAlém disso, Berith é capaz de dar dignidades e confirmá-las. Isso é especialmente útil para aqueles que procuram uma promoção ou algum tipo de reconhecimento, tanto público como privado.\n\nBerith é capaz de comandar 26 legiões de espíritos e é conhecido por ser um Duque Poderoso, Grande e Terrível. Se você precisar de ajuda financeira ou busca por reconhecimento, Berith é um espírito poderoso e capaz de ajudar.",
        "planet": "Vênus",
        "direction": "Sul",
        "pathworking": "Uma caverna cheia de objetos de ouro\nUma mesa com uma jarra com água e um copo\nUma fala com cabo dourado\nA sensação de ser esperto"
    },
    {
        "id": 29,
        "name": "Forneus",
        "enn": "Senan okat ena Forneus ayer",
        "description": "Forneus é um dos poderosos espíritos que compõem a hierarquia da Goetia, ocupando a posição de trigésimo espírito. Ele é descrito como um grande Marquês, que aparece na forma de um monstro marinho, capaz de infundir temor em qualquer um que o veja. Uma das habilidades mais notáveis de Forneus é seu poder de ensinar e tornar os homens incrivelmente sábios na arte da retórica. Ele é capaz de conceder aos seus invocadores a habilidade de falar com confiança e persuasão, tornando-os capazes de convencer outras pessoas e fazer valer seus pontos de vista. Isso os torna eficazes em debates e discursos, podendo levá-los a uma posição de destaque em qualquer ambiente social ou profissional.\n\nAlém disso, Forneus também é conhecido por facilitar o aprendizado e a compreensão de línguas e culturas estrangeiras. Ele pode ajudar seus invocadores a dominar idiomas e conhecer melhor outras culturas, o que pode ser útil em negócios internacionais e viagens para o exterior. Outra habilidade impressionante de Forneus é a de fazer com que alguém seja amado por seus inimigos, bem como por seus amigos. Isso pode ser muito útil em situações de conflito, ajudando a evitar brigas desnecessárias e alcançar acordos pacíficos.\n\nPor fim, Forneus governa sobre 29 legiões de espíritos, sendo parte da Ordem dos Tronos e parte da Ordem dos Anjos. Isso significa que ele é capaz de convocar uma grande quantidade de entidades espirituais para ajudar em suas tarefas e conceder seus poderes e habilidades aos seus invocadores. Em resumo, Forneus é um espírito poderoso e sábio que pode conceder aos seus invocadores habilidades valiosas na arte da retórica, línguas e cultura estrangeira, além de ser capaz de gerar empatia e amor entre amigos e inimigos. Se você está procurando aprimorar suas habilidades de comunicação ou buscando harmonia em relacionamentos pessoais ou profissionais, Forneus pode ser o espírito certo para invocar.",
        "planet": "Lua",
        "direction": "Oeste",
        "pathworking": "Uma biblioteca antiga\nDuas xícaras com chá quente sobre uma mesa\nUm vaso de flores com uma rosa preta\nUma sensação de calma"
    },
    {
        "id": 30,
        "name": "Foras",
        "enn": "Kaymen vefa Foras",
        "description": "O Trigésimo Primeiro Espírito é Foras, um Presidente poderoso e impressionante que aparece na forma de um homem forte e imponente. Seus poderes são vastos e variados, incluindo a capacidade de ensinar aos homens como conhecer as virtudes de todas as ervas e pedras preciosas. Além disso, Foras é um mestre das artes da lógica e da ética, oferecendo ensinamentos valiosos sobre esses temas em todas as suas partes.\n\nMas as habilidades de Foras não param por aí. Se desejado, ele pode tornar uma pessoa 'invisível' (ou seja, que outras pessoas não reparem na presença dela), permitindo que vivam por muito tempo e sejam eloquentes. Essa habilidade é extremamente útil em situações de conflito, pois permite à pessoa evitar seus inimigos e passar despercebida. Além disso, a 'invisibilidade' pode ser usada para obter informações valiosas e circular entre outras pessoas sem ser notado.\n\nForas também é capaz de descobrir tesouros e recuperar coisas perdidas. Se você perdeu algo valioso ou deseja encontrar algo que está escondido, invocar Foras pode ser a solução. Ele governa sobre 29 legiões de espíritos, tornando-se um líder poderoso e capaz de realizar feitos incríveis.\n\nSe você deseja aprender as artes da lógica e da ética, obter conhecimento sobre ervas e pedras preciosas, recuperar tesouros perdidos ou simplesmente se tornar invisível e obter vantagens táticas, Foras é o espírito que deve invocar.",
        "planet": "Mercúrio",
        "direction": "Norte",
        "pathworking": "Uma espada de ferro\nUm barco antigo navegando entre as ondas\nO camarote do capitão, com duas xícaras de café numa mesa\nUma sensação de força"
    },
    {
        "id": 31,
        "name": "Asmoday",
        "enn": "Ayer avage Aloren Asmoday aken",
        "description": "O Trigésimo Segundo Espírito é conhecido como Asmoday ou Asmodai, e é um poderoso e grande Rei Goético. Sua aparência é impressionante, com três cabeças - uma de touro, uma de homem e outra de carneiro. Além disso, ele tem a cauda de uma serpente e seus pés são como os de um réptil. Asmoday aparece montado em um dragão infernal e empunha uma lança com um estandarte.\n\nAsmoday é a versão moderna do Shedim Asmodeus, que faz várias aparições nos textos bíblicos. Segundo textos cabalísticos antigos, ele é filho do Rei Davi com a Shedim Agrat. Entre as mais conhecidas está a sua atuação como adversário no Livro de Tobias e sua aparição no Talmud, quando substitui Salomão durante um tempo, sem que ninguém perceba. Algumas fontes ligam Asmoday a Aeshma, o antigo Senhor da Ira do panteão persa.\n\nAsmoday é um espírito muito sábio e conhecedor, capaz de ensinar diversas áreas de conhecimento humano. Ele é especialmente habilidoso na Aritmética, Astronomia, Geometria e outros trabalhos manuais. Além disso, ele é capaz de responder com veracidade e precisão a qualquer demanda.\n\nOutro grande poder de Asmoday é sua capacidade de conceder invencibilidade. Isso é especialmente útil para aqueles que enfrentam situações difíceis ou perigosas, pois ele pode oferecer proteção e segurança. Asmoday é também um guardião de tesouros, e é capaz de mostrar onde esses tesouros estão escondidos. Isso é especialmente útil quando se depara com algo que se considera valioso, mas que não se pode tomar posse imediatamente. Com a ajuda de Asmoday, é possível manter esses tesouros seguros e protegidos.\n\nPor fim, Asmoday governa 72 legiões de espíritos inferiores. Sua grande sabedoria e poder são muito respeitados pelos espíritos que ele comanda, e aqueles que invocam seu nome podem esperar obter sua ajuda e orientação em muitas áreas da vida.",
        "planet": "Sol",
        "direction": "Leste",
        "pathworking": "Um escudo e uma lança\nUma mesa e dois bancos\nUm deserto de areias douradas, com grandes palmeiras\nUma sensação de alegria"
    },
    {
        "id": 32,
        "name": "Gaap",
        "enn": "Deyan Anay Tasa Gaap",
        "description": "O trigésimo terceiro espírito é conhecido como Gaap, um grande presidente e um príncipe poderoso entre os espíritos. Este ser místico tem a capacidade de se manifestar quando o sol está em algum dos signos do sul, assumindo uma forma humana. Em suas aparições, ele precede quatro grandes e poderosos reis, como um guia para conduzi-los em seus caminhos.\n\nO ofício de Gaap é tornar as pessoas insensíveis ou ignorantes, mas ele também pode ensinar filosofia para torná-las conhecedoras de diferentes temas. Essa habilidade se aplica a todas as ciências, o que faz dele um espírito de grande sabedoria e conhecimento.\n\nGaap tem o poder de causar amor ou ódio, mas esses sentimentos não são estáveis, já que ele é um Shedim (demônio antigo) de extremos opostos. Uma forma de aplicar esse poder seria fazer com que uma pessoa se apaixonasse loucamente por alguém que não a corresponderá ou que odeie alguém sem motivo aparente.\n\nAlém disso, Gaap tem a capacidade de libertar familiares da custódia de outros magos. Este é um poder muito forte, já que estaríamos retirando servidores do controle de outro mago, o que pode ser perigoso, por vários motivos.\n\nGaap pode também responder com veracidade e precisão sobre as coisas passadas, presentes e futuras. Isso faz dele um espírito de grande utilidade para aqueles que buscam conhecimento e orientação.\n\nEm sua hierarquia, Gaap governa 66 legiões de espíritos e era da Ordem das Potências.",
        "planet": "Mercúrio/Júpiter",
        "direction": "Leste",
        "pathworking": "Um tornado avança pelo deserto\nUma caverna, fresca e segura\nUm lago, iluminado só pela luz de duas tochas\nA sensação de ser observado"
    },
    {
        "id": 33,
        "name": "Furfur",
        "enn": "Ganen menach tasa Furfur",
        "description": "O trigésimo quarto espírito do Ars Goetia é Furfur, uma grande e poderosa condessa que se manifesta na forma de um cervo com uma cauda de fogo. No entanto, se o mago pedir, ela assume a forma de um belo anjo escuro, e fala com uma voz rouca.\n\nEsta Shedim tem o poder de incitar, de forma prazerosa, o amor entre duas pessoas. Além disso, de Furfur se diz que ela é capaz de criar relâmpagos, trovões, explosões e grandes tempestades. Isso, na época atual, pode ser entendido como a habilidade de criar caos nos sentimentos das pessoas, provocando conflitos entre elas. Também pode se referir à habilidade de atacar os dispositivos elétricos ou eletrônicos de alguém. Numa época em que todos usamos tecnologia, atacar essa base é um poder e tanto.\n\nNo entanto, se você busca seu auxílio, ela pode dar respostas verdadeiras tanto para as coisas secretas quanto para as divinas, mas só se isso for solicitado. Em sua hierarquia, Furfur governa 26 legiões de espíritos, o que a torna uma líder forte e respeitada entre seus pares.",
        "planet": "Marte",
        "direction": "Sul",
        "pathworking": "Um fogo que devora bosques\nUm rio desbordado, alagando tudo à medida que avança\nUma pedra alta, onde observamos tudo, seguros\nUma sensação de poder"
    },
    {
        "id": 34,
        "name": "Marchosias",
        "enn": "Es na ayer Marchosias Secore",
        "description": "O trigésimo quinto espírito é Marchosias, um grande e poderoso marquês que se manifesta na forma de um lobo com asas de grifo e uma cauda de serpente, vomitando fogo pela sua boca. No entanto, por ordem do mago, ele pode assumir a forma de um homem.\nMarchosias é um grande lutador, muito forte, e pode ser chamado em situações tensas, como por exemplo numa negociação que precise de muita força, ou para amedrontar inimigos, de forma que desistam da ideia de atacar.\nSe você precisar de proteção, Marchosias pode ser invocado para defendê-lo ou para atacar um determinado alvo. Seu poder é imenso, e ele é um espírito muito respeitado. Marchosias pertence à ordem dos Domínios, o que o torna um ser ainda mais poderoso e influente.\nAo trabalhar com Marchosias, é importante ter em mente que ele é um espírito muito poderoso e agressivo, e deve ser tratado com respeito e reverência. Ele governa 30 legiões de espíritos, o que significa que ele é um líder forte e respeitado entre seus pares.",
        "planet": "Lua",
        "direction": "Sul",
        "pathworking": "Um escudo e uma espada, sujos de sangue\nUm guerreiro com armadura completa e uma lança\nO arsenal de um castelo, cheia de instrumentos de guerra\nUma sensação de agressividade"
    },
    {
        "id": 35,
        "name": "Stolas",
        "enn": "Stolos Ramec viasa on ca",
        "description": "Stolas, também conhecido como Stolos, é o trigésimo sexto Espírito da hierarquia demoníaca. Ele é um príncipe poderoso, dotado de grande sabedoria e capacidade de transformação. Inicialmente, ele se apresenta como um corvo imponente, mas logo assume a forma humana.\nEntre seus dons, Stolas é um mestre na arte da astronomia, capaz de desvendar os segredos dos astros e das constelações. Além disso, ele detém um vasto conhecimento sobre as virtudes ocultas das plantas e das pedras preciosas, podendo ensinar a magia da cura e a utilização desses elementos em rituais de proteção.\nStolas governa 26 legiões de espíritos, exercendo uma influência significativa sobre o mundo espiritual. Sua presença é reverenciada por aqueles que buscam aprofundar seu conhecimento nas artes ocultas e desvendar os mistérios do cosmos.",
        "planet": "Júpiter",
        "direction": "Leste",
        "pathworking": "Um papiro antigo, sobre uma mesa de mármore\nUma enorme bússola de bronze\nUm jardim à noite, iluminado por tochas, sob um céu estrelado\nUma sensação de diversão ou de alegria"
    },
    {
        "id": 36,
        "name": "Phenex",
        "enn": "Ef enay Phenex ayer",
        "description": "O trigésimo sétimo espírito do Ars Goetia é conhecido como Phenex, também chamado de Pheynix. Este grandioso marquês se apresenta em forma de fênix, com a voz suave de uma criança. Contudo, é necessário que o mago lhe ordene que assuma uma forma humana antes de começar o diálogo. Quando ele assim o faz, revela-se um magnífico conhecedor de todas as ciências maravilhosas, capaz de falar com habilidade e destreza.\nPhenex é um poeta notável e admirável, sempre disposto a atender aos pedidos de seus invocadores. Basicamente, os poderes de Phenex estão na área da persuasão, seja através da palavra, da escrita, da música ou de qualquer tipo de arte. Se pedimos a ajuda deste grande marquês, nossa capacidade de influir sobre as pessoas através da nossa arte (seja ela qual for) aumentará notavelmente.\nEle governa 20 legiões de espíritos e pode ser uma grande ajuda para quem o convoca.",
        "planet": "Lua",
        "direction": "Leste",
        "pathworking": "Um grande cristal arredondado\nUm barco navegando entre altas ondas\nUma praia frente a um mar azul, sem ondas, ao meio-dia\nUma sensação de calma"
    },
    {
        "id": 37,
        "name": "Halphas",
        "enn": "Erato Halphas on ca secore",
        "description": "O trigésimo oitavo espírito é conhecido como Halphas, ou também como Malthous ou Malthas. Este imponente Conde se manifesta na forma de uma pomba, com uma voz rouca e poderosa. De acordo com o Ars Goetia, Halphas tem a habilidade de construir torres e abastecê-las com munições e armas, além de enviar navios de guerra para locais determinados. Essa descrição revela que ele é claramente um Senhor das Armas, um guerreiro que pode ser convocado em situações desafiadoras, e que pode fornecer, ou pelo menos indicar, os instrumentos necessários para ganhar uma luta.\nAlém de suas habilidades bélicas, Halphas é conhecido por governar 26 legiões de espíritos, tornando-o uma poderosa presença na invocação de espíritos. Com sua expertise militar e liderança, ele pode ser uma ajuda valiosa para quem o invoca em momentos de conflito ou dificuldade.",
        "planet": "Marte",
        "direction": "Sul",
        "pathworking": "Duas espadas cruzadas\nUma palmeira imensa, cobrindo a luz do sol\nUm rio largo e calmo, na outra beira dá para ver uma cidade\nUma sensação de raiva e desprezo"
    },
    {
        "id": 38,
        "name": "Malphas",
        "enn": "Lirach tasa Malphas ayer",
        "description": "O trigésimo nono espírito do Ars Goetia é conhecido como Malphas. A princípio, sua forma se assemelha à de um corvo, no entanto, a pedido do mago, ele assume uma forma humana e comunica-se com voz rouca. Essa presidente espiritual é dotada de uma força e poder consideráveis. Segundo o Ars Goetia, ela é capaz de construir casas e torres altas com facilidade. Essa habilidade parece estar mais relacionada ao poder dela de ajudar e facilitar a realização de projetos na parte material.\nAlém de suas habilidades de criação material, Malphas possui a capacidade de revelar ao seu invocador os desejos e pensamentos de seus inimigos, bem como as ações que eles realizaram. Isso é um poder e tanto, porque nos permite conhecer tanto as ações que os nossos inimigos estão realizando, quanto as que realizaram antes. Ou seja, podemos conhecer seus “podres”, o que é uma enorme vantagem estratégica numa situação de confronto.\nEla é capaz de fornecer bons familiares, trazendo consigo uma influência benéfica e protetora.\nÉ importante destacar que, de acordo com o Grimório original, não é recomendável oferecer sacrifícios a Malphas. Esse aviso pode indicar que ela é uma Shedim que valoriza a força em detrimento da subserviência. Portanto, é essencial que o invocador a trate com o devido respeito, mas mantenha uma postura independente e segura.\nMalphas governa sobre 40 legiões de espíritos, indicando que sua presença é poderosa e influente. Ao invocá-la, é preciso estar preparado para lidar com sua força e determinação, mas também para usufruir das suas habilidades e da sua proteção.",
        "planet": "Mercúrio",
        "direction": "Leste",
        "pathworking": "Uma taça de ouro com rubis\nUma pena e uma folha em branco\nUma biblioteca antiga\nUma sensação de certeza"
    },
    {
        "id": 39,
        "name": "Raum",
        "enn": "Furca na alle laris Raum",
        "description": "O quadragésimo espírito do Ars Goetia é conhecido como Raum. Ele é um Grande Conde que se apresenta inicialmente na forma de um corvo, mas, ao comando do mago, assume uma aparência humana.\nSua principal função é roubar tesouros preciosos que pertencem a pessoas que costumamos considerar inacessíveis. Por “tesouros” entendemos algo que é de grande valor para a pessoa. Pode ser algo material, ou imaterial. Contudo, sua habilidade não se limita a isso, uma vez que ele possui a capacidade de destruir cidades inteiras e derrubar dignidades dos homens. Basicamente, Raum é um Shedim especializado, entre outras coisas, em vingança e destruição. Não só é capaz de tirar algo que uma pessoa considera importante, como também é capaz de produzir destruição física e também no nível social.\nAlém disso, o Grande Conde Raum é dotado de um conhecimento incomparável, sendo capaz de contar absolutamente tudo - seja o passado, o presente ou o futuro. Sua habilidade de prever o que está por vir o torna um poderoso aliado para aqueles que desejam conhecer os segredos do universo.\nNão menos importante, ele também pode influenciar as relações interpessoais, capaz de provocar amor entre amigos e inimigos, a depender do objetivo de quem o convoca.\nEle era da Ordem dos Tronos, e atualmente governa 30 legiões de espíritos.",
        "planet": "Marte",
        "direction": "Sul",
        "pathworking": "Um corvo preto\nUm castelo antigo, visto de fora\nUm salão medieval, com uma longa mesa e cadeiras, frente a uma lareira\nUma sensação de medo"
    },
    {
        "id": 40,
        "name": "Focalor",
        "enn": "En Jedan on ca Focalor",
        "description": "O Quadragésimo Primeiro Espírito é conhecido por três nomes: Focalor, Forcalor ou Furcalor. Trata-se de um Duque poderoso e forte, que assume a forma de um homem com asas de Grifo.\nSeu ofício, porém, não é dos mais nobres. Focalor é um especialista em destruição, capaz de matar homens, afogá-los nas águas e derrubar navios de guerra. Isso se dá em função do seu poder sobre os ventos e os mares, que ele pode manipular de maneira impressionante.\nContudo, é importante ressaltar que Focalor não prejudicará nenhuma pessoa ou coisa se assim for ordenado pelo Mago. Ou seja, sua ação é restrita ao comando de um mago, o que o torna uma ferramenta poderosa em mãos certas. Ele é capaz de acabar com a saúde ou os negócios de qualquer pessoa, mas essa habilidade pode ser seletiva, poupando as pessoas ao redor do alvo, desde que isso seja indicado pelo mago.\nAo dizer que ele tem poder sobre “os ventos e os mares”, entendemos que, além do poder físico que Focalor possa ter, ele pode influenciar, com grande força, tanto a parte intelectual (ar, vento), quanto a parte emocional (água, mares), causando um profundo prejuízo na vida da pessoa alvo.\nFocalor governa 30 legiões de espíritos, o que demonstra a sua posição de liderança entre os Shedim. Seu poder é indiscutível e pode ser uma ferramenta poderosa nas mãos de um mago que deseja conquistar seus objetivos.",
        "planet": "Vênus",
        "direction": "Oeste",
        "pathworking": "Um martelo batendo no metal\nUma mão empunhando uma espada\nUm espaço aberto, com grama, com árvores no horizonte\nUma sensação de alerta"
    },
    {
        "id": 41,
        "name": "Vepar",
        "enn": "On ca Vepar Ag Na",
        "description": "Vepar, também conhecida como Vephar, é o quadragésimo segundo Espírito da lista dos 72 Espíritos da Goétia. Ela é uma Duquesa poderosa e imponente, com a aparência de uma Sereia.\nSeu domínio é sobre as águas e sobre os sentimentos e emoções. Ela tem a capacidade de governar e guiar pessoas em suas jornadas pelos mares intensos da emoção. A pedido do mago, ela pode atormentar a vida emocional de alguém, ou transformá-la num mar de paz e felicidade. Pode fazer com que uma pessoa seja plenamente consciente dos seus poderes na parte emocional, ou pode fazer com que outra pessoa perca completamente a noção dos pontos de referência e limites. Além disso, a pedido do mago, Vepar é capaz de causar tempestades violentas nas vidas das pessoas que ele escolher. Ela também possui o poder de causar a destruição de uma pessoa, contaminando seus pensamentos.\nVepar governa 29 legiões de espíritos, demonstrando sua grande influência e poder sobre as águas e tudo o que nelas habita. É importante ter cautela ao lidar com essa Duquesa pois, como toda sereia, o poder e a fascinação que exerce são imensos, e suas reações imprevisíveis, e isso sempre deve ser levado em consideração.",
        "planet": "Vênus",
        "direction": "Oeste",
        "pathworking": "Ondas enormes rompem aos pés da estátua de um guerreiro\nUma águia atravessa o céu com nuvens pretas\nUm terraço em ruínas, desde o qual dá para ver o mar\nUma sensação de poder"
    },
    {
        "id": 42,
        "name": "Sabnock",
        "enn": "Tasa Sabnock on ca Lirach",
        "description": "De acordo com a tradição esotérica da demonologia, o quadragésimo terceiro Espírito mencionado no Ars Goetia é conhecido como Sabnock, também grafado como Savnok. Este Marquês infernal é reputado por sua imponente presença, poder e força.\nAo se materializar, Sabnock assume a forma de um soldado armado, com os traços de um leão. Ele cavalga um majestoso cavalo de cor clara, que reforça ainda mais a aura intimidadora que cerca sua aparência.\nSegundo o Ars Goetia, a principal especialidade de Sabnock é a construção de torres, castelos e cidades impenetráveis. Além disso, ele é capaz de prover essas edificações com armaduras e outras proteções necessárias. Isto indica que seu talento para a defesa é tão marcante quanto sua habilidade para o ataque. Ou seja, por um lado, Sabnock é capaz de erguer barreiras e defesas ao redor do mago que o invocou (ou qualquer outra pessoa que lhe seja designada). Essas fortificações têm um alto grau de eficácia, pois são criadas com a energia espiritual do próprio Sabnock. Por outro lado, Sabnock também é capaz de realizar ataques perversos, que podem causar ferimentos psicológicos profundos e duradouros.\nSabnock é capaz de conceder bons familiares ao mago, caso seja solicitado. Ele comanda 50 legiões de espíritos e é considerado um dos espíritos mais fortes e poderosos na hierarquia de espíritos do Ars Goetia. Suas habilidades de ataque e defesa o tornam um aliado valioso para o mago que busca proteção ou que se especializa em ataque e defesa.",
        "planet": "Lua",
        "direction": "Sul",
        "pathworking": "Uma antiga cidade em ruínas\nUma flor cresce entre as pedras\nUm grande templo abandonado\nUma sensação de tristeza"
    },
    {
        "id": 43,
        "name": "Shax",
        "enn": "Ayer Avage Shax aken",
        "description": "Shax, também conhecido como Shaz ou Shass, é o quadragésimo quarto espírito da Ars Goetia. Este Grande Marquês é descrito como uma pomba, com uma voz rouca e sutil.\nEle é capaz de entorpecer os sentidos de qualquer pessoa indicada pelo mago que o invoca, fazendo-as deixar de ver ou ouvir aquilo que o mago desejar. Esse poder pode ser valioso quando há a necessidade de ocultar informações ou impedir que concorrentes reparem em algo que é importante para nós.\nAlém disso, Shax também possui a capacidade de prejudicar temporariamente a base econômica ou material de uma pessoa escolhida pelo mago. No entanto, o efeito desaparecerá com o tempo, e a pessoa recuperará o que foi tirado dela.\nOutra habilidade notável de Shax é sua capacidade de descobrir todas as coisas que estão ocultas e não guardadas por espíritos malignos. Em algumas ocasiões, ele também pode fornecer bons familiares.\nEste poderoso espírito é capaz de governar 30 legiões de outros espíritos. Sua aparência como uma pomba pode ser enganadora, pois sua influência e habilidades são impressionantes e úteis para aqueles que o invocam.",
        "planet": "Lua",
        "direction": "Leste",
        "pathworking": "Uma serpente se enrosca no galho de uma árvore\nUm martelo bate sobre uma espada\nO porão de uma igreja medieval\nUma sensação de angústia"
    },
    {
        "id": 44,
        "name": "Vine",
        "enn": "Eyesta nas Vine ca laris",
        "description": "Vine, também conhecido como Vinea, é o quadragésimo quinto espírito descrito no livro Ars Goetia. De acordo com as descrições, Vine é um Grande Rei e Conde que se apresenta na forma de um homem com aspecto de leão, montado em um cavalo preto e segurando uma víbora em sua mão. Sua principal função é a de descobrir coisas escondidas, sejam elas outras magias, bruxarias ou informações sobre o passado, presente e futuro.\nAlém disso, segundo os manuscritos antigos, Vine tem habilidades surpreendentes que lhe permitem construir torres, derrubar muralhas de pedra e provocar tempestades que tornam as águas turbulentas. Essas habilidades demonstram a capacidade deste espírito de criar poderosas defesas e realizar ataques devastadores.\nDe acordo com o Ars Goetia, Vine governa 36 legiões de espíritos.\nResumindo, Vine pode ser invocado tanto para ajudar na resolução de problemas relacionados a questões ocultas ou para obter informações valiosas sobre o passado, presente e futuro, quanto para defesa ou ataque. Como podemos ver, estamos perante um Shedim com um amplo espectro de habilidades, ideal para quem trabalha com magia.",
        "planet": "Sol/Marte",
        "direction": "Oeste",
        "pathworking": "Uma cidade antiga, com muralhas\nUma rua cheia de pessoas\nO interior de uma casa, com planta e com uma fonte\nUma sensação de calma"
    },
    {
        "id": 45,
        "name": "Bifrons",
        "enn": "Avage secore Bifrons remie tasa",
        "description": "Bifrons, conhecido por vezes como Bifrous ou Bifrovs, é um distinto conde que ocupa a posição de 46º na lista dos espíritos da Ars Goetia. Sua aparência é a de um monstro, mas pode transformar-se em um homem quando assim ordenado pelo mago. Seu nome indica que possui duas faces, sendo a atual manifestação de Janus, o antigo deus romano das portas, passagens, princípios e fins.\nEste poderoso deus é conhecido por conceder sabedoria em diversas áreas do conhecimento, como Astrologia, Geometria e outras Artes e Ciências. Ademais, Bifrons é um especialista em gemas e madeiras preciosas, e pode instruir sobre suas virtudes com maestria.\nSua habilidade em controlar os espíritos dos falecidos o torna um aliado valioso para magos que se dedicam à necromancia ou para aqueles que buscam vingança contra algum falecido.\nBifrons é acompanhado por seis legiões de espíritos que prontamente obedecem aos seus comandos.\nEste antigo deus é ideal tanto para quem deseja obter conhecimentos técnicos quanto para aqueles que querem ter contato com os seres que moram no Além.",
        "planet": "Marte",
        "direction": "Norte",
        "pathworking": "Uma árvore frondosa\nUm caminho de pedras\nA beira de um lago\nUma sensação de alegria"
    },
    {
        "id": 46,
        "name": "Vual",
        "enn": "As ana nany on ca Uvall",
        "description": "Vual, ou Voval, é o Quadragésimo Sétimo Espírito da hierarquia demoníaca. Ele é conhecido como um grande, poderoso e forte Duque, com habilidades sobrenaturais impressionantes. Quando invocado, Vual aparece inicialmente na forma de um dromedário poderoso, mas, após ser comandado pelo mago, pode se transformar em um ser humano.\nUma das principais habilidades de Vual é sua capacidade de obter o amor das mulheres. Além disso, ele é capaz de falar sobre as coisas passadas, presentes e futuras, o que pode ser extremamente útil para aqueles que buscam orientação em suas vidas.\nOutra habilidade interessante de Vual é sua capacidade de criar amizade entre amigos e inimigos. Essa habilidade pode ser particularmente útil para aqueles que desejam resolver conflitos ou acabar com brigas.\nVual era anteriormente parte da Ordem das Potências, e é capaz de governar 37 Legiões de Espíritos.",
        "planet": "Vênus",
        "direction": "Oeste",
        "pathworking": "Uma fonte com frutas variadas e coloridas\nUma sala com decoração oriental, com almofadas no chão\nUma fonte de água clara\nUma sensação de prazer"
    },
    {
        "id": 46,
        "name": "Vual",
        "enn": "As ana nany on ca Uvall",
        "description": "Vual, ou Voval, é o Quadragésimo Sétimo Espírito da hierarquia demoníaca. Ele é conhecido como um grande, poderoso e forte Duque, com habilidades sobrenaturais impressionantes. Quando invocado, Vual aparece inicialmente na forma de um dromedário poderoso, mas, após ser comandado pelo mago, pode se transformar em um ser humano.\nUma das principais habilidades de Vual é sua capacidade de obter o amor das mulheres. Além disso, ele é capaz de falar sobre as coisas passadas, presentes e futuras, o que pode ser extremamente útil para aqueles que buscam orientação em suas vidas.\nOutra habilidade interessante de Vual é sua capacidade de criar amizade entre amigos e inimigos. Essa habilidade pode ser particularmente útil para aqueles que desejam resolver conflitos ou acabar com brigas.\nVual era anteriormente parte da Ordem das Potências, e é capaz de governar 37 Legiões de Espíritos.",
        "planet": "Vênus",
        "direction": "Oeste",
        "pathworking": "Uma fonte com frutas variadas e coloridas\nUma sala com decoração oriental, com almofadas no chão\nUma fonte de água clara\nUma sensação de prazer"
    },
    {
        "id": 47,
        "name": "Haagenti",
        "enn": "Haaventi on ca Lirach",
        "description": "Haagenti é o Quadragésimo Oitavo Espírito da Goetia. Ele é um presidente que geralmente aparece na forma de um touro poderoso com asas de grifo, mas pode assumir a forma humana sob o comando do mago.\nSua principal função é a de tornar os homens sábios e instruí-los em diversos assuntos, além de ser capaz de provocar mudanças positivas no comportamento das pessoas, transformando-as para melhor.\nHaagenti é capaz de governar 33 legiões de espíritos e é um grande aliado para aqueles que buscam aprimorar seu conhecimento e desenvolvimento pessoal. Sob sua influência, é possível obter sabedoria em várias áreas e aprender habilidades valiosas que podem ser usadas para melhorar a vida. Além disso, suas transmu tações podem ajudar a transformar os aspectos negativos da personalidade de uma pessoa em traços positivos, permitindo que ela alcance seu potencial máximo.",
        "planet": "Mercúrio",
        "direction": "Norte",
        "pathworking": "Um prédio sólido e fortificado\nUm escudo dourado\nUma esplanada cercada por bandeiras\nUma sensação de disciplina"
    },
    {
        "id": 48,
        "name": "Crocell",
        "enn": "Jedan tasa Crocell on ca",
        "description": "O Quadragésimo Nono Espírito da Goetia é Crocell, também conhecido como Crokel. Ela é uma grande e forte Duquesa que geralmente se manifesta na forma de um anjo escuro, e é capaz de falar sobre coisas ocultas de forma mística, transmitindo conhecimento sobre a arte da geometria e as ciências liberais.\nEla é uma especialista em criar distrações.\nSob o comando do mago, pode criar situações completamente falsas, que as pessoas tomem como verdadeiras, deixando-as desconcertadas e cobrindo assim as ações do mago.\nEla melhora a parte emocional das pessoas (aquece as águas) e desperta a sensualidade e a luxúria (descobre os banhos).\nAntes de sua queda, Crocell era membro da Ordem das Potências. Hoje em dia, ela governa 48 legiões de espíritos e é uma poderosa aliada para aqueles que buscam conhecimento sobre assuntos ocultos e aprimoramento pessoal. Com sua ajuda, é possível desvendar mistérios e adquirir habilidades valiosas que podem ser usadas para aprimorar a vida.",
        "planet": "Vênus",
        "direction": "Oeste",
        "pathworking": "Uma bandeira agitada pelo vento\nUma torre de vigia\nO grande salão de um antigo templo\nUma sensação de curiosidade"
    },
    {
        "id": 49,
        "name": "Furcas",
        "enn": "Secore on ca Furcas remie",
        "description": "O Quinquagésimo Espírito da Goetia é conhecido como Furcas, um cavaleiro que se apresenta na forma de um velho cruel com uma longa barba e uma cabeça grisalha. Ele aparece montado em um cavalo de cor clara, empunhando uma arma afiada em sua mão poderosa.\nFurcas é um especialista em diversas áreas do conhecimento, incluindo filosofia, astrologia, retórica, lógica, quiromancia e piromancia, ensinando cada uma dessas artes com perfeição e detalhamento. Ele pode facilitar o aprendizado tanto de temas científicos e humanísticos, quanto de temas esotéricos e místicos, sendo um grande aliado para aqueles que buscam aprimoramento em diferentes áreas do conhecimento.\nCom seus poderes, Furcas governa 20 legiões de espíritos e pode ajudar aqueles que o invocam a adquirir sabedoria e conhecimento em uma variedade de assuntos. Seu ensinamento é preciso e completo, garantindo que seus discípulos alcancem excelência em suas áreas de estudo. Não hesite em chamar por sua ajuda se estiver buscando um mentor que possa guiá-lo em seu caminho de aprendizado e desenvolvimento pessoal.",
        "planet": "Saturno",
        "direction": "Leste",
        "pathworking": "Um martelo que bate no metal\nUm enorme barco se eleva à nossa frente\nUm cais que vai para o mar\nUma sensação de satisfação"
    },
    {
        "id": 50,
        "name": "Balam",
        "enn": "Lirach tasa vefa wehl Balam",
        "description": "O quinquagésimo primeiro Espírito da Goetia é Balam, um rei terrível e poderoso que inspira medo em todos que o invocam. Ele se apresenta com três cabeças: uma de touro, outra de homem e a terceira de carneiro, além de uma cauda de serpente e olhos flamejantes. Montado em um urso furioso e carregando um falcão em seu punho, ele é um ser imponente e temível.\nBalam tem uma voz rouca e poderosa, capaz de dar respostas verdadeiras sobre eventos passados, presentes e futuros. Além disso, ele é conhecido por ter o poder da invisibilidade, permitindo que aqueles que o invocam passem despercebidos em determinados locais e diante de determinadas pessoas.\nBalam também tem a capacidade de deixar as pessoas espirituosas e inspiradas, enchendo-as de energia e vitalidade.\nSeu domínio se estende sobre 40 legiões de espíritos, tornando-o uma presença poderosa e influente no mundo espiritual.\nApesar de sua natureza aterradora, Balam pode ser uma fonte valiosa de conhecimento e poder para aqueles que têm a coragem de invocá-lo. Se você está buscando respostas para questões importantes ou precisa de ajuda para se tornar mais forte e mais confiante, não hesite em chamá-lo. Com seu poder e sabedoria, ele pode ajudá-lo a conquistar seus objetivos e atingir seu verdadeiro potencial.",
        "planet": "Sol",
        "direction": "Norte",
        "pathworking": "Uma fogueira no meio da noite\nAs árvores de um bosque em volta\nUm espaço aberto, iluminado pelas chamas\nA sensação de ser avaliado"
    },
    {
        "id": 51,
        "name": "Alloces",
        "enn": "Typan efna Alloces met tasa",
        "description": "O quinquagésimo segundo espírito é Alloces, também conhecido como Alocas. Ele é um Duque poderoso e forte que aparece na forma de um soldado montado em um grande cavalo. Seu rosto é como o de um leão, muito vermelho e com olhos flamejantes, e sua fala é rouca e imponente.\nAlloces é especialista em ensinar a arte da astronomia e todas as ciências liberais. Com sua sabedoria e conhecimento, ele é capaz de esclarecer até mesmo os assuntos mais complexos. Além disso, ele é capaz de trazer bons espíritos familiares para aqueles que o convocam, ajudando a estabelecer conexões com outras dimensões.\nSob seu comando, 36 legiões de espíritos se curvam. Ele é capaz de invocá-los para auxiliar aqueles que buscam conhecimento e proteção. Com Alloces ao seu lado, você pode contar com um aliado poderoso em suas empreitadas mágicas e espirituais.",
        "planet": "Vênus",
        "direction": "Sul",
        "pathworking": "Um templo antigo\nUm labirinto feito de plantas\nUm espaço aberto, com uma fonte\nUma sensação de diversão"
    },
    {
        "id": 52,
        "name": "Camio",
        "enn": "Tasa on ca Caim renich",
        "description": "O Quinquagésimo Terceiro Espírito é Camio, também conhecido como Caim. Este é um poderoso Presidente do mundo espiritual, que tem o hábito de se manifestar inicialmente na forma de um pássaro chamado tordo. Posteriormente, assume a forma de um homem que empunha uma espada afiada em sua mão. Suas respostas carregam uma forte paixão, acompanhada de ira e fogo ardente. Sua habilidade em questionar e contestar diferentes pontos de vista pode ser muito útil quando se procura encontrar pontos fracos nas ideias ou discursos de adversários, ou quando se deseja identificar falhas em nossas próprias perspectivas. Camio é especializado em fornecer aos seres humanos uma compreensão mais profunda da natureza e uma melhor comunicação com ela, permitindo-nos entender não só as vozes dos seres vivos, mas também a voz das águas. Ele é capaz de fornecer respostas verdadeiras sobre coisas por vir. Ele pertencia originalmente à ordem dos Anjos. Agora governa mais de 30 legiões de espíritos. Sua presença e sabedoria são altamente valorizadas pelos praticantes da magia e espiritualidade, que o invocam em busca de orientação e sabedoria.",
        "planet": "Mercúrio",
        "direction": "Leste",
        "pathworking": "Uma torre elevada, de pedra\nUm exército organizado\nA vista desde uma muralha alta\nUma sensação de disciplina e força"
    },
    {
        "id": 53,
        "name": "Murmur",
        "enn": "Vefa mena Murmur ayer",
        "description": "Murmur, também conhecido como Murmus ou Murmux, é o quinquagésimo quarto espírito que aparece na forma de um grande duque e conde. Ele monta um grifo, uma criatura mitológica, e usa uma coroa ducal em sua cabeça. Este espírito é altamente valorizado por sua habilidade em ensinar filosofia com perfeição, oferecendo aos seus aprendizes um conhecimento profundo e abrangente do assunto. Além disso, ele possui o poder de convocar as almas falecidas e fazê-las responder às perguntas que lhe são feitas pelo mago. Este é um dom extremamente útil, especialmente quando se trata de questões relacionadas ao futuro ou a eventos passados. Murmur era parte da ordem dos tronos e, mais tarde, parte da dos anjos. Ele agora governa 30 legiões de espíritos, o que indica sua posição de autoridade e liderança. Sua presença é capaz de trazer clareza e compreensão aos assuntos mais complexos, oferecendo aos seus seguidores uma perspectiva única e valiosa. Com sua ajuda, o conhecimento e a sabedoria se tornam acessíveis a todos que desejam aprender.",
        "planet": "Vênus/Marte",
        "direction": "Oeste",
        "pathworking": "As ruínas de uma antiga cidade perdida no deserto\nA lua cheia no céu de verão\nUma praça abandonada, com um obelisco no centro\nA sensação de ser avaliado"
    },
    {
        "id": 54,
        "name": "Orobas",
        "enn": "Jedan tasa hoet naca Orobas",
        "description": "O quinquagésimo quinto espírito, Orobas, é um poderoso príncipe que se manifesta inicialmente na forma de um majestoso cavalo. No entanto, com o comando do exorcista, ele rapidamente se transforma na imagem de um homem, exibindo sua incrível capacidade de metamorfosear. Orobas é um espírito altamente habilidoso, conhecido por sua capacidade de revelar todos os segredos do passado, presente e futuro. Além disso, ele tem o poder de conceder honras e privilégios, bem como favores tanto de amigos quanto de inimigos. Este espírito é também um mestre no que diz respeito à verdadeira natureza da divindade e da criação do mundo, e pode dar respostas esclarecedoras sobre esses assuntos. Orobas é extremamente leal ao mago que o invoca e não permitirá que ele seja tentado por nenhum outro espírito. Isso é um testemunho do seu caráter fiel e confiável. Com sua autoridade e poder, Orobas governa vinte Legiões de espíritos, oferecendo orientação e liderança a todos os seus súditos. Sua presença traz clareza e sabedoria aos assuntos mais complexos e desafiadores, permitindo que seus seguidores progridam em sua jornada de crescimento espiritual. Com Orobas ao seu lado, o mago pode ter a certeza de que suas perguntas serão respondidas e seus desejos serão realizados.",
        "planet": "Júpiter",
        "direction": "Oeste",
        "pathworking": "Uma grande fonte, no centro de uma praça\nMuitas pessoas andam em volta dela\nUma rua estreita, se ninguém nela\nUma sensação de diversão"
    },
    {
        "id": 55,
        "name": "Gremory",
        "enn": "An tasa shi Gremory on ca",
        "description": "O quinquagésimo sexto espírito é a poderosa e cativante duquesa Gremory, também conhecida como Gamori. A origem de Gremory é um mistério, embora sua aparência única possa nos dar uma pista dela. Isso porque, diferente de outros Daemons, que aparecem com aparências estranhas ou até bizarras, ela se apresenta simplesmente como uma bela e poderosa mulher, montando um grande camelo, como se fosse uma rainha dos tempos antigos. E, de fato, existe um personagem bíblico que se encaixa muito bem com Gremory: A Rainha de Sheba. Isso porque, segundo a Kabbalah, a rainha de Sheba (nunca nos dizem o nome dela) era uma das rainhas dos Shedim. Isso parece ser confirmado pelo Targum Sheni, onde se diz que ela tinha as pernas cobertas de pelo, como os Se'irim, uma das categorias dos Shedim. Gremory é uma especialista em matéria de prosperidade, podendo ajudar o mago tanto em assuntos relacionados ao dinheiro quanto em empreendimentos. Outra especialidade de Gremory é revelar segredos ocultos, podendo desvendar informações sobre o passado, presente e futuro com grande precisão. Além disso, ela possui a habilidade de conhecer os segredos mais preciosos das pessoas (seus “tesouros”). Com esse poder de revelação, Gremory pode ajudar o mago mostrando os segredos dos seus inimigos. Esta poderosa duquesa é também uma “expert” em assuntos de amor, sendo talvez por isso que ela é tão procurada. Ela é capaz de ajudar a conquistar o coração de mulheres jovens e velhas. Com seu conhecimento e experiência, Gremory pode guiar seus seguidores para encontrar a verdadeira felicidade nos relacionamentos. Com o controle de vinte e seis legiões de espíritos, alguns temíveis, e outros altamente sedutores, Gremory é uma líder forte e respeitada, capaz de orientar e guiar seus súditos com sua sabedoria e discernimento. Ela é uma aliada valiosa para aqueles que buscam descobrir a verdade sobre si mesmos e o mundo ao seu redor, oferecendo uma visão única e iluminadora sobre os segredos mais profundos e preciosos, assim como sobre os labirintos do Amor. Com Gremory como guia, o mago pode ter a certeza de que terá a sabedoria e a orientação necessárias para alcançar seus objetivos.",
        "planet": "Vênus",
        "direction": "Oeste",
        "pathworking": "Um cetro de mando, feito em ouro e diamantes\nUm grande exército, bem formado e alinhado\nUm palácio, cheio de cômodos luxuosos"
    },
    {
        "id": 56,
        "name": "Ose",
        "enn": "Ayer serpente Ose",
        "description": "O quinquagésimo sétimo espírito é conhecido como Ose, Oso ou Voso. Trata-se de um grande presidente que, à primeira vista, assume a forma de um leopardo, mas depois de algum tempo se transforma em um homem. Ele fornece habilidade em todas as ciências liberais (conhecimento não técnico ou científico) e dá respostas corretas em relação às coisas secretas e divinas. Com sua magia de glamour, ele também é capaz de criar imagens falsas que fazem alguém acreditar que é outra pessoa. Essa pessoa ficará convencida de que a imagem é verdadeira e, portanto, mudará seu comportamento de acordo com ela. Ose é capaz de governar 30 legiões de espíritos e é um mestre em fornecer soluções precisas para problemas complexos. Ele é altamente valorizado por sua capacidade de desvendar mistérios e revelar segredos ocultos. Aqueles que o convocam com respeito e humildade serão agraciados com sua lealdade e dedicação, pois Ose não permitirá que seu convocador seja tentado por nenhum outro espírito.",
        "planet": "Mercúrio",
        "direction": "Leste",
        "pathworking": "Uma antiga cidade em ruínas\nUm cômodo surpreendentemente limpo, com um tapete e almofadas no chão\nUma mesa baixa com um braseiro queimando incenso"
    },
    {
        "id": 57,
        "name": "Amy",
        "enn": "Tu Fubin Amy secore",
        "description": "O quinquagésimo oitavo espírito é Amy, também conhecido como Avnas. Ele é um Grande Presidente das legiões infernais, e sua aparição inicial é como um fogo flamejante, mas após algum tempo ele assume a forma humana. Sua especialidade é a astrologia e todas as ciências liberais, que ele ensina com perfeição e maestria. Além disso, ele pode conceder aos seus invocadores bons familiares, espíritos que ajudam e protegem o mago em suas práticas ocultas. Amy é também capaz de revelar tesouros escondidos por outros espíritos, o que pode ser muito útil para aqueles que buscam riquezas ou conhecimento oculto. Ele é um governante poderoso, com 36 legiões de espíritos sob seu comando, e é conhecido por sua sabedoria e habilidade em lidar com os segredos do universo. Aqueles que o convocam com respeito podem esperar uma resposta clara e precisa para suas questões mais profundas e complexas.",
        "planet": "Mercúrio",
        "direction": "Sul",
        "pathworking": "Um chicote e uma luneta\nUma mesa de madeira, com um lampião sobre ela\nO camarote de um barco de madeira, iluminado pelo lampião"
    },
    {
        "id": 58,
        "name": "Orias",
        "enn": "Lirach mena Orias Anay na",
        "description": "O quinquagésimo nono espírito é Orias, um magnífico marquês conhecido também como Oriax, cuja aparição é majestosa como a de um guerreiro com características leoninas, montado em um poderoso cavalo preto. Em sua mão direita, ele segura com destreza duas serpentes que sibilam com poder. Os poderes de Orias transcendem os limites terrenos, estando intrinsecamente ligados ao Cosmos. Ele é o guardião do conhecimento das virtudes das estrelas e das mansões dos planetas (Astrologia), sabedoria que pode ser aplicada na vida cotidiana. Com sua habilidade inigualável, Orias é capaz de transformar homens, conceder dignidades e distinções, além de confirmá-las. Aqueles que o convocam ou são indicados pelo mago que o invoca são agraciados com favores tanto de amigos como de inimigos, tamanha é a influência e benevolência deste poderoso espírito. Orias é o governante de trinta legiões de espíritos, que o seguem lealmente em sua grandeza e poder. Sua presença é imponente e sua sabedoria é incomparável, sendo uma fonte inestimável de conhecimento e benefícios para aqueles que buscam sua ajuda.",
        "planet": "Lua",
        "direction": "Leste",
        "pathworking": "Um cetro de ouro, com esmeraldas\nUm grande livro, com uma pena sobre ele\nUm escritório com bibliotecas nas paredes e uma lareira\nUma sensação de certeza"
    },
    {
        "id": 59,
        "name": "Vapula",
        "enn": "Renich secore Vapula typan",
        "description": "Vapula, ou Naphula, é o sexagésimo espírito do Ars Goetia. Trata-se de um Grão-duque de força e poder excepcionais, que se manifesta na forma de um leão com asas de grifo. Vapula é um guia confiável para os que desejam aprimorar suas habilidades e adquirir conhecimentos em diversas áreas do saber. Além de ser um mestre nas artes e ofícios, Vapula também é um estudioso da filosofia e de outras ciências, oferecendo orientação precisa e valiosa a quem o invoca. Sua influência e sabedoria são vastas e profundas, permitindo que seus adeptos alcancem novos patamares de excelência em suas atividades. Com seus poderosos poderes, Vapula governa 36 legiões de espíritos com destreza e habilidade ímpares, garantindo que seus comandados atuem em harmonia e com precisão. Ele é um ser confiável e respeitado, capaz de fornecer orientações e ensinamentos que levam a um aprimoramento significativo em diversos aspectos da vida.",
        "planet": "Vênus",
        "direction": "Leste",
        "pathworking": "Uma costa marítima, com grandes pedras\nUm farol frente a um mar tempestuoso\nUma sala dentro do farol, com duas poltronas e uma janela que dá para o mar\nUma sensação de segurança"
    },
    {
        "id": 60,
        "name": "Zagan",
        "enn": "Anay on ca secore Zagan tasa",
        "description": "Zagan, é o sexagésimo primeiro espírito da hierarquia infernal, é um grande rei e presidente que se apresenta inicialmente na forma de um touro alado, dotado de uma majestade indescritível. Com o tempo, porém, ele se transforma em uma figura humana de grande beleza e sabedoria. Zagan é capaz de tornar os homens mais espirituosos, elevando seu espírito e proporcionando-lhes uma visão mais ampla do mundo e de si mesmos. Ele também possui o dom da transmutação, ou seja, a habilidade de transformar situações com grande destreza. Isso é especialmente útil quando nos encontramos diante de uma situação que desejamos mudar, mas sem renunciar aos aspectos positivos dela. Além disso, Zagan tem a capacidade de transformar os tolos em sábios, concedendo-lhes um conhecimento profundo e uma sabedoria inestimável. Ele governa 33 legiões de espíritos com habilidade e destreza, garantindo que seus comandados atuem em harmonia e com precisão. Com Zagan ao seu lado, é possível alcançar um elevado patamar de sabedoria e inteligência, bem como uma compreensão mais profunda dos mistérios da vida e do universo. Ele é um aliado valioso e respeitado, capaz de conceder benefícios e ensinamentos que levam a uma evolução significativa em diversos aspectos da existência.",
        "planet": "Sol/Mercúrio",
        "direction": "Terra",
        "pathworking": "O motor de um carro\nUm martelo batendo sobre metal\nUma oficina, cheia de maquinário novo e antigo\nUma sensação de diversão"
    },
    {
        "id": 61,
        "name": "Valac",
        "enn": "Avage Secore on ca Volac",
        "description": "Valac, ou Valak, ou Valu, é o sexagésimo segundo espírito do Ars Goetia, um poderoso e grande Presidente que, segundo o texto original, se apresenta como uma criança com asas de anjo, montada em um dragão, cuja imagem pode impressionar e intimidar os desavisados. Seu ofício é dar respostas verdadeiras sobre tesouros escondidos, sejam eles objetos físicos de valor inestimável ou informações preciosas que algumas pessoas escondem. Com sua habilidade sobrenatural, Valac é capaz de encontrar esses tesouros ocultos e revelá-los ao mago que o convoca. Além disso, Valac possui o dom de indicar onde está o perigo, seja ele físico ou espiritual, auxiliando seus seguidores a evitar situações perigosas e proteger-se de ameaças desconhecidas. Valac é um líder respeitado que governa 38 legiões de espíritos com maestria e disciplina, garantindo que suas ordens sejam cumpridas com precisão e eficácia. Com ele ao lado, seus seguidores podem ter certeza de que obterão respostas verdadeiras e valiosas para questões importantes e, ao mesmo tempo, serão protegidos dos perigos que espreitam em seu caminho.",
        "planet": "Mercúrio",
        "direction": "Norte",
        "pathworking": "Uma faca afiada, com cabo de ouro\nUm dragão nos observa, na escuridão\nUma caverna cheia de tesouros\nUma sensação de diversão"
    },
    {
        "id": 62,
        "name": "Andras",
        "enn": "Entey ama Andras anay",
        "description": "O Sexagésimo Terceiro Espírito é conhecido como Andras, uma Grande Marquesa que se manifesta na forma de um anjo com uma cabeça negra, com as características de um corvo noturno, montado em um poderoso lobo negro e brandindo uma espada brilhante em sua mão. Andras é conhecida por semear discórdia, conforme descrito no Ars Goetia. É importante destacar que, segundo o Ars Goetia, se o exorcista não estiver atento, ela e seus companheiros podem ser afetados por este Espírito. No entanto, se controlada com sabedoria, Andras pode ser uma poderosa aliada em situações que requerem a semeadura de discórdia, como em batalhas ou competições. Além disso, Andras governa sobre 30 legiões de espíritos, dando-lhe um grande poder e influência. Ao trabalhar com Andras é preciso mais cautela e foco do que com outros Daemons, pois suas habilidades caóticas, se não são bem direcionadas, podem afetar tanto o alvo quanto o próprio mago. Mas deixando bem claro quais são as nossas necessidades e desejos, Andras pode se tornar uma aliada preciosa em momentos críticos.",
        "planet": "Lua",
        "direction": "Sul",
        "pathworking": "Uma casa no meio da floresta\nUma bela mulher coloca água nas plantas, na frente da casa\nUma sala com duas cadeiras, uma mesa e, sobre ela, duas xícaras cheias\nUma sensação de astúcia"
    },
    {
        "id": 63,
        "name": "Haures",
        "enn": "Ganic tasa fubin Flauros",
        "description": "O sexagésimo quarto espírito é Haures, também conhecido como Hauras, Havres ou Flauros. Ele é um Grande Duque e sua aparência inicial é a de um leopardo poderoso e forte, mas sob o comando do exorcista, pode assumir forma humana com olhos flamejantes e um semblante terrível. Sua principal habilidade é fornecer respostas verdadeiras sobre tudo, desde o passado e presente até o futuro. Além disso, ele é capaz de falar sobre a criação do mundo e da divindade, assim como sobre a queda dele e de outros espíritos. Haures pode destruir e queimar os inimigos do mago que o convoca, se assim desejar, e não permitirá que nenhum outro espírito o tente ou o influencie. Ele governa 36 Legiões de Espíritos. Haures é um Shedim ideal tanto para aqueles que desejam conhecimento quanto para aqueles que precisam de proteção.",
        "planet": "Vênus",
        "direction": "Sul",
        "pathworking": "Uma grande roda que gira\nUm homem que pensa\nUm templo antigo, parcialmente destruído\nUma sensação de tristeza"
    },
    {
        "id": 64,
        "name": "Andrealphus",
        "enn": "Mena Andrealphus tasa ramec ayer",
        "description": "O 65º Espírito citado no Ars Goetia é Andrealphus, nome pelo qual se apresenta o antigo Senhor Adramelech, ou Baal Adramelech, poderoso deus solar dos Fenícios. Ele aparece agora como um poderoso Marquês. Inicialmente, ele se apresenta na forma de um majestoso pavão, mas depois de um tempo, assume forma humana, bela e perigosa ao mesmo tempo. Ele pode ser convocado para conceder conhecimento na área da geometria, engenharia e astronomia. Ele é capaz de ensinar a arte da geometria com perfeição, tornando seus invocadores extremamente sábios e habilidosos nessa ciência. Além disso, Andrealphus é capaz de usar suas habilidades metamórficas para transformar a aparência de uma pessoa, fazendo-a parecer diferente do que realmente é. Isso pode ser muito útil para aqueles que desejam projetar uma imagem diferente de si mesmos. Claro que ele não altera a aparência física da pessoa, mas afeta as mentes daqueles que estão em volta dela, fazendo-os ver algo diferente da realidade. Ele governa trinta legiões de espíritos e é altamente valorizado por aqueles que buscam conhecimento e habilidades em geometria e ciências afins.",
        "planet": "Lua",
        "direction": "Leste",
        "pathworking": "Um labirinto feito de cerca viva\nUma grande taça de cristal sobre uma mesa\nUm salão rodeado de espelhos\nA sensação de alguém tirando sarro de nós"
    },
    {
        "id": 65,
        "name": "Cimeies",
        "enn": "Ayer avage secore Cimejes",
        "description": "O sexagésimo sexto espírito é conhecido como Cimeies, Cimejes ou Kimaris. Ele é um poderoso Marquês que aparece como um guerreiro valente montado em um majestoso cavalo negro. Sua influência se estende sobre todos os espíritos na África. Ele possui a habilidade de ensinar perfeitamente gramática, lógica e retórica. Além disso, Cimeies é capaz de desvendar mistérios e revelar tesouros escondidos, tanto objetos físicos valiosos quanto informações preciosas que algumas pessoas mantêm em segredo. Seu conhecimento sobrenatural permite que ele encontre esses tesouros ocultos e entregue a informação ao mago que o evoca. Comandando 20 legiões de espíritos infernais, Cimeies é um aliado poderoso para aqueles que procuram sabedoria e riquezas.",
        "planet": "Lua",
        "direction": "Norte",
        "pathworking": "Um farol aceso na noite escura\nUma caverna cheia de tesouros, iluminada por tochas\nUma mesa com uma taça de vinho\nA sensação de sermos bem-vindos"
    },
    {
        "id": 66,
        "name": "Amdusias",
        "enn": "Denyen valocur avage secore Amdusias",
        "description": "O sexagésimo sétimo espírito é conhecido como Amdusias, ou Amdukias. Trata-se de um grande e poderoso Duque, que aparece inicialmente sob a forma de um majestoso unicórnio. Contudo, a pedido do exorcista, ele pode assumir uma forma humana que reflete toda a sua força e grandeza. Amdusias possui habilidades sobrenaturais para facilitar o aprendizado da música e aumentar a inspiração de um artista. Com sua ajuda, um músico ou compositor pode aprimorar suas habilidades musicais e criar obras que inspiram e emocionam o público. Além disso, Amdusias tem a capacidade de influenciar as vontades das pessoas. Ele pode fazer com que as pessoas concordem com o mago que o convoca e se comportem de acordo com a vontade dele. Essa habilidade pode ser muito útil em situações em que é necessário persuadir ou convencer alguém. Outra habilidade de Amdusias é a de fornecer excelentes espíritos familiares ao mago que o invoca. Em seu comando, Amdusias governa 29 legiões de espíritos que estão prontos para cumprir suas ordens e realizar seus desejos.",
        "planet": "Lua",
        "direction": "Norte",
        "pathworking": "Uma redoma de vidro, cheia de um líquido brilhante\nUm circuito montado numa placa, sobre uma mesa\nUm grande laboratório, cheio de coisas novas e antigas\nUma sensação de conhecimento"
    },
    {
          "id": 67,
          "name": "Belial",
          "enn": "Lirach Tasa Vefa Wehl Belial",
          "description": "O sexagésimo oitavo espírito é Belial, um poderoso e majestoso Rei que governa sobre 50 legiões de espíritos. Ele é uma entidade impressionante, que aparece na forma de dois anjos deslumbrantes sentados em uma carruagem flamejante. Sua voz graciosa e sedutora pode atrair até mesmo os mais desconfiados. Belial tem uma reputação de ter sido um dos mais dignos anjos antes de sua queda, mesmo acima de Miguel e outras figuras celestiais. Ele aparece no Antigo Testamento de várias formas, e uma das mais interessantes é a referência aos 'filhos de Belial', o que o coloca imediatamente numa posição de destaque entre os Shedim. Tanto pelas aparições no Antigo Testamento quanto pela descrição dada no Ars Goetia da sua forma física, ele pertence claramente ao terceiro grupo dos Shedim, os Anjos Caídos. Entre suas habilidades, Belial é capaz de facilitar o contato com pessoas importantes, o que pode ser muito útil para aqueles que buscam avançar em suas carreiras ou influenciar figuras poderosas. Além disso, ele é capaz de conseguir o favor de amigos e inimigos, ajudando aqueles que o convocam a resolver conflitos e alcançar seus objetivos de maneira mais eficaz. Belial também é conhecido por conceder excelentes familiares, companheiros mágicos que ajudam e protegem o mago em sua jornada. Ao se unir a um familiar concedido por Belial, o mago pode esperar ajuda e orientação em seus empreendimentos mágicos.",
          "planet": "Sol",
          "direction": "Sul",
          "pathworking": "Um soldado com armadura prateada, com um chicote na mão\nUma muralha com altas torres\nA porta da fortaleza, aberta para nós\nUma sensação de força"
    },
    {
          "id": 68,
          "name": "Decarabia",
          "enn": "Hoesta noc ra Decarabia secore",
          "description": "O sexagésimo nono Espírito é Decarabia, um Grande Marquês que aparece inicialmente na forma de uma estrela em um pentagrama. No entanto, após a ordem do exorcista, ele assume uma forma humana para atender às necessidades do invocador. Seu poder reside em sua capacidade de desvendar informações sigilosas, podendo ver coisas que passam despercebidas para as pessoas, assim como as aves que voam alto e enxergam tudo o que se passa na Terra, Decarabia é capaz de vislumbrar o interior dos corações e ações das pessoas e fornecer essas informações ao mago que o convoca. Ele também pode reconhecer e avisar o mago sobre as 'pedras preciosas', ou seja, os elementos únicos e muito importantes na vida de alguém, ou na vida do próprio mago. Além disso, Decarabia é hábil em indicar quais elementos da vida do mago são importantes e merecem ser reforçados ou projetados, para que o mago possa seguir o caminho mais adequado em sua jornada. Com sua sabedoria e visão apurada, ele pode ajudar o mago a tomar decisões importantes e alcançar seus objetivos de maneira mais eficaz.",
          "planet": "Lua",
          "direction": "Leste",
          "pathworking": "Uma luz intensa\nA escuridão profunda do céu numa noite sem lua\nUma clareira no bosque, iluminada por uma fogueira\nA sensação de ser observado"
    },
    {
        "id": 69,
        "name": "Seere",
        "enn": "Jeden et Renich Seere tu tasa",
        "description": "O septuagésimo espírito na hierarquia demoníaca é conhecido por diferentes nomes: Seere, Sear ou Seir. Ele é um Príncipe forte e poderoso, cuja presença é marcada pela beleza singular e uma aura majestosa. Quando se manifesta, Seere cavalga um cavalo alado com desenvoltura e destreza. De acordo com o Ars Goetia, a especialidade de Seere é ir e vir, trazendo consigo um poder sobrenatural que lhe permite realizar diversas tarefas em questão de segundos. Seu poder de deslocamento é extraordinário, capaz de percorrer o mundo inteiro em um piscar de olhos. Dessa forma, Seere é um especialista em levar e trazer informação, sendo capaz de descobrir roubos, tesouros escondidos e muitas outras coisas. Seere é um ser indiferente em sua natureza, disposto a realizar qualquer coisa que seja solicitada pelo mago. Sua habilidade em cruzar barreiras temporais e espaciais o torna um aliado valioso na busca por conhecimento e na realização de tarefas aparentemente impossíveis. Ademais, Seere governa 26 legiões de espíritos, demonstrando sua habilidade em liderar e comandar uma grande quantidade de seres. Em suas mãos, esses seres são controlados e colocados a serviço do mago, sendo utilizados em diversas atividades mágicas.",
        "planet": "Júpiter",
        "direction": "Leste",
        "pathworking": "Um rolo de papiro parcialmente aberto\nUma mesa com instrumentos de escrita\nUma biblioteca antiga, com cadeiras de madeira\nUma sensação de curiosidade"
    },
    {
        "id": 70,
        "name": "Dantalion",
        "enn": "Avage ayer Dantalion on ca",
        "description": "O septuagésimo primeiro espírito da hierarquia demoníaca é Dantalion, um Duque grande e poderoso, cuja presença é marcada por uma aparência singular: um homem com muitos semblantes, todos com rostos de homens e mulheres, segurando um livro em sua mão direita. De acordo com o Ars Goetia, Dantalion é um mestre das artes e ciências, capaz de ensinar os mais complexos conhecimentos aos magos que invocam sua presença. Além disso, ele é capaz de dar conselhos secretos, pois conhece os pensamentos de todos e pode mudá-los à vontade. Dentre suas habilidades mágicas, destaca-se sua capacidade de causar amor e de fazer com que a pessoa alvo do trabalho 'veja' o outro em todas as partes, até mesmo em sonhos. Essa influência mágica é potencializada pela capacidade de Dantalion de fixar a imagem da pessoa que está em contato com ele na mente e no coração do alvo, independentemente de onde estiverem no mundo. O efeito final é arrasador. Por fim, Dantalion governa 36 legiões de espíritos, demonstrando sua habilidade em liderar e comandar uma grande quantidade de seres. Sob sua liderança, esses espíritos são controlados e colocados a serviço do mago, sendo utilizados em diversas atividades mágicas.",
        "planet": "Vênus",
        "direction": "Oeste",
        "pathworking": "Uma nave antiga, navegando num mar agitado\nO convés, banhado em água das ondas\nO camarote do capitão, com uma lareira acesa\nUma sensação de segurança"
    },
    {
        "id": 71,
        "name": "Andromalius",
        "enn": "Tasa fubin Andromalius on ca",
        "description": "Andromalius é o septuagésimo segundo Espírito listado no Ars Goetia, e é conhecido por seu ofício em trazer de volta um ladrão e os bens roubados. Ele se apresenta como um conde grande e poderoso, de boa aparência, e sempre com a presença de uma grande serpente. Além de sua habilidade em recuperar bens roubados, Andromalius é capaz de descobrir toda a maldade e negociação desleal, sendo um poderoso aliado para aqueles que buscam a justiça e a verdade. Com sua habilidade mágica, ele pode punir todos os ladrões e outras pessoas más, demonstrando sua capacidade em fazer valer a ordem e a retidão. Mas Andromalius não se limita a trazer justiça e punição. Ele também é capaz de descobrir tesouros que estão escondidos, revelando riquezas que antes eram desconhecidas. Essa habilidade o torna um poderoso aliado para aqueles que buscam riquezas e prosperidade. Em sua posição como governante de 36 Legiões de Espíritos, Andromalius demonstra sua habilidade em liderar e comandar uma grande quantidade de seres. Sob sua liderança, esses espíritos são controlados e colocados a serviço do mago, sendo utilizados em diversas atividades mágicas.",
        "planet": "Marte",
        "direction": "Sul",
        "pathworking": "Uma espada com cabo de prata\nUma caverna cheia de tesouros empoeirados\nUma mesa, sobre ela um grimório antigo, cheio de segredos\nUma sensação de sabedoria"
    }
]

@app.route('/', methods=['GET'])
def get_all_cards():
    return jsonify(cards)

@app.route('/runes', methods=['GET'])
def get_all_runes():
    return jsonify(runes)

@app.route('/daemons', methods=['GET'])
def get_all_daemons():
    return jsonify(daemons)

@app.route('/get_card/<int:card_id>', methods=['GET'])
def get_card(card_id):
    card = next((c for c in cards if c["id"] == card_id), None)
    
    if card:
        return jsonify(card)
    else:
        return jsonify({"error": "Card not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)