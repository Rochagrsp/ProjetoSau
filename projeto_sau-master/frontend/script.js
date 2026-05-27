async function carregarTutoriais() {
    

    const resposta= await fetch("http://127.0.0.1:8000/tutoriais")

    const dados = await resposta.json()

    console.log(dados)

    const areaTutorias = document.getElementById("tutoriais")
    areaTutorias.innerHTML = ""
   
    dados.forEach(tutorial => {

        areaTutorias.innerHTML += `
        
        <div class="card">

            <h2>${tutorial.titulo}</h2>
            
            <p>Categoria: ${tutorial.categoria}</p>

            <button onclick="abrirtutorial(${tutorial.id})">
                Abrir tutorial
            </button>

        </div>
        `

})
}


function abrirtutorial(id) {
    window.location.href = `tutorial.html?id=${id}`
}



carregarTutoriais()