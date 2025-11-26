function adicionarContato() {
  const nome = document.getElementById("nome").value.trim();
  const telefone = document.getElementById("telefone").value.trim();

  if (nome !== "" && telefone !== "") {
    const li = document.createElement("li");
    li.innerHTML = `${nome} - ${telefone} 
      <button onclick="removerContato(this)">Remover</button>`;
    document.getElementById("lista").appendChild(li);

    document.getElementById("nome").value = "";
    document.getElementById("telefone").value = "";
  }
}

function removerContato(botao) {
  botao.parentElement.remove();
}
