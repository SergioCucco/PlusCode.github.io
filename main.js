// Hero title - cambiar palabra
const word = document.querySelector('.yellow-text')
const words = ['aprender', 'crear', 'programar']

let currentWordIndex = 0 //para rastrear el índice actual de la palabra en el array

//Función para cambiar palabra con transición
function changeWord() {
    word.style.opacity = 0; //transición opacidad
    setTimeout(() => {
        word.textContent = words[currentWordIndex]
        word.style.opacity = 1 //restaura la opacidad
    }, 300) //tiempo de espera en milisegundos
}


//intervalo de cambio
setInterval(() => {
    currentWordIndex = (currentWordIndex + 1) % words.length
    changeWord()
}, 3000) //cambia cada 3000ms (3s)


//cambia el texto
changeWord()



//Obtengo el icono 
let menu = document.querySelector('#menu-bars');
//Obtengo Navbar
let navbar = document.querySelector('.nav-items');

//selecciono collapse
let collapse = document.querySelector("#nav .collapse");


menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

var egresados = document.querySelector('#egresados')
function traer() {
    fetch('https://randomuser.me/api/?results=3')
        .then(res => res.json())
        .then(res => {
            console.log(res)
            console.log(res.results[0].country)
            egresados.innerHTML = `
                    <img src="${res.results[0].picture.large}" width="200px" class="img-fluid-rounded-circle">
                    <p class="kpi-item-text-t">Nombre: ${res.results[0].name.first}</p>
                    <p class="kpi-item-text-t">País: ${res.results[0].location.country}</p>
                    `
        })
        .catch(error => console.log("Ocurrió un error", error))
}



// form validation
const nombre = document.getElementById("name");
const email = document.getElementById("email");
const msg = document.getElementById("message");
const form = document.getElementById("contact-form");
const parrafo = document.getElementById("warning");
const divFlotante = document.getElementById("miDiv");
const btnCerrar = document.getElementById("close-btn")

form.addEventListener("submit", (e) => {
    e.preventDefault();
    let warning = "";
    let enter = false;
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    parrafo.innerHTML = ""

    if (nombre.value.length < 2) {
        warning += `El nombre no es válido <br>`;
        enter = true;
    }
    if (!regexEmail.test(email.value)) {
        warning += `El email no es válido <br>`;
        enter = true;
    }
    if (msg.value.length < 2) {
        warning += `El mensaje es demasiado corto <br>`;
        enter = true;
    }
    if (enter) {
        parrafo.innerHTML = warning;
        parrafo.style.color = 'rgb(189, 23, 23)'
        divFlotante.style.display = "block";
    } else {
        parrafo.innerHTML = "Enviado";
        parrafo.style.color = '#538731'
        divFlotante.style.display = "block";
        nombre.value = "";
        email.value = "";
        msg.value = "";
    }
});

function cerrarDiv() {
    divFlotante.style.display = "none";
}