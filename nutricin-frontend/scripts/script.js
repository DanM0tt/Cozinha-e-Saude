const ingredientes = [];
const input = document.getElementById("ingrediente-input");
const lista = document.getElementById("lista-ingredientes");
const btnAdd = document.getElementById("add-btn");
const btnGerar = document.getElementById("btn-receita");
const resultadoDiv = document.getElementById("resultado");

btnAdd.addEventListener("click", () => {
  const ingrediente = input.value.trim();
  if (ingrediente) {
    ingredientes.push(ingrediente);
    const li = document.createElement("li");
    li.textContent = ingrediente;
    lista.appendChild(li);
    input.value = "";
  }
});

btnGerar.addEventListener("click", async () => {
  if (ingredientes.length < 2) {
    alert("Adicione pelo menos 2 ingredientes!");
    return;
  }

  const porcoes = document.getElementById("porcoes").value || 2;
  const restricao = document.getElementById("restricao").value;

  resultadoDiv.innerHTML = "<p>⏳ Gerando receita...</p>";

  try {
    const response = await fetch("http://127.0.0.1:8000/gerar_receita/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ingredientes: ingredientes.join(", "),
        porcoes: parseInt(porcoes),
        restricao: restricao || null,
      }),
    });

    if (!response.ok) throw new Error("Erro na requisição");

    // ✅ Captura texto puro da resposta 
    const texto = await response.json();
    console.log(texto);
    // ✅ Converte Markdown em HTML formatado
    const htmlFormatado = marked.parse(texto);

    // ✅ Mostra no resultado com um estilo bonito
    resultadoDiv.innerHTML = `
      <h2>🍽️ Receita Gerada</h2>
      <div class="receita-markdown">${htmlFormatado}</div>
    `;

  } catch (error) {
    console.error(error);
    resultadoDiv.innerHTML = "<p>❌ Ocorreu um erro ao gerar a receita.</p>";
  }
});