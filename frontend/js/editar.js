document.addEventListener('DOMContentLoaded', async () => {
  const form = document.getElementById('editarForm');
  const errorMsg = document.getElementById('error');
  const exitoMsg = document.getElementById('exito');

  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');

  if (!id) {
    errorMsg.textContent = 'ID de producto no especificado.';
    form.style.display = 'none';
    return;
  }

  const producto = await obtenerProductoPorId(id);

  if (!producto) {
    errorMsg.textContent = 'Producto no encontrado.';
    form.style.display = 'none';
    return;
  }

  // Rellenar formulario
  document.getElementById('nombre').value = producto.nombre;
  document.getElementById('descripcion').value = producto.descripcion;
  document.getElementById('precio').value = producto.precio;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const descripcion = document.getElementById('descripcion').value;
    const precio = parseFloat(document.getElementById('precio').value);

    const resultado = await actualizarProducto(id, nombre, descripcion, precio);

    if (resultado.success) {
      exitoMsg.textContent = resultado.message;
      errorMsg.textContent = '';
      exitoMsg.style.opacity = '1';
      exitoMsg.style.transform = 'translateY(0)';
    } else {
      errorMsg.textContent = resultado.message;
      exitoMsg.textContent = '';
      errorMsg.style.opacity = '1';
      errorMsg.style.transform = 'translateY(0)';
    }
  });
});
