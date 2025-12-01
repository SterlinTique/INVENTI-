document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('crearForm');
  const errorMsg = document.getElementById('error');
  const exitoMsg = document.getElementById('exito');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const descripcion = document.getElementById('descripcion').value;
    const precio = parseFloat(document.getElementById('precio').value);

    const resultado = await crearProducto(nombre, descripcion, precio);

    if (resultado.success) {
      exitoMsg.textContent = resultado.message;
      errorMsg.textContent = '';
      exitoMsg.style.opacity = '1';
      exitoMsg.style.transform = 'translateY(0)';
      form.reset();
    } else {
      errorMsg.textContent = resultado.message;
      exitoMsg.textContent = '';
      errorMsg.style.opacity = '1';
      errorMsg.style.transform = 'translateY(0)';
    }
  });
});
