// Cart functionality
document.addEventListener('DOMContentLoaded', function() {
    // Add to cart
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    console.log('Found add-to-cart buttons:', addToCartButtons.length);
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Проверяем наличие data-атрибутов
            const productId = this.dataset.productId;
            const productName = this.dataset.productName;
            const productPrice = this.dataset.productPrice;
            
            if (!productId) {
                console.error('Missing product ID');
                return;
            }
            
            // Ищем поле количества
            const quantityInput = this.closest('.product-info')?.querySelector('input[name="quantity"]');
            if (!quantityInput) {
                console.error('Quantity input not found');
                return;
            }
            
            const quantity = parseInt(quantityInput.value) || 1;
            const price = parseFloat(productPrice?.replace(/[^\d.,]/g, '').replace(',', '.')) || 0;
            
            console.log('Adding to cart:', {
                productId,
                productName,
                price,
                quantity
            });
            
            // Проверяем наличие CSRF-токена
            const csrftoken = getCookie('csrftoken');
            if (!csrftoken) {
                console.error('CSRF token not found');
                return;
            }
            
            fetch('/cart/add/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    product_id: productId,
                    quantity: quantity
                })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('Server response:', data);
                if (data.success) {
                    // Обновляем счетчик корзины
                    const cartCount = document.getElementById('cart-count');
                    if (cartCount) {
                        cartCount.textContent = data.cart_count;
                        cartCount.style.display = 'block';
                    }
                    
                    // Показываем уведомление об успехе
                    Swal.fire({
                        icon: 'success',
                        title: 'Успешно',
                        text: 'Товар добавлен в корзину',
                        showConfirmButton: false,
                        timer: 1500
                    });
                } else {
                    // Показываем ошибку
                    Swal.fire({
                        icon: 'error',
                        title: 'Ошибка',
                        text: data.error || 'Произошла ошибка при добавлении товара в корзину'
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
                Swal.fire({
                    icon: 'error',
                    title: 'Ошибка',
                    text: 'Произошла ошибка при добавлении товара в корзину'
                });
            });
        });
    });

    // Update quantity in cart
    const quantityInputs = document.querySelectorAll('.cart-quantity');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            const itemId = this.dataset.itemId;
            const newQuantity = this.value;
            
            fetch('/cart/update/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    item_id: itemId,
                    quantity: newQuantity
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    updateCartCount(data.cart_count);
                    updateCartTotal(data.cart_total);
                }
            });
        });
    });

    // Обработчики кнопок +/- для количества
    const quantityButtons = document.querySelectorAll('.quantity-btn');
    quantityButtons.forEach(button => {
        button.addEventListener('click', function() {
            const container = this.closest('.quantity');
            const input = container.querySelector('input[name="quantity"]');
            const currentValue = parseInt(input.value) || 1;
            const maxValue = parseInt(input.getAttribute('max')) || 999;
            
            if (this.classList.contains('increase-quantity') && currentValue < maxValue) {
                input.value = currentValue + 1;
            } else if (this.classList.contains('decrease-quantity') && currentValue > 1) {
                input.value = currentValue - 1;
            }
            
            // Вызываем событие change для обновления состояния кнопок
            const event = new Event('change');
            input.dispatchEvent(event);
        });
    });

    // Обработчик изменения количества
    const quantityInputsAll = document.querySelectorAll('input[name="quantity"]');
    quantityInputsAll.forEach(input => {
        input.addEventListener('change', function() {
            const container = this.closest('.quantity');
            const decreaseBtn = container.querySelector('.decrease-quantity');
            const increaseBtn = container.querySelector('.increase-quantity');
            const currentValue = parseInt(this.value) || 1;
            const maxValue = parseInt(this.getAttribute('max')) || 999;
            
            // Проверяем и корректируем значение
            if (currentValue < 1) {
                this.value = 1;
            } else if (currentValue > maxValue) {
                this.value = maxValue;
            }
            
            // Обновляем состояние кнопок
            if (decreaseBtn) {
                decreaseBtn.disabled = currentValue <= 1;
            }
            if (increaseBtn) {
                increaseBtn.disabled = currentValue >= maxValue;
            }
        });
        
        // Запрещаем ввод нечисловых символов
        input.addEventListener('keypress', function(e) {
            if (!/[0-9]/.test(e.key)) {
                e.preventDefault();
            }
        });
        
        // Инициализируем начальное состояние
        input.dispatchEvent(new Event('change'));
    });
});

// Helper functions
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateCartCount(count) {
    const cartCount = document.getElementById('cart-count');
    if (cartCount) {
        cartCount.textContent = count;
        cartCount.style.display = count > 0 ? 'block' : 'none';
    }
}

function updateCartTotal(total) {
    const cartTotal = document.getElementById('cart-total');
    if (cartTotal) {
        cartTotal.textContent = total.toLocaleString('ru-RU') + ' UZS';
    }
}

function showCartToast(productName, quantity, totalPrice) {
    Toastify({
        node: (() => {
            const node = document.createElement("div");
            node.innerHTML = `
                <div class="cart-toast-content">
                    <i class="fas fa-check-circle cart-toast-icon"></i>
                    <div class="cart-toast-message">
                        <strong>${productName}</strong> добавлен в корзину<br>
                        <small>Количество: ${quantity}, Сумма: ${totalPrice} UZS</small>
                    </div>
                    <i class="fas fa-times cart-toast-close"></i>
                </div>
                <div class="cart-toast-actions">
                    <a href="/cart/" class="cart-toast-button cart-toast-view">
                        Просмотр корзины
                    </a>
                    <a href="/checkout/" class="cart-toast-button cart-toast-checkout">
                        Оформить заказ
                    </a>
                </div>
            `;
            
            // Добавляем обработчик для кнопки закрытия
            const closeBtn = node.querySelector('.cart-toast-close');
            if (closeBtn) {
                closeBtn.addEventListener('click', function() {
                    const toastElement = this.closest('.cart-toast').parentElement;
                    if (toastElement) {
                        toastElement.remove();
                    }
                });
            }
            
            return node;
        })(),
        className: "cart-toast",
        duration: 5000,
        newWindow: true,
        close: false,
        gravity: "top",
        position: "right",
        stopOnFocus: true,
        style: {
            background: "transparent",
            boxShadow: "none"
        }
    }).showToast();
}
