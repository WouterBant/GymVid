// This script makes it possible to toggle between light-mode and dark-mode

var icon = document.getElementById("icon");

// Changes the icon and theme when clicked on the symbol
icon.onclick = function()
{
    document.body.classList.toggle("dark-theme");

    if (document.body.classList.contains("dark-theme"))
    {
        localStorage.setItem('dark-theme', "no");
        icon.src = moon;
    }
    else
    {
        localStorage.setItem('dark-theme', "yes");
        icon.src = sun;
    }
}

// On load check if the user selected light-mode, if so switch theme (default is dark)
function load1()
{
    if (localStorage.getItem('dark-theme'))
    {
        const no_toggle_needed = localStorage.getItem('dark-theme');
        if (no_toggle_needed == "no")
        {
            document.body.classList.toggle("dark-theme");
            icon.src = moon;
        }
    }
}