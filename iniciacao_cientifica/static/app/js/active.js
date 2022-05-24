nav_link = document.querySelectorAll('.nav .underline_div');
link = document.querySelectorAll('.underline_div .nav-link');
nav_item = document.getElementsByClassName('nav-item');
console.log(nav_item)
console.log(link)
console.log('nav',nav_link)
for (let i = 0; i < link.length; i++) {
    link[i].addEventListener('click', (event) => {
        event.preventDefault()
        teste = nav_item[0].classList.add('active')
        console.log(nav_link[i])
    });
}



teste = document.querySelectorAll('.nav .underline_div')
console.log(teste)