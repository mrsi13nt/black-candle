function openPopup(imageUrl) {
    document.getElementById('popup-image').src = imageUrl;
    document.getElementById('popup').style.display = 'block';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
}


const darkModeBtn = document.getElementById('dark-mode-btn');
let isDarkMode = false; // Initial state

darkModeBtn.addEventListener('click', () => {
    isDarkMode = !isDarkMode; // Toggle dark mode state
    updateDarkMode();
});

function updateDarkMode() {
    if (isDarkMode) {
        document.body.classList.add('dark-mode');
        darkModeBtn.textContent = 'Light Mode';
    } else {
        document.body.classList.remove('dark-mode');
        darkModeBtn.textContent = 'Dark Mode';
    }
}
