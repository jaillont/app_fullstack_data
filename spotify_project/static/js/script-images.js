const images = document.querySelectorAll(".select-image");
const selected_image = document.forms["images-form"].elements.id_images

let label = ""

images.forEach((a) => {
    a.addEventListener("click", () => {
        label = ""
        if (a.classList.contains('active')){
            a.classList.remove('active');
        }
        else {
            a.classList.add('active');
        }
        images.forEach((a) => {
            if (a.classList.contains('active')){
                label += a.getAttribute("label") + " ";
            }
        });
        
        selected_image.value = label;
    });
});