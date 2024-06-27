console.log("Activo");

function showSideBar() {
  const sidebar = document.querySelector(".nav-side-bar");
  sidebar.style.display = "flex";
}

function closeSideBar() {
  const sidebar = document.querySelector(".nav-side-bar");
  sidebar.style.display = "none";
}

//función para poder acceder a noticia.html mediante el enlace del navbar en dispositivos moviles
function accesoNoticias(url) {
  window.location.href = url;
}

//función para poder acceder a login.html mediante el enlace del navbar en dispositivos moviles

function accesoLogin(url) {
  window.location.href = url;
}
