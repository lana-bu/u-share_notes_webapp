if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready() {
    const menuButton = document.getElementById('menu-btn');
    menuButton.addEventListener('click', () => toggleSidebar());
}

function toggleSidebar() {
    const sidebar = document.getElementById("nav-sidebar");

    if (sidebar.style.display == "block") {
        sidebar.style.display = "none";
    } else {
        sidebar.style.display = "block";
    }
}