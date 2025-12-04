document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('container'); 
  const toggle = document.getElementById('toggle');
  const welcomeTitle = document.getElementById('welcomeTitle');
  const welcomeText = document.getElementById('welcomeText');
  const toggleIcon = document.getElementById('toggle-icon'); 
  const toggleLabel = document.getElementById('toggle-label');

  toggle.addEventListener('click', () => { // el toggle es el boton para cambiar entre login y registro
    container.classList.toggle('active'); // esto es para agregar o quitar la clase active del contenedor y asi cambiar de vista

    if (container.classList.contains('active')) {
      welcomeTitle.textContent = '¡BIENVENIDO DE NUEVO!';
      welcomeText.textContent = 'Nos alegra tenerte de vuelta. Si necesitas algo, estamos aquí para ayudarte.';
      toggleIcon.textContent = '🔑';
      toggleLabel.textContent = 'Inicio';
    } else {
      welcomeTitle.textContent = 'BIENVENIDO!';
      welcomeText.textContent = 'Nos alegra tenerte aquí. Si necesitas ayuda o no tienes cuenta te invitamos a registrarte.';
      toggleIcon.textContent = '📝';
      toggleLabel.textContent = 'Registrar';
    }
  });

  // Login
  document.getElementById('loginForm').addEventListener('submit', async (e) => { //addEventListener es para escuchar eventos, en este caso el submit del formulario
    e.preventDefault(); // para que no recargue la pagina
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    const errorMsg = document.getElementById('loginError');

    const resultado = await loginUsuario(email, password);
    if (resultado.success) {
      if (resultado.rol === 1) {
        window.location.href = 'dashboard.html';
      } else {
        window.location.href = 'index.html';
      }
    } else {
      errorMsg.textContent = resultado.message;
      errorMsg.style.opacity = '1';
      errorMsg.style.transform = 'translateY(0)';
    }
  });

  // Registro
  document.getElementById('registroForm').addEventListener('submit', async (e) => {
    e.preventDefault(); // para que no recargue la pagina
    const nombre = document.getElementById('registerNombre').value;
    const password = document.getElementById('registerPassword').value;
    const email = document.getElementById('registerEmail').value;
    const confirmarPassword = document.getElementById('registerConfirmPassword').value;
    const errorMsg = document.getElementById('registerError'); // para mostrar errores
    const successMsg = document.getElementById('registerSuccess'); // para mostrar exito

    const resultado = await registrarUsuario(nombre, password, email, confirmarPassword);

    if (resultado.success) {
      successMsg.textContent = resultado.message;
      errorMsg.textContent = '';
      successMsg.style.opacity = '1';
      successMsg.style.transform = 'translateY(0)';
      setTimeout(() => {
        container.classList.remove('active');
      }, 1500);
    } else {
      errorMsg.textContent = resultado.message;
      successMsg.textContent = '';
      errorMsg.style.opacity = '1';
      errorMsg.style.transform = 'translateY(0)';
    }
  });
});
