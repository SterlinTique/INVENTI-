document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('crearForm');
  const errorMsg = document.getElementById('error');
  const exitoMsg = document.getElementById('exito');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const descripcion = document.getElementById('descripcion').value;
    const precio = parseFloat(document.getElementById('precio').value);
    const id_categoria = parseInt(document.getElementById('id_categoria').value);
    const fecha_vencimiento = document.getElementById('fecha_vencimiento').value || null;
    

    const resultado = await crearProducto(nombre, descripcion, precio, fecha_vencimiento, id_categoria);
    

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
