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
    const install = document.getElementById('installing')
    const text1 = document.getElementById('text1')
    const text2 = document.getElementById('text2')
    const text3 = document.getElementById('text3')
    const text4 = document.getElementById('text4')
    const text5 = document.getElementById('text5')
    if (check == true){
        head_text.style.color = "white"
        table.style.backgroundColor = "#4b4a4a"
        sql.style.backgroundColor = "#4b4a4a"
        xss.style.backgroundColor = "#4b4a4a"
        hh.style.backgroundColor = "#4b4a4a"
        js.style.backgroundColor = "#4b4a4a"
        footer.style.backgroundColor = "#383737"
        install.style.backgroundColor = "#4b4a4a"
        text1.style.color = "white"
        text2.style.color = "white"
        text3.style.color = "white"
        text4.style.color = "white"
        text5.style.color = "white"
        
    }else{
        head_text.style.color = "black"
        table.style.backgroundColor = "#ffffff"
        sql.style.backgroundColor = "#ffffff"
        xss.style.backgroundColor = "#ffffff"
        hh.style.backgroundColor = "#ffffff"
        js.style.backgroundColor = "#ffffff"
        footer.style.backgroundColor = "#bdb9b9"
        install.style.backgroundColor = "#ffffff"
        text1.style.color = "black"
        text2.style.color = "black"
        text3.style.color = "black"
        text4.style.color = "black"
        text5.style.color = "black"
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


// Scroll to top button appear
