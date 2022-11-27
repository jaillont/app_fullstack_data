/* Typing animation */

var typed = new Typed(".typing", {
    strings: ["", "right choice", "BEST choice"],
    typeSpeed: 100,
    backSpeed: 60,
    loop: true
});


/* Navigation */

const nav = document.querySelector(".nav");
const navList = nav.querySelectorAll("li");
const totalNavList = navList.length;

const allSection = document.querySelectorAll(".section");
const totalSection = allSection.length;

for (let i=0; i < totalNavList; i++){
    const a = navList[i].querySelector("a");
    a.addEventListener("click", function() {
        for (let j=0; j < totalNavList; j++){
            navList[j].querySelector("a").classList.remove("active");
        }
        this.classList.add("active");
        showSection(this);
    });
}

function showSection(element) {
    const target = element.getAttribute("href").split("#")[1];
    for (let i=0; i < totalSection; i++){
        if(allSection[i].classList.contains("active")){
            allSection[i].classList.remove("active");
        }
    }
    document.querySelector("#" + target).classList.add("active");
}

/* New Playlist */

const button_new_playlist = document.getElementById("button-new-playlist");
const new_playlist_section = document.getElementById("new-playlist");

button_new_playlist.addEventListener("click", () => {
    for (let i=0; i < totalSection; i++){
        if(allSection[i].classList.contains("active")){
            allSection[i].classList.remove("active");
        }
    }
    new_playlist_section.classList.add("active");
});


const cover_images = document.querySelectorAll(".select-image");
const selected_image = document.forms["playlist-form"].elements.id_image

cover_images.forEach((a) => {
    a.addEventListener("click", () => {
        cover_images.forEach((a) => {
            a.classList.remove('active');
        });
        a.classList.add('active');
        /* Ecrire le label dans le champs form */
        let label = a.getAttribute("label");
        // selected_image.value = label

        selected_image.value = label
        
        console.log(selected_image.value)
    });
});

/* New image */

const button_new_image = document.getElementById("button-new-image");
const new_image_section = document.getElementById("new-image");

button_new_image.addEventListener("click", () => {
    for (let i=0; i < totalSection; i++){
        if(allSection[i].classList.contains("active")){
            allSection[i].classList.remove("active");
        }
    }
    new_image_section.classList.add("active");
});