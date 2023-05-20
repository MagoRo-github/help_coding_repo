
// funzione per espendere e nascondere il menu hambirger 
function hamburger() {
    let hamb = document.querySelector('#hamburger')
    let nav_hamb = document.querySelector('#nav_hamb')
    hamb.addEventListener("click", (e)=>{
        e.stopImmediatePropagation();
        e.preventDefault();
        nav_hamb.classList.toggle('hidden')   
    })
}
