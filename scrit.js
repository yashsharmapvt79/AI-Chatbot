let container = document.getElementById('container')

toggle = () => {
    container.classList.toggle('sign-in')
    container.classList.toggle('sign-up')
}

setTimeout(() => {
    container.classList.add('sign-in')
}, 200)

function signin() {
    window.location.href = "i.html";
}

function signup() {
    window.location.href = "ty.html";
}
