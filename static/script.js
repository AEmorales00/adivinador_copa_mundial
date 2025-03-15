async function responder(pregunta, respuesta) {
    const datos = { [pregunta]: respuesta };

    const response = await fetch("/adivinar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(datos)
    });

    const resultado = await response.json();
    document.getElementById("resultado").innerText = "Resultado: " + resultado.resultado;
}
