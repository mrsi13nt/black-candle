// popup images

function openPopup(imageUrl) {
    document.getElementById('popup-image').src = imageUrl;
    document.getElementById('popup').style.display = 'block';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
}


// dark mode

function colors(check){
    const head_text = document.getElementById('main-head')
    const table = document.getElementById('options-contain')
    const sql = document.getElementById('sql')
    const xss = document.getElementById('xss')
    const hh = document.getElementById('hh')
    const js = document.getElementById('js')
    const footer = document.getElementById('foot') 
    if (check == true){
        head_text.style.color = "white"
        table.style.backgroundColor = "#4b4a4a"
        sql.style.backgroundColor = "#4b4a4a"
        xss.style.backgroundColor = "#4b4a4a"
        hh.style.backgroundColor = "#4b4a4a"
        js.style.backgroundColor = "#4b4a4a"
        footer.style.backgroundColor = "#383737"
    }else{
        head_text.style.color = "black"
        table.style.backgroundColor = "#ffffff"
        sql.style.backgroundColor = "#ffffff"
        xss.style.backgroundColor = "#ffffff"
        hh.style.backgroundColor = "#ffffff"
        js.style.backgroundColor = "#ffffff"
        footer.style.backgroundColor = "#bdb9b9"
    }
    
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
        colors(true);
    } else {
        document.body.classList.remove('dark-mode');
        darkModeBtn.textContent = 'Dark Mode';
        colors(false)
    }
}


// scroll up icon
