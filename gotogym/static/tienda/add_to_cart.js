// add_to_cart.js
// Este script maneja el botón de añadir al carrito y actualiza el contador en la barra de navegación

document.addEventListener('DOMContentLoaded', function() {
  // Selecciona todos los botones de añadir al carrito
  const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');

  addToCartBtns.forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      const productId = btn.getAttribute('data-product-id');
      fetch('/carrito/add/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': getCSRFToken()
        },
        body: `product_id=${productId}`
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          // Actualiza todos los contadores del carrito en la barra de navegación
          document.querySelectorAll('#cart-count').forEach(function(el) {
            el.textContent = data.cart_count;
          });
          mostrarMensaje('Producto añadido al carrito');
        }
      });
    });
  });

  // Muestra un mensaje visual de éxito
  function mostrarMensaje(msg) {
    let aviso = document.createElement('div');
    aviso.textContent = msg;
    aviso.style.position = 'fixed';
    aviso.style.top = '20px';
    aviso.style.right = '20px';
    aviso.style.background = '#C5A46B';
    aviso.style.color = '#fff';
    aviso.style.padding = '12px 24px';
    aviso.style.borderRadius = '8px';
    aviso.style.zIndex = '9999';
    aviso.style.boxShadow = '0 2px 8px rgba(0,0,0,0.15)';
    document.body.appendChild(aviso);
    setTimeout(function() {
      aviso.remove();
    }, 1200);
  }

  // Obtiene el token CSRF de la cookie
  function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, 10) === 'csrftoken=') {
          cookieValue = decodeURIComponent(cookie.substring(10));
          break;
        }
      }
    }
    return cookieValue;
  }
});
