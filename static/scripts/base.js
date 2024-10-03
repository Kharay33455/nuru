function showImg(pic, cap){
    document.getElementById('fullImgBox').style.display = 'flex' 
    document.getElementById('fullImg').src = pic
    document.getElementById('fullImg').alt = cap
    document.getElementById('caption').innerHTML = cap
}

function hideImg(){
    document.getElementById('fullImgBox').style.display = 'none'
}



if (window.innerWidth < 991) {
    document.getElementById('map-container').style.display = 'none';
    document.getElementById('map-container-phone').style.display = 'flexbox'
} else {
        document.getElementById('map-container').style.display = 'flex';
    document.getElementById('map-container-phone').style.display = 'none'
}


