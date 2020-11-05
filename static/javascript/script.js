const erreur = document.querySelector('#erreur')
if (erreur.innerText === "") {
    erreur.classList.remove("erreur")
}
else {
    erreur.classList.add("erreur")
}