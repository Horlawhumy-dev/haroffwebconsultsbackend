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



// Message Form
let messageForm = document.getElementById("form1");

let messengerName = document.getElementById('sender');
let title = document.getElementById('title');
let fromMail = document.getElementById('mail');
let messageBody = document.getElementById('mssg');

messageForm.addEventListener("submit", (e) => {
    e.preventDefault();
    if( messengerName.value === "" || title.value === "" || fromMail.value === "" || messageBody.value === ""){
      
        document.getElementById('div-al').style.visibility = 'visible';
        // document.getElementById('message-container').style.display = 'block';
        
        // Clearing Inputs
        clearInputs();
       
    }else{
        document.getElementById('message-container').style.display = 'none';
        document.getElementById('center').style.display = 'block';
    }
  
})


// clear inputs
function clearInputs(){
    messengerName = '';
    title.value = '';
    mail.value = '';
    messageBody.value = '';
}



// Closing ALert Button
let messagebtn = document.getElementById('btn');

messagebtn.addEventListener('click', () => {
    document.getElementById('div-al').style.display = 'none';
    window.location.reload();
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



