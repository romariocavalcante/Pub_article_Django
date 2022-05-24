let navbar = document.getElementById('navbar');
console.log("pegando a altura do navigation",navbar.clientHeight);

let navigation = document.getElementById('navigation');
let teste = navigation.style.marginTop = `${navbar.clientHeight}px`;
console.log('teste',teste)