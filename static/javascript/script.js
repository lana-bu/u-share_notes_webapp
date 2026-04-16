if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready() {
    const menuButton = document.getElementById('menu-btn');
    const searchToggleButton = document.getElementById('search-toggle-btn');
    const clearSearchButton = document.getElementById('clear-search');

    menuButton.addEventListener('click', toggleSidebar);
    searchToggleButton.addEventListener('click', toggleSearch);
    clearSearchButton.addEventListener('click', clearSearch);

}

function toggleSidebar() {
    const sidebar = document.getElementById("nav-sidebar");

    if (sidebar.style.display == "block") {
        sidebar.style.display = "none";
    } else {
        sidebar.style.display = "block";
    }
}

function toggleSearch(event) {
    const buttonClicked = event.target;
    const searchForm = document.getElementById('search');

    if (searchForm.style.display == "block") {
        buttonClicked.innerText = "Expand Search ˅";
        searchForm.style.display = "none";
    } else {
        buttonClicked.innerText = "Collapse Search ˄";
        searchForm.style.display = "block";
    }
}

function clearSearch() {
    const searchInputs = document.getElementsByClassName("search-input");

    for (const input of searchInputs) {
        input.value = "";
    }
}