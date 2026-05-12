document.getElementById('downloadForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const urlInput = document.getElementById('url');
    const btn = document.getElementById('downloadBtn');
    const btnText = document.getElementById('btnText');
    const spinner = document.getElementById('spinner');
    const messageBox = document.getElementById('messageBox');

    // Reset UI to loading state
    messageBox.className = 'message hidden';
    btn.disabled = true;
    btnText.textContent = 'Downloading...';
    spinner.style.display = 'block';

    try {
        // Send request to Flask backend
        const response = await fetch('/download', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: urlInput.value })
        });

        const data = await response.json();

        // Check if download was successful
        if (response.ok && data.success) {
            messageBox.textContent = `✅ ${data.message}`;
            messageBox.className = 'message success';
            urlInput.value = ''; // Clear the input field
        } else {
            messageBox.textContent = `❌ ${data.error || 'An error occurred'}`;
            messageBox.className = 'message error';
        }

    } catch (error) {
        messageBox.textContent = '❌ Failed to connect to the server.';
        messageBox.className = 'message error';
    } finally {
        // Revert UI to default state
        btn.disabled = false;
        btnText.textContent = 'Download Video';
        spinner.style.display = 'none';
    }
});