fetch("fiyat.json")
  .then(response => response.json())
  .then(data => {
    let fiyatStr = data[0]; // Örn: "₺14.999 x3 ay"

    // ₺ işaretinden sonraki sayıyı bul
    let match = fiyatStr.match(/₺\s*([\d\.]+)/);
    if (match) {
      // 14.999 → 14999
      let fiyat = parseFloat(match[1].replace(".", ""));
      let taksitTutari = fiyat * 3;

      // Her iki hücreye de doğru değerleri yaz
      document.getElementById("taksitTutari").textContent = fiyat.toLocaleString("tr-TR") + " ₺";
      document.getElementById("gerekliPuan").textContent = taksitTutari.toLocaleString("tr-TR", { minimumFractionDigits: 2 }) + " ₺  ";
    }
  })
  .catch(error => console.error("Hata:", error));
