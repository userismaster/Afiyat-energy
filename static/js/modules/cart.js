export default class Cart {
  constructor() {
    this.items = new Map();
    this.total = 0;
    this.count = 0;
    this.init();
  }

  init() {
    this.loadFromStorage();
    this.bindEvents();
    this.updateUI();
  }

  bindEvents() {
    document.addEventListener('click', (e) => {
      const addToCartBtn = e.target.closest('.add-to-cart');
      if (addToCartBtn) {
        e.preventDefault();
        const productId = addToCartBtn.dataset.productId;
        const quantity = parseInt(document.querySelector(`#quantity-${productId}`).value) || 1;
        this.addItem(productId, quantity);
      }
    });

    // Делегирование событий для кнопок изменения количества
    document.addEventListener('click', (e) => {
      const quantityBtn = e.target.closest('.quantity-btn');
      if (quantityBtn) {
        const productId = quantityBtn.dataset.productId;
        const action = quantityBtn.dataset.action;
        
        if (action === 'increase') {
          this.updateQuantity(productId, 1);
        } else if (action === 'decrease') {
          this.updateQuantity(productId, -1);
        }
      }
    });
  }

  async addItem(productId, quantity) {
    try {
      const response = await fetch('/api/cart/add/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.getCsrfToken()
        },
        body: JSON.stringify({ product_id: productId, quantity })
      });

      if (!response.ok) throw new Error('Network response was not ok');

      const data = await response.json();
      
      if (data.success) {
        this.items.set(productId, {
          ...data.product,
          quantity: (this.items.get(productId)?.quantity || 0) + quantity
        });
        
        this.updateStorage();
        this.updateUI();
        this.showNotification('Товар добавлен в корзину');
      }
    } catch (error) {
      console.error('Error adding item to cart:', error);
      this.showNotification('Ошибка при добавлении товара', 'error');
    }
  }

  async updateQuantity(productId, delta) {
    const item = this.items.get(productId);
    if (!item) return;

    const newQuantity = item.quantity + delta;
    if (newQuantity < 1) return;

    try {
      const response = await fetch('/api/cart/update/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.getCsrfToken()
        },
        body: JSON.stringify({ product_id: productId, quantity: newQuantity })
      });

      if (!response.ok) throw new Error('Network response was not ok');

      const data = await response.json();
      
      if (data.success) {
        item.quantity = newQuantity;
        this.updateStorage();
        this.updateUI();
      }
    } catch (error) {
      console.error('Error updating cart:', error);
      this.showNotification('Ошибка при обновлении корзины', 'error');
    }
  }

  removeItem(productId) {
    this.items.delete(productId);
    this.updateStorage();
    this.updateUI();
  }

  updateUI() {
    this.updateTotal();
    this.updateCount();
    this.renderCart();
  }

  updateTotal() {
    this.total = Array.from(this.items.values()).reduce((sum, item) => {
      return sum + (item.price * item.quantity);
    }, 0);

    const totalElements = document.querySelectorAll('.cart-total');
    totalElements.forEach(el => {
      el.textContent = this.formatPrice(this.total);
    });
  }

  updateCount() {
    this.count = Array.from(this.items.values()).reduce((sum, item) => {
      return sum + item.quantity;
    }, 0);

    const countElements = document.querySelectorAll('.cart-count');
    countElements.forEach(el => {
      el.textContent = this.count;
    });
  }

  renderCart() {
    const cartContainer = document.querySelector('.cart-items');
    if (!cartContainer) return;

    cartContainer.innerHTML = Array.from(this.items.values())
      .map(item => this.renderCartItem(item))
      .join('');
  }

  renderCartItem(item) {
    return `
      <div class="cart-item" data-product-id="${item.id}">
        <div class="cart-item-image">
          <img src="${item.image}" alt="${item.name}">
        </div>
        <div class="cart-item-content">
          <h3 class="cart-item-title">${item.name}</h3>
          <div class="cart-item-price">${this.formatPrice(item.price)}</div>
          <div class="cart-item-quantity">
            <button class="quantity-btn" data-action="decrease" data-product-id="${item.id}">-</button>
            <span>${item.quantity}</span>
            <button class="quantity-btn" data-action="increase" data-product-id="${item.id}">+</button>
          </div>
        </div>
        <button class="cart-item-remove" onclick="cart.removeItem('${item.id}')">×</button>
      </div>
    `;
  }

  loadFromStorage() {
    const stored = localStorage.getItem('cart');
    if (stored) {
      const data = JSON.parse(stored);
      this.items = new Map(Object.entries(data));
    }
  }

  updateStorage() {
    const data = Object.fromEntries(this.items);
    localStorage.setItem('cart', JSON.stringify(data));
  }

  formatPrice(price) {
    return new Intl.NumberFormat('ru-RU', {
      style: 'currency',
      currency: 'UZS'
    }).format(price);
  }

  getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]')?.value;
  }

  showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
      notification.remove();
    }, 3000);
  }
}
