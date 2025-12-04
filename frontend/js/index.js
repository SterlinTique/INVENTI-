document.addEventListener('DOMContentLoaded', async () => {
  const lista = document.getElementById('listaProductos');
  const productos = await obtenerProductos();
  const alertasLista = document.getElementById('listaAlertas');
  const alertas = await obtenerAlertasInventario();

  // Mostrar alertas de inventario
    if (alertas.alertas.length === 0) {
    alertasLista.innerHTML = '<li class="fade-in">No hay alertas de inventario.</li>';
  } else {
    alertas.alertas.forEach(a => {
      const item = document.createElement('li');
      item.classList.add('fade-in');
      item.innerHTML = `<strong>${a.producto}</strong> - Stock actual: ${a.stock_actual}, mínimo requerido: ${a.stock_minimo}`;
      alertasLista.appendChild(item);
    });
  }

  // Mostrar productos
  if (productos.length === 0) {
    lista.innerHTML = '<li class="fade-in">No hay productos disponibles.</li>';
    return;
  }

  productos.forEach(p => {
    const item = document.createElement('li');
    item.classList.add('fade-in');
    item.innerHTML = `<strong>${p.nombre}</strong> - $${p.precio_venta}<br><p>${p.descripcion}</p>`;
    lista.appendChild(item);
  });
});
