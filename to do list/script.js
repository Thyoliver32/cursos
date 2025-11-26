function adicionarTarefa() {
  const input = document.getElementById("novaTarefa");
  const texto = input.value.trim();

  if (texto !== "") {
    const li = document.createElement("li");
    li.innerHTML = `${texto} <button onclick="removerTarefa(this)">Remover</button>`;
    document.getElementById("lista").appendChild(li);
    input.value = "";
  }
}

function removerTarefa(botao) {
  botao.parentElement.remove();
}
