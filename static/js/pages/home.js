document.addEventListener('DOMContentLoaded', function() {
    // Инициализация быстрого просмотра
    initQuickView();
    
    // Инициализация добавления в корзину
    initAddToCart();
});

function initQuickView() {
    const quickViewButtons = document.querySelectorAll('.quick-view');
    
    quickViewButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            
            // Показываем прелоадер
            Swal.fire({
                title: 'Загрузка...',
                allowOutsideClick: false,
                showConfirmButton: false,
                willOpen: () => {
                    Swal.showLoading();
                }
            });
            
            // Запрашиваем данные о товаре
            fetch(`/api/products/${productId}/`)
                .then(response => response.json())
                .then(product => {
                    // Закрываем прелоадер
                    Swal.close();
                    
                    // Показываем модальное окно с информацией о товаре
                    Swal.fire({
                        title: product.name,
                        html: `
                            <div class="quick-view-modal">
                                <div class="quick-view-image">
                                    <img src="${product.image}" alt="${product.name}">
                                </div>
                                <div class="quick-view-info">
                                    <div class="quick-view-price">
                                        ${product.old_price ? `<span class="old-price">${product.old_price} сум</span>` : ''}
                                        <span class="current-price">${product.price} сум</span>
                                    </div>
                                    <div class="quick-view-stock">
                                        ${product.stock > 0 
                                            ? '<i class="fas fa-check-circle text-success"></i> В наличии'
                                            : '<i class="fas fa-times-circle text-danger"></i> Нет в наличии'
                                        }
                                    </div>
                                    <div class="quick-view-description">
                                        ${product.description}
                                    </div>
                                </div>
                            </div>
                        `,
                        showCancelButton: true,
                        confirmButtonText: 'В корзину',
                        cancelButtonText: 'Закрыть',
                        confirmButtonColor: getComputedStyle(document.documentElement)
                            .getPropertyValue('--primary-color').trim(),
                        customClass: {
                            popup: 'quick-view-popup',
                            content: 'quick-view-content'
                        }
                    }).then((result) => {
                        if (result.isConfirmed && product.stock > 0) {
                            addToCart(productId);
                        }
                    });
                })
                .catch(error => {
                    Swal.fire({
                        icon: 'error',
                        title: 'Ошибка',
                        text: 'Не удалось загрузить информацию о товаре'
                    });
                });
        });
    });
}

function initAddToCart() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            addToCart(productId);
        });
    });
}

function addToCart(productId) {
    // Показываем индикатор загрузки на кнопке
    const button = document.querySelector(`.add-to-cart[data-product-id="${productId}"]`);
    const originalContent = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
    button.disabled = true;
    
    // Отправляем запрос на добавление в корзину
    fetch('/api/cart/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            product_id: productId,
            quantity: 1
        })
    })
    .then(response => response.json())
    .then(data => {
        // Обновляем счетчик корзины
        const cartCounter = document.querySelector('.cart-counter');
        if (cartCounter) {
            cartCounter.textContent = data.total_items;
        }
        
        // Показываем уведомление об успехе
        Swal.fire({
            icon: 'success',
            title: 'Товар добавлен в корзину',
            showConfirmButton: false,
            timer: 1500
        });
    })
    .catch(error => {
        Swal.fire({
            icon: 'error',
            title: 'Ошибка',
            text: 'Не удалось добавить товар в корзину'
        });
    })
    .finally(() => {
        // Возвращаем кнопку в исходное состояние
        button.innerHTML = originalContent;
        button.disabled = false;
    });
}

// Вспомогательная функция для получения CSRF-токена
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
