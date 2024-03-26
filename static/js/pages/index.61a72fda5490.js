let propertyTypeBtns = document.querySelectorAll('.swiper-slide .btn') 
let allProperties = document.querySelectorAll('.item.property') 


propertyTypeBtns.forEach((btn) => {
    // console.log(btn.dataset.property_type)
    btn.addEventListener('click', () => {
        if (btn.dataset.property_type == 'all') {
            allProperties.forEach((ad) => {
                ad.style.display = 'flex';
            })
        } else {

            
            allProperties.forEach((ad) => {
                ad.style.display = 'flex';
            })
            allProperties.forEach((property) => {
                if (property.querySelector('[name="property_type_input"]').value != btn.dataset.property_type) {
                    property.style.display = 'none';
                } 
            })
        }
    })
})


let propertyCoverImg = document.querySelectorAll('.property__cover_img img'); 

propertyCoverImg.forEach((img) => {
    if (img.src == window.location.href) {
        img.src = img.parentElement.parentElement.querySelector("[name=propertyFirstImgUrl]").value
    }
})



let allSwiperSlide = document.querySelectorAll('.swiper-slide') 
allSwiperSlide.forEach((btn) => {
    btn.addEventListener('click', () => {
        allSwiperSlide.forEach((b) => b.classList.remove('fill')) 
        btn.classList.add('fill') 
    })
})