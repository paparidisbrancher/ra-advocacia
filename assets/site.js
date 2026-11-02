// RA Advocacia: menu do celular e formulário de contato (abre o WhatsApp com a mensagem pronta).
const WHATSAPP = "5535998871336"; // (35) 99887-1336 — confirmar com o escritório

// Menu do celular: abre e fecha pelo botão; fecha com Esc, ao escolher um link ou ao tocar fora.
const menuBotao = document.querySelector(".menu-botao");
if (menuBotao) {
  const abrir = (sim) => menuBotao.setAttribute("aria-expanded", String(sim));
  menuBotao.addEventListener("click", () => abrir(menuBotao.getAttribute("aria-expanded") !== "true"));
  document.querySelectorAll(".menu a").forEach((a) => a.addEventListener("click", () => abrir(false)));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && menuBotao.getAttribute("aria-expanded") === "true") { abrir(false); menuBotao.focus(); }
  });
  document.addEventListener("click", (e) => { if (!e.target.closest(".menu")) abrir(false); });
}

const form = document.getElementById("form-contato");
if (form) {
  const status = document.getElementById("form-status");
  const mensagens = {
    nome: "Escreva seu nome para sabermos como chamar você.",
    mensagem: "Conte em poucas palavras como podemos ajudar.",
  };

  const validar = (campo) => {
    const erro = document.getElementById(`erro-${campo.name}`);
    const ok = campo.value.trim().length > 0;
    campo.setAttribute("aria-invalid", String(!ok));
    erro.textContent = ok ? "" : mensagens[campo.name];
    return ok;
  };

  form.querySelectorAll("[required]").forEach((c) => {
    c.addEventListener("blur", () => validar(c));
    // Limpa o erro já durante a digitação: se esperasse o blur, o layout pularia no meio do próximo clique.
    c.addEventListener("input", () => c.getAttribute("aria-invalid") === "true" && validar(c));
  });

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const campos = [...form.querySelectorAll("[required]")];
    const invalidos = campos.filter((c) => !validar(c));
    if (invalidos.length) {
      status.textContent = "Faltam informações. Confira os campos marcados.";
      invalidos[0].focus();
      return;
    }
    const d = new FormData(form);
    const texto =
      `Olá, gostaria de informações sobre o atendimento.\n\n` +
      `Nome: ${d.get("nome").trim()}\n` +
      `Prefiro retorno por: ${d.get("retorno")}\n\n` +
      `${d.get("mensagem").trim()}`;
    // Sem "noopener" no window.open: com ele o retorno é sempre null e não daria para saber se abriu.
    const janela = window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(texto)}`, "_blank");
    if (janela) janela.opener = null;
    status.textContent = janela
      ? "Abrimos o WhatsApp com sua mensagem. Confira o texto e toque em enviar para concluir."
      : "O navegador bloqueou a nova janela. Use o botão “Conversar pelo WhatsApp” nesta página.";
  });
}

// Um vídeo por vez
document.addEventListener('play', (e) => document.querySelectorAll('video').forEach((v) => { if (v !== e.target) v.pause(); }), true);
