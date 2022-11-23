const home_button = document.getElementById("home-button");
const home_content = document.getElementById("home");

const playlist_button = document.getElementById("playlist-button");
const playlist_content = document.getElementById("playlist");

const services_button = document.getElementById("services-button");
const services_content = document.getElementById("services");

const account_button = document.getElementById("account-button");
const account_content = document.getElementById("account");

const contact_button = document.getElementById("contact-button");
const contact_content = document.getElementById("contact");

const contact_button_2 = document.getElementById("contact-button-2");


/* Home actions */

home_button.addEventListener("click", () => {
    displayHomeContent();
    updateSidebarHome();
});

function displayHomeContent() {
    home_content.classList.remove("hidden");
    if (!playlist_content.classList.contains("hidden")){
        playlist_content.classList.add("hidden");
    };
    if (!services_content.classList.contains("hidden")){
        services_content.classList.add("hidden");
    };
    if (!account_content.classList.contains("hidden")){
        account_content.classList.add("hidden");
    };
    if (!contact_content.classList.contains("hidden")){
        contact_content.classList.add("hidden");
    };
}

function updateSidebarHome() {
    home_button.classList.add("active");
    console.log(home_button.classList);
    if (playlist_button.classList.contains("active")){
        playlist_button.classList.remove("active");
    };
    if (services_button.classList.contains("active")){
        services_button.classList.remove("active");
    };
    if (account_button.classList.contains("active")){
        account_button.classList.remove("active");
    };
    if (contact_button.classList.contains("active")){
        contact_button.classList.remove("active");
    };
    console.log(playlist_button.classList);
}

/* Playlist actions */

playlist_button.addEventListener("click", () => {
    displayPlaylistContent();
    updateSidebarPlaylist();
});

function displayPlaylistContent() {
    playlist_content.classList.remove("hidden");
    if (!home_content.classList.contains("hidden")){
        home_content.classList.add("hidden");
    };
    if (!services_content.classList.contains("hidden")){
        services_content.classList.add("hidden");
    };
    if (!account_content.classList.contains("hidden")){
        account_content.classList.add("hidden");
    };
    if (!contact_content.classList.contains("hidden")){
        contact_content.classList.add("hidden");
    };
}

function updateSidebarPlaylist() {
    playlist_button.classList.add("active");
    if (home_button.classList.contains("active")){
        home_button.classList.remove("active");
    };
    if (services_button.classList.contains("active")){
        services_button.classList.remove("active");
    };
    if (account_button.classList.contains("active")){
        account_button.classList.remove("active");
    };
    if (contact_button.classList.contains("active")){
        contact_button.classList.remove("active");
    };
}

/* Services actions */

services_button.addEventListener("click", () => {
    displayServicesContent();
    updateSidebarServices();
});

function displayServicesContent() {
    services_content.classList.remove("hidden");
    if (!home_content.classList.contains("hidden")){
        home_content.classList.add("hidden");
    };
    if (!playlist_content.classList.contains("hidden")){
        playlist_content.classList.add("hidden");
    };
    if (!account_content.classList.contains("hidden")){
        account_content.classList.add("hidden");
    };
    if (!contact_content.classList.contains("hidden")){
        contact_content.classList.add("hidden");
    };
}

function updateSidebarServices() {
    services_button.classList.add("active");
    if (home_button.classList.contains("active")){
        home_button.classList.remove("active");
    };
    if (playlist_button.classList.contains("active")){
        playlist_button.classList.remove("active");
    };
    if (account_button.classList.contains("active")){
        account_button.classList.remove("active");
    };
    if (contact_button.classList.contains("active")){
        contact_button.classList.remove("active");
    };
}

/* Account actions */

account_button.addEventListener("click", () => {
    displayAccountContent();
    updateSidebarAccount();
});

function displayAccountContent() {
    account_content.classList.remove("hidden");
    if (!home_content.classList.contains("hidden")){
        home_content.classList.add("hidden");
    };
    if (!playlist_content.classList.contains("hidden")){
        playlist_content.classList.add("hidden");
    };
    if (!services_content.classList.contains("hidden")){
        services_content.classList.add("hidden");
    };
    if (!contact_content.classList.contains("hidden")){
        contact_content.classList.add("hidden");
    };
}

function updateSidebarAccount() {
    account_button.classList.add("active");
    if (home_button.classList.contains("active")){
        home_button.classList.remove("active");
    };
    if (playlist_button.classList.contains("active")){
        playlist_button.classList.remove("active");
    };
    if (services_button.classList.contains("active")){
        services_button.classList.remove("active");
    };
    if (contact_button.classList.contains("active")){
        contact_button.classList.remove("active");
    };
}

/* Contact actions */

contact_button.addEventListener("click", () => {
    displayContactContent();
    updateSidebarContact();
});

function displayContactContent() {
    contact_content.classList.remove("hidden");
    if (!home_content.classList.contains("hidden")){
        home_content.classList.add("hidden");
    };
    if (!playlist_content.classList.contains("hidden")){
        playlist_content.classList.add("hidden");
    };
    if (!services_content.classList.contains("hidden")){
        services_content.classList.add("hidden");
    };
    if (!account_content.classList.contains("hidden")){
        account_content.classList.add("hidden");
    };
}

function updateSidebarContact() {
    contact_button.classList.add("active");
    if (home_button.classList.contains("active")){
        home_button.classList.remove("active");
    };
    if (playlist_button.classList.contains("active")){
        playlist_button.classList.remove("active");
    };
    if (services_button.classList.contains("active")){
        services_button.classList.remove("active");
    };
    if (account_button.classList.contains("active")){
        account_button.classList.remove("active");
    };
}

/* Contact actions 2 */

contact_button_2.addEventListener("click", () => {
    displayContactContent();
    updateSidebarContact();
});




/* Typing animation */

var typed = new Typed(".typing", {
    strings: ["", "right choice", "BEST choice"],
    typeSpeed: 100,
    backSpeed: 60,
    loop: true
});