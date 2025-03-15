let respuestas = {};

function responder(pregunta, respuesta) {
    respuestas[pregunta] = respuesta;

    fetch("/adivinar_pais", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(respuestas)
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").innerHTML = `<h3>Resultado: ${data.pais}</h3>`;
        })
        .catch(error => console.error("Error:", error));
}
