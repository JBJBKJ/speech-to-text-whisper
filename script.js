document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    document.getElementById('status').innerText = '⏳ Идёт обработка...';

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    if (result.text) {
        document.getElementById('status').innerText = '✅ Готово!';
        document.getElementById('result').innerText = result.text;
    } else {
        document.getElementById('status').innerText = '❌ Ошибка!';
    }
});
