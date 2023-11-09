const formOpenBtn=document.querySelector("#form-op"),
 home=document.querySelector(".home"),
 formcontainer=document.querySelector(".form_container"),
 formCloseBtn=document.querySelector(".form_close"),
 signupBtn=document.querySelector("#signup"),
 loginBtn=document.querySelector("#login"),
 pwShowHide=document.querySelectorAll(".pw_hide");

 formOpenBtn.addEventListener("click",()=>home.classList.add("show"));
 formCloseBtn.addEventListener("click",()=>home.classList.remove("show"));

 pwShowHide.forEach(icon =>{
    icon.addEventListener("click", () => {
        let getPassInput=icon.parentElement.querySelector("input");
        if(getPassInput.type =="password"){
            getPassInput.type="text";
            icon.classList.replace("uil-eye-slash","uil-eye");
        }else{
            getPassInput.type="password";
            icon.classList.replace("uil-eye","uil-eye-slash");
        }
    })

 })
signupBtn.addEventListener("click",(e)=>{
   e.preventDefault(); 
   formcontainer.classList.add("active")
})

loginBtn.addEventListener("click",(e)=>{
    e.preventDefault(); 
    formcontainer.classList.remove("active")
 })