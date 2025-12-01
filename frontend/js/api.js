const API_BASE_URL = 'http://localhost:5000/api'; 

async function loginUsuario(email, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al conectar con la API:', error);
        return { success: false, message: 'Error de conexión con el servidor' };
    }
}


async function registrarUsuario(username, password, email) {
    try {
        const response = await fetch(`${API_BASE_URL}/registro`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password, email })
        });

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al conectar con la API:', error);
        return { success: false, message: 'Error de conexión con el servidor' };
    }
}


async function obtenerProductos() {
    try {
        const response = await fetch(`${API_BASE_URL}/productos`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al obtener productos:', error);
        return [];
    }
}


async function crearProducto(nombre, descripcion, precio) {
    try {
        const response = await fetch(`${API_BASE_URL}/productos`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre, descripcion, precio })
        });

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al crear producto:', error);
        return { success: false, message: 'Error de conexión con el servidor' };
    }
}


async function eliminarProducto(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/productos/${id}`, {
            method: 'DELETE'
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al eliminar producto:', error);
        return { success: false, message: 'Error de conexión con el servidor' };
    }
}


async function obtenerProductoPorId(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/productos`);
        const productos = await response.json();
        return productos.find(p => p.id == id);
    } catch (error) {
        console.error('Error al obtener producto:', error);
        return null;
    }
}

async function actualizarProducto(id, nombre, descripcion, precio) {
    try {
        const response = await fetch(`${API_BASE_URL}/productos/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre, descripcion, precio })
        });

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al actualizar producto:', error);
        return { success: false, message: 'Error de conexión con el servidor' };
    }
}
