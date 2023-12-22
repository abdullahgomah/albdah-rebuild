let sliderInputs = document.querySelectorAll('.slider_input'); 
let streetWidthSliderValueInput = document.querySelector("[name=street-width-input]")
let grid = document.querySelectorAll('.grid'); 
let markterTypeGrid =document.querySelector('#markter-type-grid'); 
let subItems =markterTypeGrid.querySelectorAll('.sub-item'); 
let propertyInfoSection = document.querySelector('.property__info'); 
let propertyDetailsSection = document.querySelector('.property__details'); 
let propertyImgs = document.querySelector('.property__imgs');
let propertyLocation = document.querySelector('.property__location'); 
let propertyLocationNextPrev = document.querySelector('.property__location__next-prev'); 
let propertyFeatures = document.querySelector('.property__features'); 
let propertyFeaturesNextPrev = document.querySelector('.property__features__next-prev'); 
let rentTypeInput = document.querySelector("[name=rent_type_input]"); 
let advertiser_relation = document.querySelector('[name=advertiser_relation]'); 
let exclusiveInput = document.querySelector("[name=exclusive]"); 
let propertyImgsNextPrev = document.querySelector('.property__imgs__next-prev'); 
let overlayLayer = document.querySelector('.overlay-layer'); 
let noImgsPopup = document.querySelector('.on-imgs-popup');
let noImgsPopupYesBtn = document.querySelector('#no-imgs-popup-yes-btn'); 
let noImgsPopupNoBtn = document.querySelector('#no-imgs-popup-no-btn'); 
let imagesFileInput = document.querySelector('[name=property__imgs]'); 
let previewImgsContainer = document.querySelector('.preview_imgs_container'); 
let videoFileInput = document.querySelector('[name=property__video]'); 
let previewVideoContainer = document.querySelector('.preview_video_container'); 
let extraRoomInput = document.querySelector('[name=extra-room-input]'); 

let extraLoungesInput = document.querySelector('[name=extra-lounges-input]')

let extraBathroomInput = document.querySelector('[name=extra-bathroom-input]') 

let extraFloorInput = document.querySelector('[name=extra-floor-input]') 

let extraPropertyAgeInput = document.querySelector('[name=extra-property-age-input]') 


sliderInputs.forEach((input) => {
    input.addEventListener('input', () => {
        input.parentElement.parentElement.querySelector('.value').querySelector('span').textContent = input.value ;
        if (input.parentElement.parentElement.querySelector('[name=street-width-input]')) {
            streetWidthSliderValueInput.value = input.value; 
        } else if (input.parentElement.parentElement.querySelector('[name=stores-count-input]')) {
            document.querySelector('[name=stores-count-input]').value = input.value
        }
    })
})

subItems.forEach((item) => {
    item.addEventListener('click', () => {
        subItems.forEach((x) => {
            x.classList.remove('fill') 
        })
        item.classList.add('fill') 
    })
})

grid.forEach((grid_item) => {
    grid_item.querySelectorAll('.item').forEach((item) => {
        item.addEventListener('click', () => {
            if (item.textContent == 'مسوق') {
                document.querySelector('#markter-type-grid').style.display = 'flex'; 
            } else { 
                document.querySelector('#markter-type-grid').style.display = 'none'; 
            }
            grid_item.querySelectorAll('.item').forEach((item) => {
                // item.style.background = '#eee' 
                // item.style.color = '#1e2957'
                // this is reset code 
                item.classList.remove('filled'); 
            })

            // item.style.background = "#1e2957"; 
            // item.style.color = '#ffffff'
            item.classList.add('filled') 
        })
    })
})

let advertiser_relation_grid = document.querySelector('#advertiser_relation_grid') 
advertiser_relation_grid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        advertiser_relation.value = item.textContent;  
        // console.log(advertiser_relation.value)
    })
})


markterTypeGrid.querySelectorAll('.sub-item').forEach((item) => {
    item.addEventListener('click', () => {
        if (item.textContent == "حصري") { 
            exclusiveInput.value = 1 
        } else { 
            exclusiveInput.value = 0 
        }
    })
 
})


let timelineItemsWrapper = document.querySelector(".timeline-items-wrapper")
// let progressBarInk = document.querySelector('.timeline-progressbar-ink') 

let fillProgress = function (item) { 
    let space = timelineItemsWrapper.getBoundingClientRect().right - item.getBoundingClientRect().right 
    let nestedSpace = item.getBoundingClientRect().right - item.querySelector('.status-circle').getBoundingClientRect().right; 

    progressBarInk.style.width = space + nestedSpace + 10 + "px"; 
    
}

let interfaceOptions = document.querySelectorAll('.interface-field a.btn'); 
let interfaceInput = document.querySelector('[name=interface-input]'); 


interfaceOptions.forEach((btn) => {
    btn.addEventListener('click', () => {
        interfaceOptions.forEach((item) => {
            item.classList.remove("btn-solid") 
            item.classList.add('btn-outline')
        })
        btn.classList.remove('btn-outline')
        btn.classList.add('btn-solid')
        interfaceInput.value = btn.textContent; 
        
    })
})


let propertyInfoNextPrev = document.querySelector('.property__info__next-prev'); 
propertyInfoNextPrev.querySelector('.btn-next').addEventListener('click', () => {

    let limit = 4; 
    console.log(document.querySelector('[name=property_type]'));
    
    if (document.querySelector("[name=property_type]").value == 'land_rent') {
        limit = 7; 



    }

    // check form validation 
    let inputs = propertyInfoSection.querySelectorAll('.input') 
    let inputsLen = inputs.length; 
    let counter = 0; 

    inputs.forEach((input) => {
        let inputElement = input.querySelector("input") 
        if (inputElement.value == "") {
            inputElement.style.border = "1px solid #dc3546"
            // console.log("نص فارغ")
        } else {
            counter = counter + 1; 
            inputElement.style.border = "1px solid #00000040"
            // console.log(counter) 
            // console.log(inputElement.value); 
        }

        // console.log(counter) 
    })



    if (rentTypeInput.textContent == "" ) {
        rentTypeInput.parentElement.style.border= "1px solid #dc3546"; 
    } else { 
        counter += 1; 
        rentTypeInput.parentElement.style.border = "1px solid #00000040"
    }

    if (advertiser_relation.value == "") { 
        advertiser_relation_grid.style.border = '1px solid #dc3546'; 
    } else { 
        advertiser_relation_grid.style.border = '1px solid #00000040'; 
        counter +=1; 
    }


    




    if (counter == limit) { 
        propertyInfoSection.style.display = 'none' ; 
        propertyImgs.style.display = 'flex'; 
        let completedTimelineElement = document.querySelector('.timeline-item:first-child'); 
        completedTimelineElement.classList.remove('current')
        completedTimelineElement.classList.add('completed'); 
        
        let nextTimelineElement =  completedTimelineElement.nextElementSibling; 
        nextTimelineElement.classList.add('current') ;

        fillProgress(nextTimelineElement)


        
    }


    

}) 


// Handle Images Uploader
imagesFileInput.addEventListener('change', () => {
    
    // Remove All Images
    previewImgsContainer.innerHTML = ''; 

    const files = imagesFileInput.files; 

    const selectedFiles = Array.from(files);

    console.log(selectedFiles); 

    for (let i =0; i < files.length; i++ ) {
        
        // Get the File 
        const file = files[i]; 

        // Create New Image Container 
        const imageContainer = document.createElement('div'); 
        imageContainer.classList.add('image-container'); 
        
        // image container header 
        const imageContainerHeader = document.createElement('div'); 
        imageContainerHeader.classList.add('image-container-header'); 

        // hidden input element 
        let mainHiddenInput = document.createElement('input');
        mainHiddenInput.type = 'hidden'; 
        mainHiddenInput.name = 'mainImage';

        // create 'x' button 
        const delButton = document.createElement('div'); 
        delButton.classList.add('del-btn'); 
        delButton.innerHTML = '<i class="fa-solid fa-x"></i>'; 


        // Create "Main Image" button 
        let makeMainButton = document.createElement('button'); 
        makeMainButton.type = 'button'; 
        makeMainButton.classList.add('make-main-btn') ; 
        makeMainButton.textContent = "تعيين كصورة رئيسية" 


        delButton.addEventListener('click', () => {
            // Remove Image Container From Preview Images Container
            previewImgsContainer.removeChild(imageContainer); 

            // Remove The Image From File List to Set new file list 
            // Remove the corresponding file from the selectedFiles array
            const index = selectedFiles.indexOf(file);
            if (index > -1) {
                selectedFiles.splice(index, 1);
            }

            // Update the file input's files property with the modified selectedFiles array
            const remainingFileList = new DataTransfer() ; 
            selectedFiles.forEach((file) => {
                remainingFileList.items.add(file); 
            }) 

            imagesFileInput.files = remainingFileList.files

            // console.log(imagesFileInput.files); 
        })

        imageContainerHeader.appendChild(delButton); 
        imageContainerHeader.appendChild(makeMainButton); 
        imageContainerHeader.appendChild(mainHiddenInput); 
        
        //  Create New Image Element 
        const image = document.createElement('img')
        image.classList.add('preview_img'); 


        imageContainer.appendChild(imageContainerHeader)
        imageContainer.appendChild(image)

        // Read The URL of Image 
        const reader = new FileReader(); 
        reader.onload = function () {
            image.src = reader.result 
        }
        reader.readAsDataURL(file) 

        // Add Image To Container
        previewImgsContainer.appendChild(imageContainer); 

        document.querySelectorAll('.image-container-header').forEach((img_header_container) => {
            img_header_container.querySelector('.make-main-btn').addEventListener('click', () => {
                document.querySelectorAll('.make-main-btn').forEach((btn) => { 
                    btn.classList.remove('clicked') 
                    btn.parentElement.querySelector('[name=mainImage]').value = 0;
                    // console.log(btn.parentElement.querySelector('[name=mainImage]')) ; 
                    
                })

                img_header_container.querySelector('.make-main-btn').classList.add('clicked') 
                img_header_container.querySelector('.make-main-btn').parentElement.querySelector('[name=mainImage]').value = 1; 

            })
        })
        
    }

}) ; 




// Handle Video Uploader 
videoFileInput.addEventListener('change', () => {
    // Reset the preview video container 
    previewVideoContainer.innerHTML = ""; 

    const file = videoFileInput.files[0]; 
    const reader = new FileReader() 
    reader.onload = () => {
        const video = document.createElement('video') 
        video.classList.add("preview_video"); 
        video.setAttribute('controls', "true") 
        video.src = reader.result; 
        previewVideoContainer.appendChild(video) ; 
    }

    reader.readAsDataURL(file)
})

propertyImgsNextPrev.querySelector('.btn-next').addEventListener('click', () => { 
    // GET FILE INPUT FOR PROPERTY IMAGES 
    let propertyImgsInput = document.querySelector('[name=property__imgs]'); 
    if (propertyImgsInput.files.length == 0 ) { 
        // SHOW CONFIRMATION POPUP 
        overlayLayer.style.display = 'block'; 
        noImgsPopup.style.display = 'block'; 

        
    } else { 
        // CONTINUE TO THE NEXT PAGE  
        propertyImgs.style.display = 'none'; 
        propertyLocation.style.display = 'block'; 

        let completedTimelineElement = document.querySelector('.timeline-item:nth-child(2)'); 
        completedTimelineElement.classList.remove('current')
        completedTimelineElement.classList.add('completed'); 
        
        let nextTimelineElement =  completedTimelineElement.nextElementSibling; 
        nextTimelineElement.classList.add('current') ;

        fillProgress(nextTimelineElement)

    }
})

noImgsPopupYesBtn.addEventListener('click', () => {
    propertyImgs.style.display = 'none'; 
    propertyLocation.style.display = 'block' ; 
    overlayLayer.style.display = 'none'; 
    noImgsPopup.style.display = 'none'; 

    let completedTimelineElement = document.querySelector('.timeline-item:nth-child(2)'); 
    completedTimelineElement.classList.remove('current')
    completedTimelineElement.classList.add('completed'); 
    
    let nextTimelineElement =  completedTimelineElement.nextElementSibling; 
    nextTimelineElement.classList.add('current') ;

    fillProgress(nextTimelineElement)

})

noImgsPopupNoBtn.addEventListener('click', () => {
    overlayLayer.style.display = 'none'; 
    noImgsPopup.style.display = 'none'; 
})



let propertyDetailsNextPrev = document.querySelector('.property__details__next-prev'); 
propertyDetailsNextPrev.querySelector('.btn-prev').addEventListener('click', () => {
    propertyDetailsSection.style.display = 'none' ;
    propertyLocation.style.display = 'block';
})



// propertyImgsNextPrev.querySelector('.btn-next').addEventListener('click', () => {
//     propertyImgs.style.display = 'none'; 
//     propertyLocation.style.display = 'block'
    
// })

propertyImgsNextPrev.querySelector('.btn-prev').addEventListener('click', () => {
    propertyImgs.style.display = 'none'; 
    propertyInfoSection.style.display = 'block'
    
})

propertyLocationNextPrev.querySelector('.btn-prev').addEventListener('click', () => {
    propertyLocation.style.display = 'none'; 
    propertyImgs.style.display = 'flex'
})

propertyLocationNextPrev.querySelector('.btn-next').addEventListener('click', () => {
    propertyLocation.style.display = 'none'; 
    propertyDetailsSection.style.display = 'block'

    let completedTimelineElement = document.querySelector('.timeline-item:nth-child(3)'); 
    completedTimelineElement.classList.remove('current')
    completedTimelineElement.classList.add('completed'); 
    
    let nextTimelineElement =  completedTimelineElement.nextElementSibling; 
    nextTimelineElement.classList.add('current') ;

    fillProgress(nextTimelineElement)

})


propertyFeaturesNextPrev.querySelector('.btn-prev').addEventListener('click', () => {
    propertyFeatures.style.display = 'none'; 
    propertyDetailsSection.style.display = 'block'
})


function disableButton() {
    // Disable the button

    document.getElementById("submitButton").disabled = true;

}


if (document.querySelector('[name=property_type]').value != 'land_rent' && document.querySelector('[name=property_type]').value != "building_rent" && document.querySelector('[name=property_type]').value != "shop_rent" && document.querySelector('[name=property_type]').value != 'commercial_office_rent' && document.querySelector('[name=property_type]').value != 'branch_rent') { 
    
    let roomCountGrid = document.querySelector('.room-count'); 
    roomCountGrid.querySelectorAll('.item').forEach((item) => {
        item.addEventListener('click', () => {
            if (item.classList.contains('item_more') == false) { 
                extraRoomInput.value = "أكثر" ;
            }
            item.parentElement.querySelector("[name=room-input]").value = item.textContent; 
            // console.log(item.parentElement.querySelector('[name=room-input]').value)
        })
    })




    let loungesCountGrid = document.querySelector('.lounges-count'); 
    loungesCountGrid.querySelectorAll('.item').forEach((item) => {
        item.addEventListener('click', () => {
            if (item.classList.contains('item_more') == false) {
                extraLoungesInput.value = 'أكثر';
            }
            item.parentElement.querySelector("[name=lounges-input]").value = item.textContent; 
            // console.log(item.parentElement.querySelector('[name=lounges-input]').value)
        })
    })


    let bathroomCountGrid = document.querySelector('.bathroom-count'); 
    bathroomCountGrid.querySelectorAll('.item').forEach((item) => {
        item.addEventListener('click', () => {
            if (item.classList.contains('item_more') == false) { 
                extraBathroomInput.value = 'أكثر'; 
            }
            item.parentElement.querySelector("[name=bathroom-input]").value = item.textContent; 
            // console.log(item.parentElement.querySelector('[name=bathroom-input]').value)
        })
    })


    if (document.querySelector('[name=property_type]').value != 'chalet_rent' && document.querySelector('[name=property_type]').value != 'villa_rent' && document.querySelector('[name=property_type]').value != 'resthouse_rent') {
        let floorNumberGrid = document.querySelector('.floor-number'); 
        floorNumberGrid.querySelectorAll('.item').forEach((item) => {
            item.addEventListener('click', () => {
                if (item.classList.contains('item_more') == false) { 
                    extraFloorInput.value = 'أكثر'; 
                }
                item.parentElement.querySelector("[name=floor-input]").value = item.textContent; 
                // console.log(item.parentElement.querySelector('[name=floor-input]').value)
            })
        })
    }







}


// let propertyAgeGrid = document.querySelector('.property-age'); 
// propertyAgeGrid.querySelectorAll('.item').forEach((item) => {
//     item.addEventListener('click', () => {
//         item.parentElement.querySelector("[name=property-age-input]").value = item.textContent; 
//         console.log(item);
//         // console.log(item.parentElement.querySelector('[name=property-age-input]').value)
//     })
// })


if (document.querySelector('[name=property_type]').value != 'land_rent') {
let propertyAgeGrid = document.querySelector('.property-age'); 
propertyAgeGrid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        item.parentElement.querySelector("[name=property-age-input]").value = item.textContent; 
        console.log(item)
        // console.log(item.parentElement.querySelector('[name=property-age-input]').value)
    })
})
}


if (document.querySelector('[name=property_type]').value == 'building_rent' || document.querySelector('[name=property_type]').value == 'villa_rent') { 
    let apartmentsCountGrid = document.querySelectorAll('.apartments-count .item'); 
    let apartmentsCountInput = document.querySelector('[name=apartments-count-input]'); 
    apartmentsCountGrid.forEach((item) => {
        item.addEventListener('click', () => {
            item.parentElement.querySelector('[name=apartments-count-input]').value = item.textContent; 
        })
    })


    if (document.querySelector('[name=property_type]').value != 'villa_rent') {

        let extraApartmentsCountInput = document.querySelector('[name=extra-apartments-count-input]'); 
        extraApartmentsCountInput.addEventListener('change', () => {
            apartmentsCountInput.value = "" // after that I will modify this in the views 
        })
        
    }


    let propertyAgeGrid = document.querySelector('.property-age'); 
    propertyAgeGrid.querySelectorAll('.item').forEach((item) => {
        item.addEventListener('click', () => {
            item.parentElement.querySelector("[name=property-age-input]").value = item.textContent; 
            console.log(item)
            // console.log(item.parentElement.querySelector('[name=property-age-input]').value)
        })
    })
}

let rentTypeGrid = document.querySelector('.rent-type') 
rentTypeGrid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        item.parentElement.querySelector('[name=rent_type_input]').textContent = item.getAttribute('data-value') 
        item.parentElement.querySelector('[name=rent_type_input]').value = item.getAttribute('data-value') 
    })
})


// handle the inputs in the property__details section 
let roomInput = document.querySelector('[name=room-input]'); 
let loungesInput = document.querySelector("[name=lounges-input]")
let bathroomInput = document.querySelector("[name=bathroom-input]")

if (document.querySelector("[name=property_type]").textContent != "chalet_rent" && document.querySelector("[name=property_type]").textContent != "villa_rent") {
    let floorInput = document.querySelector('[name=floor-input]'); 
} 



let propertyAgeInput = document.querySelector('[name=property-age-input]'); 


if (document.querySelector("[name=property_type]").value != "land_rent") { 


    if (document.querySelector("[name=property_type]").value != 'shop_rent' || document.querySelector('[name=property_type]').value != 'commercial_office_rent' || document.querySelector('[name=property_type]').value != 'branch_rent' ) {

        if (extraRoomInput !== null) { 
            extraRoomInput.addEventListener('change', () => { 
                // roomInput.value = "";
                roomInput.value = extraRoomInput.value;
                
            })
        }

    



        if (document.querySelector('[name=property_type]').value != 'building_rent') {


            if (extraLoungesInput !== null) { 
                extraLoungesInput.addEventListener('change', () => {
                    // loungesInput.value = ''; 
                    loungesInput.value = extraLoungesInput.value; 
                })
            }

            
            
            if (extraBathroomInput !== null ) { 
                extraBathroomInput.addEventListener('change', () => {
                    // bathroomInput.value = ''; 
                    bathroomInput.value = extraBathroomInput.value; 
                })
            }

        

        }
    }






    extraPropertyAgeInput.addEventListener('change', () => {
        // propertyAgeInput.value = ''; 
        propertyAgeInput.value = extraPropertyAgeInput.value; 
    })
}




propertyDetailsNextPrev.querySelector('.btn-next').addEventListener('click', () => {
    // check all these inputs

    let counter = 0 ; 
    let limit = 6; 

    if (document.querySelector('[name=property_type]').value == 'chalet_rent') { 
        limit = 5; 
        console.log(limit) ; 
    }

    if (document.querySelector('[name=property_type]').value == 'land_rent') { 
        limit = 3; 
        console.log(limit) ; 
    }

    if (document.querySelector('[name=property_type]').value == 'shop_rent') {
        limit = 3; 
    }

    if (document.querySelector('[name=property_type]').value == 'floor_rent') { 
        limit = 7; 
    }

    if (document.querySelector('[name=property_type]').value == 'resthouse_rent') { 
        limit = 5; 
    }

    if (document.querySelector('[name=property_type]').value == 'commercial_office_rent') { 
        limit = 3; 
    }

    if (document.querySelector('[name=property_type]').value == 'building_rent') { 
        limit = 7; 
    }

    if (document.querySelector('[name=property_type]').value == 'branch_rent') { 
        limit = 3; 
    }

    

    if (document.querySelector('[name=property_type]').value == "shop_rent" || document.querySelector('[name=property_type]').value == 'branch_rent' || document.querySelector('[name=property_type]').value == 'land_rent' || document.querySelector('[name=property_type]').value == 'building_rent' || document.querySelector('[name=property_type]').value == 'villa_rent' || document.querySelector('[name=property_type]').value == 'floor_rent' || document.querySelector('[name=property_type]').value == 'commercial_office_rent') { 
        if (interfaceInput.value == "") { 
            document.querySelector('.interface-field').style.border = "1px solid #dc3546" 
        } else { 
            document.querySelector('.interface-field').style.border = "none"; 
            counter +=1; 

            console.log(counter) 
        }
    }

    if (document.querySelector('[name=property_type]').value == "land_rent" || document.querySelector('[name=property_type]').value == 'building_rent') {
        let purposeInput = document.querySelector('[name=purpose-input]'); 
        if (purposeInput.value == "") { 
            purposeInput.style.border = "1px solid #dc3546" 
        } else { 
            purposeInput.parentElement.style.border = '1px solid #1e295750'; 
            counter +=1; 
            console.log("purpose")
            console.log(counter) 
            console.log("=====")  
        }

        if (document.querySelector("[name=property_type]").value == 'building_rent') {
            if (document.querySelector('[name=stores-count-input]').value == "") { 
                document.querySelector('[name=stores-count-input]').parentElement.style.border = "1px solid #dc3546" 
            } else { 
                document.querySelector('[name=stores-count-input]').style.border = "none"; 
                counter +=1; 
                console.log('stores count') 
                console.log(counter) ; 
                console.log("=====") ;
            }

            let apartmentsCountInput = document.querySelector('[name=apartments-count-input]'); 
            let extraApartmentsCountInput = document.querySelector('[name=extra-apartments-count-input]');

            if (apartmentsCountInput.value != "" || extraApartmentsCountInput.value != '') { 
                // not empty condition 
                document.querySelector('.grid.apartments-count').style.border = '1px solid #1e295750'; 
                counter +=1; 
                console.log("apartments count") 
                console.log(counter) 
                console.log("======") 
            } else { 
                // empty condition 
                document.querySelector('.grid.apartments-count').style.border = " 1px solid #dc3546"; 
            }
        }

    }

    // check purpose input, move interface validation functions from propertyInfo to propertyDetails

    if (document.querySelector('[name=property_type]').value != 'land_rent' && document.querySelector('[name=property_type]').value != 'building_rent' && document.querySelector('[name=property_type]').value != 'shop_rent' && document.querySelector('[name=property_type]').value != 'commercial_office_rent' && document.querySelector('[name=property_type]').value != 'branch_rent') {
        if (document.querySelector("[name=property_type]").value != 'building_rent') {
            if (document.querySelector('[name=property_type]').value != 'villa_rent' && document.querySelector('[name=property_type]').value != 'resthouse_rent') {
                let floorInput = document.querySelector('[name=floor-input]'); 
            }

            //1 
            if (roomInput.value == "") {
                roomInput.parentElement.style.border = "1px solid #dc3546"
            } else { 
                roomInput.parentElement.style.border = "1px solid #00000040"
                counter = counter+1 ;
            }

            //2 
            if (loungesInput.value == "") {
                loungesInput.parentElement.style.border = "1px solid #dc3546"
            } else { 
                loungesInput.parentElement.style.border = "1px solid #00000040"
                counter = counter+1 ;
            }

            //3
            if (bathroomInput.value == "") {
                bathroomInput.parentElement.style.border = "1px solid #dc3546"
            } else { 
                bathroomInput.parentElement.style.border = "1px solid #00000040"
                counter = counter+1 ;
            }

            // 4
            if (document.querySelector('[name=property_type]').value != 'chalet_rent' && document.querySelector("[name=property_type]").value != "villa_rent" ) { 
                if (document.querySelector('[name=property_type]').value != 'resthouse_rent') { 
                    let floorInput = document.querySelector('[name=floor-input]'); 
                    if (floorInput.value == "") {
                        floorInput.parentElement.style.border = "1px solid #dc3546"
                    } else { 
                        floorInput.parentElement.style.border = "1px solid #00000040"
                        counter = counter+1 ;
                    }
                }

            }
            

        }
    


        // 5
        if (propertyAgeInput.value == "") {
            propertyAgeInput.parentElement.style.border = "1px solid #dc3546"
        } else { 
            propertyAgeInput.parentElement.style.border = "1px solid #00000040"
            counter = counter+1 ;

            console.log('property age increament in condition')

        }

        



    } 


    if (document.querySelector('[name=property_type]').value != 'land_rent' && document.querySelector('[name=property_type]').value != 'floor_rent' && document.querySelector('[name=property_type]').value != 'resthouse_rent' && document.querySelector('[name=property_type]').value != 'shop_rent' && document.querySelector('[name=property_type]').value != 'villa_rent' && document.querySelector('[name=property_type]').value != 'apartment_rent' && document.querySelector('[name=property_type]').value != 'chalet_rent' && document.querySelector('[name=property_type]').value != 'furnished_apartment_rent') {
        // 5
        if (propertyAgeInput.value == "") {
            propertyAgeInput.parentElement.style.border = "1px solid #dc3546"
        } else { 
            propertyAgeInput.parentElement.style.border = "1px solid #00000040"
            counter = counter+1 ;
            console.log('property age increament out of the condition')


        }
    }






    if (document.querySelector('[name=property_type]').value == 'building_rent' || document.querySelector('[name=property_type]').value == 'shop_rent') {
            
        

        console.log("this is shop rent")

        // 5
        if (propertyAgeInput.value == "") {
            propertyAgeInput.parentElement.style.border = "1px solid #dc3546"
        } else { 
            propertyAgeInput.parentElement.style.border = "1px solid #00000040"
            counter = counter+1 ;
            console.log("property age grid") 
            console.log(counter) 
        }
    } 

    //6 
    if (streetWidthSliderValueInput.value == "") {
        streetWidthSliderValueInput.parentElement.style.border = "1px solid #dc3546"
    } else { 
        // streetWidthSliderValueInput.parentElement.style.border = "1px solid #00000040"
        counter = counter+1 ;
        console.log(counter);
    }


    if (counter == limit) { 
        propertyDetailsSection.style.display = 'none'; 
        propertyFeatures.style.display = 'block'; 

        let completedTimelineElement = document.querySelector('.timeline-item:nth-child(4)'); 
        completedTimelineElement.classList.remove('current')
        completedTimelineElement.classList.add('completed'); 
        
        let nextTimelineElement =  completedTimelineElement.nextElementSibling; 
        nextTimelineElement.classList.add('current') ;

        fillProgress(nextTimelineElement)

        console.log(true) 
    } else { 
        console.log(counter); 
    }
})


/*
            inputElement.style.border = "1px solid #dc3546"
            inputElement.style.border = "1px solid #00000040"

*/

let calc_meter_price_input_value = function () {
    let input = document.querySelector('[name=unit-price-input]');
    let priceInputValue = Number(document.querySelector('[name=price-input]').value); 
    let spaceInputValue = Number(document.querySelector('[name=space-input]').value); 

    input.value = priceInputValue / spaceInputValue; 

}


if (document.querySelector("[name=property_type]").value == 'land_rent') {

    let priceInput = document.querySelector('[name=price-input]'); 
    let spaceInput = document.querySelector('[name=space-input]');
    
    console.log('land_rent');
    
    priceInput.addEventListener('input', () => {
        calc_meter_price_input_value(); 
    })
    
    spaceInput.addEventListener('input', () => {
        calc_meter_price_input_value(); 
    })

} 

document.querySelector('form').onsubmit = function () { 
    // var description = `{% autoescape off %}{{ property.description }}{% endautoescape %}`; 
    var description = document.querySelector('[name=property__description__input]').value; 
    document.querySelector('[name=property__description__input]').value = marked(description); 
    alert(document.querySelector('[name=property__description__input]').value)

}