const form_cadastro = document.getElementById("form-cadastro");
form_cadastro.addEventListener("submit", async (event) => {
    event.preventDefault();
    const email = event.target.email.value;
    const senha = event.target.senha.value;
    const senha_confirmacao = event.target.confirmacao_senha.value;

    if (senha != senha_confirmacao) {
        window.location.href = "/";
        return;
    }

    const nome_usuario = event.target.nome_usuario.value;

    const elemento_select = document.getElementById("genero-escolha");
    const indice_escolhido = elemento_select.selectedIndex; 
    const opcao_escolhida = elemento_select.options[indice_escolhido].value;
    
    const data_nascimento = event.target.ano.value + "-" 
        + event.target.mes.value + "-" + event.target.dia.value;
    
    const response = await fetch('/api/usuarios', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            username: nome_usuario,
            senha: senha,
            birthday: data_nascimento,
            gender: opcao_escolhida,
        })
    });

    if (response.status > 399) {
        return new Error("Algo deu errado: " + response.status);
    }

    window.location.href = "/";
});