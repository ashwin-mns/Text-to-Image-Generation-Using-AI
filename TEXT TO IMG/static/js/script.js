document.addEventListener('DOMContentLoaded', () => {
    // Elements
    const generateBtn = document.getElementById('generateBtn');
    const promptInput = document.getElementById('promptInput');
    const resultArea = document.getElementById('resultArea');
    const placeholder = document.querySelector('.placeholder-content');
    const loader = document.getElementById('loader');
    const generatedImage = document.getElementById('generatedImage');
    const errorMsg = document.getElementById('errorMsg');
    const downloadBtn = document.getElementById('downloadBtn');
    const imageActions = document.getElementById('imageActions');

    // Settings Elements
    const toggleSettingsBtn = document.getElementById('toggleSettingsBtn');
    const settingsPanel = document.getElementById('settingsPanel');
    const widthInput = document.getElementById('widthInput');
    const heightInput = document.getElementById('heightInput');
    const seedInput = document.getElementById('seedInput');
    const widthValue = document.getElementById('widthValue');
    const heightValue = document.getElementById('heightValue');

    // History Elements
    const historyGrid = document.getElementById('historyGrid');
    const clearHistoryBtn = document.getElementById('clearHistoryBtn');

    // State
    const MAX_HISTORY = 10;

    // --- Initialization ---
    loadHistory();

    // --- Event Listeners ---

    // Toggle Settings
    toggleSettingsBtn.addEventListener('click', () => {
        settingsPanel.classList.toggle('hidden');
    });

    // Update Range Values
    widthInput.addEventListener('input', (e) => widthValue.textContent = e.target.value);
    heightInput.addEventListener('input', (e) => heightValue.textContent = e.target.value);

    // Clear History
    clearHistoryBtn.addEventListener('click', () => {
        if (confirm('Clear all history?')) {
            localStorage.removeItem('imageHistory');
            loadHistory();
        }
    });

    // Generate Button
    generateBtn.addEventListener('click', generateImage);

    // Enter Key
    promptInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') generateBtn.click();
    });

    // --- Functions ---

    async function generateImage() {
        const prompt = promptInput.value.trim();
        if (!prompt) {
            showError("Please enter a prompt!");
            return;
        }

        // Reset UI
        setLoading(true);
        errorMsg.classList.add('hidden');
        imageActions.classList.add('hidden');

        // Gather Params
        const payload = {
            prompt: prompt,
            width: parseInt(widthInput.value),
            height: parseInt(heightInput.value),
            seed: seedInput.value ? parseInt(seedInput.value) : null
        };

        try {
            console.log("Sending:", payload);
            const response = await fetch('/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload),
            });

            const data = await response.json();

            if (response.ok) {
                // Success
                const imgUrl = data.image;
                generatedImage.src = imgUrl;
                generatedImage.classList.remove('hidden');
                placeholder.classList.add('hidden');

                // Show actions
                imageActions.classList.remove('hidden');
                downloadBtn.href = imgUrl;

                // Save to history
                saveToHistory(prompt, imgUrl);
            } else {
                throw new Error(data.error || 'Failed to generate image');
            }
        } catch (error) {
            console.error(error);
            showError(error.message);
        } finally {
            setLoading(false);
        }
    }

    function setLoading(isLoading) {
        if (isLoading) {
            generateBtn.disabled = true;
            generateBtn.style.opacity = '0.7';
            loader.classList.remove('hidden');
            generatedImage.classList.add('hidden');
            placeholder.classList.add('hidden');
        } else {
            generateBtn.disabled = false;
            generateBtn.style.opacity = '1';
            loader.classList.add('hidden');
        }
    }

    function showError(msg) {
        errorMsg.textContent = msg;
        errorMsg.classList.remove('hidden');
    }

    // --- History Logic ---
    function saveToHistory(prompt, imgData) {
        let history = JSON.parse(localStorage.getItem('imageHistory') || '[]');

        const newItem = {
            id: Date.now(),
            prompt: prompt,
            image: imgData,
            date: new Date().toLocaleTimeString()
        };

        // Add to front, slice to max
        history.unshift(newItem);
        if (history.length > MAX_HISTORY) history.pop();

        localStorage.setItem('imageHistory', JSON.stringify(history));
        loadHistory();
    }

    function loadHistory() {
        const history = JSON.parse(localStorage.getItem('imageHistory') || '[]');
        historyGrid.innerHTML = '';

        if (history.length === 0) {
            historyGrid.innerHTML = '<div class="empty-history">No images yet</div>';
            return;
        }

        history.forEach(item => {
            const div = document.createElement('div');
            div.className = 'history-item';
            div.title = item.prompt;

            const img = document.createElement('img');
            img.src = item.image;
            img.loading = 'lazy';

            div.appendChild(img);

            // Allow clicking history to view content
            div.addEventListener('click', () => {
                generatedImage.src = item.image;
                generatedImage.classList.remove('hidden');
                placeholder.classList.add('hidden');
                downloadBtn.href = item.image;
                imageActions.classList.remove('hidden');
                promptInput.value = item.prompt;
            });

            historyGrid.appendChild(div);
        });
    }
});
