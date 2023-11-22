let btnGetAll = document .querySelector('#btn-get-all'),
    btnGetSale = document.querySelector('#btn-get-sale'),
    btnGetRent = document.querySelector("#btn-get-rent"); 

// Set background for the clicked button 

let removeBg = function () { 
    document.querySelectorAll('.wrpper__heading .item').forEach((btn) => {
        btn.classList.remove("clicked"); 
    }
)}

document.querySelectorAll('.wrpper__heading .item').forEach((btn) => {
    btn.addEventListener('click', () => {
        removeBg() 
        btn.classList.add('clicked'); 
    })
})

btnGetSale.addEventListener('click', () => {
    document.querySelector("#all").style.display = 'none'
    document.querySelector("#rent").style.display = 'none'
    document.querySelector("#sale").style.display = 'block'
})

btnGetAll.addEventListener('click', () => {
    document.querySelector("#all").style.display = 'block'
    document.querySelector("#rent").style.display = 'none'
    document.querySelector("#sale").style.display = 'none'
})

btnGetRent.addEventListener('click', () => {
    document.querySelector("#all").style.display = 'none'
    document.querySelector("#rent").style.display = 'block'
    document.querySelector("#sale").style.display = 'none'
})