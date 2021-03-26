// Hamburger Toggling
// opening Button
let openHamburger = document.getElementById('open');
let ulLinks = document.getElementById('links');

openHamburger.addEventListener("click", () => {
    // console.log(ulLinks);
    ulLinks.classList.toggle('toggle-open');
})

// Closing Button
let closeHamburger = document.getElementById('close');

closeHamburger.addEventListener("click", () => {
    // console.log(ulLinks) 
    ulLinks.classList.toggle('toggle-close');
})



// Scrolling Top Button
let scrollBtn = document.getElementById('scroll-top');

scrollBtn.addEventListener('click', () => {
    // document.documentElement.scrollTop = '0';
    currentYOffset = self.pageYOffset;
    initYOffset = currentYOffset;

    var intervalId = setInterval(function(){
    currentYOffset -= initYOffset*0.05; 
    document.body.scrollTop = currentYOffset ;
    document.documentElement.scrollTop = currentYOffset;

        if(self.pageYOffset == 0){
        clearInterval(intervalId);
        }
    }, 15);

})









