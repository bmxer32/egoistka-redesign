// Client-side interactions for Salon Egoistka Redesign

document.addEventListener('DOMContentLoaded', () => {

  // DIKIDI Booking Modal Logic
  const dikidiModal = document.getElementById('dikidiModal');
  const dikidiButtons = document.querySelectorAll('.btn-dikidi');
  const modalClose = document.querySelector('.modal-close');

  if (dikidiModal) {
    dikidiButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        dikidiModal.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });

    if (modalClose) {
      modalClose.addEventListener('click', () => {
        dikidiModal.classList.remove('active');
        document.body.style.overflow = '';
      });
    }

    dikidiModal.addEventListener('click', (e) => {
      if (e.target === dikidiModal) {
        dikidiModal.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  // Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      mobileToggle.classList.toggle('active');
    });
  }

  // Tab Filtering for Massage services & Works portfolio
  const tabButtons = document.querySelectorAll('.tab-btn');

  tabButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      e.preventDefault();

      const container = button.closest('.container') || document;
      container.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      button.classList.add('active');

      const filter = button.getAttribute('data-filter');

      // Filter massage cards
      const massageCards = container.querySelectorAll('.massage-card');
      if (massageCards.length > 0) {
        massageCards.forEach(card => {
          const cat = card.getAttribute('data-category');
          if (filter === 'all' || cat === filter) {
            card.classList.remove('hidden');
          } else {
            card.classList.add('hidden');
          }
        });
      }

      // Filter work items
      const workItems = container.querySelectorAll('.work-item');
      if (workItems.length > 0) {
        workItems.forEach(item => {
          const cat = item.getAttribute('data-cat');
          if (filter === 'all' || cat === filter) {
            item.classList.remove('hidden');
          } else {
            item.classList.add('hidden');
          }
        });
      }
    });
  });

});
