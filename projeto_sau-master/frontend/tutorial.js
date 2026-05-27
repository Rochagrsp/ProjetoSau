async function carregarTutoriais() {

    const parametros= new URLSearchParams(window.location.search)
    const id = parametros.get("id")
    
    const resposta = await fetch(`http://127.0.0.1:8000/tutoriais/${id}`)
    const tutorial = await resposta.json()

    document.getElementById("titulo").innerText = tutorial.titulo
    document.getElementById("categoria").innerText = "Categoria:" + tutorial.categoria
    document.getElementById("descricao").innerText = tutorial.descricao || "Sem descrição cadastrada"

    document.getElementById("pdfViewer").src = tutorial.pdf

}

function voltar() {
    window.location.href = "index.html"
}
    
carregarTutoriais()
   