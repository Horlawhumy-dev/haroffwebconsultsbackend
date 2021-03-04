
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

let messengerName = document.getElementById('sender');
let title = document.getElementById('title');
let fromMail = document.getElementById('mail');
let messageBody = document.getElementById('mssg');

messageForm.addEventListener("submit", (e) => {
    
    if( messengerName.value === "" || title.value === "" || mail.value === "" || messageBody.value === ""){
      
        document.getElementById('alert').style.visibility = 'visible';
        document.getElementById('message-container').style.display = 'block';
        
        // Clearing Inputs
        clearInputs();
       
    }else{
        document.getElementById('message-container').style.display = 'none';
        document.getElementById('center').style.display = 'block';
    }
    e.preventDefault();
})


// clear inputs
function clearInputs(){
    messengerName = '';
    title.value = '';
    mail.value = '';
    messageBody.value = '';
}

// Closing ALert Button
const alertBtn = document.getElementById('alert-btn');

alertBtn.addEventListener('click', (e) => {
    document.getElementById('alert').style.display = 'none';
    window.location.reload();
})