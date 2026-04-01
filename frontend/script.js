let chat = document.querySelector('#chat');
let input = document.querySelector('#input');
let botaoEnviar = document.querySelector('#enviar_mensagem');

if (botaoEnviar) {
    botaoEnviar.addEventListener('click', function(event) {
        event.preventDefault(); 
    });
}

async function enviarMensagem(event) {
    if (event) event.preventDefault();
    if(input.value == "" || input.value == null) return;
    let menssagem = input.value;
    input.value = "";

    let novaMensagem = exibirMensagemUsuario();
    chat.appendChild(novaMensagem);

    let novaMensagemBot = exibirMensagemBot();
    chat.appendChild(novaMensagemBot);
    chat.scrollTop = chat.scrollHeight;
    novaMensagemBot.innerHTML = "Pensando ..."
    const resposta = await fetch("/api/enviar_mensagem", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({'msg': menssagem}),
    });

    const textoDaResposta = await resposta.text();
    novaMensagemBot.innerHTML = textoDaResposta.replace(/\n/g, "<br>");
    vaiParaFinalDoChat();

};