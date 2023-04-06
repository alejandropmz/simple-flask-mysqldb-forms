/* Elementos */

/* mensajes de agregado y eliminado */
let msgContent = document.getElementsByClassName("create-delete-message");
msgContent = [...msgContent];
let close = document.getElementsByClassName("close");
close = [...close];

/* formulario */

let addContact = document.getElementById("add-contact")
let form = document.getElementById("index-form-father")
let buttonClose = document.getElementById("close-form-button")



/* logica */


/* mostrar mensajes de agregado y ocultado */

const noShowMsg = () => {
  msgContent[0].className = "d-none";
};


if (close[0]) {
  setTimeout(() => {
    noShowMsg();
  }, 4000);
  close[0].addEventListener("click", () => {
    noShowMsg();
  });
}


/* Mostrar formulario */

buttonClose.addEventListener('click', ()=> {
  form.className = "d-none"
  addContact.className = "d-flex justify-content-start align-items-center"
})

addContact.addEventListener('click', ()=> {
  form.className = ""
  addContact.className = "d-none"
})