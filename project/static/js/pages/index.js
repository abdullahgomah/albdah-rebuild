let propertyTypeBtns = document.querySelectorAll('.swiper-slide .btn') 
let allProperties = document.querySelectorAll('.item.property') 


propertyTypeBtns.forEach((btn) => {
    // console.log(btn.dataset.property_type)
    btn.addEventListener('click', () => {
        allProperties.forEach((ad) => {
            ad.style.display = 'flex';
        })
        allProperties.forEach((property) => {
            if (property.querySelector('[name="property_type_input"]').value != btn.dataset.property_type) {
                property.style.display = 'none';
            }
        })
    })
})