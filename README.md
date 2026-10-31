# Site RA Advocacia

Site estático (HTML + CSS + um pouco de JS). Não precisa de build no servidor: basta copiar a pasta inteira para a hospedagem.

## Como editar

Textos, áreas de atuação, artigos, topo e rodapé ficam em `gerar.py`. Depois de editar, rode:

    python gerar.py

Isso regrava todos os `.html`, o `sitemap.xml` e o `robots.txt`. Estilos em `assets/site.css`; formulário e menu em `assets/site.js`.

- Trechos com `class="pendente"` (fundo pêssego tracejado) são dados a confirmar. Ao confirmar, troque o texto e remova a classe.
- Artigos em `conteudos/` saem com `noindex` e selo "Rascunho". Depois da revisão, mude `noindex=True` para `False` em `pagina_artigo` e preencha autoria e datas.
- Formulário: não envia nada a servidor. Monta a mensagem e abre o WhatsApp do escritório (número em `assets/site.js` e `gerar.py`).

## Antes de publicar (pendências do escritório)

- [ ] Logo oficial em SVG/PNG. A atual foi recortada da arte do Instagram (`assets/img/logo-*.png`).
- [ ] Fotos originais em alta resolução e autorização de uso de imagem de todas as pessoas.
- [ ] Domínio: trocar `DOMINIO` em `gerar.py`, mudar `DEMO = False` (hoje o site está fora dos buscadores) e rodar de novo.
- [ ] Razão social, CNPJ e inscrição da sociedade na OAB/MG.
- [ ] Números de OAB/MG da Dra. Renata Maria e da Dra. Ana Cristina Faria.
- [ ] Nome completo e função de Marina e Mylena (não identificar estagiária como advogada).
- [ ] Endereço atual (os posts mostram endereços diferentes), horário, e-mail, telefone/WhatsApp.
- [ ] Confirmar as cinco áreas de atuação e revisar juridicamente os textos das áreas e artigos.
- [ ] Dados estruturados (JSON-LD de escritório) só depois dos dados acima confirmados.
- [ ] Política de privacidade: empresa de hospedagem, prazo de guarda de registros, data da versão.
- [ ] Revisão final do escritório quanto ao Provimento 205/2021 da OAB.
