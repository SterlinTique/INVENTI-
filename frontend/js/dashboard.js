document.addEventListener('DOMContentLoaded', async () => {
  const loader = document.getElementById('loaderDashboard');
  const tarjetas = document.querySelector('.tarjetas-dashboard');

  // Mostrar loader
  loader.style.display = 'block';
  tarjetas.style.display = 'none';

  const productos = await obtenerProductos();

  // Ocultar loader y mostrar tarjetas
  loader.style.display = 'none';
  tarjetas.style.display = 'flex';

  document.getElementById('totalProductos').textContent = productos.length;

  if (productos.length > 0) {
    const ultimo = productos[productos.length - 1];
    const maxPrecio = Math.max(...productos.map(p => p.precio));

    document.getElementById('ultimoProducto').textContent = ultimo.nombre;
    document.getElementById('precioMaximo').textContent = `$${maxPrecio.toFixed(2)}`;
  }


   // Reporte general
  const reporteGeneral = await obtenerReporteGeneral();
  const tbodyGeneral = document.querySelector('#tablaReporteGeneral tbody');
  reporteGeneral.data.forEach(p => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${p.nombre}</td>
      <td>${p.categoria}</td>
      <td>$${p.precio_venta}</td>
      <td>${p.inventario.stock_actual ?? '-'}</td>
      <td>${p.inventario.alerta_stock_bajo ? 'Alerta' : 'Normal'}</td>
    `;
    tbodyGeneral.appendChild(row);
  });

  // Reporte por categorías
  const reporteCategorias = await obtenerReporteCategorias();
  const tbodyCategorias = document.querySelector('#tablaReporteCategorias tbody');
  reporteCategorias.data.forEach(c => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${c.categoria}</td>
      <td>${c.total_productos_activos}</td>
      <td>${c.stock_total}</td>
      <td>$${c.valor_total_inventario}</td>
    `;
    tbodyCategorias.appendChild(row);
  });
});
