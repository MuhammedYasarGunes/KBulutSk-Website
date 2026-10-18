/* ─────────────────────────────────────────
   NAVBAR – Mobile Menu Toggle
───────────────────────────────────────── */
const menuToggle = document.getElementById('menuToggle');
const navLinks   = document.getElementById('navLinks');
 
if (menuToggle && navLinks) {
 
  menuToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = navLinks.classList.toggle('active');
    menuToggle.classList.toggle('active', isOpen);
  });
 
  // Link tıklandığında menüyü kapat + aktif linki işaretle
  document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      closeMenu();
      document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
      link.classList.add('active');
    });
  });
 
  // Navbar dışına tıklanınca kapat
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.navbar')) closeMenu();
  });
 
  // ESC tuşuyla kapat
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
} 

function closeMenu() {
  menuToggle?.classList.remove('active');
  navLinks?.classList.remove('active');
}

