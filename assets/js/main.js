/**
 * Main Script - Website Kementrans 2026
 * Tugas: Mengelola navigasi aktif dan interaktivitas dasar
 */

document.addEventListener("DOMContentLoaded", () => {
  // 1. LOGIKA NAVIGASI AKTIF
  const currentPath = window.location.pathname;
  const pageName = currentPath.split("/").pop() || "index.html";

  // Ambil semua link di navigasi
  const navLinks = document.querySelectorAll(".nav-link");

  navLinks.forEach((link) => {
    const linkHref = link.getAttribute("href");

    // Cek jika href link sama dengan halaman saat ini
    if (linkHref === pageName) {
      link.classList.add("active");
      // Tambahkan styling inline sederhana jika CSS belum ada class active
      link.style.color = "var(--warning)";
      link.style.fontWeight = "700";
    }
  });

  // 2. STICKY HEADER EFFECT
  const header = document.querySelector(".header");
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      header.style.boxShadow = "0 4px 20px rgba(0,0,0,0.1)";
      header.style.background = "rgba(13, 50, 68, 0.95)"; // Glassmorphism tipis
      header.style.backdropFilter = "blur(10px)";
    } else {
      header.style.boxShadow = "none";
      header.style.background = "var(--primary)";
    }
  });

  // 3. LOGIKA BUTTON "DAFTAR SEKARANG"
  // Memastikan tombol di Hero Section mengarah ke formregistrasi.html
  const heroBtn = document.querySelector(".hero-content .btn-primary");
  if (heroBtn && !heroBtn.getAttribute("href")) {
    heroBtn.addEventListener("click", (e) => {
      window.location.href = "formregistrasi.html";
    });
  }
});
