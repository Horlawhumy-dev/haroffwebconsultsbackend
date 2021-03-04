
// Hamburger Toggling

// opening Button
const openHamburger = document.getElementById('open');

let ulLinks = document.getElementById('links');

openHamburger.addEventListener("click", () => {
    // console.log(ulLinks);
    ulLinks.classList.toggle('toggle-open');
})

// Closing Button
const closeHamburger = document.getElementById('close');


closeHamburger.addEventListener("click", () => {
    // console.log(ulLinks) 
    ulLinks.classList.toggle('toggle-close');
})

// Scrolling Top Button
const scrollBtn = document.getElementById('scroll-top');

scrollBtn.addEventListener('click', (e) => {
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

    e.preventDefault();
})

// Message Form
const messageForm = document.getElementById("form");

messageForm.addEventListener("submit", (e) => {
    document.getElementById('message-container').style.display = 'none';
    document.getElementById('center').style.display = 'block';
    e.preventDefault();
})