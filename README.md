# Site RA Advocacia

Site estático (HTML + CSS + um pouco de JS). Não precisa de build no servidor: basta copiar a pasta inteira para a hospedagem.

## Como editar

Textos, áreas de atuação, artigos, topo e rodapé ficam em `gerar.py`. Depois de editar, rode:

    python gerar.py

Isso regrava todos os `.html`, o `sitemap.xml` e o `robots.txt`. Estilos em `assets/site.css`; formulário e menu em `assets/site.js`.

- Trechos com `class="pendente"` (fundo pêssego sublinhado) são dados a confirmar. Ao confirmar, troque o texto e remova a classe.
- Artigos em `conteudos/` saem com `noindex` e selo "Rascunho". Depois da revisão, mude `noindex=True` para `False` em `pagina_artigo` e preencha autoria e datas.
- Formulário: não envia nada a servidor. Monta a mensagem e abre o WhatsApp do escritório (número em `assets/site.js` e `gerar.py`).

## Visual

- Títulos em Newsreader e texto em Atkinson Hyperlegible Next, feita pelo Braille Institute para leitores com baixa visão (o zero cortado é do desenho dela). As duas são OFL e ficam em `assets/fonts`, sem depender do Google.
- Tudo com cantos retos. O canto arredondado das artes do Instagram aparece só nos painéis de contato e na foto do escritório.
- Fotos: o topo (`topo-*.webp`) e a do escritório saíram do perfil no Google Empresas. Os retratos das sócias são do ensaio. Marina e Mylena foram recortadas das artes do Instagram e precisam de foto própria.
- Referências: sites de escritórios com menção honrosa no Awwwards (IMK Avocats, Setia Law, Hafnia Law) e The Law Practice. Os princípios foram adaptados, sem copiar layout nem texto.

## Antes de publicar (pendências do escritório)

- [ ] Logo oficial em SVG/PNG. A atual foi recortada da arte do Instagram (`assets/img/logo-*.png`).
- [ ] Fotos originais em alta resolução e autorização de uso de imagem de todas as pessoas.
- [ ] Domínio: trocar `DOMINIO` em `gerar.py`, mudar `DEMO = False` (hoje o site está fora dos buscadores) e rodar de novo.
- [ ] Razão social, CNPJ e inscrição da sociedade na OAB/MG.
- [ ] Números de OAB/MG da Dra. Renata Maria e da Dra. Ana Cristina Faria.
- [ ] Nome completo e função de Marina e Mylena (não identificar estagiária como advogada).
- [x] Endereço, telefone/WhatsApp, nomes completos das sócias e acessibilidade: tirados do perfil no Google Empresas em 31/10/2026.
- [ ] Horário completo (o Google só mostra "abre às 9h" e "fechado aos sábados") e e-mail.
- [ ] Perfil no Google: o site cadastrado (rajadvocaciaespecializada.com.br) não existe mais; trocar pelo novo endereço quando publicar.
- [ ] Fotos do Google com a marca antiga "Alves & Faria" ficaram fora do site de propósito.
- [ ] Confirmar as cinco áreas de atuação e revisar juridicamente os textos das áreas e artigos.
- [ ] Dados estruturados (JSON-LD de escritório) só depois dos dados acima confirmados.
- [ ] Política de privacidade: empresa de hospedagem, prazo de guarda de registros, data da versão.
- [ ] Revisão final do escritório quanto ao Provimento 205/2021 da OAB.

## Atualização de 02/11/2026 (Instagram com login)

- Funções confirmadas pelas legendas do Instagram (posts DUWW-zHkvhC, DUWWdN7Ero2, Dau4mllxeq9): Dra. Marina Lima é advogada; Mylena é estudante de Direito e estagiária. Retratos delas refeitos em resolução maior.
- Seção "Vídeos" com 6 reels da @renatamaria.adv em `videos/` (720p, só baixam ao dar play). Temas escolhidos sem promessa de resultado.
