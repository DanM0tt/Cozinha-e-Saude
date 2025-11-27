const login_form = document.getElementById("login-form1");
// vou adicionar error checking dps aqui..

login_form.addEventListener("submit", async (event) => {
    event.preventDefault()
    const email_ou_usuario = event.target.username.value;
    const senha = event.target.password.value;
    console.log(email_ou_usuario)
    console.log(senha)
    const request = await fetch("/api/usuarios", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email_ou_usuario,
            senha: senha
        })
    });

    if (request.status > 299) {
        window.location.href = "/"
        return new Error("Algo deu errado durante o login: " + request.status);
    };
    window.location.href = "/receita";
});