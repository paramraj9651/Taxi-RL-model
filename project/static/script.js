async function runAgent() {
    const output = document.getElementById('output');
    output.innerText = "Running...\n";

    const response = await fetch("/run", {
        method: "POST"
    });

    if (!response.ok) {
        output.innerText = "Failed to run agent.";
        return;
    }

    const data = await response.json();

    let text = "";
    data.forEach((step, i) => {
        text += `Step ${i+1}\n`;
        text += `state: ${step.state}\n`;
        text += `action: ${step.action}\n`;
        text += `reward: ${step.reward}\n\n`;
    });

    output.innerText = text;
}
