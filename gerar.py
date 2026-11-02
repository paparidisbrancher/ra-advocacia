"""Gera as páginas estáticas do site RA Advocacia.

Edite os textos aqui e rode:  python gerar.py
Topo, rodapé e metadados ficam num lugar só; o resultado é HTML puro, sem build no servidor.
Trechos com class="pendente" são dados a confirmar com o escritório: remova a classe quando confirmar.
"""
from pathlib import Path
from html import escape

RAIZ = Path(__file__).parent
DOMINIO = "https://paparidisbrancher.github.io/ra-advocacia"  # trocar pelo domínio real quando houver
DEMO = True  # apresentação ao cliente: fora dos buscadores. Mudar para False ao publicar de verdade.
WHATS = "https://wa.me/5535998871336?text=" + "Ol%C3%A1%2C%20gostaria%20de%20informa%C3%A7%C3%B5es%20sobre%20o%20atendimento."
TELEFONE = "(35) 99887-1336"
MAPA = "https://maps.google.com/?cid=9352116726334135630"  # perfil da RA Advocacia no Google Empresas
ENDERECO = "R. Antônio Ancleto Rezende, 19, apto. 203, Centro"  # como está no Google Empresas

MENU = [("index.html#escritorio", "O escritório"), ("index.html#areas", "Áreas de atuação"),
        ("index.html#equipe", "Equipe"), ("index.html#conteudos", "Conteúdos"), ("index.html#contato", "Contato")]

AREAS = [
    {
        "slug": "aposentadoria-rural",
        "titulo": "Aposentadoria do trabalhador rural",
        "resumo": "Para quem trabalha ou trabalhou na roça, como empregado, diarista ou em regime de economia familiar.",
        "corpo": """
<p class="intro">Quem vive do trabalho no campo tem regras próprias na Previdência Social. Em muitos casos, a aposentadoria pode ser pedida com idade menor do que a exigida de quem trabalha na cidade.</p>
<h2>Para quem é</h2>
<p>Pode envolver pequenos produtores, meeiros, arrendatários, boias-frias, empregados rurais e quem trabalha com a família na terra. Cada situação é tratada de um jeito pelo INSS (Instituto Nacional do Seguro Social), e o tempo de trabalho no campo precisa ser comprovado.</p>
<h2>O ponto que mais pesa: a prova do trabalho rural</h2>
<p>Muitas vezes o trabalhador rural não tem carteira assinada nem recibos. Por isso, documentos do dia a dia que mostram a ligação com a roça costumam ser importantes. Alguns exemplos:</p>
<ul>
  <li>notas fiscais de venda da produção ou bloco de produtor rural;</li>
  <li>contratos de arrendamento, parceria ou comodato da terra;</li>
  <li>documentos do imóvel rural, como ITR (Imposto Territorial Rural) ou CCIR (Certificado de Cadastro de Imóvel Rural);</li>
  <li>certidões de casamento ou de nascimento dos filhos em que conste a profissão de lavrador ou agricultor;</li>
  <li>ficha de sindicato rural, cadastro em cooperativa ou documentos de financiamento agrícola.</li>
</ul>
<p>A lista certa depende de cada história. Não descarte nenhum papel antigo antes de conversar com o escritório.</p>""",
        "faq": [
            ("Trabalhei na roça e depois na cidade. Perco o tempo rural?", "Não necessariamente. Há situações em que os dois períodos podem ser considerados juntos. Isso depende das datas, dos documentos e das regras em vigor, e precisa de análise individual."),
            ("Não tenho nenhum documento em meu nome. E agora?", "Documentos em nome de familiares próximos, do tempo em que vocês trabalhavam juntos, às vezes ajudam. Traga o que tiver para avaliarmos."),
            ("Preciso ir até o INSS antes de procurar o escritório?", "Não. Você pode conversar com o escritório antes de fazer o pedido, para entender quais documentos reunir."),
        ],
    },
    {
        "slug": "beneficios-por-incapacidade",
        "titulo": "Benefícios por incapacidade",
        "resumo": "Quando uma doença ou lesão impede o trabalho, por um tempo ou de forma permanente.",
        "corpo": """
<p class="intro">Quando uma doença ou um acidente impede a pessoa de trabalhar, a Previdência Social prevê benefícios para garantir uma renda nesse período.</p>
<h2>Os dois benefícios mais comuns</h2>
<ul>
  <li><strong>Auxílio por incapacidade temporária</strong>, antes chamado de auxílio-doença: para quem precisa se afastar por um período e tem expectativa de voltar ao trabalho.</li>
  <li><strong>Aposentadoria por incapacidade permanente</strong>, antes chamada de aposentadoria por invalidez: para quem não tem condições de voltar a trabalhar nem de ser readaptado para outra função.</li>
</ul>
<h2>Como o INSS decide</h2>
<p>A decisão passa pela perícia médica do INSS. Por isso, a organização dos documentos médicos faz diferença. Costumam ajudar:</p>
<ul>
  <li>laudos e relatórios médicos atualizados, com o diagnóstico e as limitações para o trabalho;</li>
  <li>exames, receitas e atestados, em ordem de data;</li>
  <li>documentos que mostrem a sua profissão e o que você faz no dia a dia do trabalho.</li>
</ul>
<p>Também é preciso verificar a qualidade de segurado e a carência, que são exigências ligadas às contribuições ou ao trabalho rural. Isso varia conforme o caso.</p>""",
        "faq": [
            ("A perícia negou, mas continuo sem conseguir trabalhar. O que fazer?", "Há caminhos para contestar a decisão, como recurso ao próprio INSS ou ação na Justiça. Os prazos são curtos, então procure orientação assim que receber a resposta."),
            ("Trabalhador rural também tem direito?", "Sim, o trabalhador rural pode ter direito, desde que comprove a atividade no campo e cumpra os demais requisitos."),
            ("Quais documentos levo para a primeira conversa?", "Documento com foto, carteira de trabalho, se tiver, e todos os laudos e exames que você já reuniu."),
        ],
    },
    {
        "slug": "auxilio-acidente",
        "titulo": "Auxílio-acidente",
        "resumo": "Para quem ficou com sequela de um acidente que reduziu a capacidade de trabalho.",
        "corpo": """
<p class="intro">O auxílio-acidente é uma espécie de indenização paga pelo INSS a quem ficou com uma sequela permanente depois de um acidente, e por isso passou a ter mais dificuldade para fazer o trabalho que fazia antes.</p>
<h2>O que é diferente nesse benefício</h2>
<p>A pessoa não precisa estar totalmente impedida de trabalhar. Em geral, o auxílio-acidente pode ser recebido junto com o salário, porque ele compensa a redução da capacidade, não a falta dela.</p>
<p>O acidente não precisa ter acontecido no trabalho. Acidentes domésticos, de trânsito ou em outras situações também podem ser analisados.</p>
<h2>Documentos que costumam ajudar</h2>
<ul>
  <li>boletim de ocorrência, ficha de atendimento no pronto-socorro ou CAT (Comunicação de Acidente de Trabalho), quando houver;</li>
  <li>laudos e exames que mostrem a sequela;</li>
  <li>documentos sobre a sua função antes e depois do acidente.</li>
</ul>
<p>Nem todo segurado tem direito a esse benefício, e as regras mudam conforme a categoria. Por isso, a análise individual é indispensável.</p>""",
        "faq": [
            ("Recebi auxílio-doença por causa do acidente. Posso ter direito ao auxílio-acidente depois?", "Pode ser. É comum que a análise aconteça quando o auxílio por incapacidade temporária termina e a sequela permanece."),
            ("O acidente foi há muitos anos. Ainda vale procurar orientação?", "Vale conversar. Há regras sobre prazos e valores atrasados que só podem ser avaliadas com os documentos em mãos."),
            ("Continuo trabalhando. Faz sentido pedir?", "Sim, em muitos casos o benefício é justamente para quem continua trabalhando com limitações."),
        ],
    },
    {
        "slug": "bpc-loas",
        "titulo": "BPC: Benefício de Prestação Continuada",
        "resumo": "Para pessoas idosas ou com deficiência de famílias de baixa renda, mesmo sem contribuição ao INSS.",
        "corpo": """
<p class="intro">O BPC (Benefício de Prestação Continuada), também conhecido como LOAS por causa da Lei Orgânica da Assistência Social, garante um salário mínimo por mês a pessoas idosas ou com deficiência que vivem em famílias de baixa renda.</p>
<h2>O que é importante saber</h2>
<ul>
  <li>O BPC não é aposentadoria. Ele faz parte da assistência social, por isso não exige contribuições ao INSS.</li>
  <li>A renda da família é analisada. Por isso, o cadastro no CadÚnico (Cadastro Único para Programas Sociais) precisa estar correto e atualizado.</li>
  <li>No caso de pessoa com deficiência, há avaliação médica e social feita pelo INSS.</li>
</ul>
<h2>Documentos que costumam ajudar</h2>
<ul>
  <li>documentos pessoais de todas as pessoas que moram na casa;</li>
  <li>comprovante de inscrição atualizada no CadÚnico;</li>
  <li>laudos, exames e relatórios que descrevam a deficiência e as dificuldades do dia a dia;</li>
  <li>comprovantes de despesas com saúde, quando houver.</li>
</ul>""",
        "faq": [
            ("Nunca contribuí para o INSS. Posso pedir o BPC?", "Sim. O BPC não depende de contribuição, mas exige o cumprimento dos requisitos de idade ou deficiência e de renda familiar."),
            ("O BPC deixa pensão para a família?", "Não. Por ser um benefício assistencial, o BPC não gera pensão por morte."),
            ("O pedido foi negado por causa da renda. Vale insistir?", "Depende. Às vezes a renda foi calculada de forma errada ou há despesas que podem ser consideradas. Isso só se descobre analisando o caso."),
        ],
    },
    {
        "slug": "beneficio-negado",
        "titulo": "Benefício negado pelo INSS",
        "resumo": "Para entender o motivo da negativa e avaliar se cabe recurso ou ação na Justiça.",
        "corpo": """
<p class="intro">Receber um “indeferido” do INSS é frustrante, mas nem sempre é o fim do caminho. O primeiro passo é entender exatamente por que o pedido foi negado.</p>
<h2>Onde está o motivo</h2>
<p>O INSS envia uma carta de decisão, que também fica disponível no aplicativo e no site Meu INSS. Ela traz o motivo da negativa e a data da decisão. Guarde esse documento.</p>
<h2>Caminhos possíveis</h2>
<ul>
  <li><strong>Novo pedido</strong>, quando faltou algum documento que agora você tem.</li>
  <li><strong>Recurso ao próprio INSS</strong>, analisado por um órgão chamado Conselho de Recursos da Previdência Social.</li>
  <li><strong>Ação na Justiça</strong>, quando a análise indicar que esse é o melhor caminho.</li>
</ul>
<p>Cada caminho tem prazos e riscos diferentes. O prazo para recorrer é curto e começa a contar a partir da ciência da decisão, então não deixe para depois.</p>""",
        "faq": [
            ("Perdi o prazo do recurso. Não tem mais jeito?", "Ainda pode haver alternativas, como um novo pedido ou uma ação judicial. Traga a carta de decisão para avaliarmos."),
            ("Como encontro a carta de decisão?", "No aplicativo ou no site Meu INSS, na área de consulta de pedidos. Se tiver dificuldade, o escritório ajuda você a localizar."),
            ("Preciso pagar para fazer a primeira conversa?", "As condições do atendimento são explicadas diretamente pelo escritório. Entre em contato para saber como funciona."),
        ],
    },
]

ARTIGOS = [
    {
        "slug": "documentos-atividade-rural",
        "titulo": "Como reunir documentos da atividade rural",
        "resumo": "Um guia simples para organizar os papéis que mostram o seu trabalho no campo.",
        "corpo": """
<p class="intro">Para o INSS (Instituto Nacional do Seguro Social), o trabalho rural precisa ser demonstrado com documentos. Organizar esses papéis com calma, antes do pedido, evita idas e vindas.</p>
<h2>Comece pelo que está em casa</h2>
<p>Separe certidões de casamento e de nascimento dos filhos, documentos da terra, notas de venda da produção, carteirinhas de sindicato e contratos de arrendamento ou parceria. Documentos antigos costumam ser valiosos.</p>
<h2>Organize por data</h2>
<p>Coloque os documentos em ordem, do mais antigo para o mais recente. Isso ajuda a mostrar a continuidade do trabalho ao longo dos anos.</p>
<h2>Não jogue nada fora</h2>
<p>Um papel que parece sem importância pode ajudar a comprovar um período. Antes de descartar qualquer documento, converse com o escritório.</p>""",
        "fontes": [("Lei nº 8.213/1991 (Planos de Benefícios da Previdência Social)", "https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm"),
                   ("INSS no portal gov.br", "https://www.gov.br/inss/pt-br")],
    },
    {
        "slug": "beneficio-negado-o-que-observar",
        "titulo": "Benefício negado: o que observar primeiro",
        "resumo": "Onde encontrar o motivo da negativa e por que o prazo importa.",
        "corpo": """
<p class="intro">Quando o INSS nega um benefício, a reação natural é desanimar. Antes disso, vale olhar com atenção para três pontos.</p>
<h2>1. O motivo</h2>
<p>A carta de decisão informa por que o pedido foi negado. Pode ter faltado documento, a perícia pode não ter reconhecido a incapacidade ou a renda pode ter sido considerada acima do limite.</p>
<h2>2. A data</h2>
<p>Os prazos para contestar começam a contar quando você toma conhecimento da decisão. Anote a data e procure orientação logo.</p>
<h2>3. O que mudou desde o pedido</h2>
<p>Novos laudos, documentos encontrados depois ou uma piora na saúde podem mudar a análise. Leve tudo para a conversa com o escritório.</p>""",
        "fontes": [("Meu INSS", "https://meu.inss.gov.br/"), ("INSS no portal gov.br", "https://www.gov.br/inss/pt-br")],
    },
    {
        "slug": "o-que-e-bpc",
        "titulo": "O que é o BPC e para quem ele existe",
        "resumo": "Entenda a diferença entre o BPC e a aposentadoria.",
        "corpo": """
<p class="intro">O BPC (Benefício de Prestação Continuada) é um benefício da assistência social. Ele paga um salário mínimo por mês a pessoas idosas ou com deficiência que vivem em famílias de baixa renda.</p>
<h2>BPC não é aposentadoria</h2>
<p>Para receber o BPC não é preciso ter contribuído para o INSS. Em compensação, ele não gera pensão por morte para a família.</p>
<h2>O papel do CadÚnico</h2>
<p>O CadÚnico (Cadastro Único para Programas Sociais) é usado para verificar a renda da família. Manter o cadastro atualizado, com todas as pessoas da casa, é parte essencial do pedido.</p>
<h2>Cada família é diferente</h2>
<p>A análise da renda e, no caso de deficiência, a avaliação médica e social dependem da realidade de cada família. Por isso, a orientação individual faz diferença.</p>""",
        "fontes": [("Lei nº 8.742/1993 (Lei Orgânica da Assistência Social)", "https://www.planalto.gov.br/ccivil_03/leis/l8742.htm"),
                   ("INSS no portal gov.br", "https://www.gov.br/inss/pt-br")],
    },
]


def topo(p, atual=""):
    itens = "".join(
        f'<li><a href="{p}{href}"{" aria-current=\"page\"" if atual == txt else ""}>{txt}</a></li>' for href, txt in MENU
    )
    return f"""<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo">
  <div class="contido">
    <a class="marca" href="{p}index.html">
      <img src="{p}assets/img/logo-monograma-terracota.png" alt="" width="696" height="408">
      <span>RA Advocacia</span>
    </a>
    <nav class="menu" aria-label="Principal">
      <button class="menu-botao" type="button" aria-expanded="false" aria-controls="menu-lista">Menu</button>
      <ul id="menu-lista">{itens}</ul>
    </nav>
  </div>
</header>"""


def rodape(p):
    return f"""<footer class="rodape">
  <div class="contido grade">
    <div class="rodape-marca">
      <img src="{p}assets/img/logo-completa-claro.png" alt="RA Advocacia" width="1153" height="600" loading="lazy">
      <p>Direito Previdenciário em Alpinópolis, Minas Gerais.</p>
      <p><span class="pendente">Razão social, CNPJ e inscrição da sociedade na OAB/MG a confirmar</span></p>
    </div>
    <nav class="rodape-nav" aria-label="Rodapé">
      <h2>Navegação</h2>
      <ul>{"".join(f'<li><a href="{p}{h}">{t}</a></li>' for h, t in MENU)}</ul>
    </nav>
    <div class="rodape-contato">
      <h2>Contato</h2>
      <ul>
        <li><a href="{WHATS}">WhatsApp {TELEFONE}</a></li>
        <li><a href="{MAPA}">{ENDERECO}, Alpinópolis, MG</a></li>
        <li><a href="https://www.instagram.com/renatamaria.adv/">Instagram da Dra. Renata Maria</a></li>
        <li><a href="https://www.instagram.com/anafaria.adv/">Instagram da Dra. Ana Cristina</a></li>
        <li><a href="{p}privacidade.html">Política de privacidade</a></li>
      </ul>
    </div>
    <p class="final">Conteúdo informativo. Não substitui a análise individual do seu caso. © 2026 RA Advocacia.</p>
  </div>
</footer>
<script src="{p}assets/site.js" defer></script>"""


def pagina(caminho, titulo, descricao, corpo, atual="", noindex=False):
    p = "../" * caminho.count("/")
    url = f"{DOMINIO}/{caminho}".replace("/index.html", "/")
    robots = '\n<meta name="robots" content="noindex">' if noindex or DEMO else ""
    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(titulo)}</title>
<meta name="description" content="{escape(descricao)}">{robots}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{escape(titulo)}">
<meta property="og:description" content="{escape(descricao)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMINIO}/assets/img/og-image.jpg">
<meta name="theme-color" content="#8C4A3C">
<script>document.documentElement.classList.add("js")</script>
<link rel="icon" href="{p}assets/img/logo-monograma-terracota.png" type="image/png">
<link rel="preload" href="{p}assets/fonts/newsreader.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}assets/fonts/atkinson-hyperlegible-next.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/site.css">
</head>
<body>
{topo(p, atual)}
<main id="conteudo">
{corpo}
</main>
{rodape(p)}
</body>
</html>
"""
    destino = RAIZ / caminho
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8", newline="\n")
    return caminho, noindex


AVISO_REVISAO = """<div class="revisao" role="note"><p><strong>Texto em revisão pelo escritório.</strong> Este conteúdo é informativo, não substitui a análise individual do seu caso e pode mudar conforme a legislação.</p></div>"""

CHAMADA = f"""<section class="chamada" aria-labelledby="chamada-titulo">
  <h2 id="chamada-titulo">Quer conversar sobre o seu caso?</h2>
  <p>Cada situação depende dos seus documentos e da sua história. Fale com o escritório para entender os caminhos possíveis.</p>
  <div class="acoes">
    <a class="botao claro" href="{WHATS}">Conversar pelo WhatsApp</a>
    <a class="link-acao" href="../index.html#contato">Outras formas de contato</a>
  </div>
</section>"""

# Coluna de atendimento das páginas internas (fica fixa ao rolar, no computador)
LATERAL = f"""<aside class="lateral" aria-label="Atendimento">
  <p class="lateral-titulo">Atendimento</p>
  <p><a class="lateral-tel" href="tel:+5535998871336">{TELEFONE}</a></p>
  <p><a href="{WHATS}">Conversar pelo WhatsApp</a></p>
  <p>{ENDERECO}<br>Alpinópolis, MG<br><a href="{MAPA}">Ver no Google Maps</a></p>
</aside>"""


def cabeca_interna(trilha, titulo, intro="", meta=""):
    intro = f'\n  <p class="intro">{intro}</p>' if intro else ""
    meta = f'\n  <p class="meta">{meta}</p>' if meta else ""
    return f"""<div class="cabeca-interna"><div class="contido">
  <p class="trilha">{trilha}</p>
  <h1>{titulo}</h1>{intro}{meta}
</div></div>"""


def pagina_area(a):
    perguntas = "".join(f"<details><summary>{q}</summary><p>{r}</p></details>" for q, r in a["faq"])
    trilha = '<a href="../index.html">Início</a> / <a href="../index.html#areas">Áreas de atuação</a>'
    corpo = f"""{cabeca_interna(trilha, a["titulo"], a["resumo"])}
<div class="interna"><div class="contido grade">
  {LATERAL}
  {AVISO_REVISAO}
  <article class="texto">
    {a["corpo"]}
    <h2>Perguntas frequentes</h2>
    <div class="perguntas">{perguntas}</div>
  </article>
  {CHAMADA}
</div></div>"""
    return pagina(f"areas/{a['slug']}.html", f"{a['titulo']} | RA Advocacia", a["resumo"], corpo, "Áreas de atuação")


def pagina_artigo(a):
    fontes = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in a["fontes"])
    trilha = '<a href="../index.html">Início</a> / <a href="../index.html#conteudos">Conteúdos</a>'
    meta = 'Autoria: <span class="pendente">a definir</span>. Publicado em: <span class="pendente">a definir</span>. Revisão jurídica: <span class="pendente">pendente</span>.'
    corpo = f"""{cabeca_interna(trilha, a["titulo"], meta=meta)}
<div class="interna"><div class="contido grade">
  {LATERAL}
  <div class="revisao" role="note"><p><strong>Rascunho.</strong> Este texto aguarda revisão do escritório e ainda não aparece nos buscadores.</p></div>
  <article class="texto">
    {a["corpo"]}
    <h2>Fontes</h2>
    <ul>{fontes}</ul>
  </article>
  {CHAMADA}
</div></div>"""
    return pagina(f"conteudos/{a['slug']}.html", f"{a['titulo']} | RA Advocacia", a["resumo"], corpo, "Conteúdos", noindex=True)


def pagina_inicio():
    areas = "".join(
        f'<li><a href="areas/{a["slug"]}.html"><h3>{a["titulo"]}</h3><p>{a["resumo"]}</p><span class="seta" aria-hidden="true"></span></a></li>'
        for a in AREAS
    )
    artigos = "".join(
        f'<article class="artigo{" destaque" if i == 0 else ""}"><p class="estado">Rascunho em revisão</p>'
        f'<h3><a href="conteudos/{a["slug"]}.html">{a["titulo"]}</a></h3><p>{a["resumo"]}</p></article>'
        for i, a in enumerate(ARTIGOS)
    )
    corpo = f"""
<section class="hero" aria-labelledby="titulo">
  <div class="contido grade hero-texto">
    <h1 id="titulo">Advocacia previdenciária em Alpinópolis</h1>
    <div class="hero-apoio">
      <p>Aposentadoria rural, auxílio-doença, auxílio-acidente e benefícios para idosos e pessoas com deficiência. Atendimento no escritório ou pelo WhatsApp.</p>
      <div class="acoes">
        <a class="botao" href="{WHATS}">Conversar pelo WhatsApp</a>
        <a class="link-acao" href="#areas">Áreas de atuação</a>
      </div>
    </div>
  </div>
  <figure class="hero-foto">
    <picture>
      <source media="(max-width: 700px)" srcset="assets/img/topo-celular.webp" width="800" height="1000">
      <img src="assets/img/topo-1600.webp" srcset="assets/img/topo-1600.webp 1600w, assets/img/topo-2560.webp 2560w" sizes="100vw"
        width="1600" height="700" fetchpriority="high"
        alt="As duas sócias, lado a lado e sorrindo, diante da parede com a logo RA Advocacia">
    </picture>
    <figcaption class="legenda">Dra. Ana Cristina Faria de Lima e Dra. Renata Maria Alves Silva, sócias, na recepção do escritório.</figcaption>
  </figure>
</section>

<section class="secao" id="escritorio" aria-labelledby="escritorio-titulo">
  <div class="contido grade">
    <div class="escritorio-texto">
      <h2 id="escritorio-titulo">O escritório. <span class="tom">Em Alpinópolis, para quem precisa resolver uma questão com o INSS.</span></h2>
      <p>A RA Advocacia atua em Direito Previdenciário. Recebemos trabalhadores rurais, pessoas idosas, pessoas com deficiência e famílias que precisam entender seus direitos junto ao INSS (Instituto Nacional do Seguro Social).</p>
      <p>O trabalho começa por ouvir a sua história, sem pressa e sem palavras difíceis. Como cada caso tem documentos e requisitos próprios, a orientação vem depois de analisar a sua situação.</p>
      <h3>Como é o primeiro atendimento</h3>
      <ol class="passos">
        <li><span><strong>Você conta o que está acontecendo</strong>, no escritório ou pelo WhatsApp.</span></li>
        <li><span><strong>Olhamos os documentos que você já tem</strong> e dizemos o que mais pode ser necessário.</span></li>
        <li><span><strong>Explicamos os caminhos possíveis</strong> para você decidir com tranquilidade.</span></li>
      </ol>
    </div>
    <figure class="escritorio-foto">
      <img src="assets/img/escritorio-trabalho.webp" width="800" height="1000" loading="lazy"
        alt="Dra. Renata Maria sentada à mesa e Dra. Ana Cristina em pé ao lado, no escritório">
    </figure>
  </div>
</section>

<section class="secao areas-secao" id="areas" aria-labelledby="areas-titulo">
  <div class="contido grade">
    <div class="areas-cabeca">
      <h2 id="areas-titulo">Áreas de atuação</h2>
      <p class="intro">Em todas elas, o primeiro passo é analisar a sua situação e os seus documentos.</p>
      <p><span class="pendente">Lista a confirmar com o escritório.</span></p>
    </div>
    <ul class="areas">{areas}</ul>
  </div>
</section>

<section class="secao" id="equipe" aria-labelledby="equipe-titulo">
  <div class="contido grade">
    <div class="equipe-cabeca">
      <h2 id="equipe-titulo">Equipe. <span class="tom">As sócias e quem recebe você no escritório.</span></h2>
    </div>
    <article class="socia">
      <img class="retrato" src="assets/img/renata-maria.webp" width="800" height="1000" loading="lazy" alt="Dra. Renata Maria à mesa de trabalho no escritório">
      <h3>Dra. Renata Maria Alves Silva</h3>
      <p class="funcao">Advogada e sócia. <span class="pendente">OAB/MG nº a confirmar</span></p>
      <p>Advoga há mais de 10 anos e atua em Direito Previdenciário.</p>
      <blockquote class="citacao"><p>“Amo o que faço e tenho um carinho especial pelo trabalhador rural.”</p></blockquote>
      <p><a href="https://www.instagram.com/renatamaria.adv/">Instagram @renatamaria.adv</a></p>
    </article>
    <article class="socia">
      <img class="retrato" src="assets/img/ana-faria.webp" width="800" height="1000" loading="lazy" alt="Dra. Ana Cristina Faria à mesa de trabalho no escritório">
      <h3>Dra. Ana Cristina Faria de Lima</h3>
      <p class="funcao">Advogada e sócia. <span class="pendente">OAB/MG nº a confirmar</span></p>
      <p>Atua na área jurídica há mais de 5 anos e se dedica a benefícios do INSS, como BPC, auxílio-doença e auxílio-acidente.</p>
      <blockquote class="citacao"><p>“Nunca tive dúvidas: advogar é minha paixão.”</p></blockquote>
      <p><a href="https://www.instagram.com/anafaria.adv/">Instagram @anafaria.adv</a></p>
    </article>
    <div class="apoio grade">
      <h3>Também no escritório</h3>
      <ul>
        <li><img src="assets/img/marina.webp" width="620" height="747" loading="lazy" alt="Retrato da Dra. Marina Lima"><strong>Dra. Marina Lima</strong><p>Advogada. <span class="pendente">OAB/MG nº a confirmar</span></p></li>
        <li><img src="assets/img/mylena.webp" width="488" height="588" loading="lazy" alt="Retrato de Mylena"><strong>Mylena</strong><p>Estudante de Direito e estagiária. <span class="pendente">Sobrenome a confirmar</span></p></li>
      </ul>
    </div>
  </div>
</section>

<section class="secao conteudos" id="conteudos" aria-labelledby="conteudos-titulo">
  <div class="contido grade">
    <div class="conteudos-cabeca">
      <h2 id="conteudos-titulo">Conteúdos</h2>
      <p class="intro">Textos curtos para ajudar você a entender seus direitos. Eles passam por revisão do escritório antes de serem publicados.</p>
    </div>
    {artigos}
  </div>
</section>

<section class="secao videos" id="videos" aria-labelledby="videos-titulo">
  <div class="contido">
    <h2 id="videos-titulo">Vídeos. <span class="tom">Dúvidas comuns sobre o INSS, explicadas pelas advogadas.</span></h2>
    <p class="intro">Informação geral: cada caso depende da análise dos documentos.</p>
    <ul class="videos-lista" role="region" tabindex="0" aria-label="Vídeos da RA Advocacia">
      <li><figure>
        <video controls preload="none" playsinline poster="videos/Dci83AGx6vk.webp" width="720" height="1280" aria-label="Trabalha na roça e ficou doente ou sofreu um acidente?"><source src="videos/Dci83AGx6vk.mp4" type="video/mp4"></video>
        <figcaption>Trabalha na roça e ficou doente ou sofreu um acidente?<span>0:36 · <a href="https://www.instagram.com/reel/Dci83AGx6vk/">ver no Instagram</a></span></figcaption>
      </figure></li>
      <li><figure>
        <video controls preload="none" playsinline poster="videos/DaDTSXyR6SL.webp" width="720" height="1280" aria-label="Quais são os requisitos do BPC-LOAS?"><source src="videos/DaDTSXyR6SL.mp4" type="video/mp4"></video>
        <figcaption>Quais são os requisitos do BPC-LOAS?<span>0:42 · <a href="https://www.instagram.com/reel/DaDTSXyR6SL/">ver no Instagram</a></span></figcaption>
      </figure></li>
      <li><figure>
        <video controls preload="none" playsinline poster="videos/DdZCKZXhK-j.webp" width="720" height="1280" aria-label="Aposentadoria rural com idade reduzida"><source src="videos/DdZCKZXhK-j.mp4" type="video/mp4"></video>
        <figcaption>Aposentadoria rural com idade reduzida<span>0:37 · <a href="https://www.instagram.com/reel/DdZCKZXhK-j/">ver no Instagram</a></span></figcaption>
      </figure></li>
      <li><figure>
        <video controls preload="none" playsinline poster="videos/DcQ61UfxA2l.webp" width="720" height="1280" aria-label="Sofreu um acidente e não trabalha mais como antes?"><source src="videos/DcQ61UfxA2l.mp4" type="video/mp4"></video>
        <figcaption>Sofreu um acidente e não trabalha mais como antes?<span>0:32 · <a href="https://www.instagram.com/reel/DcQ61UfxA2l/">ver no Instagram</a></span></figcaption>
      </figure></li>
      <li><figure>
        <video controls preload="none" playsinline poster="videos/DbTIGVfxCl_.webp" width="720" height="1280" aria-label="Burnout e ansiedade podem dar direito a benefício?"><source src="videos/DbTIGVfxCl_.mp4" type="video/mp4"></video>
        <figcaption>Burnout e ansiedade podem dar direito a benefício?<span>0:40 · <a href="https://www.instagram.com/reel/DbTIGVfxCl_/">ver no Instagram</a></span></figcaption>
      </figure></li>
      <li><figure>
        <video controls preload="none" playsinline poster="videos/DaNnFT-RJ3T.webp" width="720" height="1280" aria-label="Cuidado com golpes envolvendo o INSS"><source src="videos/DaNnFT-RJ3T.mp4" type="video/mp4"></video>
        <figcaption>Cuidado com golpes envolvendo o INSS<span>0:57 · <a href="https://www.instagram.com/reel/DaNnFT-RJ3T/">ver no Instagram</a></span></figcaption>
      </figure></li>
    </ul>
    <p><a href="https://www.instagram.com/renatamaria.adv/reels/">Todos os vídeos no Instagram</a></p>
  </div>
</section>

<section class="secao contato" id="contato" aria-labelledby="contato-titulo">
  <div class="contido grade">
    <div class="contato-dados">
      <h2 id="contato-titulo">Contato</h2>
      <p class="intro">Conte em poucas palavras o que está acontecendo. Respondemos pelo WhatsApp ou por ligação, como você preferir.</p>
      <a class="telefone" href="tel:+5535998871336">{TELEFONE}</a>
      <div><a class="botao contorno" href="{WHATS}">Conversar pelo WhatsApp</a></div>
      <dl class="dados">
        <div><dt>Endereço</dt><dd>{ENDERECO}<br>Alpinópolis, MG, 37940-000<br><a href="{MAPA}">Ver no Google Maps</a></dd></div>
        <div><dt>Horário de atendimento</dt><dd>A partir das 9h. Fechado aos sábados.<br><span class="pendente">Dias e horário de fechamento a confirmar</span></dd></div>
        <div><dt>Acessibilidade</dt><dd>Estacionamento acessível para cadeira de rodas</dd></div>
        <div><dt>E-mail</dt><dd><span class="pendente">E-mail a confirmar</span></dd></div>
        <div><dt>Instagram</dt><dd><a href="https://www.instagram.com/renatamaria.adv/">@renatamaria.adv</a> e <a href="https://www.instagram.com/anafaria.adv/">@anafaria.adv</a></dd></div>
      </dl>
    </div>
    <div class="cartao">
      <h3>Escreva sua mensagem</h3>
      <form id="form-contato" novalidate aria-describedby="aviso-form">
        <div>
          <label for="nome">Seu nome</label>
          <input type="text" id="nome" name="nome" autocomplete="name" required maxlength="80" aria-describedby="erro-nome">
          <span class="erro" id="erro-nome"></span>
        </div>
        <fieldset>
          <legend>Prefere retorno por</legend>
          <div class="opcoes">
            <label><input type="radio" name="retorno" value="WhatsApp" checked> WhatsApp</label>
            <label><input type="radio" name="retorno" value="ligação"> Ligação</label>
          </div>
        </fieldset>
        <div>
          <label for="mensagem">Como podemos ajudar?</label>
          <span class="dica" id="dica-mensagem">Por exemplo: “Meu auxílio foi negado” ou “Quero saber sobre aposentadoria rural”.</span>
          <textarea id="mensagem" name="mensagem" required maxlength="600" aria-describedby="dica-mensagem erro-mensagem"></textarea>
          <span class="erro" id="erro-mensagem"></span>
        </div>
        <p class="aviso-form" id="aviso-form">Ao enviar, abrimos o WhatsApp com a sua mensagem pronta. Nada fica guardado neste site. Não envie CPF, documentos ou informações de saúde por aqui. Veja a <a href="privacidade.html">política de privacidade</a>.</p>
        <div><button class="botao" type="submit">Enviar pelo WhatsApp</button></div>
        <p class="status" id="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>"""
    return pagina("index.html", "RA Advocacia | Direito Previdenciário em Alpinópolis, MG",
                  "Orientação em Direito Previdenciário para trabalhadores rurais e pessoas que buscam compreender seus direitos junto ao INSS, em Alpinópolis, MG.",
                  corpo)


def pagina_privacidade():
    meta = 'Última atualização: <span class="pendente">data a definir na publicação</span>'
    corpo = f"""{cabeca_interna('<a href="index.html">Início</a>', "Política de privacidade", meta=meta)}
<div class="interna"><div class="contido grade">
  <div class="revisao" role="note"><p><strong>Texto em revisão pelo escritório.</strong> Ele descreve como este site funciona hoje e deve ser atualizado se algo mudar.</p></div>
  <article class="texto">
    <p class="intro">Esta política explica quais dados este site trata, para quê e quais são os seus direitos, conforme a LGPD (Lei Geral de Proteção de Dados, Lei nº 13.709/2018).</p>
    <h2>Quem é o responsável</h2>
    <p>RA Advocacia, {ENDERECO}, Alpinópolis, MG, 37940-000. <span class="pendente">Razão social e CNPJ a confirmar.</span></p>
    <h2>O formulário de contato</h2>
    <p>O formulário pede apenas o seu nome, a forma de retorno preferida e uma mensagem curta. Esses dados não são enviados nem guardados por este site: ao tocar em “Enviar pelo WhatsApp”, o seu próprio aparelho abre o WhatsApp com a mensagem pronta, e você decide se envia.</p>
    <p>Se você enviar a mensagem, o escritório usará os dados apenas para responder ao seu contato e, se for o caso, iniciar o atendimento. O WhatsApp é um serviço da Meta e tem política de privacidade própria.</p>
    <p>Pedimos que não envie CPF, documentos ou informações de saúde pelo formulário. Quando forem necessários, o escritório orienta a forma adequada de entregá-los.</p>
    <h2>Cookies e estatísticas</h2>
    <p>Este site não usa cookies, ferramentas de estatística nem rastreadores de publicidade. As fontes e imagens são carregadas do próprio site.</p>
    <h2>Registros técnicos</h2>
    <p>Como qualquer site, o servidor de hospedagem pode registrar dados técnicos de acesso, como endereço IP, data e hora, para segurança e funcionamento. <span class="pendente">Empresa de hospedagem e prazo de guarda a confirmar.</span></p>
    <h2>Links externos</h2>
    <p>Os links para Instagram, WhatsApp e sites do governo levam a serviços de terceiros, com políticas próprias.</p>
    <h2>Seus direitos</h2>
    <p>Você pode pedir a confirmação, o acesso, a correção ou a exclusão dos seus dados, entre outros direitos previstos na LGPD, pelos canais de contato do escritório.</p>
  </article>
</div></div>"""
    return pagina("privacidade.html", "Política de privacidade | RA Advocacia",
                  "Como o site da RA Advocacia trata dados pessoais.", corpo)


if __name__ == "__main__":
    paginas = [pagina_inicio(), pagina_privacidade(), *map(pagina_area, AREAS), *map(pagina_artigo, ARTIGOS)]
    urls = "".join(
        f"  <url><loc>{DOMINIO}/{c.replace('index.html', '')}</loc></url>\n" for c, noindex in paginas if not noindex
    )
    (RAIZ / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n',
        encoding="utf-8", newline="\n")
    regra = "Disallow: /" if DEMO else "Allow: /"
    (RAIZ / "robots.txt").write_text(f"User-agent: *\n{regra}\nSitemap: {DOMINIO}/sitemap.xml\n", encoding="utf-8", newline="\n")
    print("\n".join(c for c, _ in paginas))
