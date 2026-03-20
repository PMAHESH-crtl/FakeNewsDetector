async function predict() {
    let text = document.getElementById("news").value;

    let response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({text: text})
    });

    let data = await response.json();
    document.getElementById("result").innerText = data.result;
}