async function generateCV() {
    const prompt = document.getElementById('cvPrompt').value;
    const response = await fetch('/create_cv', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: prompt }),
    });
    const result = await response.json();
    document.getElementById('cvResult').innerText = result.cv;
}
