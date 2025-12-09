const href_cadastro = document.getElementById("botao-href-cadastro");

href_cadastro.addEventListener("click", () => window.location.href = '/cadastro');

const login_form = document.getElementById("login-form1");
// vou adicionar error checking dps aqui..

login_form.addEventListener("submit", async (event) => {
    event.preventDefault()
    const email_ou_usuario = event.target.email.value;
    const senha = event.target.password.value;
    console.log(email_ou_usuario)
    console.log(senha)
    const request = await fetch("/api/sessao", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email_ou_usuario,
            senha: senha
        })
    });

    if (request.status > 399) {
        window.location.href = "/"
        return new Error("Algo deu errado durante o login: " + request.status);
    };
    window.location.href = "/receita";
});