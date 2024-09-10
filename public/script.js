document.getElementById('fetch-data').addEventListener('click', async function () {
  const response = await fetch('/api/backend');
  const data = await response.json();
  document.getElementById('response').innerText = data.message;
});

