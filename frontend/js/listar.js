document.addEventListener('DOMContentLoaded', async () => {
  const lista = document.getElementById('listaProductos');
  const productos = await obtenerProductos();

  if (productos.length === 0) {
    lista.innerHTML = '<li class="fade-in">No hay productos disponibles.</li>';
    return;
  }

  productos.forEach(p => {
    const item = document.createElement('li');
    item.classList.add('fade-in');
    item.innerHTML = `
      <strong>${p.nombre}</strong> - $${p.precio}
      <p>${p.descripcion}</p>
      <p>Vence: ${p.fecha_vencimiento ? p.fecha_vencimiento : 'N/A'}</p>
      <div class="acciones-producto">
        <a href="editar.html?id=${p.id}" class="btn-sm">✏️ Editar</a>
        <button data-id="${p.id}" class="btn-sm eliminarBtn">🗑️ Eliminar</button>
      </div>
    `;
    lista.appendChild(item);
  });

  lista.addEventListener('click', async (e) => {
    if (e.target.classList.contains('eliminarBtn')) {
      const id = e.target.getAttribute('data-id');
      const confirmado = confirm('¿Estás seguro de que deseas eliminar este producto?');
      if (confirmado) {
        const resultado = await eliminarProducto(id);
        if (resultado.success) {
          e.target.closest('li').remove();
        } else {
          alert(resultado.message);
        }
      }
    }
  });
});
