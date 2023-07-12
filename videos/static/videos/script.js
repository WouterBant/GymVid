var icon = document.getElementById("icon");

// Changes the icon and theme when clicked on the symbol
icon.onclick = function() {
  document.body.classList.toggle("dark-theme");
  
  if (document.body.classList.contains("dark-theme")) {
    localStorage.setItem('dark-theme', "yes");
    icon.src = moon;
  } else {
    localStorage.setItem('dark-theme', "no");
    icon.src = sun;
  }
}

// On load, check if the user selected a mode, if not, use the default mode
function loadTheme() {
  var userPreference = localStorage.getItem('dark-theme');
  
  if (userPreference === null) {
    var prefersDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;
    userPreference = prefersDarkMode ? "yes" : "no";
    localStorage.setItem('dark-theme', userPreference);
  }
  
  if (userPreference === "yes") {
    document.body.classList.add("dark-theme");
    icon.src = moon;
  }
}

// Call the loadTheme function when the page finishes loading
window.addEventListener('load', loadTheme);
