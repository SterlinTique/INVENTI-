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
});
