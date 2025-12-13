const userId = localStorage.getItem("user_id");

async function carregarHistorico() {
  const container = document.getElementById("historico-container");
  container.innerHTML = "";

  const response = await fetch(
    `/api/receitas/ultimas/${userId}`
  );

  const receitas = await response.json();

  if (receitas.length === 0) {
    container.innerHTML = "<p>Nenhuma receita salva ainda.</p>";
    return;
  }

  receitas.forEach(r => {
    const div = document.createElement("div");
    div.className = "receita-card";

    div.innerHTML = `
      <h4>🍽 Receita</h4>
      <div class="data">
        ${new Date(r.created_at).toLocaleDateString()}
      </div>
      <div class="receita-markdown">
        ${marked.parse(r.resposta)}
      </div>
    `;

    container.appendChild(div);
  });
}

carregarHistorico();
