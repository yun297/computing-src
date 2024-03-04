const generate_button = document.getElementbyId("generate-button");
const generate_icon = document.getElementbyId("generate-icon");
function generate() {
    alert("button clicked")
}

document.getElementById('slay').onclick = function generate() {
    alert("button clicked")
}

generate_button.addEventListener("click", ()=>{
   alert("button is clicked");
})

generate_icon.addEventListener("click", ()=>{
    alert("button is clicked");
 })