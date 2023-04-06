/* Elementos */

/* mensajes de agregado y eliminado */
let msgContent = document.getElementsByClassName("create-delete-message");
msgContent = [...msgContent];
let close = document.getElementsByClassName("close");
close = [...close];

/* logica */

/* const sh = () => {
  console.log("object");
};

setTimeout(() => {
  sh();
}, 3000); */

const noShowMsg = () => {
  msgContent[0].className = "d-none";
};

/* mostrar mensajes de agregado y ocultado */

if (close[0]) {
  setTimeout(() => {
    noShowMsg();
  }, 3000);
  close[0].addEventListener("click", () => {
    noShowMsg();
  });
}
