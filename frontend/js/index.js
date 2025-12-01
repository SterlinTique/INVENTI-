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
    item.innerHTML = `<strong>${p.nombre}</strong> - $${p.precio}<br><p>${p.descripcion}</p>`;
    lista.appendChild(item);
  });
});
